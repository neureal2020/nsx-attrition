#!/usr/bin/env python3
"""PHASE 1 of roster discovery: find each program's CURRENT resident-roster page
by crawling the live site.

Why not do this in Wayback? Because the Wayback CDX API throttles aggressively
under sustained load (measured: a query that takes 5s cold takes 37s once we
have a few hundred queries in flight), which makes broad enumeration a
multi-hour job. Live institutional sites have no such limit and can be crawled
in parallel. So we find the roster URL here, cheaply, and spend our small
Wayback budget on targeted per-URL history queries in phase 2.

Strategy per program: seed from the department homepage (guessing the usual
neurosurgery subdomain, plus the ACGME email domain and AANS URL), fetch it,
then follow in-site links whose text or href looks like a resident roster.
"""
import sqlite3, json, re, sys, time
from urllib.parse import urlparse, urljoin
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from bs4 import BeautifulSoup

DB="db/neurosurgery_attrition.db"
UA={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                 "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
# \bresident\b-ish, but NOT "residential"; "residency" alone is too weak on its own.
LINK_POS=re.compile(r"\bresidents?\b|housestaff|house staff|\btrainees?\b|our team|"
                    r"meet the|current class|\balumni\b|former resident|graduates?",re.I)
LINK_NEG=re.compile(r"residential|apply|application|how to|faq|salary|benefit|prospective|"
                    r"alumni association|giving|news|blog|registrar|wellness|housing|life\b",re.I)
# The link must be anchored to neurosurgery somewhere, or it is some other
# department's roster (we were matching anesthesiology and the registrar).
NEURO=re.compile(r"neuro(?:logical)?[-_ ]?surg|neurosurgery|nsgy",re.I)
OTHER_SPECIALTY=re.compile(
  r"/(anesthesi|orthopaed|orthoped|psychiat|dermatolog|radiolog|pediatr|internal[-_]?medicine|"
  r"emergency|patholog|ophthalmolog|urolog|obgyn|obstetric|family[-_]?medicine|surgery/general|"
  r"neurology|cardiolog|oncolog|plastic)",re.I)

def link_score(full,txt,seed_is_neuro):
    u=full.lower(); path=urlparse(u).path; host=urlparse(u).netloc
    if OTHER_SPECIALTY.search(path): return -99
    sc=0.0
    if re.search(r"\bresidents?\b|housestaff|house[-_]staff",path): sc+=3
    if re.search(r"\bresidents?\b|housestaff",txt,re.I): sc+=2
    if re.search(r"current|meet|our",txt,re.I): sc+=1
    if NEURO.search(host): sc+=3
    elif NEURO.search(path): sc+=2.5
    elif seed_is_neuro: sc+=1.5
    else: return -99          # no neurosurgery anchor at all -> reject
    if re.search(r"alumni|former|past|graduat",u+" "+txt,re.I): sc+=1
    d=path.strip("/").count("/")
    if d>5: sc-=0.8*(d-5)
    return sc
PATHS=["/residency/residents","/education/residency/residents","/residents","/our-residents",
       "/education/residents","/residency/current-residents","/people/residents",
       "/education/residency-program/residents","/training/residents","/residency"]

def registrable(h):
    p=[x for x in (h or "").lower().replace(":80","").split(".") if x]
    if len(p)>2 and p[-2] in ("ac","co","edu","gov") and len(p[-1])==2: return ".".join(p[-3:])
    return ".".join(p[-2:]) if len(p)>=2 else h

def get(u,timeout=20):
    try:
        r=requests.get(u,headers=UA,timeout=timeout,allow_redirects=True)
        if r.status_code==200 and "text/html" in r.headers.get("content-type",""): return r
    except Exception: pass
    return None

def work(row):
    pid,name,website,notes=row
    try: meta=json.loads(notes or "{}")
    except Exception: meta={}
    seeds=[]
    email=(meta.get("email") or "").strip().lower()
    regs=[]
    if "@" in email: regs.append(registrable(email.split("@")[-1]))
    if website:
        h=urlparse(website if "//" in website else "http://"+website).netloc.lower()
        if h: regs.append(registrable(h))
    s=set(); regs=[r for r in regs if r and not (r in s or s.add(r))]
    if website: seeds.append(website if "//" in website else "http://"+website)
    for r in regs: seeds += [f"https://neurosurgery.{r}/", f"https://{r}/neurosurgery/"]

    found, homepage = [], None
    for u in seeds[:5]:
        r=get(u)
        if not r: continue
        homepage=r.url
        soup=BeautifulSoup(r.text,"html.parser")
        base=r.url
        seed_is_neuro=bool(NEURO.search(base))
        for a in soup.find_all("a",href=True):
            txt=a.get_text(" ",strip=True)[:70]; href=a["href"]
            blob=txt+" "+href
            if not LINK_POS.search(blob) or LINK_NEG.search(blob): continue
            full=urljoin(base,href)
            if urlparse(full).netloc.split(":")[0].lower() != urlparse(base).netloc.split(":")[0].lower():
                continue
            sc=link_score(full,txt,seed_is_neuro)
            if sc<2.0: continue
            kind="alumni" if re.search(r"alumni|former|past|graduat",blob,re.I) else "roster"
            found.append((full,kind,txt,sc))
        if found: break
    # fall back to guessing conventional paths on the department host
    if not found and homepage and NEURO.search(homepage):
        root=f"{urlparse(homepage).scheme}://{urlparse(homepage).netloc}"
        for p in PATHS[:6]:
            r=get(root+p,timeout=12)
            if r: found.append((r.url,"roster","(path guess)",2.5)); break
    found.sort(key=lambda x:-x[3])
    seen=set(); out=[]
    for u,k,t,sc in found:
        key=u.rstrip("/").lower()
        if key in seen: continue
        seen.add(key); out.append((u,k,f"{t} [score={sc:.1f}]"))
    return pid,name,homepage,out[:8]

con=sqlite3.connect(DB)
con.execute('PRAGMA busy_timeout=60000')
progs=con.execute("SELECT program_id,name,website,notes FROM programs ORDER BY program_id").fetchall()
con.close()
con=sqlite3.connect(DB)
con.execute('PRAGMA busy_timeout=60000'); cur=con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS live_roster_urls(
  id INTEGER PRIMARY KEY, program_id INTEGER REFERENCES programs(program_id),
  url TEXT, kind TEXT, link_text TEXT, homepage TEXT, found_on TEXT,
  UNIQUE(program_id,url))""")
con.commit()

ok=0; res=[]
with ThreadPoolExecutor(max_workers=12) as ex:
    futs={ex.submit(work,p):p for p in progs}
    for i,f in enumerate(as_completed(futs),1):
        try: pid,name,hp,out=f.result()
        except Exception as e: print("ERR",e,flush=True); continue
        res.append((pid,hp,out))
        if out: ok+=1
        print(f"[{i:3d}/124] {name[:40]:42s} hp={'Y' if hp else 'N'} links={len(out)}",flush=True)

today=time.strftime("%Y-%m-%d"); n=0
for pid,hp,out in res:
    for u,k,t in out:
        cur.execute("""INSERT OR IGNORE INTO live_roster_urls(program_id,url,kind,link_text,homepage,found_on)
                       VALUES (?,?,?,?,?,?)""",(pid,u,k,t,hp,today)); n+=cur.rowcount
con.commit()
print(f"\nprograms with >=1 live roster link: {ok}/124")
print(f"rows inserted: {n}")
print("roster links:",cur.execute("SELECT COUNT(*) FROM live_roster_urls WHERE kind='roster'").fetchone()[0])
print("alumni links:",cur.execute("SELECT COUNT(*) FROM live_roster_urls WHERE kind='alumni'").fetchone()[0])
con.close()
