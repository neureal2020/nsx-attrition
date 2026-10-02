#!/usr/bin/env python3
"""Recover roster pages from COMMON CRAWL when Wayback has no capture.

    python3 scripts/17_commoncrawl_rosters.py --program-id 60 --host neurosurgery.slu.edu

Common Crawl is an independent web archive with different coverage from the
Internet Archive. For SLU it supplied a roster page Wayback never captured:

    neurosurgery.slu.edu/index.php?page=residents   (CC-MAIN-2017-22)

That page is the ONLY record of the 2016-17 cohort, and it contains Doug
Snyder, PGY-1 -- a resident who left after one year and switched specialty. He
was invisible to every other method: his roster year falls in a Wayback gap,
and NPPES shows only his current (ophthalmology) taxonomy, so the switch
detector could not see him either. He was found because a user knew his name.

Lesson encoded here: when Wayback shows a gap, query Common Crawl before
concluding the data does not exist. Note also that the page had been RENAMED
(housestaff-2 -> residents), so enumerating one known path is not enough.

Content lives in WARC files fetched by HTTP byte-range from the index record.
"""
import argparse, gzip, io, json, re, sqlite3, sys, time, urllib.parse, urllib.request
sys.path.insert(0,"scripts")
from roster_parser import parse

UA={"User-Agent":"neurosurgery-attrition-research/1.0"}
ROSTER=re.compile(r"resident|housestaff|house-staff|alumni|former|graduat|trainee",re.I)
SKIP=re.compile(r"\.(jpg|jpeg|png|gif|pdf|css|js)$",re.I)
# Index names change each crawl; these span the era Wayback tends to miss.
DEFAULT_IDX=["CC-MAIN-2016-22","CC-MAIN-2017-22","CC-MAIN-2017-43",
             "CC-MAIN-2018-22","CC-MAIN-2018-34","CC-MAIN-2019-18"]

def _get(url,timeout=75,tries=4,headers=None):
    h=dict(UA); h.update(headers or {})
    for a in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url,headers=h),timeout=timeout).read()
        except Exception:
            if a==tries-1: return None
            time.sleep(3*(a+1))

def index_query(host, idx):
    u=f"https://index.commoncrawl.org/{idx}-index?url={urllib.parse.quote(host+'/*',safe='')}&output=json"
    b=_get(u)
    if not b: return []
    out=[]
    for line in b.decode("utf-8","replace").splitlines():
        try: out.append(json.loads(line))
        except Exception: pass
    return out

def warc_html(rec):
    off,ln=int(rec["offset"]),int(rec["length"])
    raw=_get("https://data.commoncrawl.org/"+rec["filename"],timeout=90,
             headers={"Range":f"bytes={off}-{off+ln-1}"})
    if not raw: return None
    try:
        body=gzip.GzipFile(fileobj=io.BytesIO(raw)).read().decode("utf-8","replace")
    except Exception:
        return None
    return body.split("\r\n\r\n",2)[-1]

def crawl_year(idx):
    m=re.search(r"CC-MAIN-(\d{4})",idx)
    return int(m.group(1)) if m else None

ap=argparse.ArgumentParser()
ap.add_argument("--program-id",type=int,required=True)
ap.add_argument("--host",required=True)
ap.add_argument("--indexes",nargs="*",default=DEFAULT_IDX)
a=ap.parse_args()

con=sqlite3.connect("db/neurosurgery_attrition.db"); con.execute("PRAGMA busy_timeout=60000")
cur=con.cursor(); today=time.strftime("%Y-%m-%d"); total=0
for idx in a.indexes:
    recs=index_query(a.host, idx)
    hits=[r for r in recs if ROSTER.search(r.get("url","")) and not SKIP.search(r.get("url",""))]
    print(f"  {idx}: {len(recs)} records, {len(hits)} roster-ish", flush=True)
    for r in hits:
        html=warc_html(r)
        if not html: print(f"     {r['url'][:70]}  WARC fetch failed"); continue
        names=parse(html,main_only=True) or parse(html)
        if not names: print(f"     {r['url'][:70]}  0 names"); continue
        ts=r.get("timestamp","")
        cap=f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}" if len(ts)>=8 else f"{crawl_year(idx)}-01-01"
        y,m_=int(cap[:4]),int(cap[5:7])
        ay=f"{y}-{y+1}" if m_>=7 else f"{y-1}-{y}"
        cur.execute("""INSERT OR IGNORE INTO roster_snapshots
            (program_id,source_url,source_type,captured_at,retrieved_at,academic_year,parse_status,notes)
            VALUES (?,?,'other',?,?,?,'parsed',?)""",
            (a.program_id,r["url"],cap,today,ay,f"commoncrawl {idx}"))
        sid=cur.lastrowid if cur.rowcount else cur.execute(
            "SELECT snapshot_id FROM roster_snapshots WHERE program_id=? AND source_url=? AND captured_at=?",
            (a.program_id,r["url"],cap)).fetchone()[0]
        if cur.rowcount:
            for n in names:
                cur.execute("""INSERT INTO roster_observations
                    (snapshot_id,program_id,name_as_listed,pgy_as_listed,pgy_numeric,academic_year,raw_context)
                    VALUES (?,?,?,?,?,?,?)""",
                    (sid,a.program_id,n["name"],n["pgy_raw"],n["pgy"],ay,(n.get("context") or "")[:200]))
            total+=len(names)
        con.commit()
        print(f"     {cap}  AY {ay}  {len(names)} names: {', '.join(x['name'] for x in names[:8])}")
    time.sleep(1)
print(f"\nstored {total} observations from Common Crawl")
con.close()
