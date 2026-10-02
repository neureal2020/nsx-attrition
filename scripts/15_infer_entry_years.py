#!/usr/bin/env python3
"""Reconstruct ENTRY (match) year from PGY level observed at a known date.

    python3 scripts/15_infer_entry_years.py --program-id 60

Where the roster is archived with PGY labels, a single snapshot reconstructs the
entry year of everyone on it:

    entry_year = academic_year_start - (PGY - 1)

So SLU's 2020-21 roster alone recovers entry cohorts back to ~2014, covering
years whose roster pages were never archived.

LIMIT -- and it is the important one: this only sees people who SURVIVED to a
captured year. Anyone who entered 2015-2019 and left before the 2020 capture
appears nowhere. Those cohorts are therefore LEFT-CENSORED: their attrition is
systematically undercounted, and must be reported as censored rather than as a
rate. Only cohorts whose entire span is covered by snapshots yield an honest
denominator.

Caveat: dedicated research years break the PGY:calendar mapping (SLU residents
show doubled PGY levels, e.g. 4,4 or 6,6), so an inferred entry year drifts
later by roughly the number of research years taken. Inferences are therefore
ranges, and the earliest observation of a person is the most reliable.
"""
import argparse, sqlite3, sys
from collections import defaultdict
sys.path.insert(0,"scripts")
from entity_resolution import split_name, canon_first

ap=argparse.ArgumentParser()
ap.add_argument("--program-id",type=int,required=True)
a=ap.parse_args()

con=sqlite3.connect("db/neurosurgery_attrition.db"); con.execute("PRAGMA busy_timeout=60000")
rows=con.execute("""SELECT o.academic_year,o.name_as_listed,o.pgy_numeric
                    FROM roster_observations o
                    WHERE o.program_id=? AND o.pgy_numeric IS NOT NULL
                    ORDER BY o.academic_year""",(a.program_id,)).fetchall()
people=defaultdict(list)
for ay,name,pgy in rows:
    f,m,l=split_name(name)
    people[(canon_first(f),l)].append((ay,name,pgy))

print(f"\nentry-year reconstruction, program {a.program_id}")
print(f"{'name':24s} {'observations (AY:PGY)':42s} {'entry est.':12s} note")
print("-"*100)
est={}
for k,obs in sorted(people.items(), key=lambda kv: kv[1][0][0]):
    name=max((o[1] for o in obs), key=len)
    seq=" ".join(f"{o[0][2:4]}:{o[2]}" for o in obs)
    cands=[]
    for ay,_,pgy in obs:
        start=int(ay[:4])
        cands.append(start-(pgy-1))
    lo,hi=min(cands),max(cands)
    # earliest observation is least distorted by research years
    first_ay,_,first_pgy=obs[0]
    best=int(first_ay[:4])-(first_pgy-1)
    note="" if lo==hi else f"range {lo}-{hi} (research years shift later obs)"
    print(f"{name[:24]:24s} {seq[:42]:42s} {best:<12d} {note}")
    est[name]=best
print("\nreconstructed entry cohorts:")
from collections import Counter
for y,n in sorted(Counter(est.values()).items()):
    who=[k for k,v in est.items() if v==y]
    print(f"   {y}: {n}  {', '.join(who)}")
con.close()
