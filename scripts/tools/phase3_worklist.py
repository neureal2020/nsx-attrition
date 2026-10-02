#!/usr/bin/env python3
"""Build the phase-3 (US News / Doximity / Google) verification worklist.

    python3 scripts/tools/phase3_worklist.py [--batch-size 25] [--append]

Reads the adjudication tables in data/intake/adjudication/program<ID>.txt
(written by 16_adjudicate_program.py) plus roster_observations and
training_history, and writes:

    data/verify/phase3/worklist.json         every person, with tier and question
    data/verify/phase3/batch_<NNN>_in.json   batches, tier 1 first

Tiers:
  1  left the roster before completing and the outcome is still open
     ('did not complete', 'outcome unknown', NPI hint only)
  2  a recorded transfer / switch / left-medicine outcome that rests on a
     judgement call or weak evidence (notes say probable/likely/judgement/inferred)
  3  everyone else entering 2011+ (completed / in training): confirm training
     years and completion
Pre-2011 entrants are included only if they are tier 1 or 2.
"""
import argparse, glob, json, os, re, sqlite3
from collections import defaultdict

ap = argparse.ArgumentParser()
ap.add_argument("--batch-size", type=int, default=25)
ap.add_argument("--append", action="store_true",
                help="keep existing batch_*_in.json files; batch only people not already in one, numbering after the last")
a = ap.parse_args()

con = sqlite3.connect("db/neurosurgery_attrition.db")
pname = dict(con.execute("select program_id, name from programs"))

# people per program from rosters (longest listed form of each surname+first-3)
def key(n):
    t = re.sub(r"[^A-Za-z\- ]", " ", n).split()
    t = [x for x in t if x.upper() not in ("MD", "DO", "PHD", "MS", "MPH", "MBA", "JR", "SR", "II", "III", "DR")]
    return (t[0][:3].lower(), t[-1].lower()) if len(t) >= 2 else None
P = defaultdict(lambda: {"names": set(), "years": {}})
for pid, ay, nm, pgy in con.execute("select program_id, academic_year, name_as_listed, pgy_numeric from roster_observations"):
    k = key(nm)
    if not k: continue
    d = P[(pid,) + k]; d["names"].add(nm); d["years"][ay] = pgy

TH = defaultdict(list)
for nm, pid, sy, ey, c, dep, notes in con.execute(
        "select resident_name, program_id, start_year, end_year, completed, departure_type, notes from training_history"):
    k = key(nm)
    if k and pid: TH[(pid,) + k].append(dict(start=sy, end=ey, completed=c, dep=dep, notes=(notes or "")[:300]))

# adjudicated outcome per (program, 24-char name prefix)
OUT = {}
for f in glob.glob("data/intake/adjudication/program*.txt"):
    pid = int(re.search(r"program(\d+)", f).group(1))
    for line in open(f):
        # fixed-width: entry(5) mark(1) ' ' name(24) ' ' grad(6) ' ' last(8) ' ' pgy(3) ' ' ev(12) ' ' outcome
        line = line.rstrip("\n")
        if not re.match(r"^\d{4} ", line) or len(line) < 70: continue
        OUT[(pid, line[7:31].strip())] = dict(entry=int(line[:4]), outcome=line[31 + 1 + 6 + 1 + 8 + 1 + 3 + 1 + 12 + 1:].strip())

WEAK = re.compile(r"(?i)probabl|likely|judg|inferred|unconfirmed|possibl|\?")
rows = []
for (pid, f3, sur), v in P.items():
    name = max(v["names"], key=len)
    o = OUT.get((pid, name[:24].strip()))
    if not o: continue
    ys = sorted(v["years"]); first, last = ys[0], ys[-1]
    outcome = o["outcome"]; entry = o["entry"]
    th = TH.get((pid, f3, sur), [])
    if outcome.startswith("LEFT -> did not complete") or outcome.startswith("LEFT -> outcome unknown") or "PROGRAM CLOSED -> outcome unknown" in outcome:
        tier, q = 1, "Left this program before completing: where did they go, and in which year? (transfer / other specialty / left medicine)"
    elif any(t in outcome for t in ("TRANSFERRED", "SWITCHED", "LEFT MEDICINE")) and any(WEAK.search(t["notes"]) for t in th):
        tier, q = 2, "Recorded outcome rests on weak evidence: confirm the destination and the year they left."
    elif entry >= 2011:
        tier, q = 3, "Confirm residency program and years (and completion if finished)."
    else:
        continue
    rows.append(dict(key=f"{pid}:{f3}:{sur}", name=name, program_id=pid, program=pname.get(pid, "")[:70],
                     entry_year=entry, first_seen=first, first_pgy=v["years"][first], last_seen=last,
                     last_pgy=v["years"][last], recorded_outcome=outcome,
                     recorded_notes=[t["notes"][:200] for t in th][:3], tier=tier, question=q))

rows.sort(key=lambda r: (r["tier"], r["program_id"], r["entry_year"], r["name"]))
os.makedirs("data/verify/phase3", exist_ok=True)
json.dump(rows, open("data/verify/phase3/worklist.json", "w"), indent=1)
n = 0
if a.append:
    old = sorted(glob.glob("data/verify/phase3/batch_*_in.json"))
    done = {r["key"] for f in old for r in json.load(open(f))}
    n = max((int(re.search(r"batch_(\d+)_in", f).group(1)) for f in old), default=0)
    rows = [r for r in rows if r["key"] not in done]
for t in (1, 2, 3):
    tr = [r for r in rows if r["tier"] == t]
    for i in range(0, len(tr), a.batch_size):
        n += 1
        json.dump(tr[i:i + a.batch_size], open(f"data/verify/phase3/batch_{n:03d}_in.json", "w"), indent=1)
from collections import Counter
print(Counter(r["tier"] for r in rows), "->", n, "batches of <=", a.batch_size)
