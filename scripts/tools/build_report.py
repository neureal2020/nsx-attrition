#!/usr/bin/env python3
"""Build the attrition report page (static HTML with inline SVG charts).

    python3 scripts/tools/build_report.py

Inputs: data/verify/report/analysis.json, program_rates.csv, data/verify/programs/*, data/verify/lit/literature.json.
Output: data/verify/report/report.html
"""
import csv, html, json, math
from scipy.stats import binom
import openpyxl

R = "data/verify/report"
A = json.load(open(f"{R}/analysis.json"))
PROG = list(csv.DictReader(open(f"{R}/program_rates.csv")))
NT = {r["academic_year"]: r for r in json.load(open("data/verify/programs/national_totals.json"))}
COV = list(csv.DictReader(open("data/verify/programs/coverage.csv")))
WB = openpyxl.load_workbook("data/verify/programs/program_year_confidence.xlsx")
HM = [r for r in WB["Confidence heatmap"].iter_rows(values_only=True)]
BYYEAR = [r for r in WB["By year"].iter_rows(min_row=2, values_only=True)]
e = html.escape
N, K = A["cohort"], A["attrition"]
p0 = K / N


def pct(x, d=1):
    return f"{x:.{d}f}%"


# ---------- chart helpers ----------
def bar_chart(items, w=720, h=260, ymax=None, ylab="%", ci=True, highlight=None, fmt=lambda v: f"{v:.1f}"):
    """items: list of dict(label, value, lo, hi, muted, tip)"""
    ml, mr, mt, mb = 44, 12, 14, 34
    pw, ph = w - ml - mr, h - mt - mb
    ymax = ymax or max((it.get("hi") or it["value"]) for it in items) * 1.1
    step = 2 if ymax <= 12 else 5 if ymax <= 30 else 10
    ymax = math.ceil(ymax / step) * step
    y = lambda v: mt + ph - ph * v / ymax
    bw = pw / len(items)
    s = [f'<svg viewBox="0 0 {w} {h}" class="chart" role="img">']
    for t in range(0, int(ymax) + 1, step):
        s.append(f'<line x1="{ml}" x2="{w - mr}" y1="{y(t):.1f}" y2="{y(t):.1f}" class="grid"/>'
                 f'<text x="{ml - 6}" y="{y(t) + 4:.1f}" class="tick" text-anchor="end">{t}{ylab}</text>')
    for i, it in enumerate(items):
        x = ml + i * bw + bw * 0.18
        bwid = bw * 0.64
        top = y(it["value"])
        cls = "bar muted" if it.get("muted") else "bar"
        r = min(4, bwid / 2)
        hgt = max(0.0, y(0) - top)
        s.append(f'<g class="mark"><title>{e(it.get("tip", ""))}</title>'
                 f'<path d="M{x:.1f},{y(0):.1f} V{top + r:.1f} Q{x:.1f},{top:.1f} {x + r:.1f},{top:.1f} H{x + bwid - r:.1f} Q{x + bwid:.1f},{top:.1f} {x + bwid:.1f},{top + r:.1f} V{y(0):.1f} Z" class="{cls}"/>'
                 if hgt > r else f'<g class="mark"><title>{e(it.get("tip", ""))}</title><rect x="{x:.1f}" y="{top:.1f}" width="{bwid:.1f}" height="{hgt:.1f}" class="{cls}"/>')
        if ci and it.get("lo") is not None:
            cx = x + bwid / 2
            s.append(f'<line x1="{cx:.1f}" x2="{cx:.1f}" y1="{y(it["hi"]):.1f}" y2="{y(it["lo"]):.1f}" class="whisk"/>'
                     f'<line x1="{cx - 4:.1f}" x2="{cx + 4:.1f}" y1="{y(it["hi"]):.1f}" y2="{y(it["hi"]):.1f}" class="whisk"/>'
                     f'<line x1="{cx - 4:.1f}" x2="{cx + 4:.1f}" y1="{y(it["lo"]):.1f}" y2="{y(it["lo"]):.1f}" class="whisk"/>')
        s.append(f'<rect x="{ml + i * bw:.1f}" y="{mt}" width="{bw:.1f}" height="{ph}" class="hit"/></g>')
        s.append(f'<text x="{ml + i * bw + bw / 2:.1f}" y="{h - mb + 16}" class="tick" text-anchor="middle">{e(str(it["label"]))}</text>')
    if highlight is not None:
        s.append(f'<line x1="{ml}" x2="{w - mr}" y1="{y(highlight[0]):.1f}" y2="{y(highlight[0]):.1f}" class="ref"/>'
                 f'<text x="{w - mr}" y="{y(highlight[0]) - 5:.1f}" class="reflab" text-anchor="end">{e(highlight[1])}</text>')
    s.append(f'<line x1="{ml}" x2="{w - mr}" y1="{y(0):.1f}" y2="{y(0):.1f}" class="axis"/></svg>')
    return "".join(s)


def hbar(items, w=720, rowh=24, unit=""):
    ml, mr = 250, 60
    mx = max(v for _, v in items)
    s = [f'<svg viewBox="0 0 {w} {rowh * len(items) + 8}" class="chart" role="img">']
    for i, (lab, v) in enumerate(items):
        yy = 4 + i * rowh
        bw = (w - ml - mr) * v / mx
        s.append(f'<g class="mark"><title>{e(lab)}: {v}</title><text x="{ml - 8}" y="{yy + rowh / 2 + 4:.1f}" class="lab" text-anchor="end">{e(lab)}</text>'
                 f'<rect x="{ml}" y="{yy + 4}" width="{bw:.1f}" height="{rowh - 8}" rx="3" class="bar"/>'
                 f'<text x="{ml + bw + 6:.1f}" y="{yy + rowh / 2 + 4:.1f}" class="val">{v}{unit}</text></g>')
    s.append("</svg>")
    return "".join(s)


def funnel(w=720, h=380):
    ml, mr, mt, mb = 48, 16, 14, 40
    pw, ph = w - ml - mr, h - mt - mb
    xs = [int(r["residents"]) for r in PROG]
    xmax = math.ceil(max(xs) / 10) * 10
    ymax = 35
    X = lambda n: ml + pw * n / xmax
    Y = lambda v: mt + ph - ph * v / ymax
    s = [f'<svg viewBox="0 0 {w} {h}" class="chart" role="img">']
    for t in range(0, ymax + 1, 5):
        s.append(f'<line x1="{ml}" x2="{w - mr}" y1="{Y(t):.1f}" y2="{Y(t):.1f}" class="grid"/><text x="{ml - 6}" y="{Y(t) + 4:.1f}" class="tick" text-anchor="end">{t}%</text>')
    for t in range(0, xmax + 1, 10):
        s.append(f'<text x="{X(t):.1f}" y="{h - mb + 16}" class="tick" text-anchor="middle">{t}</text>')
    s.append(f'<text x="{ml + pw / 2:.1f}" y="{h - 6}" class="tick" text-anchor="middle">Residents in cohort (program size)</text>')
    for q, cls, lab in ((0.975, "lim95", "95% limit"), (0.999, "lim998", "99.8% limit")):
        pts = []
        for n in range(5, xmax + 1):
            k = binom.ppf(q, n, p0)
            pts.append(f"{X(n):.1f},{Y(min(ymax, 100 * k / n)):.1f}")
        s.append(f'<polyline points="{" ".join(pts)}" class="{cls}"/>')
        s.append(f'<text x="{X(xmax) - 4:.1f}" y="{Y(100 * binom.ppf(q, xmax, p0) / xmax) - 5:.1f}" class="reflab" text-anchor="end">{lab}</text>')
    s.append(f'<line x1="{ml}" x2="{w - mr}" y1="{Y(100 * p0):.1f}" y2="{Y(100 * p0):.1f}" class="ref"/>'
             f'<text x="{ml + 6}" y="{Y(100 * p0) - 5:.1f}" class="reflab">National {100 * p0:.1f}%</text>')
    for r in PROG:
        n, k = int(r["residents"]), int(r["attrition"])
        v = 100 * k / n
        cls = "dot hot" if r["above_95"] == "True" else "dot"
        s.append(f'<circle cx="{X(n):.1f}" cy="{Y(min(v, ymax)):.1f}" r="5" class="{cls}"><title>{e(r["program"])}: {k}/{n} ({v:.1f}%), p={float(r["p_greater"]):.3f}, q={float(r["q_bh"]):.2f}</title></circle>')
    s.append(f'<line x1="{ml}" x2="{w - mr}" y1="{Y(0):.1f}" y2="{Y(0):.1f}" class="axis"/></svg>')
    return "".join(s)


def stacked_years(w=720, h=250):
    ml, mr, mt, mb = 40, 12, 12, 34
    pw, ph = w - ml - mr, h - mt - mb
    tot = max(r[1] + r[2] + r[3] for r in BYYEAR)
    bw = pw / len(BYYEAR)
    Y = lambda v: mt + ph - ph * v / tot
    s = [f'<svg viewBox="0 0 {w} {h}" class="chart" role="img">']
    for t in range(0, tot + 1, 20):
        s.append(f'<line x1="{ml}" x2="{w - mr}" y1="{Y(t):.1f}" y2="{Y(t):.1f}" class="grid"/><text x="{ml - 6}" y="{Y(t) + 4:.1f}" class="tick" text-anchor="end">{t}</text>')
    for i, (yr, hi, me, lo, na) in enumerate(BYYEAR):
        x = ml + i * bw + bw * 0.15
        wd = bw * 0.7
        base = 0
        for v, cls, nm in ((hi, "c-hi", "high"), (me, "c-me", "medium"), (lo, "c-lo", "low")):
            if v:
                y1, y0 = Y(base + v), Y(base)
                s.append(f'<rect x="{x:.1f}" y="{y1 + 1:.1f}" width="{wd:.1f}" height="{max(0, y0 - y1 - 2):.1f}" class="{cls}"><title>{yr}: {v} programs {nm}</title></rect>')
                base += v
        s.append(f'<text x="{x + wd / 2:.1f}" y="{h - mb + 16}" class="tick" text-anchor="middle">{yr[2:4]}–{yr[7:9]}</text>')
    s.append("</svg>")
    return "".join(s)



def program_bars(minres=20, w=720, rowh=17):
    """Sorted bars per program (>= minres residents) with the range expected by chance for that size."""
    rows = [r for r in PROG if int(r["residents"]) >= minres]
    rows.sort(key=lambda r: -float(r["rate"]))
    ml, mr, mt = 260, 50, 26
    xmax = 25
    X = lambda v: ml + (w - ml - mr) * min(v, xmax) / xmax
    h = mt + rowh * len(rows) + 10
    s = [f'<svg viewBox="0 0 {w} {h}" class="chart" role="img">']
    for t in range(0, xmax + 1, 5):
        s.append(f'<line x1="{X(t):.1f}" x2="{X(t):.1f}" y1="{mt - 6}" y2="{h - 6}" class="grid"/><text x="{X(t):.1f}" y="{mt - 10}" class="tick" text-anchor="middle">{t}%</text>')
    for i, r in enumerate(rows):
        n, k = int(r["residents"]), int(r["attrition"])
        lo, hi = 100 * binom.ppf(0.025, n, p0) / n, 100 * binom.ppf(0.975, n, p0) / n
        y = mt + i * rowh
        v = 100 * k / n
        out = k > binom.ppf(0.975, n, p0)
        nm = r["program"].replace(" Program", "").replace("University of ", "U. ").replace("Medical Center", "MC")[:38]
        s.append(f'<g class="mark"><title>{e(r["program"])}: {k} of {n} left ({v:.1f}%). By chance alone a program this size would usually fall between {lo:.0f}% and {hi:.0f}%.</title>'
                 f'<rect x="{X(lo):.1f}" y="{y + 2}" width="{max(1, X(hi) - X(lo)):.1f}" height="{rowh - 4}" class="band"/>'
                 f'<rect x="{ml}" y="{y + 5}" width="{max(0, X(v) - ml):.1f}" height="{rowh - 10}" rx="2" class="{"bar hotbar" if out else "bar"}"/>'
                 f'<text x="{ml - 8}" y="{y + rowh - 5}" class="lab" text-anchor="end">{e(nm)}</text>'
                 f'<text x="{X(v) + 5:.1f}" y="{y + rowh - 5}" class="val">{k}/{n}</text></g>')
    s.append(f'<line x1="{X(100 * p0):.1f}" x2="{X(100 * p0):.1f}" y1="{mt - 6}" y2="{h - 6}" class="ref"/></svg>')
    return "".join(s), len(rows)

# ---------- data blocks ----------
cls_items = [dict(label=str(c["entry_year"]), value=c["rate"], lo=c["ci95"][0], hi=c["ci95"][1], muted=not c["complete_class"],
                  tip=f'{c["entry_year"]} class: {c["attrition"]} of {c["entrants"]} ({c["rate"]}%), 95% CI {c["ci95"][0]}–{c["ci95"][1]}%'
                  + ("" if c["complete_class"] else " — still in training; will rise")) for c in A["by_entry_class"]]
ay_items = [dict(label=r["year"][2:4] + "–" + r["year"][7:9], value=r["rate"], lo=r["ci95"][0], hi=r["ci95"][1],
                 tip=f'{r["year"]}: {r["departures"]} of {r["residents"]} residents left ({r["rate"]}%)') for r in A["by_academic_year"]]
pgy = A["pgy_at_exit"]
pgy_items = [dict(label=f"PGY-{k}" if k != "0" else "unk.", value=100 * v / K, tip=f"PGY-{k}: {v} residents ({100 * v / K:.0f}% of attrition)")
             for k, v in pgy.items() if k != "0"]
types = A["attrition_types"]
TYPELAB = {"switched_specialty": "Switched specialty", "left_destination_unknown": "Left, destination not found", "left_medicine": "Left clinical medicine", "left_other": "Other (e.g. PA, general practice)"}
c18 = A["complete_classes_2011_2018"]
early = pgy.get("1", 0) + pgy.get("2", 0)
dest = sorted(A["switch_destinations"].items(), key=lambda x: -x[1])
unk = types.get("left_destination_unknown", 0)

# coverage vs ACGME
cov_tot = {}
for r in COV:
    cov_tot[r["year"]] = cov_tot.get(r["year"], 0) + int(r["listed"])
acgme_rows = "".join(f'<tr><td>{y}</td><td class="n">{NT[y]["programs_count"]}</td><td class="n">{NT[y]["residents_on_duty"]:,}</td><td class="n">{cov_tot[y]:,}</td>'
                     f'<td class="n">{100 * cov_tot[y] / NT[y]["residents_on_duty"]:.0f}%</td></tr>' for y in sorted(NT) if y in cov_tot)

# heatmap grid (clustered order from workbook)
years = HM[0][2:16]
hm_rows = []
for r in HM[1:]:
    cells = "".join(f'<td class="{ {"L": "c-lo", "M": "c-me", "–": "c-na"}.get(v or "", "c-hi")}" title="{e(str(r[1]))} {years[j]}: {({"L": "low", "M": "medium", "–": "not open"}).get(v or "", "high")}"></td>'
                    for j, v in enumerate(r[2:16]))
    hm_rows.append(f'<tr><th scope="row">{e(str(r[1]))}</th>{cells}</tr>')
hm_head = "".join(f"<th>{y[2:4]}</th>" for y in years)

# program table
def verdict(r):
    n, k = int(r["residents"]), int(r["attrition"])
    if k == 0: return "No one left"
    if k > binom.ppf(0.975, n, p0): return "Higher than chance alone would usually give"
    return "Within the normal range" if 100 * k / n > 100 * p0 else "At or below average"
def rosterq(r):
    lo, me = int(r.get("low_confidence_years") or 0), int(r.get("medium_confidence_years") or 0)
    return "complete" if lo == 0 and me == 0 else (f"{lo} uncertain yr" + ("s" if lo != 1 else "") if lo else f"{me} filled-in yr" + ("s" if me != 1 else ""))
prog_sorted = sorted(PROG, key=lambda r: (-float(r["rate"]), -int(r["residents"])))
prog_rows = "".join(
    f'<tr><td>{e(r["program"].replace(" Program", ""))}</td><td class="n">{r["residents"]}</td><td class="n">{r["attrition"]}</td>'
    f'<td class="n">{float(r["rate"]):.1f}%</td><td>{verdict(r)}</td><td class="muted">{rosterq(r)}</td></tr>' for r in prog_sorted)
top = [r for r in prog_sorted if int(r["residents"]) >= 20][:5]
top_txt = "; ".join(f'{e(r["program"].split(" Program")[0].replace("University of ", "U. "))} {r["attrition"]}/{r["residents"]}' for r in top)

LIT = [
    ("Lynch 2015, J Neurosurg", "Matched 1990–99 (n=1,361)", "Did not complete residency", "14.0% (86.0% completed); women 24%, men 12.8%", "full text"),
    ("Renfrow 2016, J Neurosurg", "Matched 2000–09 (n=1,992)", "Did not complete neurosurgery", "6.7% (women 17%, men 5.3%); 76% in PGY-1–3", "full text"),
    ("Agarwal 2019, J Neurosurg", "Started 2005–10 (n=1,275)", "Left first program, incl. NS→NS transfers and deaths", "11.0% as published; 7.7% on our definition (98/1,275)", "full text"),
    ("Haruno 2023, JAMA Surg", "2001–18 (n=4,434)", "Withdrew, dismissed or changed specialty; NS→NS transfers not counted", "10.4%, highest surgical specialty", "full text"),
    ("Yaeger 2020, Neurosurg Focus", "AY 2009–19", "ACGME annual, transfers included", "2.6% per year (all ACGME 2.1%)", "full text"),
    ("Kabangu 2023, World Neurosurg", "AY 2007–22", "ACGME annual: transfer + withdrawal + dismissal", "2.5% per year; 2.7% pre-COVID vs 1.7% during", "full text"),
    ("Sundel 2024, J Surg Educ", "AY 2012–21", "ACGME annual, transfers included", "Neurosurgery 2.1% per year", "full text"),
    ("Kabangu 2023, Neurosurgery", "Matriculants 2017–20", "Retention from public listings", "93–95% retained; no sex or race difference", "full text"),
    ("Chainey 2026 (Canada)", "2013–23", "Program-reported attrition", "Mean institutional 14.1% (range 0–28.6%)", "full text"),
    ("Khoushhal 2017, JAMA Surg (general surgery)", "22 studies to 2015", "Left program; transfers counted", "18% pooled", "full text"),
]
lit_rows = "".join(f'<tr><td>{e(a)}</td><td>{e(b)}</td><td>{e(c)}</td><td>{e(d)}</td><td class="muted">{e(f)}</td></tr>' for a, b, c, d, f in LIT)
PDFS = [
    ("Agarwal N et al. Analysis of national trends in neurosurgical resident attrition. J Neurosurg 2019;131(5):1668-73.", "10.3171/2018.5.JNS18519", "Recompute their rate without NS→NS transfers; PGY and program breakdown."),
    ("Renfrow JJ et al. Positive trends in neurosurgery enrollment and attrition (2000-2009 cohort). J Neurosurg 2016;124(3):834-9.", "10.3171/2015.3.JNS142313", "How transfers were handled; PGY distribution."),
    ("Lynch G et al. Attrition rates in neurosurgery residency: 1361 residents matched 1990-1999. J Neurosurg 2015;122(2):240-9.", "10.3171/2014.10.JNS132436", "Completion definition; transfer handling."),
    ("Kabangu JK et al. Neurosurgery resident attrition rates defy trends and decrease during COVID-19. World Neurosurg 2023;179:e374-9.", "10.1016/j.wneu.2023.08.093", "Yearly ACGME rates split into transfer / withdrawal / dismissal."),
    ("Kabangu JK et al. Evaluating match and attrition rates for women and African Americans in neurosurgery. Neurosurgery 2023;92(4):695-702.", "10.1227/neu.0000000000002257", "Public-roster method closest to ours; 2017-20 overlap for direct comparison."),
    ("Yaeger KA et al. Trends in US neurosurgery residency education and training 2009-2019. Neurosurg Focus 2020;48(3):E6.", "10.3171/2019.12.FOCUS19827", "Year-by-year graduation and attrition table."),
    ("Raman HS et al. Prevalence, management and outcome of problem residents. J Neurosurg 2019;130(1):322-6.", "10.3171/2017.8.JNS171719", "Program-director view of departures."),
    ("Kabangu JK et al. Gender parity in neurosurgery residencies. J Neurosurg 2024;141(1):48-54.", "10.3171/2023.11.JNS231152", "Attrition vs. share of women residents."),
    ("Sundel M et al. Cutting ties: general surgery residents have higher attrition. J Surg Educ 2024;81(7):900-4.", "10.1016/j.jsurg.2024.04.004", "Neurosurgery annual rate 2012-22 (in full text only)."),
    ("Cusimano MD et al. An analysis of attrition from Canadian neurosurgery residency programs. Acad Med 1999;74(8):925-31.", "10.1097/00001888-199908000-00019", "Verify the unconfirmed 42.6% figure."),
    ("Khoushhal Z et al. Prevalence and causes of attrition among surgical residents: meta-analysis. JAMA Surg 2017;152(3):265-72.", "10.1001/jamasurg.2016.4086", "General-surgery comparator."),
    ("Shweikeh F et al. Status of resident attrition from surgical residency. J Surg Educ 2018;75(2):254-62.", "10.1016/j.jsurg.2017.07.015", "Annual vs. cumulative comparator."),
    ("Yeo H et al. A national study of attrition in general surgery training. Ann Surg 2010;252(3):529-34.", "10.1097/SLA.0b013e3181f2789c", "Where leavers go (destination comparison)."),
]
pdf_rows = "".join(f'<li><span class="cite">{e(c)}</span> <a href="https://doi.org/{d}" target="_blank" rel="noopener">doi:{d}</a><span class="why">{e(w)}</span></li>' for c, d, w in PDFS)

PB, _npb = program_bars()
ev = A["evidence_levels"]
from statsmodels.stats.proportion import proportion_confint as _pc
_det = {(r[0], r[2]): r[3] for r in WB["Detail"].iter_rows(min_row=2, values_only=True)}
_m = [q for q in json.load(open("data/verify/phase3/merged_final.json")) if not q["outcome_2025"].startswith("excluded")]
def _touch(q):
    return any(_det.get((q["program_id"], f"{y}-{y + 1}")) == "low" for y in range(int(q["first_seen"][:4]), int(q["last_seen"][:4]) + 1))
def _r(g):
    k = sum(q["attrition_2025"] for q in g); lo, hi = _pc(k, len(g), method="wilson")
    return f'<td class="n">{k}</td><td class="n">{len(g):,}</td><td class="n"><b>{100 * k / len(g):.1f}%</b></td><td class="n muted">{100 * lo:.1f}–{100 * hi:.1f}%</td>'
_clean = [q for q in _m if not _touch(q)]
SENS = [("All residents (main result)", _m), ("Finished classes 2011–18", [q for q in _m if q["entry_year"] <= 2018]),
        ("Leaving out anyone who spent a year in a red program-year", _clean), ("… finished classes only", [q for q in _clean if q["entry_year"] <= 2018]),
        ("Entrants 2011–15 only (weaker rosters)", [q for q in _m if q["entry_year"] <= 2015]), ("Entrants 2016–24 only (stronger rosters)", [q for q in _m if q["entry_year"] >= 2016])]
sens_rows = "".join(f"<tr><td>{e(a)}</td>{_r(g)}</tr>" for a, g in SENS)
_lowkinds = {"entrant": 0, "gap": 0}
for r in WB["Detail"].iter_rows(min_row=2, values_only=True):
    if r[3] == "low":
        _lowkinds["entrant" if "unaccounted" in (r[7] or "") else "gap"] += 1
cov_low = sum(r[3] for r in BYYEAR[:4])

acgme_rows_simple = "".join(f'<tr><td>{y}</td><td class="n">{NT[y]["residents_on_duty"]:,}</td><td class="n">{cov_tot[y]:,}</td><td class="n">{100 * cov_tot[y] / NT[y]["residents_on_duty"]:.0f}%</td></tr>' for y in sorted(NT) if y in cov_tot)
_per = [("2011–2013", BYYEAR[0:3]), ("2014–2016", BYYEAR[3:6]), ("2017–2019", BYYEAR[6:9]), ("2020–2022", BYYEAR[9:12]), ("2023–2024", BYYEAR[12:14])]
def _pc3(rs, i):
    t = sum(r[1] + r[2] + r[3] for r in rs); return f"{100 * sum(r[i] for r in rs) / t:.0f}%"
conf_rows = "".join(f'<tr><td>{lab}</td><td class="n">{_pc3(rs, 1)}</td><td class="n">{_pc3(rs, 2)}</td><td class="n">{_pc3(rs, 3)}</td></tr>' for lab, rs in _per)
def _rt(g):
    k = sum(q["attrition_2025"] for q in g); return f"{100 * k / len(g):.1f}% ({k} of {len(g):,})"
sens_simple = (f'<tr><td>Everyone (main result)</td><td class="n"><b>{_rt(_m)}</b></td></tr>'
               f'<tr><td>Leaving out every resident who spent a year in a red program-year</td><td class="n">{_rt(_clean)}</td></tr>'
               f'<tr><td>Finished classes (2011–2018)</td><td class="n"><b>{_rt([q for q in _m if q["entry_year"] <= 2018])}</b></td></tr>'
               f'<tr><td>Finished classes, leaving out anyone who spent a year in a red program-year</td><td class="n">{_rt([q for q in _clean if q["entry_year"] <= 2018])}</td></tr>')
page = f"""<title>Neurosurgery Residency Attrition</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,500;6..72,600&family=Public+Sans:wght@400;500;600&display=swap">
<style>
/* Layout: single reading column (~72ch) with full-width figures; tables scroll inside their own frames. */
:root {{
  --bg:#f7f8fa; --panel:#ffffff; --fg:#14181f; --fg2:#4b5361; --muted:#77808e; --rule:#dde1e7;
  --accent:#2a78d6; --accent-soft:#9fc2ec; --hot:#d9552a;
  --c-lo:#f2b3ad; --c-me:#f6dc8c; --c-hi:#eef1f5; --c-na:#d5d9df;
  --display:"Newsreader", Georgia, "Times New Roman", serif; --body:"Public Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg:#12151a; --panel:#1a1e25; --fg:#eef0f3; --fg2:#b6bcc6; --muted:#8a92a0; --rule:#2c323c;
  --accent:#4a90e8; --accent-soft:#2f5b8f; --hot:#ec7a4f; --c-lo:#8a3b36; --c-me:#7d6a25; --c-hi:#20252d; --c-na:#343a44; color-scheme:dark; }} }}
:root[data-theme="dark"] {{ --bg:#12151a; --panel:#1a1e25; --fg:#eef0f3; --fg2:#b6bcc6; --muted:#8a92a0; --rule:#2c323c;
  --accent:#4a90e8; --accent-soft:#2f5b8f; --hot:#ec7a4f; --c-lo:#8a3b36; --c-me:#7d6a25; --c-hi:#20252d; --c-na:#343a44; color-scheme:dark; }}
body {{ background:var(--bg); color:var(--fg); font:15px/1.6 var(--body); }}
.wrap {{ max-width:880px; margin:0 auto; padding-inline:20px; padding-block:40px 80px; display:flex; flex-direction:column; gap:44px; }}
header {{ display:flex; flex-direction:column; gap:10px; }}
.eyebrow {{ font-size:12px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); }}
h1 {{ font:600 40px/1.1 var(--display); margin:0; text-wrap:balance; letter-spacing:-.01em; }}
h2 {{ font:600 26px/1.2 var(--display); margin:0; text-wrap:balance; }}
h3 {{ font:600 15px/1.3 var(--body); margin:0; }}
p {{ margin:0; max-width:68ch; color:var(--fg2); }}
.lede {{ font-size:17px; color:var(--fg); }}
section {{ display:flex; flex-direction:column; gap:14px; }}
.stats {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); gap:1px; background:var(--rule); border:1px solid var(--rule); border-radius:8px; overflow:hidden; }}
.stat {{ background:var(--panel); padding:16px; display:flex; flex-direction:column; gap:4px; }}
.stat b {{ font:600 30px/1 var(--display); font-variant-numeric:tabular-nums; }}
.stat span {{ font-size:13px; color:var(--fg2); }}
figure {{ margin:0; background:var(--panel); border:1px solid var(--rule); border-radius:8px; padding:16px; display:flex; flex-direction:column; gap:10px; min-width:0; }}
figcaption {{ font-size:13px; color:var(--muted); }}
.chart {{ width:100%; height:auto; display:block; }}
.chart .grid {{ stroke:var(--rule); stroke-width:1; }} .chart .axis {{ stroke:var(--fg2); stroke-width:1; }}
.chart .tick,.chart .lab {{ fill:var(--fg2); font:12px var(--body); }} .chart .val {{ fill:var(--fg); font:600 12px var(--body); }}
.chart .bar {{ fill:var(--accent); }} .chart .bar.muted {{ fill:var(--accent-soft); }}
.chart .whisk {{ stroke:var(--fg2); stroke-width:1.2; }} .chart .hit {{ fill:transparent; }}
.chart .mark:hover .bar {{ opacity:.8; }}
.chart .ref {{ stroke:var(--hot); stroke-width:1.5; stroke-dasharray:4 3; }} .chart .reflab {{ fill:var(--fg2); font:12px var(--body); }}
.chart .lim95 {{ fill:none; stroke:var(--muted); stroke-width:1.5; stroke-dasharray:2 3; }} .chart .lim998 {{ fill:none; stroke:var(--muted); stroke-width:1.5; }}
.chart .dot {{ fill:var(--accent); stroke:var(--panel); stroke-width:2; opacity:.85; }} .chart .dot.hot {{ fill:var(--hot); opacity:1; }}
.chart .c-hi {{ fill:var(--accent-soft); }} .chart .c-me {{ fill:var(--c-me); }} .chart .c-lo {{ fill:var(--c-lo); }}
.chart .band {{ fill:var(--rule); }} .chart .hotbar {{ fill:var(--hot); }} i.bandkey {{ background:var(--rule); }}
details summary {{ cursor:pointer; color:var(--accent); font-weight:600; margin-block:6px; }}
.legend {{ display:flex; flex-wrap:wrap; gap:14px; font-size:13px; color:var(--fg2); }}
.legend i {{ display:inline-block; width:12px; height:12px; border-radius:2px; vertical-align:-1px; margin-right:6px; }}
.scroll {{ overflow-x:auto; min-width:0; }}
table {{ border-collapse:collapse; width:100%; font-size:13.5px; }}
th,td {{ text-align:left; padding:7px 10px; border-bottom:1px solid var(--rule); vertical-align:top; }}
th {{ font-weight:600; color:var(--fg2); font-size:12px; letter-spacing:.03em; }}
td.n,th.n {{ text-align:right; font-variant-numeric:tabular-nums; white-space:nowrap; }} .muted {{ color:var(--muted); }}
.prog-table {{ max-height:520px; overflow:auto; border:1px solid var(--rule); border-radius:8px; }}
.prog-table thead th {{ position:sticky; top:0; background:var(--panel); cursor:pointer; }}
.prog-table thead th:focus-visible {{ outline:2px solid var(--accent); }}
.hm {{ border-collapse:separate; border-spacing:2px; font-size:11.5px; }}
.hm th[scope=row] {{ font-weight:400; color:var(--fg2); white-space:nowrap; padding:0 8px 0 0; border:0; max-width:320px; overflow:hidden; text-overflow:ellipsis; }}
.hm thead th {{ text-align:center; padding:0 0 4px; border:0; font-size:11px; }}
.hm td {{ width:22px; height:14px; padding:0; border:0; border-radius:2px; }}
td.c-lo,i.c-lo {{ background:var(--c-lo); }} td.c-me,i.c-me {{ background:var(--c-me); }} td.c-hi,i.c-hi {{ background:var(--c-hi); outline:1px solid var(--rule); outline-offset:-1px; }}
td.c-na,i.c-na {{ background:repeating-linear-gradient(135deg,var(--c-na) 0 2px,transparent 2px 5px); }}
ul.plain {{ margin:0; padding-left:20px; display:flex; flex-direction:column; gap:8px; max-width:70ch; color:var(--fg2); }}
ol.pdfs {{ margin:0; padding-left:22px; display:flex; flex-direction:column; gap:10px; }}
ol.pdfs li {{ color:var(--fg2); }} .cite {{ color:var(--fg); }} .why {{ display:block; font-size:13px; color:var(--muted); }}
a {{ color:var(--accent); }}
.two {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:16px; }}
.note {{ font-size:13px; color:var(--muted); max-width:72ch; }}
@media (max-width:520px) {{ h1 {{ font-size:31px; }} .stat b {{ font-size:26px; }} }}
</style>
<div class="wrap">
<header>
  <div class="eyebrow">US ACGME neurosurgery residencies · entrants 2011–2024 · status as of 30 June 2025</div>
  <h1>Neurosurgery Residency Attrition</h1>
  <p class="lede">Of {N:,} residents who entered a US neurosurgery residency between 2011 and 2024, {K} ({pct(100 * K / N)}) had left neurosurgery without graduating by 30 June 2025. Among the classes that have had time to finish (2011–2018), the figure is {pct(c18["rate"])} (95% CI {c18["ci95"][0]}–{c18["ci95"][1]}%).</p>
  <p>Every resident was traced from program rosters (live pages and web archives) and checked against an outside source such as a current faculty or practice bio, a match list or a program announcement. Attrition means failing to graduate from any neurosurgery residency: moving to another neurosurgery program is a transfer, not attrition.</p>
</header>

<div class="stats">
  <div class="stat"><b>{pct(100 * K / N)}</b><span>{K} of {N:,} residents left neurosurgery</span></div>
  <div class="stat"><b>{pct(c18["rate"])}</b><span>finished classes 2011–2018 ({c18["attrition"]} of {c18["entrants"]:,})</span></div>
  <div class="stat"><b>{100 * early / K:.0f}%</b><span>of those who left did so in PGY-1 or PGY-2</span></div>
  <div class="stat"><b>{types.get("switched_specialty", 0)}</b><span>switched to another specialty, most often radiology</span></div>
</div>

<section id="by-class">
  <h2>Attrition by entering class</h2>
  <p>Each bar is the share of an entering class that had left neurosurgery by 30 June 2025. Classes that entered in 2019 or later are still in training, so their bars will rise. Class-to-class variation ({min(c['rate'] for c in A['by_entry_class'] if c['complete_class'])}% to {max(c['rate'] for c in A['by_entry_class'] if c['complete_class'])}%) is mostly within the confidence intervals.</p>
  <figure>{bar_chart(cls_items, ymax=16, highlight=(c18["rate"], f'2011–18 average {c18["rate"]}%'))}
    <div class="legend"><span><i style="background:var(--accent)"></i>Class has finished training</span><span><i style="background:var(--accent-soft)"></i>Still in training (rate will rise)</span><span>Whiskers: 95% confidence interval</span></div>
    <figcaption>Entrants per class: {", ".join(f'{c["entry_year"]} n={c["entrants"]}' for c in A["by_entry_class"])}.</figcaption></figure>
</section>

<section id="by-year">
  <h2>Attrition per academic year</h2>
  <p>The share of residents on rosters in a given year who left neurosurgery by the end of it. Shown from 2017–18, the first year every training level is filled by 2011-or-later entrants. The rate sits near 1% a year and rose to {A["by_academic_year"][-1]["rate"]}% in 2024–25. Published ACGME figures of about 2.5% a year also count moves between neurosurgery programs, which we treat as transfers.</p>
  <figure>{bar_chart(ay_items, ymax=3, highlight=None)}
    <figcaption>Residents in denominator: {", ".join(f'{r["year"][2:]} {r["residents"]:,}' for r in A["by_academic_year"])}. A departure is dated to the last academic year on a roster, so the year can be off by one where a roster is missing.</figcaption></figure>
</section>

<section id="who">
  <h2>When residents leave, and where they go</h2>
  <div class="two">
    <figure><h3>Training level at departure</h3>{bar_chart(pgy_items, w=360, h=230, ci=False, ymax=35)}<figcaption>Share of the {K} departures, by last PGY on a roster.</figcaption></figure>
    <figure><h3>How they left</h3>{hbar([(TYPELAB[k], v) for k, v in sorted(types.items(), key=lambda x: -x[1])], w=360, rowh=30)}<figcaption>"Destination not found" means the resident is absent from the program's current roster and alumni list, and no other roster, match list or bio names them.</figcaption></figure>
  </div>
  <figure><h3>New specialty of the {types.get("switched_specialty", 0)} who switched</h3>{hbar(dest, rowh=24)}</figure>
</section>

<section id="programs">
  <h2>Attrition by program</h2>
  <p>Programs are small, so their rates swing a lot by luck alone. A program that trains 25 residents will see anywhere from 0 to about 4 of them leave, even if its true rate is exactly the national {100 * p0:.1f}%. So a single program's rate only means something when it falls outside that normal range.</p>
  <figure><h3>Programs with at least 20 residents, highest rate first</h3>{PB}
    <div class="legend"><span><i style="background:var(--accent)"></i>Program's attrition rate (label: left / residents)</span><span><i class="bandkey"></i>Range expected by chance for a program that size</span><span><i style="background:var(--hot)"></i>Above that range</span><span>Dashed line: national rate</span></div>
    <figcaption>Only one program, UAMS, sits above its expected range, and even that could be chance: when you compare {A["programs"]} programs, a few will land outside the range by luck. {A["zero_attrition_programs"]} programs had no attrition. Hover a bar for details.</figcaption></figure>
  <details><summary>All {A["programs"]} programs as a table</summary>
  <div class="prog-table"><table id="progtable"><thead><tr>
    <th tabindex="0">Program</th><th class="n" tabindex="0">Residents</th><th class="n" tabindex="0">Left</th><th class="n" tabindex="0">Rate</th><th tabindex="0">Compared with the national rate</th><th tabindex="0">Roster record</th></tr></thead>
    <tbody>{prog_rows}</tbody></table></div>
  <p class="note">"Roster record" says how complete our year-by-year rosters are for that program: complete, some years filled in from the years around them, or some years where a resident could be missing. Click a column heading to sort.</p></details>
</section>

<section id="confidence">
  <h2>How complete is the data?</h2>
  <p><b>We found almost everyone.</b> Each year the ACGME publishes the official number of neurosurgery residents in the country. Our rosters contain 96–105% of that number in every year from 2011 to 2025, so very few residents can be missing overall.</p>
  <figure><h3>Residents we found vs the official count</h3><div class="scroll"><table><thead><tr><th>Year</th><th class="n">Official count (ACGME)</th><th class="n">We found</th><th class="n">Share found</th></tr></thead><tbody>{acgme_rows_simple}</tbody></table></div>
    <figcaption>A share slightly over 100% means our rosters also list a few people the official count leaves out, such as residents on research years.</figcaption></figure>
  <p><b>Some program-years are less certain.</b> For each program and year we asked: could a resident be missing? Green means we saw that year's roster. Yellow means the roster was never archived, but every resident reappears the next year and the intern class matches the national match count, so no one can be missing. Red means someone could be missing.</p>
  <figure><h3>How many program-years are certain</h3><div class="scroll"><table><thead><tr><th>Years</th><th class="n">Roster seen (green)</th><th class="n">Filled in, no one missing (yellow)</th><th class="n">Someone could be missing (red)</th></tr></thead><tbody>{conf_rows}</tbody></table></div>
    <figcaption>Red is concentrated in 2011–2016, when fewer program websites were archived.</figcaption></figure>
  <p><b>The uncertain years don't change the answer.</b> We recalculated the rate with and without the red years. If the red years were hiding a lot of attrition, leaving them out would change the rate a lot; it moves by only a few tenths of a percent, and upward, so the uncertain years are not inflating the result.</p>
  <figure><div class="scroll"><table><thead><tr><th>Calculation</th><th class="n">Attrition rate</th></tr></thead><tbody>{sens_simple}</tbody></table></div></figure>
  <figure><h3>Program × year confidence, clustered by pattern</h3>
    <div class="legend"><span><i class="c-lo"></i>Low</span><span><i class="c-me"></i>Medium</span><span><i class="c-hi"></i>High</span><span><i class="c-na"></i>Program not open</span></div>
    <div class="scroll" style="max-height:560px"><table class="hm"><thead><tr><th></th>{hm_head}</tr></thead><tbody>{"".join(hm_rows)}</tbody></table></div>
    <figcaption>Programs with similar weak years are grouped together; programs with no weak years are at the bottom. The Excel file <code>program_year_confidence.xlsx</code> has the same grid plus, for every program-year, the gap length, the match count, the entrants we hold, and the reason for the grade.</figcaption></figure>
  <h3>Evidence behind each resident's outcome</h3>
  <p>{ev.get("gold", 0):,} residents ({100 * ev.get("gold", 0) / N:.0f}%) are confirmed by a gold-standard outside source that was opened and quoted: a current faculty or practice bio for those who finished or left, and a medical-school match list or program announcement for those still training. {ev.get("silver", 0):,} ({100 * ev.get("silver", 0) / N:.0f}%) rest on silver sources (board-certified Doximity profile, NPI registry, alumni page), and {ev.get("program_only", 0) + ev.get("none", 0):,} ({100 * (ev.get("program_only", 0) + ev.get("none", 0)) / N:.0f}%) on the program's own website only.</p>
</section>

<section id="context">
  <h2>How this compares with earlier studies</h2>
  <p>Our cumulative rate for finished classes, {pct(c18["rate"])}, sits between Renfrow's 6.7% for 2000–09 matches and Haruno's 10.4% for 2001–18. The closest match is Agarwal's 2005–10 cohort. Their published 11.0% counts residents who left their first program, and 40 of the 119 leavers with a known outcome simply moved to another neurosurgery program, with 2 deaths. Counting their leavers the way we do (switched specialty, left medicine, or destination unknown) gives 98 of 1,275, or 7.7%, close to our rate. Annual ACGME rates of 2.1–2.6% also count transfers; our comparable annual figure is about 1%. Every study finds most attrition early: Agarwal 65% in PGY-1–2, Renfrow 76% in PGY-1–3, and {100 * early / K:.0f}% in PGY-1–2 here.</p>
  <div class="scroll"><table><thead><tr><th>Study</th><th>Cohort</th><th>What counts as attrition</th><th>Rate</th><th>Read from</th></tr></thead><tbody>{lit_rows}
    <tr><td><b>This study</b></td><td>Entered 2011–24 (n={N:,})</td><td>Failed to graduate any NS residency; transfers, deaths and post-completion exits excluded</td><td><b>{pct(c18["rate"])}</b> (finished classes); ~1% per year</td><td class="muted">rosters + outside sources</td></tr></tbody></table></div>
  <p class="note">All rates above were checked against the full text. Gender could not be compared: our data does not record it.</p>
</section>

<section id="pdfs">
  <h2>Sources</h2>
  <p>Full texts reviewed: Lynch 2015, Renfrow 2016, Agarwal 2019, Raman 2019, Yaeger 2020, Kabangu 2023 (two papers), Kabangu 2024, Sundel 2024, Chainey 2026, Khoushhal 2017, Shweikeh 2018, Yeo 2010, and Haruno 2023 (open access).</p>
</section>

<section id="methods">
  <h2>Methods and limits</h2>
  <ul class="plain">
    <li><b>Cohort.</b> Residents first seen on a roster in 2011–12 through 2024–25 at {A["programs"]} ACGME programs. Excluded: 543 later entrants; 29 residents who entered before 2011 (the source lists only captured them if they left, which would bias the rate upward); 2 people found to be fellows rather than residents; and the military National Capital Consortium (2 residents).</li>
    <li><b>Cutoff.</b> Status as of 30 June 2025. Anyone still on a 2025–26 roster counts as in training, whatever happened later. Departures are dated to the last roster year.</li>
    <li><b>Transfers.</b> A resident who moved to another neurosurgery program and finished, or is still training there, is a transfer. A resident who transferred and then left neurosurgery counts once, at the last program. Residents who finished and later left the field, and deaths, are not attrition.</li>
    <li><b>Bounds.</b> If all {unk} residents whose destination was not found had quietly transferred to another neurosurgery program, the rate would be {100 * (K - unk) / N:.1f}%. Twelve matched residents could not be named because they left before appearing on any archived roster (Albany 2016, Emory 2013, Houston Methodist 2017, Mayo Jacksonville 2018, MCG 2011, MCW 2013, Arizona 2015, Oklahoma 2016, Wisconsin 2013, Puerto Rico 2011, and both Westchester 2024 interns, who are missing from its October 2025 roster). Counting all of them as attrition gives {100 * (K + 12) / (N + 12):.1f}%.</li>
    <li><b>Missing program.</b> PCOM, a former osteopathic program that matched one resident a year in 2020–22, is not in our program list.</li>
    <li><b>Evidence rules.</b> Directory listings (Doximity without board certification, Healthgrades, WebMD, LinkedIn) and publication affiliations never counted as proof. About 58 current-resident confirmations come from program posts on X that were read in a logged-in browser; if those are set aside, they drop from gold to silver but no outcome changes.</li>
    <li><b>Program comparisons.</b> Program rates use residents as the denominator and are not adjusted for class year or roster confidence. Treat them as a screen, not a ranking.</li>
  </ul>
</section>
</div>
<script>
(function () {{
  var t = document.getElementById("progtable"); if (!t) return;
  var heads = t.tHead.rows[0].cells;
  function key(td) {{ var s = td.textContent.replace(/[%,]/g, ""); var n = parseFloat(s); return isNaN(n) ? s.toLowerCase() : n; }}
  Array.prototype.forEach.call(heads, function (th, i) {{
    function go() {{
      var dir = th.dataset.dir === "asc" ? -1 : 1; th.dataset.dir = dir === 1 ? "asc" : "desc";
      var rows = Array.prototype.slice.call(t.tBodies[0].rows);
      rows.sort(function (a, b) {{ var x = key(a.cells[i]), y = key(b.cells[i]); return (x > y ? 1 : x < y ? -1 : 0) * dir; }});
      rows.forEach(function (r) {{ t.tBodies[0].appendChild(r); }});
    }}
    th.addEventListener("click", go);
    th.addEventListener("keydown", function (ev) {{ if (ev.key === "Enter" || ev.key === " ") {{ ev.preventDefault(); go(); }} }});
  }});
}})();
</script>
"""
open(f"{R}/report.html", "w").write(page)
print(f"wrote {R}/report.html ({len(page) // 1024} KB)")
