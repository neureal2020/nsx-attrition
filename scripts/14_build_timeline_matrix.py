#!/usr/bin/env python3
"""Build a person x academic-year matrix for ONE program and flag departures.

    python3 scripts/14_build_timeline_matrix.py --program-id 60

Reads roster_observations (raw, per-snapshot) and produces, per person:
  first/last academic year seen, PGY at each, and whether their disappearance
  looks like completion or departure.

INTERPRETATION RULES
  * A person last seen at PGY 7 (or at the program's terminal PGY) COMPLETED.
  * A person last seen below that, in a year that is NOT the final observed
    year, DEPARTED -- candidate attrition, to be adjudicated against external
    sources, never asserted from roster absence alone.
  * A year with NO SNAPSHOT is MISSING DATA and breaks the chain; anyone whose
    disappearance coincides with a coverage gap is marked 'gap_adjacent' and is
    NOT counted as attrition.
"""
import argparse, sqlite3, sys, re
from collections import defaultdict
sys.path.insert(0,"scripts")
from entity_resolution import split_name, canon_first

ap=argparse.ArgumentParser()
ap.add_argument("--program-id",type=int,required=True)
ap.add_argument("--terminal-pgy",type=int,default=7)
a=ap.parse_args()

con=sqlite3.connect("db/neurosurgery_attrition.db"); con.execute("PRAGMA busy_timeout=60000")
rows=con.execute("""SELECT o.academic_year, o.name_as_listed, o.pgy_numeric, s.captured_at
                    FROM roster_observations o JOIN roster_snapshots s USING(snapshot_id)
                    WHERE o.program_id=? ORDER BY s.captured_at""",(a.program_id,)).fetchall()
prog=con.execute("SELECT name FROM programs WHERE program_id=?",(a.program_id,)).fetchone()[0]

def key(n):
    f,m,l=split_name(n)
    return (canon_first(f),l)

people=defaultdict(lambda:{"names":set(),"years":{},"pgy":{}})
years=set(); ay_dates=defaultdict(set)
for ay,name,pgy,cap in rows:
    k=key(name)
    people[k]["names"].add(name)
    people[k]["years"][ay]=True
    if pgy: people[k]["pgy"][ay]=pgy
    years.add(ay); ay_dates[ay].add(cap[:7])

years=sorted(years)
# academic years with NO snapshot at all -> missing data, not absence
allspan=[]
if years:
    y0=int(years[0][:4]); y1=int(years[-1][:4])
    allspan=[f"{y}-{y+1}" for y in range(y0,y1+1)]
missing=[y for y in allspan if y not in years]

print(f"\n{prog}  (program {a.program_id})")
print(f"observed academic years : {', '.join(years)}")
print(f"NO-SNAPSHOT years       : {', '.join(missing) if missing else '(none)'}")
print(f"distinct people         : {len(people)}\n")

hdr="".join(f"{y[2:4]}/{y[7:9]} " for y in allspan)
print(f"{'name':26s} {hdr}  entry  last   lastPGY  status       conf")
print("-"*(26+len(hdr)+34))

results=[]
def _entry_key(v):
    """Sort by seniority: PGY-derived entry year where available, else first seen."""
    seen=[y for y in allspan if y in v["years"]]
    fy=seen[0]; fp=v["pgy"].get(fy)
    return (int(fy[:4])-(fp-1)) if fp else int(fy[:4])

for k,v in sorted(people.items(), key=lambda kv:(_entry_key(kv[1]), kv[0][1])):
    name=max(v["names"],key=len)
    seen=[y for y in allspan if y in v["years"]]
    first,last=seen[0],seen[-1]
    lastpgy=v["pgy"].get(last)
    obs_first_year=first[:4]; first_pgy=v["pgy"].get(first)
    row=""
    for y in allspan:
        if y in v["years"]:
            p=v["pgy"].get(y)
            row += f"{'  '+str(p)+'   ' if p else '  *   '}"
        elif y in missing: row += "  ?   "
        else: row += "  .   "
    # Classify. Anyone once listed as a resident who does not reappear COUNTS
    # toward attrition -- a coverage gap lowers confidence, it does not remove
    # the person from the denominator. (Dropping gap-adjacent people silently
    # discards exactly the cohorts where attrition is most likely.)
    nxt=allspan[allspan.index(last)+1] if allspan.index(last)+1<len(allspan) else None
    gapnext = bool(nxt and nxt in missing)
    if last==years[-1]:
        status,conf="in_training","high"
    elif lastpgy and lastpgy>=a.terminal_pgy:
        status,conf="completed","high"
    elif lastpgy and lastpgy>=a.terminal_pgy-1:
        status,conf="completed?","low"          # last seen one year short
    else:
        status="left_roster"
        conf="low" if gapnext else ("medium" if lastpgy else "low")
    # seniority key: prefer PGY-derived entry year, else first year seen
    entry = (int(obs_first_year)-(first_pgy-1)) if (first_pgy) else int(first[:4])
    order_conf = "" if first_pgy else "  (order uncertain: no PGY label)"
    print(f"{name[:26]:26s} {row}  {entry:<6d} {last[:4]}   {str(lastpgy or '-'):5s}   "
          f"{status:12s} {conf:6s}{order_conf}")
    results.append((entry,name,first,last,lastpgy,status,conf))

print("\nsummary:")
from collections import Counter
for s,n in Counter(r[5] for r in results).most_common(): print(f"   {s:14s} {n}")
print("\nleft_roster = once listed, never reappears -> counts toward attrition,")
print("              confidence lowered when a coverage gap follows.")
print("\nlegend: digit=PGY observed, *=listed w/o PGY, .=absent, ?=no snapshot that year")
con.close()
