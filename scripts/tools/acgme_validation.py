#!/usr/bin/env python3
"""Year-by-year validation against ACGME Data Resource Book, using EVERY resident on duty (all entry years).

    python3 scripts/tools/acgme_validation.py -> data/verify/report/acgme_validation.json

Residents on duty in academic year Y = 2011+ entrants (verified cohort, merged_final) + pre-2011 entrants from the
per-program roster audits (data/intake/adjudication), whose outcomes were verified where they left (phase-3 tiers 1-2).
Departures in Y (ACGME schema = transferred [any specialty] + withdrew + dismissed + unsuccessful + deceased) =
everyone whose last roster year is Y and who did not complete there: our transferred + left NS + died.
Forced relocations at program closure (Wayne State, UNM, 2019-20) are reported separately: ACGME totals do not include them.
"""
import json, re
from collections import defaultdict
ac = {r["academic_year"]: r for r in json.load(open("data/verify/programs/acgme_attrition.json"))}
merged = json.load(open("data/verify/phase3/merged_final.json"))
adj = json.load(open("data/verify/report/adjudication_all.json"))
COH = [p for p in merged if p["outcome_2025"] not in ("excluded_not_a_resident", "excluded_program_out_of_scope") and p.get("entry_year")]
mk = {}
for p in merged:
    t = re.sub(r"[^A-Za-z \-]", " ", p["name"]).split()
    if t: mk[(p["program_id"], t[-1].lower(), t[0][:3].lower())] = p
people = []
for p in COH:
    if p["entry_year"] >= 2011:
        people.append(dict(src="cohort", pid=p["program_id"], first=p["first_seen"], last=p["last_seen"], out=p["outcome"], pgy=p["last_pgy"]))
for r in adj:
    if r["entry"] >= 2011 or r["pid"] == 47:
        continue
    last = f'{r["last"][:4]}-{int(r["last"][:4]) + 1}' if r["last"][:4].isdigit() else None
    if not last or last < "2011-2012":
        continue
    t = re.sub(r"[^A-Za-z \-]", " ", r["name"]).split()
    v = mk.get((r["pid"], t[-1].lower(), t[0][:3].lower())) if t else None
    if r["out"].startswith("COMPLETED"):
        out = "completed"
    elif v and v["outcome"] not in ("unknown",):
        out = v["outcome"]
    elif "TRANSFERRED" in r["out"]:
        out = "transferred"
    elif r["out"].startswith("DIED"):
        out = "deceased"
    else:
        out = "left_destination_unknown"
    people.append(dict(src="pre2011", pid=r["pid"], first=f"{max(r['entry'], 2011)}-{max(r['entry'], 2011) + 1}", last=last, out=out, pgy=int(r["pgy"]) if r["pgy"].isdigit() else None))
CLOSURE = {(125, "2019-2020"), (97, "2019-2020")}
LEFT = ("switched_specialty", "left_medicine", "left_other", "left_destination_unknown", "unknown")
rows = []
for a in range(2011, 2025):
    y = f"{a}-{a + 1}"
    duty = [q for q in people if q["first"] <= y <= q["last"]]
    dep = [q for q in people if q["last"] == y and q["out"] not in ("completed", "in_training")]
    clos = [q for q in dep if q["out"] == "transferred" and (q["pid"], y) in CLOSURE]
    dep = [q for q in dep if q not in clos]
    tr = sum(q["out"] == "transferred" for q in dep); lf = sum(q["out"] in LEFT for q in dep); de = sum(q["out"] == "deceased" for q in dep)
    A = ac.get(y) or {}
    rows.append(dict(year=y, ours_on_duty=len(duty), acgme_on_duty=A.get("residents_on_duty"), ours_departures=len(dep), ours_transferred_ns=tr, ours_left_ns=lf, ours_died=de,
                     closure_relocations=len(clos), acgme_departures=A.get("attrition_total"), acgme_transferred=A.get("transferred"),
                     acgme_withdrew=A.get("withdrew"), acgme_dismissed=A.get("dismissed"), acgme_unsuccessful=A.get("unsuccessful_completion"), acgme_died=A.get("deceased"),
                     acgme_transferred_same=A.get("transferred_same_specialty"), acgme_transferred_other=A.get("transferred_other_specialty")))
json.dump(rows, open("data/verify/report/acgme_validation.json", "w"), indent=1)
print("year       on duty ours/ACGME   departures ours/ACGME   ours: NS-transfer left died | ACGME: transfer withdraw dismiss unsucc died | closure")
T = [0, 0]
for r in rows:
    print(f'{r["year"]}  {r["ours_on_duty"]:5}/{r["acgme_on_duty"] or "-":>5}   {r["ours_departures"]:3}/{r["acgme_departures"] if r["acgme_departures"] is not None else "-":>3}    '
          f'{r["ours_transferred_ns"]:3} {r["ours_left_ns"]:3} {r["ours_died"]:2} | {r["acgme_transferred"]} {r["acgme_withdrew"]} {r["acgme_dismissed"]} {r["acgme_unsuccessful"]} {r["acgme_died"]} | {r["closure_relocations"]}')
    if r["acgme_departures"] is not None:
        T[0] += r["ours_departures"]; T[1] += r["acgme_departures"]
print("TOTAL (years with ACGME data):", T)
