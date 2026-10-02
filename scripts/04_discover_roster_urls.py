#!/usr/bin/env python3
"""Find candidate resident-roster / alumni pages per program via Wayback CDX.

HANDLING URL & DOMAIN CHANGES (main correctness risk)
-----------------------------------------------------
Wayback indexes by URL, not institution, so a program that moved hosts between
2012 and 2026 is invisible from its current URL alone. Mitigations:
 1. MULTI-SEED per program: ACGME program-director email domain, AANS directory
    host, and department-subdomain patterns (neurosurgery.<domain>).
 2. SUBDOMAIN MOVES caught by enumerating the department subdomain, plus cheap
    path-prefix queries against the institutional apex.
 3. CROSS-DOMAIN REBRANDS (thebarrow.org -> barrowneuro.org) cannot be guessed;
    they surface as holes in the per-program/per-year coverage matrix and are
    seeded by hand. Gaps are reported, never silently treated as attrition.

PERFORMANCE
-----------
Measured: matchType=domain on an apex .edu returns 20k rows in ~10s, on a
department subdomain ~5s, and matchType=prefix ~3s. Wayback throttles hard
above ~4 concurrent clients, so this uses a FLAT task queue (not one worker per
program, which let a single slow program block a worker for 13 serial queries)
with modest concurrency and exponential backoff.
"""
import sqlite3, json, re, time, random, urllib.request, urllib.error, sys
from urllib.parse import urlparse, quote
from concurrent.futures import ThreadPoolExecutor, as_completed

DB="db/neurosurgery_attrition.db"; YEAR_FROM=2011; WORKERS=4
BASE=("http://web.archive.org/cdx/search/cdx?url={u}&matchType={mt}&output=json"
      "&collapse=urlkey&fl=timestamp,original,statuscode&limit={lim}&from={yf}")
APEX_PATHS=["neurosurgery/","neurological-surgery/","neurosurgery/residency/",
            "departments/neurosurgery/","medicine/neurosurgery/","surgery/neurosurgery/"]
ROSTER_POS=[(r"resident",3.0),(r"housestaff|house-staff|house_staff",3.0),(r"trainee",2.0),
            (r"current",1.5),(r"our-?team|our-?people",1.0),(r"meet",1.0),(r"residency",1.0),
            (r"people|staff",0.5)]
ALUMNI_POS=[(r"alumni",3.0),(r"former",2.5),(r"past",2.0),(r"graduat",2.0)]
NEG=[(r"\.(pdf|jpg|jpeg|png|gif|doc|docx|css|js|ico|xml|zip|mp4)$",-8.0),
     (r"/news/|/blog/|/events?/|/press|/story|/article",-3.0),
     (r"apply|application|how-?to|faq|salary|benefit|prospective|sitemap|search|login|contact",-2.5),
     (r"\?",-0.8),(r"wp-content|/tag/|/category/|/feed",-2.5),
     (r"/(anesthesi|orthopaed|orthoped|psychiat|dermatolog|radiolog|pediatr|internal-?medicine|"
      r"emergency|patholog|ophthalmolog|urolog|obgyn|family-?medicine|neurolog(?!ical-?surg))",-4.0)]
KEYS=("resident","housestaff","house-staff","trainee","alumni","former","graduat","our-team","people")

def registrable(h):
    p=[x for x in h.lower().replace(":80","").split(".") if x]
    if len(p)>2 and p[-2] in ("ac","co","edu","gov") and len(p[-1])==2: return ".".join(p[-3:])
    return ".".join(p[-2:]) if len(p)>=2 else h

def score(path,table):
    s=sum(w for rx,w in table if re.search(rx,path))+sum(w for rx,w in NEG if re.search(rx,path))
    d=path.strip("/").count("/")
    return s-1.2*(d-4) if d>4 else s

def cdx(u,mt,lim=20000,tries=3):
    for a in range(tries):
        try:
            with urllib.request.urlopen(BASE.format(u=quote(u),mt=mt,lim=lim,yf=YEAR_FROM),timeout=120) as r:
                d=json.load(r)
            return d[1:] if d else []
        except Exception:
            if a==tries-1: return []
            time.sleep((2**a)+random.random()*2)
    return []

# ---- build a flat task list -------------------------------------------------
con=sqlite3.connect(DB)
con.execute('PRAGMA busy_timeout=60000')
progs=con.execute("SELECT program_id,name,website,notes FROM programs ORDER BY program_id").fetchall()
con.close()
tasks=[]
for pid,name,website,notes in progs:
    try: meta=json.loads(notes or "{}")
    except Exception: meta={}
    regs,hosts=[],[]
    email=(meta.get("email") or "").strip().lower()
    if "@" in email:
        d=email.split("@")[-1]; regs.append(registrable(d)); hosts.append(d)
    if website:
        h=urlparse(website if "//" in website else "http://"+website).netloc.lower()
        if h: regs.append(registrable(h)); hosts.append(h)
    s=set(); regs=[r for r in regs if r and not (r in s or s.add(r))]
    s=set(); hosts=[h for h in hosts if h and not (h in s or s.add(h))]
    seeds=[]
    for r in regs: seeds.append((f"neurosurgery.{r}","domain"))
    for h in hosts:
        # enumerate only real subdomains; apex domains are far too large
        if h.count(".")>=2 and not h.startswith("www."): seeds.append((h,"domain"))
    for r in regs:
        for p in APEX_PATHS: seeds.append((f"{r}/{p}","prefix")); seeds.append((f"www.{r}/{p}","prefix"))
    if website:
        pu=urlparse(website if "//" in website else "http://"+website)
        if pu.path.strip("/"): seeds.append(((pu.netloc+pu.path).rstrip("/")+"/","prefix"))
    s=set()
    for u,mt in seeds:
        if (u,mt) in s: continue
        s.add((u,mt)); tasks.append((pid,u,mt))

print(f"{len(progs)} programs -> {len(tasks)} CDX queries ({len(tasks)/len(progs):.1f} per program)",flush=True)
raw={}
done=0
with ThreadPoolExecutor(max_workers=WORKERS) as ex:
    futs={ex.submit(cdx,u,mt):(pid,u,mt) for pid,u,mt in tasks}
    for f in as_completed(futs):
        pid,u,mt=futs[f]; done+=1
        try: rows=f.result()
        except Exception: rows=[]
        raw.setdefault(pid,[]).extend(rows)
        if done%40==0 or done==len(tasks):
            print(f"  {done}/{len(tasks)} queries  ({done*100//len(tasks)}%)",flush=True)

# ---- aggregate & score ------------------------------------------------------
con=sqlite3.connect(DB)
con.execute('PRAGMA busy_timeout=60000'); cur=con.cursor(); ins=0
for pid,rows in raw.items():
    agg={}
    for ts,url,sc in rows:
        if not sc.startswith("2"): continue
        pu=urlparse(url); path=(pu.path or "/").lower()
        if not any(k in path for k in KEYS): continue
        rs,as_=score(path,ROSTER_POS),score(path,ALUMNI_POS)
        kind,v=("roster",rs) if rs>=as_ else ("alumni",as_)
        if v<2.0: continue
        key=(pu.netloc.lower().replace(":80","")+pu.path.rstrip("/")).lower()
        e=agg.setdefault(key,{"url":url,"host":pu.netloc,"kind":kind,"score":v,"years":set()})
        e["years"].add(int(ts[:4]))
    out=[]
    for e in agg.values():
        y=sorted(e["years"])
        out.append((e["url"],e["host"],e["kind"],round(e["score"]+min(len(y),12)*0.8,2),
                    len(y),y[0],y[-1],json.dumps(y)))
    out.sort(key=lambda r:-r[3])
    for r in out[:30]:
        cur.execute("""INSERT OR IGNORE INTO roster_url_candidates
          (program_id,url,host,kind,score,n_snapshots,first_year,last_year,years)
          VALUES (?,?,?,?,?,?,?,?,?)""",(pid,)+r); ins+=cur.rowcount
con.commit()
q=lambda s:cur.execute(s).fetchone()[0]
print(f"\n=== inserted {ins} candidate URLs ===")
print("programs with a roster candidate :",q("SELECT COUNT(DISTINCT program_id) FROM roster_url_candidates WHERE kind='roster'"),"/",len(progs))
print("programs with an alumni candidate:",q("SELECT COUNT(DISTINCT program_id) FROM roster_url_candidates WHERE kind='alumni'"),"/",len(progs))
print("programs with ZERO candidates    :",q("SELECT COUNT(*) FROM programs WHERE program_id NOT IN (SELECT program_id FROM roster_url_candidates)"))
con.close()
