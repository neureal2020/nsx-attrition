#!/usr/bin/env python3
"""Match residents who left one program's roster early with residents who
joined another program's roster above PGY-1, by name similarity and timing.

    python3 scripts/tools/crossmatch.py [--out data/intake/crossmatch.json]

A "departure" is someone whose last observed PGY is below the terminal year
(6) and whose last year is before the program's latest observed year. A
"joiner" is someone whose first observation is at PGY >= 2. A pair is
proposed when the surnames match (compound surnames: any shared token of 4+
letters) and the joiner's first year is 0-4 years after the departure's last
year. Output is CANDIDATES for review, never written to the DB.
"""
import argparse, json, re, sqlite3, unicodedata
from collections import defaultdict

ap = argparse.ArgumentParser()
ap.add_argument("--out", default="data/intake/crossmatch.json")
a = ap.parse_args()

def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\b(md|do|phd|mph|ms|mba|jr|sr|ii|iii|dr)\b\.?", " ", s)
    return re.sub(r"[^a-z\s\-']", " ", s).split()

con = sqlite3.connect("db/neurosurgery_attrition.db")
names = dict(con.execute("select program_id, name from programs"))
latest = dict(con.execute("select program_id, max(academic_year) from roster_observations group by 1"))
P = defaultdict(lambda: {"years": {}, "names": set()})
for pid, nm, ay, pgy in con.execute("""select program_id, name_as_listed, academic_year, pgy_numeric
                                       from roster_observations where academic_year is not null"""):
    t = norm(nm)
    if len(t) < 2: continue
    key = (pid, t[0], t[-1])
    P[key]["names"].add(nm)
    y = int(ay[:4])
    if pgy: P[key]["years"][y] = max(pgy, P[key]["years"].get(y, 0))
    else: P[key]["years"].setdefault(y, 0)

deps, joins = [], []
for (pid, f, l), v in P.items():
    ys = sorted(v["years"])
    if not ys: continue
    first, last = ys[0], ys[-1]
    fp, lp = v["years"][first], v["years"][last]
    nm = max(v["names"], key=len)
    toks = set(norm(nm))
    if lp and lp < 6 and last < int(latest[pid][:4]):
        deps.append(dict(pid=pid, name=nm, toks=toks, first=f, last_year=last, last_pgy=lp))
    if fp and fp >= 2 and first >= 2011:
        joins.append(dict(pid=pid, name=nm, toks=toks, first=f, first_year=first, first_pgy=fp))

def sur(t):
    # surname tokens only: drop the first token (given name) and short tokens / initials
    t = list(t) if isinstance(t, list) else t
    return {x for x in t if len(x) >= 4}
for rec in deps + joins:
    toks = norm(rec["name"])
    rec["toks"] = [x for x in toks[1:]]   # everything after the given name
out = []
for d in deps:
    for j in joins:
        if j["pid"] == d["pid"]: continue
        gap = j["first_year"] - d["last_year"]
        if not (0 <= gap <= 4): continue
        shared = sur(d["toks"]) & sur(j["toks"])
        if not shared: continue
        same_first = d["first"] == j["first"] or d["first"][:3] == j["first"][:3]
        score = len(shared) + (2 if same_first else 0) + (1 if j["first_pgy"] >= d["last_pgy"] else 0) - gap * 0.3
        out.append(dict(score=round(score, 1), departure=f'{d["name"]} ({names[d["pid"]][:40]} [{d["pid"]}], last {d["last_year"]}-{d["last_year"]+1} PGY{d["last_pgy"]})',
                        joiner=f'{j["name"]} ({names[j["pid"]][:40]} [{j["pid"]}], first {j["first_year"]}-{j["first_year"]+1} PGY{j["first_pgy"]})',
                        dep_pid=d["pid"], join_pid=j["pid"], gap_years=gap, same_first_name=same_first))
out.sort(key=lambda r: -r["score"])
json.dump(out, open(a.out, "w"), indent=1)
print(f"{len(deps)} departures, {len(joins)} joiners, {len(out)} candidate pairs -> {a.out}")
for r in out:
    if r["same_first_name"]:
        print(f'{r["score"]:>4}  {r["departure"]}  ->  {r["joiner"]}')
