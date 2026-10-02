#!/usr/bin/env python3
"""PHASE B: fetch the sitemap-discovered announcement URLs and extract cohorts.

Applies the same guards that the news-crawl version needed:
  * the page must actually be about neurosurgery (shared med-school hosts
    otherwise contribute other departments' announcements)
  * names must sit near the classifying cue (distant names are faculty quoted
    later in the article, not cohort members)
  * an event with more than MAX_COHORT people is a roster, not a class
"""
import sqlite3, re, sys, time, json, unicodedata
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
sys.path.insert(0,"scripts")
from roster_parser import parse_announcement
from entity_resolution import split_name, canon_first

def _key(n):
    f,m,l=split_name(n)
    return (canon_first(f), l)

def dedupe(people):
    """Collapse 'Daniel Hafez' / 'Daniel M. Hafez' within one announcement."""
    seen={}
    for q in people:
        k=_key(q["name"])
        if k in seen:
            # keep the richer record (med school, longer name)
            old=seen[k]
            if (q.get("med_school") and not old.get("med_school")) or len(q["name"])>len(old["name"]):
                seen[k]=q
        else: seen[k]=q
    return list(seen.values())

DB="db/neurosurgery_attrition.db"
UA={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                 "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
NEURO_BODY=re.compile(r"neurosurg|neurological surgery|neuro-?surgical",re.I)
MAX_COHORT=8
MAX_CUE_DIST=700
YEAR=re.compile(r"\b(20[0-2]\d)\b")

def work(row):
    aid,pid,url=row
    try:
        r=requests.get(url,headers=UA,timeout=25,allow_redirects=True)
        if r.status_code!=200 or "html" not in r.headers.get("content-type",""): return None
    except Exception: return None
    try: p=parse_announcement(r.text)
    except Exception: return None
    if not p["type"] or p["n_people"]==0: return None
    if not NEURO_BODY.search(p["body"] or ""): return None
    near=[q for q in p["people"]
          if q.get("dist_from_cue") is None or q["dist_from_cue"]<=MAX_CUE_DIST]
    near=[q for q in near if _key(q["name"]) not in EXCLUDE.get(pid,set())]
    near=dedupe(near)
    if not near or len(near)>MAX_COHORT: return None
    yr=None
    m=YEAR.search(p.get("date_text") or "") or YEAR.search(url)
    if m: yr=int(m.group(1))
    return (pid,p["type"],p.get("date_text"),yr,r.url,p["body"][:4000],near)

con=sqlite3.connect(DB); con.execute('PRAGMA busy_timeout=60000')
rows=con.execute("SELECT id,program_id,url FROM announcement_urls").fetchall()
# Announcements quote the chair/program director ("Dr. Zipfel said..."), who
# then parses as a member of the cohort. Exclude each program's own leadership.
EXCLUDE={}
for pid,notes in con.execute("SELECT program_id,notes FROM programs"):
    try: d=json.loads(notes or "{}")
    except Exception: d={}
    names=set()
    pd=(d.get("director") or "").strip()
    if pd: names.add(_key(re.sub(r",.*$","",pd)))
    EXCLUDE[pid]=names
con.close()
print(f"fetching {len(rows)} announcement URLs",flush=True)

res=[]
with ThreadPoolExecutor(max_workers=10) as ex:
    futs={ex.submit(work,r):r for r in rows}
    for i,f in enumerate(as_completed(futs),1):
        try: out=f.result()
        except Exception: out=None
        if out: res.append(out)
        if i%40==0: print(f"  {i}/{len(rows)}  kept={len(res)}",flush=True)

con=sqlite3.connect(DB); con.execute('PRAGMA busy_timeout=60000'); cur=con.cursor()
today=time.strftime("%Y-%m-%d"); ne=npl=0
for pid,typ,dt,yr,url,body,people in res:
    cur.execute("""INSERT OR IGNORE INTO cohort_events
        (program_id,event_type,event_date,event_year,source_url,source_type,retrieved_at,body_text)
        VALUES (?,?,?,?,?,'live',?,?)""",(pid,typ,dt,yr,url,today,body))
    if cur.rowcount==0: continue
    ne+=1; eid=cur.lastrowid
    for q in people:
        cur.execute("""INSERT INTO cohort_event_people
            (event_id,name_as_listed,degrees,med_school,undergrad,raw_context)
            VALUES (?,?,?,?,?,?)""",
            (eid,q["name"],q.get("degrees"),q.get("med_school"),q.get("undergrad"),
             (q.get("context") or "")[:300])); npl+=1
con.commit()
q=lambda s:cur.execute(s).fetchone()[0]
print(f"\n=== stored {ne} events, {npl} named people ===")
for t,n in cur.execute("SELECT event_type,COUNT(*) FROM cohort_events GROUP BY 1"): print(f"   {t}: {n}")
print("programs w/ match event:",q("SELECT COUNT(DISTINCT program_id) FROM cohort_events WHERE event_type='match'"))
print("programs w/ grad event :",q("SELECT COUNT(DISTINCT program_id) FROM cohort_events WHERE event_type='graduation'"))
print("by year:",[r for r in cur.execute("SELECT event_year,COUNT(*) FROM cohort_events WHERE event_year IS NOT NULL GROUP BY 1 ORDER BY 1")])
con.close()
