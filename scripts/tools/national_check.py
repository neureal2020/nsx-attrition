#!/usr/bin/env python3
"""Year-level check of our departure counts against the ACGME Data Resource Book (national, all reasons).

    python3 scripts/tools/national_check.py  ->  data/verify/programs/national_check.json

Ours = attrition + NS->NS transfers + deaths in the cohort, dated to the last roster year, excluding forced transfers
at program closures (Wayne State, UNM 2019-20), which the ACGME does not report as attrition.
Only years where our cohort (2011+ entrants) covers >= 90% of residents on duty are comparable.
"""
import json
ac = {r["academic_year"]: r for r in json.load(open("data/verify/programs/acgme_attrition.json"))}
m = [p for p in json.load(open("data/verify/phase3/merged_final.json")) if not p["outcome_2025"].startswith("excluded")]
CLOSURE = {(125, "2019-2020"), (97, "2019-2020")}
out = []
for y in [f"{a}-{a + 1}" for a in range(2011, 2025)]:
    a = ac.get(y)
    act = sum(1 for p in m if p["first_seen"] <= y <= p["last_seen"])
    dep = [p for p in m if p["last_seen"] == y and (p["attrition_2025"] or p["outcome_2025"] in ("transferred", "deceased"))
           and not (p["outcome_2025"] == "transferred" and (p["program_id"], y) in CLOSURE)]
    row = dict(year=y, ours=len(dep), ours_left=sum(1 for p in dep if p["attrition_2025"]), ours_transferred=sum(1 for p in dep if p["outcome_2025"] == "transferred"))
    if not a or a.get("attrition_total") is None:
        row.update(status="no ACGME figure", acgme=None)
    else:
        cov = act / a["residents_on_duty"]
        row.update(acgme=a["attrition_total"], acgme_transferred=a["transferred"], acgme_left=a["withdrew"] + a["dismissed"] + a["unsuccessful_completion"],
                   cohort_coverage=round(cov, 2), ratio=round(len(dep) / a["attrition_total"], 2) if a["attrition_total"] else None)
        if cov < 0.9:
            row["status"] = "not comparable (cohort covers only part of residents)"
        else:
            gap = a["attrition_total"] - len(dep)
            row["gap"] = gap
            row["status"] = "matches" if gap <= 3 else ("we may be missing a few departures" if gap <= 7 else "we are missing departures")
    out.append(row)
json.dump(out, open("data/verify/programs/national_check.json", "w"), indent=1)
for r in out:
    print(r["year"], r.get("acgme"), r["ours"], r.get("ratio"), r["status"])
