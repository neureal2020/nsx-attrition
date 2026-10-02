#!/usr/bin/env python3
"""Attach each phase-3 person's program-website evidence (roster pages that list them) from the DB.

    python3 scripts/tools/phase3_program_sources.py  -> data/verify/phase3/program_sources.json
Keys match data/verify/phase3/worklist.json (program_id:first3:surname).
"""
import json, re, sqlite3
from collections import defaultdict
con = sqlite3.connect("db/neurosurgery_attrition.db")
def key(n):
    t = re.sub(r"[^A-Za-z\- ]", " ", n).split()
    t = [x for x in t if x.upper() not in ("MD", "DO", "PHD", "MS", "MPH", "MBA", "JR", "SR", "II", "III", "DR")]
    return (t[0][:3].lower(), t[-1].lower()) if len(t) >= 2 else None
out = defaultdict(list)
q = """select o.program_id, o.name_as_listed, o.academic_year, o.pgy_as_listed, s.source_url, s.source_type, s.captured_at
       from roster_observations o join roster_snapshots s on s.snapshot_id = o.snapshot_id"""
for pid, nm, ay, pgy, url, st, cap in con.execute(q):
    k = key(nm)
    if k: out[f"{pid}:{k[0]}:{k[1]}"].append(dict(year=ay, pgy=pgy, url=url, type=st, captured=cap))
for k in out: out[k].sort(key=lambda r: (r["year"] or "", r["captured"] or ""))
json.dump(out, open("data/verify/phase3/program_sources.json", "w"), indent=1)
w = json.load(open("data/verify/phase3/worklist.json"))
have = sum(1 for r in w if out.get(r["key"]))
print(f"{len(out)} people with roster sources; worklist coverage {have}/{len(w)}")
