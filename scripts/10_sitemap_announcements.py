#!/usr/bin/env python3
"""PHASE A: find announcement URLs via sitemaps (not by crawling news indexes).

Crawling a live news section only ever surfaces the current year: index pages
paginate, and older posts fall off. The first harvest returned 2 usable events,
all from 2026, across 87 programs.

Sitemaps list every published URL regardless of pagination. Pitt's has 887
entries including /news/congratulations-new-residents and
/news/congratulations-graduating-chief-residents.

Critically, many programs REUSE one URL each year ("congratulations-new-
residents" is overwritten annually) -- so the sitemap gives the address and
Wayback (phase B) gives the yearly history of that address.
"""
import sqlite3, re, sys, time
from urllib.parse import urlparse, urljoin
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

DB="db/neurosurgery_attrition.db"
UA={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                 "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
SM_PATHS=["/sitemap.xml","/sitemap_index.xml","/sitemap-index.xml","/sitemap1.xml"]
SLUG=re.compile(r"match|graduat|new-?residents?|welcome|congratulat|incoming|"
                r"class-of|chief-residents?|intern",re.I)
SLUG_NEG=re.compile(r"\.(jpg|png|pdf|css|js)$|/tag/|/category/|/author/|residential",re.I)
NEURO=re.compile(r"neurosurg|neurological-?surg|nsgy",re.I)

def get(u,t=25):
    try:
        r=requests.get(u,headers=UA,timeout=t,allow_redirects=True)
        if r.status_code==200: return r
    except Exception: pass
    return None

def locs(xml):
    return re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml or "")

def sitemap_urls(root, depth=0, seen=None):
    """Fetch a sitemap, following sitemap-index files one level down."""
    seen = seen if seen is not None else set()
    out=[]
    for p in (SM_PATHS if depth==0 else [""]):
        u = root+p if depth==0 else root
        if u in seen: continue
        seen.add(u)
        r=get(u)
        if not r or "<loc" not in r.text: continue
        found=locs(r.text)
        if "<sitemapindex" in r.text[:2000].lower() and depth<2:
            for sub in found[:25]:
                out += sitemap_urls(sub, depth+1, seen)
        else:
            out += found
        if depth==0 and out: break
    return out

def work(row):
    pid,name,homepage=row
    if not homepage: return pid,name,[]
    pu=urlparse(homepage)
    root=f"{pu.scheme}://{pu.netloc}"
    urls=sitemap_urls(root)
    if not urls: return pid,name,[]
    host_is_neuro=bool(NEURO.search(pu.netloc))
    hits=[]
    for u in urls:
        if SLUG_NEG.search(u): continue
        if not SLUG.search(u): continue
        # on a shared med-school host, require neurosurgery in the path
        if not host_is_neuro and not NEURO.search(u): continue
        hits.append(u)
    seen=set(); out=[]
    for u in hits:
        k=u.rstrip("/").lower()
        if k in seen: continue
        seen.add(k); out.append(u)
    return pid,name,out[:40]

con=sqlite3.connect(DB); con.execute('PRAGMA busy_timeout=60000')
con.execute("""CREATE TABLE IF NOT EXISTS announcement_urls(
   id INTEGER PRIMARY KEY, program_id INTEGER REFERENCES programs(program_id),
   url TEXT, found_via TEXT, found_on TEXT, UNIQUE(program_id,url))""")
con.commit()
progs=con.execute("""SELECT program_id,name,homepage FROM (
   SELECT l.program_id,p.name,l.homepage,
          ROW_NUMBER() OVER (PARTITION BY l.program_id ORDER BY l.id) rn
   FROM live_roster_urls l JOIN programs p USING(program_id)
   WHERE l.homepage IS NOT NULL AND l.homepage<>'') WHERE rn=1""").fetchall()
con.close()
print(f"reading sitemaps for {len(progs)} programs",flush=True)

res=[]
with ThreadPoolExecutor(max_workers=10) as ex:
    futs={ex.submit(work,p):p for p in progs}
    for i,f in enumerate(as_completed(futs),1):
        try: pid,name,urls=f.result()
        except Exception: continue
        res.append((pid,urls))
        if urls: print(f"[{i:3d}/{len(progs)}] {name[:36]:38s} {len(urls):3d} candidate urls",flush=True)

con=sqlite3.connect(DB); con.execute('PRAGMA busy_timeout=60000'); cur=con.cursor()
today=time.strftime("%Y-%m-%d"); n=0
for pid,urls in res:
    for u in urls:
        cur.execute("INSERT OR IGNORE INTO announcement_urls(program_id,url,found_via,found_on) VALUES (?,?,'sitemap',?)",(pid,u,today))
        n+=cur.rowcount
con.commit()
print(f"\n=== {n} announcement URLs found across "
      f"{cur.execute('SELECT COUNT(DISTINCT program_id) FROM announcement_urls').fetchone()[0]} programs ===")
for r in cur.execute("""SELECT substr(p.name,1,30), COUNT(*) FROM announcement_urls a
                        JOIN programs p USING(program_id) GROUP BY 1 ORDER BY 2 DESC LIMIT 12"""):
    print(f"   {r[0]:32s} {r[1]}")
con.close()
