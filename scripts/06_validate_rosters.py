#!/usr/bin/env python3
"""Validate candidate roster URLs by CONTENT rather than by URL shape.

URL/link-text heuristics top out around 50% precision here: '/residents/' is
equally likely to be a roster, a resident portal, a resident-research page or a
generic GME index. The only reliable test is to fetch the page and ask whether
a roster parser can actually pull names out of it. Cheap (a few hundred live
fetches) and definitive.
"""
import sqlite3, sys, time, json
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
sys.path.insert(0,"scripts")
from roster_parser import parse

DB="db/neurosurgery_attrition.db"
UA={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                 "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"}

def check(row):
    rid,pid,url,kind=row
    try:
        r=requests.get(url,headers=UA,timeout=25,allow_redirects=True)
        if r.status_code!=200: return rid,0,0,f"HTTP {r.status_code}",None
        names_full=parse(r.text)
        names_main=parse(r.text,main_only=True)
        names = names_main if len(names_main)>=len(names_full)*0.6 else names_full
        pgy=sum(1 for n in names if n["pgy"])
        sample=", ".join(n["name"] for n in names[:5])
        return rid,len(names),pgy,"ok",sample
    except Exception as e:
        return rid,0,0,type(e).__name__,None

con=sqlite3.connect(DB)
con.execute('PRAGMA busy_timeout=60000'); cur=con.cursor()
for col,typ in [("n_names","INTEGER"),("n_pgy","INTEGER"),("check_status","TEXT"),
                ("sample_names","TEXT"),("validated_on","TEXT")]:
    try: cur.execute(f"ALTER TABLE live_roster_urls ADD COLUMN {col} {typ}")
    except sqlite3.OperationalError: pass
con.commit()
rows=cur.execute("SELECT id,program_id,url,kind FROM live_roster_urls").fetchall()
print(f"validating {len(rows)} candidate URLs by fetching and parsing them",flush=True)
today=time.strftime("%Y-%m-%d"); res=[]
with ThreadPoolExecutor(max_workers=12) as ex:
    futs={ex.submit(check,r):r for r in rows}
    for i,f in enumerate(as_completed(futs),1):
        res.append(f.result())
        if i%50==0: print(f"  {i}/{len(rows)}",flush=True)
for rid,n,pgy,st,sample in res:
    cur.execute("UPDATE live_roster_urls SET n_names=?,n_pgy=?,check_status=?,sample_names=?,validated_on=? WHERE id=?",
                (n,pgy,st,sample,today,rid))
con.commit()
q=lambda s:cur.execute(s).fetchone()[0]
print(f"\nURLs yielding >=3 names : {q('SELECT COUNT(*) FROM live_roster_urls WHERE n_names>=3')}")
print(f"URLs yielding >=8 names : {q('SELECT COUNT(*) FROM live_roster_urls WHERE n_names>=8')}")
print(f"programs with a CONTENT-VALIDATED roster page: "
      f"{q(chr(39).join(['SELECT COUNT(DISTINCT program_id) FROM live_roster_urls WHERE n_names>=3']))}/124")
print("\ntop validated pages:")
for r in cur.execute("""SELECT substr(p.name,1,26),l.n_names,l.n_pgy,substr(l.url,1,60),substr(l.sample_names,1,54)
                        FROM live_roster_urls l JOIN programs p USING(program_id)
                        WHERE l.n_names>=5 ORDER BY l.n_names DESC LIMIT 15"""):
    print(f"  {r[0]:28s} n={r[1]:3d} pgy={r[2]:3d} {r[3]}\n      {r[4]}")
con.close()
