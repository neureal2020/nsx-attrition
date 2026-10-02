#!/usr/bin/env python3
"""Build a year-by-year roster timeline for ONE program from Wayback snapshots.

    python3 scripts/13_program_timeline.py --program-id 60 \
        --url slu.edu/medicine/neurological-surgery/residency/residents.php

CDX GOTCHA (cost hours): with matchType=prefix, appending '*' to the url
returns ZERO results silently. 'slu.edu/medicine/neurological-surgery*' -> 0,
'slu.edu/medicine/neurological-surgery/' -> 263. Never append '*'.

Snapshots are sampled at most one per half-year: rosters change annually, so
more is wasted requests against an API that throttles hard.
"""
import argparse, json, re, sqlite3, sys, time, urllib.parse, urllib.request
sys.path.insert(0,"scripts")
from roster_parser import parse

DB="db/neurosurgery_attrition.db"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"

def cdx(url, frm=2009):
    q=("http://web.archive.org/cdx/search/cdx?url="+urllib.parse.quote(url)
       +f"&output=json&fl=timestamp,original&filter=statuscode:200"
       f"&collapse=timestamp:6&limit=2000&from={frm}")     # <=1 capture per half-year
    for a in range(3):
        try:
            with urllib.request.urlopen(q,timeout=90) as fh:
                d=json.load(fh)
            return d[1:] if d else []
        except Exception:
            time.sleep(2**a)
    return []

def fetch(ts,url):
    # 'id_' returns the ORIGINAL archived bytes without Wayback's injected toolbar
    full=f"https://web.archive.org/web/{ts}id_/{url}"
    req=urllib.request.Request(full,headers={"User-Agent":UA})
    for a in range(2):
        try:
            with urllib.request.urlopen(req,timeout=90) as r:
                return r.read().decode("utf-8","replace")
        except Exception:
            time.sleep(2)
    return None

def academic_year(ts):
    y,m=int(ts[:4]),int(ts[4:6])
    return f"{y}-{y+1}" if m>=7 else f"{y-1}-{y}"

ap=argparse.ArgumentParser()
ap.add_argument("--program-id",type=int,required=True)
ap.add_argument("--url",required=True)
ap.add_argument("--delay",type=float,default=2.5)
a=ap.parse_args()

url=a.url.replace("https://","").replace("http://","")
snaps=cdx(url)
print(f"{len(snaps)} snapshots (<=1 per half-year) for {url}")
if not snaps: sys.exit("no captures -- check the URL has no trailing '*'")

con=sqlite3.connect(DB); con.execute("PRAGMA busy_timeout=60000"); cur=con.cursor()
today=time.strftime("%Y-%m-%d"); total=0
for ts,orig in snaps:
    html=fetch(ts,orig)
    if not html: print(f"  {ts[:8]}  FETCH FAILED"); continue
    names=parse(html,main_only=True) or parse(html)
    ay=academic_year(ts)
    cur.execute("""INSERT OR IGNORE INTO roster_snapshots
        (program_id,source_url,source_type,captured_at,retrieved_at,academic_year,parse_status)
        VALUES (?,?,'wayback',?,?,?,?)""",
        (a.program_id,orig,f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}",today,ay,
         "parsed" if names else "empty"))
    sid=cur.lastrowid if cur.rowcount else cur.execute(
        "SELECT snapshot_id FROM roster_snapshots WHERE program_id=? AND source_url=? AND captured_at=?",
        (a.program_id,orig,f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}")).fetchone()[0]
    for n in names:
        cur.execute("""INSERT INTO roster_observations
            (snapshot_id,program_id,name_as_listed,pgy_as_listed,pgy_numeric,academic_year,raw_context)
            VALUES (?,?,?,?,?,?,?)""",
            (sid,a.program_id,n["name"],n["pgy_raw"],n["pgy"],ay,(n.get("context") or "")[:200]))
    total+=len(names)
    con.commit()
    print(f"  {ts[:4]}-{ts[4:6]}  AY {ay}  {len(names):2d} names: "
          f"{', '.join(x['name'] for x in names[:6])}{' ...' if len(names)>6 else ''}")
    time.sleep(a.delay)
print(f"\nstored {total} roster observations")
con.close()
