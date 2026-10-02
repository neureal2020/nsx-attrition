#!/usr/bin/env python3
"""Program x academic-year roster confidence, clustered, as an Excel heat map.

    python3 scripts/tools/confidence_heatmap.py

Inputs: data/verify/programs/coverage.csv (gap-file audit), program_years.json (NRMP filled per match year),
roster_holes.json + holes_*_out.json (unexplained NRMP shortfalls), and hand-coded weak years for the 12 programs
audited in docs/PROGRAM_STATUS.md. Output: data/verify/programs/program_year_confidence.xlsx.

Levels:
  high   roster observed that year, and the entering class matches the NRMP filled count
  medium roster not archived that year, but every continuing resident reappears after the gap AND the entering class
         matches the NRMP filled count (so no one can be hidden in it)
  low    a continuing resident could have left unseen (gap judged significant, or no roster on one side), or the entering
         class is smaller than the NRMP filled count with the difference unexplained (a new intern could be hidden)
"""
import csv, json, glob
from collections import defaultdict
import numpy as np
from scipy.cluster.hierarchy import linkage, leaves_list, optimal_leaf_ordering
from scipy.spatial.distance import pdist
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment
from openpyxl.utils import get_column_letter

P = "data/verify/programs"
YEARS = [f"{y}-{y + 1}" for y in range(2011, 2025)]
rows = [r for r in csv.DictReader(open(f"{P}/coverage.csv")) if r["program_id"] != "47"]  # NCC removed (user 2026-09-30)
filled = defaultdict(int)
for r in json.load(open(f"{P}/program_years.json")):
    if r.get("our_program_id") and r.get("positions_filled") is not None:
        filled[(int(r["our_program_id"]), int(r["match_year"]))] += int(r["positions_filled"])

# Hand-coded from docs/PROGRAM_STATUS.md (programs audited before the gap-file format existed)
DETAILED = {
    4: {"low": ["2011-2012", "2012-2013"], "medium": ["2015-2016", "2021-2022"]},  # Barrow: no roster archived 2010-13
    19: {"low": [], "medium": ["2021-2022"]},  # Duke: one name reconstructed
    30: {"low": [], "medium": ["2018-2019"]},  # Hopkins: 2018-19 from photo caption; extraction dropped 2 people (fixed)
    40: {"low": ["2011-2012", "2012-2013", "2013-2014", "2014-2015"], "medium": ["2017-2018", "2018-2019"]},  # Mayo Rochester: no roster published 2011-15
    41: {"low": [], "medium": []}, 76: {"low": [], "medium": []}, 91: {"low": [], "medium": []}, 116: {"low": [], "medium": []},
    60: {"low": [], "medium": ["2011-2012", "2014-2015", "2015-2016", "2018-2019", "2019-2020", "2022-2023"]},  # SLU
    67: {"low": ["2011-2012", "2012-2013", "2013-2014"], "medium": []},  # UCLA: roster never archived 2011-14
    100: {"low": [], "medium": ["2016-2017", "2017-2018", "2021-2022", "2022-2023", "2023-2024"]},  # Penn
    120: {"low": [], "medium": ["2011-2012", "2020-2021", "2021-2022", "2022-2023"]},  # WashU
}
# Unexplained NRMP shortfalls (unnamed matchee who left / never started before the first roster) -> low in that entry year
UNNAMED = set()
for f in glob.glob(f"{P}/holes_*_out.json"):
    for r in json.load(open(f)):
        if any(m.get("fate") == "unknown" and not m.get("in_our_data_as") for m in r.get("matchees", [])):
            UNNAMED.add((int(r["program_id"]), f"{r['match_year']}-{int(r['match_year']) + 1}"))

# Entering-class check (user 2026-09-30): an intern who starts and leaves between archived rosters is invisible to
# rosters; the NRMP filled count catches it. Entrants we hold per program x entry year (all merged people, incl.
# additions and entry-year fixes) vs NRMP filled; a shortfall not offset by a surplus in an adjacent entry year
# (entry-year misdating) and not explained by the roster-hole checks marks that year LOW.
merged = json.load(open("data/verify/phase3/merged_final.json"))
ent = defaultdict(int)
for q in merged:
    if q.get("entry_year") and not q["outcome_2025"].startswith("excluded_not") and q["program_id"] != 47:
        ent[(q["program_id"], q["entry_year"])] += 1
EXPLAINED = set()
for f in glob.glob(f"{P}/holes_*_out.json"):
    for r in json.load(open(f)):
        if not any(m.get("fate") == "unknown" and not m.get("in_our_data_as") for m in r.get("matchees", [])):
            EXPLAINED.add((int(r["program_id"]), int(r["match_year"])))
def entrant_gap(pid, yr):
    f = filled.get((pid, yr))
    if f is None:
        return None, None, 0
    short = f - ent[(pid, yr)]
    if short <= 0 or (pid, yr) in EXPLAINED:
        return f, ent[(pid, yr)], 0
    adj = sum(max(0, ent[(pid, a)] - filled.get((pid, a), ent[(pid, a)])) for a in (yr - 1, yr + 1))
    return f, ent[(pid, yr)], max(0, short - adj)

RED_RESOLVED = {}  # final red-year search (data/verify/programs/red_*_out.json)
for f in glob.glob(f"{P}/red_*_out.json"):
    for r in json.load(open(f)):
        for yv in r.get("years", []):
            if yv.get("resolved"):
                RED_RESOLVED[(int(r["program_id"]), yv["year"])] = (yv.get("how") or "")[:200]
level, reason, names, extra = {}, {}, {}, {}
byprog = defaultdict(list)
for r in rows:
    byprog[int(r["program_id"])].append(r)
runlen = {}
for pid, rs in byprog.items():
    rs.sort(key=lambda r: r["year"])
    i = 0
    while i < len(rs):
        if rs[i]["status"].startswith(("reconstructed", "missing")):
            j = i
            while j < len(rs) and rs[j]["status"].startswith(("reconstructed", "missing")):
                j += 1
            for k in range(i, j):
                runlen[(pid, rs[k]["year"])] = j - i
            i = j
        else:
            i += 1
for r in rows:
    pid, y = int(r["program_id"]), r["year"]
    names[pid] = r["program"].split(" ©")[0].replace(" Program", "")[:60]
    if r["status"] in ("before_program", "not_applicable"):
        level[(pid, y)], reason[(pid, y)] = "n/a", "program not yet open"
        extra[(pid, y)] = ("", "", "")
        continue
    if pid in DETAILED:
        d = DETAILED[pid]
        lv = "low" if y in d["low"] else "medium" if y in d["medium"] else "high"
        why = "PROGRAM_STATUS.md audit"
    elif r["status"].startswith("observed"):
        lv, why = "high", f"roster observed ({r['listed']} listed)"
    elif r["grade"] == "C":
        lv, why = "low", f"{r['status']}; gap judged significant (a continuing resident could have left unseen)"
    else:
        lv, why = "medium", f"{r['status']}; continuing residents reappear after the gap"
    f, e_, short = entrant_gap(pid, int(y[:4]))
    if short > 0:
        lv, why = "low", why + f"; entering class {e_} vs {f} matched (NRMP): {short} entrant(s) unaccounted for"
    elif f is not None and lv == "medium":
        why += f"; entering class complete ({e_} vs {f} matched)"
    if lv == "low" and (pid, y) in RED_RESOLVED:
        lv, why = "medium", why + "; RESOLVED in final search: " + RED_RESOLVED[(pid, y)]
    level[(pid, y)], reason[(pid, y)] = lv, why
    extra[(pid, y)] = (runlen.get((pid, y), 0) or "", "" if f is None else f, "" if f is None else e_)

pids = sorted(names)
score = {"high": 0, "medium": 1, "low": 2, "n/a": 0}
M = np.array([[score[level.get((p, y), "n/a")] for y in YEARS] for p in pids], dtype=float)
weak = M.sum(axis=1) > 0
wp = [p for p, w in zip(pids, weak) if w]
Mw = M[weak]
Z = optimal_leaf_ordering(linkage(Mw, "average", metric="euclidean"), Mw)
order = [wp[i] for i in leaves_list(Z)]
# weakest clusters first, fully-high programs last
order = order + [p for p, w in zip(pids, weak) if not w]

wb = Workbook()
ws = wb.active
ws.title = "Confidence heatmap"
RED, YEL, GRY = PatternFill("solid", fgColor="F4A6A6"), PatternFill("solid", fgColor="FFE699"), PatternFill("solid", fgColor="D9D9D9")
ws.append(["ID", "Program"] + YEARS + ["# low", "# medium"])
for c in ws[1]:
    c.font = Font(bold=True)
    c.alignment = Alignment(horizontal="center", text_rotation=90 if c.column > 2 else 0)
for p in order:
    lv = [level.get((p, y), "n/a") for y in YEARS]
    ws.append([p, names[p]] + [{"high": "", "medium": "M", "low": "L", "n/a": "–"}[v] for v in lv] + [lv.count("low"), lv.count("medium")])
    rr = ws.max_row
    for j, v in enumerate(lv):
        cell = ws.cell(row=rr, column=3 + j)
        cell.alignment = Alignment(horizontal="center")
        if v == "low": cell.fill = RED
        elif v == "medium": cell.fill = YEL
        elif v == "n/a": cell.fill = GRY
ws.column_dimensions["A"].width = 5
ws.column_dimensions["B"].width = 48
for j in range(len(YEARS) + 2):
    ws.column_dimensions[get_column_letter(3 + j)].width = 4.5
ws.freeze_panes = "C2"

ws2 = wb.create_sheet("By year")
ws2.append(["Year", "high", "medium", "low", "not open"])
for y in YEARS:
    c = [level.get((p, y), "n/a") for p in pids]
    ws2.append([y, c.count("high"), c.count("medium"), c.count("low"), c.count("n/a")])

ws3 = wb.create_sheet("Detail")
ws3.append(["ID", "Program", "Year", "Confidence", "Gap length (yrs, if roster not archived)", "NRMP matched that year", "Entrants we hold", "Reason"])
for p in order:
    for y in YEARS:
        ex = extra.get((p, y), ("", "", ""))
        ws3.append([p, names[p], y, level.get((p, y), "n/a"), *ex, reason.get((p, y), "")])

ws4 = wb.create_sheet("Method")
for line in (__doc__ or "").strip().splitlines():
    ws4.append([line])
ws4.append([""])
ws4.append(["Row order: programs with any medium/low year are clustered (average linkage on the year pattern, optimal leaf ordering) so programs with similar weak years sit together; programs with all-high years follow."])
ws4.column_dimensions["A"].width = 140
wb.save(f"{P}/program_year_confidence.xlsx")
tot = {k: sum(1 for v in level.values() if v == k) for k in ("high", "medium", "low", "n/a")}
print(f"programs {len(pids)} (weak {len(wp)}); program-years {tot}; unnamed-matchee lows {len(UNNAMED)}")
