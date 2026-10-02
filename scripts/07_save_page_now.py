#!/usr/bin/env python3
"""Deliberately archive every program's roster/graduates page via the Internet
Archive's Save Page Now, converting Wayback from "whatever the crawler happened
to grab" into a controlled annual panel with a KNOWN capture cadence.

Why this matters: measured capture gaps on real program pages run to 376 days.
A resident present for under a year can fall entirely between crawls and appear
in zero snapshots — and that missingness is biased toward short-tenure
departures, i.e. exactly the attrition being measured. Captures we schedule
ourselves have a cadence we control and can report.

Run this twice a year (September, when the new PGY-1s are listed, and June,
before the graduating class is removed).

Rate limits: anonymous SPN is throttled to roughly 4-6 captures/minute. An
Internet Archive account gives an S3-style key and a much higher ceiling --
set IA_ACCESS_KEY / IA_SECRET_KEY to use it (get them at
https://archive.org/account/s3.php).
"""
import sqlite3, time, os, sys, json, argparse
import urllib.request, urllib.error, urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ia_creds import load as load_ia_creds

DB="db/neurosurgery_attrition.db"
SPN="https://web.archive.org/save/"
# Anonymous Save Page Now returns 401 ("You need to be logged in") / 429, so
# credentials are mandatory, not optional.
AK,SK=load_ia_creds()
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"

def save(url, timeout=180):
    """Request a capture. Uses the JSON API so we get back a job id / error."""
    data=urllib.parse.urlencode({"url":url,"skip_first_archive":"1",
                                 "capture_outlinks":"0"}).encode()
    req=urllib.request.Request("https://web.archive.org/save", data=data, method="POST",
        headers={"User-Agent":UA,"Accept":"application/json",
                 "Content-Type":"application/x-www-form-urlencoded"})
    if AK and SK: req.add_header("Authorization", f"LOW {AK}:{SK}")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body=r.read().decode("utf-8","replace")[:400]
            try: j=json.loads(body)
            except Exception: j={}
            return ("ok", r.status, j.get("job_id") or j.get("url") or body[:120])
    except urllib.error.HTTPError as e:
        detail=""
        try: detail=e.read().decode("utf-8","replace")[:160]
        except Exception: pass
        return ("http_error", e.code, detail)
    except Exception as e:
        return ("error", type(e).__name__, "")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--min-names",type=int,default=3,
                    help="only archive URLs a parser could pull this many names from")
    ap.add_argument("--workers",type=int,default=1)
    ap.add_argument("--delay",type=float,default=8.0,
                    help="seconds between requests; IA 429s aggressively")
    ap.add_argument("--retry-429",action="store_true",
                    help="only retry URLs whose last attempt was rate-limited")
    ap.add_argument("--dry-run",action="store_true")
    ap.add_argument("--limit",type=int,default=0)
    a=ap.parse_args()

    con=sqlite3.connect(DB)
    con.execute('PRAGMA busy_timeout=60000'); cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS spn_log(
        id INTEGER PRIMARY KEY, program_id INTEGER, url TEXT, kind TEXT,
        requested_at TEXT, result TEXT, http_status TEXT, wayback_path TEXT)""")
    con.commit()
    if a.retry_429:
        rows=cur.execute(f"""
            SELECT l.program_id,l.url,l.kind FROM live_roster_urls l
            WHERE l.n_names>={a.min_names} AND l.check_status='ok'
              AND l.url IN (SELECT url FROM spn_log WHERE result='http_error' AND http_status='429')
              AND l.url NOT IN (SELECT url FROM spn_log WHERE result='ok')
            ORDER BY l.kind,l.program_id""").fetchall()
    else:
        rows=cur.execute(f"""SELECT program_id,url,kind FROM live_roster_urls
                             WHERE n_names>={a.min_names} AND check_status='ok'
                             ORDER BY kind,program_id""").fetchall()
    if a.limit: rows=rows[:a.limit]
    print(f"{len(rows)} URLs to archive (min_names={a.min_names})"
          f"{'  [DRY RUN]' if a.dry_run else ''}")
    if not (AK and SK):
        sys.exit("No Internet Archive credentials -- run scripts/set_ia_credentials.py first.")
    print(f"auth: IA S3 key {AK[:4]}{'*'*(len(AK)-4)}")
    if a.dry_run:
        for pid,u,k in rows[:20]: print(f"   {k:7s} {u[:96]}")
        return

    now=time.strftime("%Y-%m-%dT%H:%M:%S"); done=0; okc=0
    # Sequential with a delay: SPN rate-limits per ACCOUNT, so parallelism does
    # not help and actively hurts (concurrent requests all get 429'd).
    for pid,u,k in rows:
        res,st,cl=save(u); done+=1
        if res=="ok": okc+=1
        cur.execute("""INSERT INTO spn_log(program_id,url,kind,requested_at,result,http_status,wayback_path)
                       VALUES (?,?,?,?,?,?,?)""",(pid,u,k,now,res,str(st),cl))
        if done%5==0:
            con.commit(); print(f"  {done}/{len(rows)}  ok={okc}",flush=True)
        if st==429:          # back off harder when throttled
            time.sleep(a.delay*3)
        elif done<len(rows):
            time.sleep(a.delay)
    con.commit()
    print("\nresults:")
    for r,n in cur.execute("SELECT result||' '||http_status, COUNT(*) FROM spn_log WHERE requested_at=? GROUP BY 1 ORDER BY 2 DESC",(now,)):
        print(f"  {n:4d}  {r}")
    con.close()

if __name__=="__main__": main()
