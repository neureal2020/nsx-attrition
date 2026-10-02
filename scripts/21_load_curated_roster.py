#!/usr/bin/env python3
"""Load a reviewed, per-program roster file into roster_snapshots/observations.

    python3 scripts/21_load_curated_roster.py --program-id 120 --file data/intake/rosters_program120.json [--replace]

Program sites differ too much for one parser (WashU alone had four layouts:
Lotus Notes, Sitecore, a numbered CMS, then WordPress with JS-loaded lists), so
extraction is done per program and REVIEWED first; this script only stores the
result. File format -- one entry per dated capture actually used:

  [{"source_url": "...", "source_type": "wayback|live|instagram|other",
    "captured_at": "YYYY-MM-DD", "academic_year": "2015-2016", "note": "...",
    "rows": [{"name": "Chris Dibble", "pgy": 1, "context": "PGY 1st Year"}]}]

Rules the reviewer applies before writing the file (learned on WashU):
  * one capture per academic year, the LATEST in that year -- July captures
    often still show last year's roster (sites update in August);
  * never use a Wayback REPLAY of a JS-rendered roster unless every PGY group is
    populated and consistent with neighbouring years: replay silently serves
    API responses from other dates (WashU Oct-2021 replay showed 2022-23 data);
  * partial lists (announcements, a single PGY group) use source_type 'other'
    or 'instagram' so they never set the "current year" in 16_adjudicate.

  * a year with no complete capture may be RECONSTRUCTED: source_type 'manual',
    each row carrying "reconstructed": true and its evidence in "context"
    (e.g. listed at the right PGY in the years before AND after, or alumni
    graduation year). Stored with role='reconstructed' so it can always be
    separated from what a source literally said. Only add people NOT already
    observed in that year.

--replace deletes this program's existing snapshots/observations first.
"""
import argparse, json, sqlite3, time

ap = argparse.ArgumentParser()
ap.add_argument("--program-id", type=int, required=True)
ap.add_argument("--file", required=True)
ap.add_argument("--replace", action="store_true")
a = ap.parse_args()

caps = json.load(open(a.file))
con = sqlite3.connect("db/neurosurgery_attrition.db"); con.execute("PRAGMA busy_timeout=60000")
cur = con.cursor()
if a.replace:
    cur.execute("DELETE FROM roster_observations WHERE program_id=?", (a.program_id,))
    cur.execute("DELETE FROM roster_snapshots WHERE program_id=?", (a.program_id,))
today = time.strftime("%Y-%m-%d"); n = 0
for c in caps:
    cur.execute("""INSERT OR IGNORE INTO roster_snapshots
        (program_id,source_url,source_type,captured_at,retrieved_at,academic_year,parse_status,notes)
        VALUES (?,?,?,?,?,?,?,?)""",
        (a.program_id, c["source_url"], c["source_type"], c["captured_at"], today,
         c["academic_year"], "parsed" if c["rows"] else "empty", c.get("note")))
    sid = cur.execute("""SELECT snapshot_id FROM roster_snapshots
        WHERE program_id=? AND source_url=? AND captured_at=?""",
        (a.program_id, c["source_url"], c["captured_at"])).fetchone()[0]
    for r in c["rows"]:
        cur.execute("""INSERT INTO roster_observations
            (snapshot_id,program_id,name_as_listed,pgy_as_listed,pgy_numeric,academic_year,role,raw_context)
            VALUES (?,?,?,?,?,?,?,?)""",
            (sid, a.program_id, r["name"], f"PGY-{r['pgy']}" if r.get("pgy") else None,
             r.get("pgy"), c["academic_year"],
             "reconstructed" if r.get("reconstructed") else "resident", (r.get("context") or "")[:200]))
        n += 1
    print(f"  {c['academic_year']}  {c['source_type']:9s} {c['captured_at']}  {len(c['rows']):2d} names")
con.commit(); con.close()
print(f"stored {n} observations from {len(caps)} captures")
