#!/usr/bin/env python3
"""Attrition statistics for the report (status as of 30 June 2025).

    python3 scripts/tools/attrition_analysis.py

Reads data/verify/phase3/merged_final.json (run phase3_final_merge.py first) and data/verify/programs/*.
Writes data/verify/report/analysis.json and program_rates.csv. Read-only on the DB.

Definitions
- Cohort: residents first seen on a roster in 2011-12..2024-25, excluding non-residents (fellows/prelims).
- Attrition: failed to graduate a neurosurgery residency (switched specialty, left medicine, left other, left with
  destination unknown). Transfers that stayed in neurosurgery, deaths and post-completion exits are not attrition.
- Transfers: attrition is counted once, at the last NS program left; the origin record is a transfer.
- Per entering class: attrition / entrants, by entry year. Classes 2011-2018 are complete (7 years elapsed).
- Per academic year: departures in year y / cohort residents on rosters in y; only 2017-18 onward, when entrants
  2011+ fill every PGY level of a 7-year program.
- Per program: person-level attrition / residents; funnel limits from the national rate (binomial 95% and 99.8%),
  plus an exact one-sided binomial p-value with Benjamini-Hochberg FDR.
"""
import csv, json, os
from collections import Counter, defaultdict
from scipy.stats import binom, binomtest
from statsmodels.stats.proportion import proportion_confint
from statsmodels.stats.multitest import multipletests

D = "data/verify/phase3"
OUT = "data/verify/report"
os.makedirs(OUT, exist_ok=True)
m = [p for p in json.load(open(f"{D}/merged_final.json")) if not p["outcome_2025"].startswith("excluded")]
ATT = lambda p: p["attrition_2025"] is True


def ci(k, n):
    lo, hi = proportion_confint(k, n, method="wilson") if n else (0, 0)
    return round(100 * lo, 1), round(100 * hi, 1)


res = {"cohort": len(m), "attrition": sum(ATT(p) for p in m)}
res["rate"] = round(100 * res["attrition"] / res["cohort"], 2)
res["outcomes"] = dict(Counter(p["outcome_2025"] for p in m))
att = [p for p in m if ATT(p)]
res["attrition_types"] = dict(Counter(p["outcome_2025"] for p in att))
res["pgy_at_exit"] = dict(sorted(Counter(p["last_pgy"] or 0 for p in att).items()))

# per entering class
cls = []
for y in range(2011, 2025):
    g = [p for p in m if p["entry_year"] == y]
    k = sum(ATT(p) for p in g)
    o = Counter(p["outcome_2025"] for p in g)
    cls.append(dict(entry_year=y, entrants=len(g), attrition=k, rate=round(100 * k / len(g), 1) if g else None, ci95=ci(k, len(g)),
                    completed=o["completed"], in_training=o["in_training"], transferred=o["transferred"], complete_class=y <= 2018))
res["by_entry_class"] = cls
c18 = [p for p in m if p["entry_year"] and p["entry_year"] <= 2018]
k18 = sum(ATT(p) for p in c18)
res["complete_classes_2011_2018"] = dict(entrants=len(c18), attrition=k18, rate=round(100 * k18 / len(c18), 1), ci95=ci(k18, len(c18)))

# per academic year (2017-18 on)
ay = []
for y in range(2017, 2025):
    s = f"{y}-{y + 1}"
    active = [p for p in m if p["first_seen"] <= s <= p["last_seen"]]
    k = sum(1 for p in att if p["last_seen"] == s)
    ay.append(dict(year=s, residents=len(active), departures=k, rate=round(100 * k / len(active), 2), ci95=ci(k, len(active))))
res["by_academic_year"] = ay

# per program + funnel
p0 = res["attrition"] / res["cohort"]
prog = defaultdict(list)
for p in m:
    prog[(p["program_id"], (p["program"] or "").split(" ©")[0])].append(p)
rows = []
for (pid, name), g in prog.items():
    n, k = len(g), sum(ATT(p) for p in g)
    pv = binomtest(k, n, p0, alternative="greater").pvalue if n else 1
    u95, u998 = binom.ppf(0.975, n, p0), binom.ppf(0.999, n, p0)
    rows.append(dict(program_id=pid, program=name, residents=n, attrition=k, rate=round(100 * k / n, 1), ci95=ci(k, n),
                     expected=round(n * p0, 1), p_greater=pv, above_95=k > u95, above_998=k > u998,
                     low_confidence_years=None))
q = multipletests([r["p_greater"] for r in rows], method="fdr_bh")[1]
for r, qq in zip(rows, q):
    r["q_bh"] = round(qq, 4)
    r["p_greater"] = round(r["p_greater"], 4)
# attach low/medium confidence years from the heat map, if built
try:
    import openpyxl
    ws = openpyxl.load_workbook("data/verify/programs/program_year_confidence.xlsx")["Confidence heatmap"]
    lowc = {r[0]: (r[-2], r[-1]) for r in ws.iter_rows(min_row=2, values_only=True)}
    for r in rows:
        r["low_confidence_years"], r["medium_confidence_years"] = lowc.get(r["program_id"], (None, None))
except Exception:
    pass
rows.sort(key=lambda r: (-r["rate"], -r["residents"]))
with open(f"{OUT}/program_rates.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
res["programs"] = len(rows)
res["outliers_998"] = [r for r in rows if r["above_998"]]
res["outliers_95"] = [r for r in rows if r["above_95"] and not r["above_998"]]
res["fdr_significant"] = [r for r in rows if r["q_bh"] < 0.05]
res["zero_attrition_programs"] = sum(1 for r in rows if r["attrition"] == 0)
res["program_rows"] = rows

# destinations of switchers: destination fields first, then notes; strict patterns
import re
fin = {r["key"]: r["finding"] for r in json.load(open(f"{D}/final.json"))}
PAT = [("diagnostic/interventional radiology", r"radiolog|\bDR\b|\bIR\b|neuroradiolog"), ("radiation oncology", r"radiation oncolog|rad onc"),
       ("neurology", r"\bneurology\b"), ("anesthesiology/pain", r"anesthes|pain medicine"), ("emergency medicine", r"emergency medicine|\bEM\b"),
       ("orthopaedics", r"orthop"), ("psychiatry", r"psychiatr"), ("internal medicine (incl. subspecialties)", r"internal medicine|\bIM\b|gastroenterolog|cardiolog|oncology fellow"),
       ("family/primary care", r"family medicine|primary care|general practi|urgent care"), ("general/other surgery", r"general surgery|plastic|urolog|vascular surgery|cardiac surgery|otolaryng"),
       ("ophthalmology", r"ophthalm"), ("dermatology", r"dermatolog"), ("pathology", r"patholog"), ("pediatrics", r"pediatric"),
       ("PM&R", r"physical medicine|PM&R|physiatr"), ("preventive/occupational/aerospace", r"preventive|occupational|aerospace"), ("other clinical", r"wound care|genetics")]
dest = Counter()
for p in att:
    if p["outcome_2025"] != "switched_specialty":
        continue
    f = fin.get(p["key"], {})
    parts = [str(f.get("destination_program") or ""), " ".join(n for n in (p.get("notes") or []) if "destination" in n), str(f.get("current") or ""),
             str(f.get("outcome_detail") or ""), " ".join(p.get("notes") or []), str(p.get("gold_evidence") or "")]
    txt = re.sub(r"neurological surgery|neurosurg\w*", " ", " || ".join(parts), flags=re.I)
    hit = next((lab for lab, rx in PAT if re.search(rx, txt, flags=re.I)), "unspecified")
    dest[hit] += 1
res["switch_destinations"] = dict(dest.most_common())
res["evidence_levels"] = dict(Counter(p["evidence_level"] or "none" for p in m))
json.dump(res, open(f"{OUT}/analysis.json", "w"), indent=1, default=str)
print(json.dumps({k: res[k] for k in ("cohort", "attrition", "rate", "complete_classes_2011_2018", "attrition_types", "evidence_levels")}, indent=1))
print("outliers 99.8%:", [(r["program"][:40], r["attrition"], r["residents"]) for r in res["outliers_998"]])
print("outliers 95%:", [(r["program"][:40], r["attrition"], r["residents"]) for r in res["outliers_95"]])
print("FDR<0.05:", [(r["program"][:40], r["attrition"], r["residents"], r["q_bh"]) for r in res["fdr_significant"]])
print("switch destinations:", res["switch_destinations"])
