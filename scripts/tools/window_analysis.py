#!/usr/bin/env python3
"""Departures in the ACGME-validated window, AY 2016-17 .. 2023-24, all residents on duty (any entry year).

    python3 scripts/tools/window_analysis.py -> data/verify/report/window_analysis.json
"""
import json, re
from collections import Counter, defaultdict
from scipy.stats import poisson
from statsmodels.stats.multitest import multipletests

YEARS = [f"{a}-{a + 1}" for a in range(2014, 2024)]  # ACGME-validated window (see acgme_validation.py; 2014-15 via Yaeger 2020 Table 2)
merged = json.load(open("data/verify/phase3/merged_final.json"))
adj = json.load(open("data/verify/report/adjudication_all.json"))
fin = {r["key"]: r["finding"] for r in json.load(open("data/verify/phase3/final.json"))}
CLOSURE = {(125, "2019-2020"), (97, "2019-2020")}
LEFT = ("switched_specialty", "left_medicine", "left_other", "left_destination_unknown", "unknown")
pname = {}
P = []
for p in merged:
    if p["outcome_2025"] in ("excluded_not_a_resident", "excluded_program_out_of_scope") or not p.get("entry_year"):
        continue
    pname[p["program_id"]] = (p["program"] or "").split(" ©")[0]
    P.append(dict(key=p["key"], pid=p["program_id"], first=p["first_seen"], last=p["last_seen"], out=p["outcome"], pgy=p["last_pgy"], notes=p.get("notes") or [], ev=p.get("evidence_level"), entry=p["entry_year"]))
have = {(q["pid"], q["key"].split(":")[-1]) for q in P}
for r in adj:  # pre-2011 entrants still on duty in the window (not already in merged)
    if r["entry"] >= 2011 or r["pid"] == 47 or not r["last"][:4].isdigit():
        continue
    last = f'{r["last"][:4]}-{int(r["last"][:4]) + 1}'
    t = re.sub(r"[^A-Za-z \-]", " ", r["name"]).split()
    if last < YEARS[0] or not t or (r["pid"], t[-1].lower()) in have:
        continue
    out = "completed" if r["out"].startswith("COMPLETED") else "transferred" if "TRANSFERRED" in r["out"] else "deceased" if r["out"].startswith("DIED") else "left_destination_unknown"
    P.append(dict(key=f'adj:{r["pid"]}:{r["name"]}', pid=r["pid"], first=f'{r["entry"]}-{r["entry"] + 1}', last=last, out=out, pgy=int(r["pgy"]) if r["pgy"].isdigit() else None, notes=[], ev=None, entry=r["entry"]))

duty_py = Counter()  # resident-years on duty in window, per program
for q in P:
    for y in YEARS:
        if q["first"] <= y <= q["last"]:
            duty_py[q["pid"]] += 1
dep = [q for q in P if q["last"] in YEARS and q["out"] not in ("completed", "in_training") and not (q["out"] == "transferred" and (q["pid"], q["last"]) in CLOSURE)]
left = [q for q in dep if q["out"] in LEFT]
trans = [q for q in dep if q["out"] == "transferred"]
RY = sum(duty_py.values())
nat = len(left) / RY

# destination of those who left NS
PAT = [("Radiology (diagnostic/interventional)", r"radiolog|neuroradiolog|\bIR\b"), ("Radiation oncology", r"radiation oncolog|rad onc"), ("Neurology", r"\bneurology\b"),
       ("Anesthesiology / pain", r"anesthes|pain medicine"), ("Emergency medicine", r"emergency medicine"), ("Orthopaedics", r"orthop"), ("Psychiatry", r"psychiatr"),
       ("Internal medicine", r"internal medicine|gastroenterolog|cardiolog"), ("Family / primary care", r"family medicine|primary care|general practi|urgent care"),
       ("General / other surgery", r"general surgery|plastic|urolog|vascular surgery|cardiac surgery|otolaryng"), ("Other specialty", r"ophthalm|dermatolog|patholog|pediatric|physical medicine|PM&R|preventive|occupational|aerospace|wound|genetics")]
def dest(q):
    if q["out"] == "left_medicine":
        return "Left clinical medicine"
    if q["out"] in ("left_destination_unknown", "unknown"):
        return "Destination not found"
    f = fin.get(q["key"], {})
    txt = " ".join([str(f.get("destination_program") or ""), str(f.get("current") or ""), str(f.get("outcome_detail") or ""), " ".join(q["notes"])])
    txt = re.sub(r"neurological surgery|neurosurg\w*", " ", txt, flags=re.I)
    for lab, rx in PAT:
        if re.search(rx, txt, re.I):
            return lab
    return "Other (PA, non-physician role)" if q["out"] == "left_other" else "Other specialty"
def stage(p):
    return "Junior (PGY-1–2)" if p in (1, 2) else "Middle (PGY-3–4)" if p in (3, 4) else "Senior (PGY-5–7)" if p and p >= 5 else "Unknown"
xt = defaultdict(Counter)
for q in left:
    xt[stage(q["pgy"])][dest(q)] += 1
trst = Counter(stage(q["pgy"]) for q in trans)

# per program (annual rate per resident-year), exact Poisson vs national
prog = []
for pid, ry in duty_py.items():
    k = sum(1 for q in left if q["pid"] == pid)
    pv = 1 - poisson.cdf(k - 1, nat * ry) if k else 1.0
    prog.append(dict(pid=pid, program=pname.get(pid, str(pid)), resident_years=ry, left=k, annual_rate=100 * k / ry, expected=nat * ry, p=pv))
q = multipletests([r["p"] for r in prog], method="fdr_bh")[1]
for r, qq in zip(prog, q):
    r["q"] = qq
prog.sort(key=lambda r: -r["annual_rate"])
rates = sorted(r["annual_rate"] for r in prog)
def pct(a, f):
    i = (len(a) - 1) * f; lo = int(i); return a[lo] + (a[min(lo + 1, len(a) - 1)] - a[lo]) * (i - lo)
# by year
by_year = []
for y in YEARS:
    d = [q for q in dep if q["last"] == y]
    duty = sum(1 for q in P if q["first"] <= y <= q["last"])
    by_year.append(dict(year=y, on_duty=duty, left=sum(q["out"] in LEFT for q in d), transferred=sum(q["out"] == "transferred" for q in d)))
pgy_tbl = {g: dict(transferred=sum(q["out"] == "transferred" and q["pgy"] == g for q in dep), left=sum(q["out"] in LEFT and q["pgy"] == g for q in dep)) for g in [1, 2, 3, 4, 5, 6, 7, None]}
res = dict(pgy_table=pgy_tbl, window=f"{YEARS[0]} to {YEARS[-1]}", resident_years=RY, departures=len(dep), left_ns=len(left), transferred_ns=len(trans), died=sum(q["out"] == "deceased" for q in dep),
           annual_left_rate=100 * nat, annual_departure_rate=100 * len(dep) / RY, by_year=by_year,
           stage_counts=dict(Counter(stage(q["pgy"]) for q in left)), stage_dest={k: dict(v.most_common()) for k, v in xt.items()}, transfers_by_stage=dict(trst),
           programs=len(prog), programs_zero=sum(r["left"] == 0 for r in prog), median_rate=pct(rates, .5), iqr=(pct(rates, .25), pct(rates, .75)), max_rate=rates[-1],
           above_2x=sum(r["annual_rate"] > 2 * 100 * nat for r in prog), fdr_sig=[(r["program"], r["left"], r["resident_years"], round(r["q"], 3)) for r in prog if r["q"] < 0.05],
           p05=[(r["program"], r["left"], r["resident_years"], round(r["p"], 4)) for r in prog if r["p"] < 0.05],
           evidence=dict(Counter(q["ev"] or "none" for q in left)), program_rows=prog)
json.dump(res, open("data/verify/report/window_analysis.json", "w"), indent=1, default=float)
for k in ("window", "resident_years", "departures", "left_ns", "transferred_ns", "died", "annual_left_rate", "annual_departure_rate", "stage_counts", "transfers_by_stage",
          "programs", "programs_zero", "median_rate", "iqr", "max_rate", "above_2x", "fdr_sig", "p05", "evidence"):
    print(k, res[k])
for s, d in res["stage_dest"].items():
    print(s, d)
print([(r["year"], r["on_duty"], r["left"], r["transferred"]) for r in by_year])
