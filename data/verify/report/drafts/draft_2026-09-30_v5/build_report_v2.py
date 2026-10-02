#!/usr/bin/env python3
"""Simplified attrition report (v2): one quality score, a few analyses, method comparison.

    python3 scripts/tools/build_report_v2.py   ->  data/verify/report/report.html

Run phase3_final_merge.py, confidence_heatmap.py and attrition_analysis.py first.
"""
import html, json, math, sqlite3
from collections import Counter
import openpyxl
from scipy.stats import binom
from statsmodels.stats.proportion import proportion_confint

e = html.escape
R = "data/verify/report"
A = json.load(open(f"{R}/analysis.json"))
M = [p for p in json.load(open("data/verify/phase3/merged_final.json")) if not p["outcome_2025"].startswith("excluded")]
NT = {r["academic_year"]: r for r in json.load(open("data/verify/programs/national_totals.json"))}
WB = openpyxl.load_workbook("data/verify/programs/program_year_confidence.xlsx")
DET = {(r[0], r[2]): r[3] for r in WB["Detail"].iter_rows(min_row=2, values_only=True)}
HM = [r for r in WB["Confidence heatmap"].iter_rows(values_only=True)]
DB = sqlite3.connect("db/neurosurgery_attrition.db")
STATE = dict(DB.execute("select program_id, state from programs"))
LISTED = {}
for pid, ay, n in DB.execute("select program_id, academic_year, count(distinct name_as_listed) from roster_observations where program_id != 47 group by 1, 2"):
    LISTED[ay] = LISTED.get(ay, 0) + n

ATT = lambda q: q["attrition_2025"] is True
FIN = [q for q in M if q["entry_year"] <= 2018]
N, K = len(M), sum(ATT(q) for q in M)
NF, KF = len(FIN), sum(ATT(q) for q in FIN)
p_fin = KF / NF


def ci(k, n):
    lo, hi = proportion_confint(k, n, method="wilson")
    return 100 * lo, 100 * hi


def rate(g):
    k = sum(ATT(q) for q in g)
    lo, hi = ci(k, len(g))
    return k, len(g), 100 * k / len(g), lo, hi


def red(q):
    return any(DET.get((q["program_id"], f"{y}-{y + 1}")) == "low" for y in range(int(q["first_seen"][:4]), int(q["last_seen"][:4]) + 1))


# ---- quality score ----
VER = [q for q in M if q["evidence_level"] in ("gold", "silver") and not red(q)]
QS = 100 * len(VER) / N
GOLD = 100 * sum(q["evidence_level"] == "gold" for q in M) / N
EXT = 100 * sum(q["evidence_level"] in ("gold", "silver") for q in M) / N
NORED = 100 * sum(not red(q) for q in M) / N
FOUND = [100 * LISTED[y] / NT[y]["residents_on_duty"] for y in NT if y in LISTED]

# ---- analyses ----
classes = []
for y in range(2011, 2025):
    g = [q for q in M if q["entry_year"] == y]
    k, n, r, lo, hi = rate(g)
    classes.append(dict(y=y, k=k, n=n, r=r, lo=lo, hi=hi, fin=y <= 2018))
att = [q for q in M if ATT(q)]
pgy = Counter(q["last_pgy"] or 0 for q in att)
early = pgy[1] + pgy[2]
types = Counter(q["outcome_2025"] for q in att)
dest = sorted(A["switch_destinations"].items(), key=lambda x: -x[1])
trans = [q for q in M if q["outcome_2025"] == "transferred"]
tr_share = 100 * len(trans) / (len(trans) + K)
# periods (annual)
act = lambda s: [q for q in M if q["first_seen"] <= s <= q["last_seen"]]
def period(ys, incl_tr=False):
    n = sum(len(act(f"{y}-{y + 1}")) for y in ys)
    ss = [f"{y}-{y + 1}" for y in ys]
    k = sum(1 for q in M if q["last_seen"] in ss and (ATT(q) or (incl_tr and q["outcome_2025"] == "transferred")))
    return 100 * k / n
PER = [("2017–18 to 2018–19 (before COVID)", [2017, 2018]), ("2019–20 to 2020–21 (COVID years)", [2019, 2020]), ("2021–22 to 2024–25", [2021, 2022, 2023, 2024])]
# region, size
REG = {"Northeast": "CT ME MA NH RI VT NJ NY PA", "Midwest": "IL IN MI OH WI IA KS MN MO NE ND SD",
       "South": "DE FL GA MD NC SC VA DC WV AL KY MS TN AR LA OK TX PR", "West": "AZ CO ID MT NV NM UT WY AK CA HI OR WA"}
reg = {s: r for r, v in REG.items() for s in v.split()}
ent = Counter((q["program_id"], q["entry_year"]) for q in M)
size = {}
for pid in {q["program_id"] for q in M}:
    ys = [ent[(pid, y)] for y in range(2011, 2019) if ent[(pid, y)]]
    size[pid] = sum(ys) / len(ys) if ys else 0
SIZES = [("1 resident a year", 0, 1.5), ("2 a year", 1.5, 2.5), ("3 or more a year", 2.5, 99)]
# method comparison: our data on others' definitions
fin_tr = sum(1 for q in FIN if q["outcome_2025"] == "transferred")
agarwal_style = 100 * (KF + fin_tr) / NF
annual_incl_tr = period([2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024], incl_tr=True)
annual_ours = period([2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])

# ---- programs (finished classes) ----
by = {}
for q in FIN:
    by.setdefault((q["program_id"], (q["program"] or "").split(" ©")[0]), []).append(q)
PR = []
for (pid, name), g in by.items():
    k, n = sum(ATT(q) for q in g), len(g)
    lo_b, hi_b = binom.ppf(0.025, n, p_fin), binom.ppf(0.975, n, p_fin)
    PR.append(dict(name=name, k=k, n=n, r=100 * k / n, lo=100 * lo_b / n, hi=100 * hi_b / n, out=k > hi_b))
PR.sort(key=lambda r: (-r["r"], -r["n"]))


# ---- charts ----
def bars(items, w=720, h=250, ymax=16, ref=None):
    ml, mr, mt, mb = 44, 12, 14, 34
    pw, ph = w - ml - mr, h - mt - mb
    Y = lambda v: mt + ph - ph * v / ymax
    bw = pw / len(items)
    s = [f'<svg viewBox="0 0 {w} {h}" class="chart" role="img">']
    step = 2 if ymax <= 16 else 5
    for t in range(0, ymax + 1, step):
        s.append(f'<line x1="{ml}" x2="{w - mr}" y1="{Y(t):.1f}" y2="{Y(t):.1f}" class="grid"/><text x="{ml - 6}" y="{Y(t) + 4:.1f}" class="tick" text-anchor="end">{t}%</text>')
    for i, it in enumerate(items):
        x, wd = ml + i * bw + bw * .18, bw * .64
        s.append(f'<g class="mark"><title>{e(it["tip"])}</title><rect x="{x:.1f}" y="{Y(it["v"]):.1f}" width="{wd:.1f}" height="{max(0, Y(0) - Y(it["v"])):.1f}" rx="3" class="{it.get("cls", "bar")}"/>')
        if it.get("lo") is not None:
            cx = x + wd / 2
            s.append(f'<line x1="{cx:.1f}" x2="{cx:.1f}" y1="{Y(it["hi"]):.1f}" y2="{Y(it["lo"]):.1f}" class="whisk"/>')
        s.append(f'<rect x="{ml + i * bw:.1f}" y="{mt}" width="{bw:.1f}" height="{ph}" class="hit"/></g><text x="{ml + i * bw + bw / 2:.1f}" y="{h - mb + 16}" class="tick" text-anchor="middle">{e(it["lab"])}</text>')
    if ref:
        s.append(f'<line x1="{ml}" x2="{w - mr}" y1="{Y(ref[0]):.1f}" y2="{Y(ref[0]):.1f}" class="ref"/><text x="{w - mr}" y="{Y(ref[0]) - 5:.1f}" class="reflab" text-anchor="end">{e(ref[1])}</text>')
    s.append(f'<line x1="{ml}" x2="{w - mr}" y1="{Y(0):.1f}" y2="{Y(0):.1f}" class="axis"/></svg>')
    return "".join(s)


def hbar(items, w=720, rowh=24, ml=230):
    mx = max(v for _, v in items)
    s = [f'<svg viewBox="0 0 {w} {rowh * len(items) + 8}" class="chart" role="img">']
    for i, (lab, v) in enumerate(items):
        y = 4 + i * rowh
        bw = (w - ml - 60) * v / mx
        s.append(f'<g class="mark"><title>{e(lab)}: {v}</title><text x="{ml - 8}" y="{y + rowh / 2 + 4:.1f}" class="lab" text-anchor="end">{e(lab)}</text><rect x="{ml}" y="{y + 4}" width="{bw:.1f}" height="{rowh - 8}" rx="3" class="bar"/><text x="{ml + bw + 6:.1f}" y="{y + rowh / 2 + 4:.1f}" class="val">{v}</text></g>')
    return "".join(s) + "</svg>"


def program_chart(minn=10, w=720, rowh=17):
    rows = [r for r in PR if r["n"] >= minn]
    ml, mr, mt = 250, 50, 26
    xmax = 40
    X = lambda v: ml + (w - ml - mr) * min(v, xmax) / xmax
    h = mt + rowh * len(rows) + 10
    s = [f'<svg viewBox="0 0 {w} {h}" class="chart" role="img">']
    for t in range(0, xmax + 1, 10):
        s.append(f'<line x1="{X(t):.1f}" x2="{X(t):.1f}" y1="{mt - 6}" y2="{h - 6}" class="grid"/><text x="{X(t):.1f}" y="{mt - 10}" class="tick" text-anchor="middle">{t}%</text>')
    for i, r in enumerate(rows):
        y = mt + i * rowh
        nm = r["name"].replace(" Program", "").replace("University of ", "U. ").replace("Medical Center", "MC")[:36]
        s.append(f'<g class="mark"><title>{e(r["name"])}: {r["k"]} of {r["n"]} residents who entered 2011–2018 did not finish ({r["r"]:.0f}%). By chance a program this size usually falls between {r["lo"]:.0f}% and {r["hi"]:.0f}%.</title>'
                 f'<rect x="{X(r["lo"]):.1f}" y="{y + 2}" width="{max(1, X(r["hi"]) - X(r["lo"])):.1f}" height="{rowh - 4}" class="band"/>'
                 f'<rect x="{ml}" y="{y + 5}" width="{max(0, X(r["r"]) - ml):.1f}" height="{rowh - 10}" rx="2" class="{"bar hotbar" if r["out"] else "bar"}"/>'
                 f'<text x="{ml - 8}" y="{y + rowh - 5}" class="lab" text-anchor="end">{e(nm)}</text><text x="{X(r["r"]) + 5:.1f}" y="{y + rowh - 5}" class="val">{r["k"]}/{r["n"]}</text></g>')
    s.append(f'<line x1="{X(100 * p_fin):.1f}" x2="{X(100 * p_fin):.1f}" y1="{mt - 6}" y2="{h - 6}" class="ref"/></svg>')
    return "".join(s), len(rows)


cls_items = [dict(lab=str(c["y"]), v=c["r"], lo=c["lo"], hi=c["hi"], cls="bar" if c["fin"] else "bar muted",
                  tip=f'{c["y"]} class: {c["k"]} of {c["n"]} left ({c["r"]:.1f}%)' + ("" if c["fin"] else "; still in training, will rise")) for c in classes]
pgy_items = [dict(lab=f"PGY-{k}", v=100 * pgy[k] / K, tip=f"PGY-{k}: {pgy[k]} of {K} departures") for k in range(1, 8) if pgy[k]]
TYPE = {"switched_specialty": "Switched specialty", "left_destination_unknown": "Left, destination not found", "left_medicine": "Left clinical medicine", "left_other": "Other (e.g. PA)"}
PCH, NPCH = program_chart()
outs = [r for r in PR if r["out"] and r["n"] >= 10]


def trow(cells, num=()):
    return "<tr>" + "".join(f'<td class="{"n" if i in num else ""}">{c}</td>' for i, c in enumerate(cells)) + "</tr>"


reg_rows = "".join(trow([r, f"{rate([q for q in FIN if reg.get(STATE.get(q['program_id'])) == r])[2]:.1f}%",
                         "{:.1f}–{:.1f}%".format(*rate([q for q in FIN if reg.get(STATE.get(q['program_id'])) == r])[3:]),
                         f"{rate([q for q in FIN if reg.get(STATE.get(q['program_id'])) == r])[1]:,}"], (1, 2, 3)) for r in REG)
size_rows = "".join(trow([lab, f"{rate([q for q in FIN if a <= size[q['program_id']] < b])[2]:.1f}%",
                          "{:.1f}–{:.1f}%".format(*rate([q for q in FIN if a <= size[q['program_id']] < b])[3:]),
                          f"{rate([q for q in FIN if a <= size[q['program_id']] < b])[1]:,}"], (1, 2, 3)) for lab, a, b in SIZES)
per_rows = "".join(trow([lab, f"{period(ys):.1f}%"], (1,)) for lab, ys in PER)

METHODS = [
    ("Lynch 2015", "1990–99 matches", "1,361", "SF Match lists + ABNS diplomate directory + NPI", "Board certification / directory", "Not stated", "14.0%"),
    ("Renfrow 2016", "2000–09 matches", "1,992", "AANS and ABNS graduation records + internet search", "Graduation records", "Unclear", "6.7%"),
    ("Agarwal 2019", "2005–10 starts", "1,275", "AANS resident database + internet search", "Internet search of each leaver", "Yes (counted as attrition)", "11.0% (7.7% without transfers and deaths)"),
    ("Haruno 2023", "2001–18", "4,434", "AAMC GME Track census (program-reported)", "Program reports", "No", "10.4%"),
    ("Kabangu 2023", "2017–20 starts", "1,780", "Match lists + public program pages", "Public listings", "Unclear", "5–7% not retained"),
    ("ACGME-based (Yaeger, Kabangu, Sundel)", "2007–22", "all residents", "ACGME Data Resource Book (program-reported)", "Program reports", "Yes", "2.1–2.6% per year"),
    ("This study", "2011–24 entrants", f"{N:,}", "Program roster web pages, live and archived (Wayback, Common Crawl), every year", "Each resident checked against a current bio, match list or program post", "No (tracked separately)", f"{100 * KF / NF:.1f}% finished classes; {annual_ours:.1f}% per year"),
]
meth_rows = "".join(trow([e(a) if a != "This study" else "<b>This study</b>", e(b), e(c), e(d), e(f), e(g), e(h)], (2,)) for a, b, c, d, f, g, h in METHODS)

hm_years = HM[0][2:16]
hm_rows = "".join('<tr><th scope="row">' + e(str(r[1])) + "</th>" + "".join(
    f'<td class="{ {"L": "c-lo", "M": "c-me", "–": "c-na"}.get(v or "", "c-hi")}" title="{e(str(r[1]))} {hm_years[j]}"></td>' for j, v in enumerate(r[2:16])) + "</tr>" for r in HM[1:])

page = f"""<title>Neurosurgery Residency Attrition</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,500;6..72,600&family=Public+Sans:wght@400;500;600&display=swap">
<style>
/* Layout: one reading column (~70ch) with full-width figures; supporting detail tucked into <details>. */
:root {{
  --bg:#f7f8fa; --panel:#ffffff; --fg:#14181f; --fg2:#4b5361; --muted:#77808e; --rule:#dde1e7;
  --accent:#2a78d6; --accent-soft:#9fc2ec; --hot:#d9552a; --band:#e4e8ee;
  --c-lo:#f2b3ad; --c-me:#f6dc8c; --c-hi:#eef1f5; --c-na:#d5d9df;
  --display:"Newsreader", Georgia, "Times New Roman", serif; --body:"Public Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg:#12151a; --panel:#1a1e25; --fg:#eef0f3; --fg2:#b6bcc6; --muted:#8a92a0; --rule:#2c323c;
  --accent:#4a90e8; --accent-soft:#2f5b8f; --hot:#ec7a4f; --band:#2a3039; --c-lo:#8a3b36; --c-me:#7d6a25; --c-hi:#20252d; --c-na:#343a44; color-scheme:dark; }} }}
:root[data-theme="dark"] {{ --bg:#12151a; --panel:#1a1e25; --fg:#eef0f3; --fg2:#b6bcc6; --muted:#8a92a0; --rule:#2c323c;
  --accent:#4a90e8; --accent-soft:#2f5b8f; --hot:#ec7a4f; --band:#2a3039; --c-lo:#8a3b36; --c-me:#7d6a25; --c-hi:#20252d; --c-na:#343a44; color-scheme:dark; }}
body {{ background:var(--bg); color:var(--fg); font:15px/1.6 var(--body); }}
.wrap {{ max-width:860px; margin:0 auto; padding-inline:20px; padding-block:40px 80px; display:flex; flex-direction:column; gap:40px; }}
header, section {{ display:flex; flex-direction:column; gap:12px; }}
.eyebrow {{ font-size:12px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); }}
h1 {{ font:600 40px/1.1 var(--display); margin:0; text-wrap:balance; }}
h2 {{ font:600 25px/1.2 var(--display); margin:0; text-wrap:balance; }}
h3 {{ font:600 15px/1.3 var(--body); margin:0; }}
p {{ margin:0; max-width:68ch; color:var(--fg2); }} .lede {{ font-size:17px; color:var(--fg); }}
.stats {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(170px,1fr)); gap:1px; background:var(--rule); border:1px solid var(--rule); border-radius:8px; overflow:hidden; }}
.stat {{ background:var(--panel); padding:16px; display:flex; flex-direction:column; gap:4px; }}
.stat b {{ font:600 30px/1 var(--display); font-variant-numeric:tabular-nums; }} .stat span {{ font-size:13px; color:var(--fg2); }}
figure {{ margin:0; background:var(--panel); border:1px solid var(--rule); border-radius:8px; padding:16px; display:flex; flex-direction:column; gap:10px; min-width:0; }}
figcaption, .note {{ font-size:13px; color:var(--muted); max-width:72ch; }}
.chart {{ width:100%; height:auto; display:block; }}
.chart .grid {{ stroke:var(--rule); }} .chart .axis {{ stroke:var(--fg2); }} .chart .tick,.chart .lab {{ fill:var(--fg2); font:12px var(--body); }}
.chart .val {{ fill:var(--fg); font:600 12px var(--body); }} .chart .bar {{ fill:var(--accent); }} .chart .bar.muted {{ fill:var(--accent-soft); }}
.chart .hotbar {{ fill:var(--hot); }} .chart .band {{ fill:var(--band); }} .chart .whisk {{ stroke:var(--fg2); stroke-width:1.2; }} .chart .hit {{ fill:transparent; }}
.chart .ref {{ stroke:var(--hot); stroke-width:1.5; stroke-dasharray:4 3; }} .chart .reflab {{ fill:var(--fg2); font:12px var(--body); }}
.legend {{ display:flex; flex-wrap:wrap; gap:14px; font-size:13px; color:var(--fg2); }}
.legend i {{ display:inline-block; width:12px; height:12px; border-radius:2px; vertical-align:-1px; margin-right:6px; }}
.two {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:16px; }}
.scroll {{ overflow-x:auto; min-width:0; }}
table {{ border-collapse:collapse; width:100%; font-size:13.5px; }} th,td {{ text-align:left; padding:7px 10px; border-bottom:1px solid var(--rule); vertical-align:top; }}
th {{ font-weight:600; color:var(--fg2); font-size:12px; }} td.n {{ text-align:right; font-variant-numeric:tabular-nums; white-space:nowrap; }}
.score {{ display:grid; grid-template-columns:auto 1fr; gap:18px; align-items:center; background:var(--panel); border:1px solid var(--rule); border-radius:8px; padding:18px; }}
.score b {{ font:600 48px/1 var(--display); color:var(--accent); font-variant-numeric:tabular-nums; }}
.score ul {{ margin:6px 0 0; padding-left:18px; color:var(--fg2); font-size:14px; }}
details summary {{ cursor:pointer; color:var(--accent); font-weight:600; }}
.hm {{ border-collapse:separate; border-spacing:2px; font-size:11.5px; width:auto; }}
.hm th[scope=row] {{ font-weight:400; color:var(--fg2); white-space:nowrap; padding:0 8px 0 0; border:0; }} .hm thead th {{ text-align:center; padding:0 0 4px; border:0; }}
.hm td {{ width:22px; height:14px; padding:0; border:0; border-radius:2px; }}
td.c-lo,i.c-lo {{ background:var(--c-lo); }} td.c-me,i.c-me {{ background:var(--c-me); }} td.c-hi,i.c-hi {{ background:var(--c-hi); outline:1px solid var(--rule); outline-offset:-1px; }}
td.c-na,i.c-na {{ background:repeating-linear-gradient(135deg,var(--c-na) 0 2px,transparent 2px 5px); }}
ul.plain {{ margin:0; padding-left:20px; display:flex; flex-direction:column; gap:6px; color:var(--fg2); max-width:70ch; }}
a {{ color:var(--accent); }}
@media (max-width:520px) {{ h1 {{ font-size:31px; }} .score {{ grid-template-columns:1fr; }} }}
</style>
<div class="wrap">
<header>
  <div class="eyebrow">US neurosurgery residencies · entrants 2011–2024 · status on 30 June 2025</div>
  <h1>Neurosurgery Residency Attrition</h1>
  <p class="lede">About 1 in 14 neurosurgery residents leaves the field before graduating. Of residents who entered in 2011–2018 and have had time to finish, {100 * KF / NF:.1f}% did not graduate from any neurosurgery residency (95% CI {ci(KF, NF)[0]:.1f}–{ci(KF, NF)[1]:.1f}%).</p>
</header>

<div class="stats">
  <div class="stat"><b>{100 * KF / NF:.1f}%</b><span>of 2011–18 entrants did not finish ({KF} of {NF:,})</span></div>
  <div class="stat"><b>{annual_ours:.1f}%</b><span>of residents leave in a typical year</span></div>
  <div class="stat"><b>{100 * early / K:.0f}%</b><span>of those who leave do so in PGY-1 or PGY-2</span></div>
  <div class="stat"><b>{QS:.0f}%</b><span>data quality score (see below)</span></div>
</div>

<section id="quality">
  <h2>Data quality score</h2>
  <div class="score"><b>{QS:.0f}%</b><div><p>of the {N:,} residents are <b>fully verified</b>: their outcome is confirmed by an outside source (a current faculty or practice bio, a match list, a program announcement or board certification), <b>and</b> every year they spent in training is covered by a roster with no chance of someone missing.</p>
  <ul><li>{EXT:.0f}% have an outside source confirming their outcome ({GOLD:.0f}% from a page we opened and quoted, the rest from registry or alumni listings).</li>
  <li>{NORED:.0f}% have no uncertain roster years.</li>
  <li>Our rosters found {min(FOUND):.0f}–{max(FOUND):.0f}% of the official ACGME resident count in every year.</li></ul></div></div>
</section>

<section id="classes">
  <h2>1. How many leave</h2>
  <p>Share of each entering class that left neurosurgery without graduating. Classes from 2019 on are still training, so their bars will rise.</p>
  <figure>{bars(cls_items, ref=(100 * KF / NF, f"2011–18: {100 * KF / NF:.1f}%"))}
    <div class="legend"><span><i style="background:var(--accent)"></i>Finished training</span><span><i style="background:var(--accent-soft)"></i>Still training</span><span>Line through each bar: 95% confidence interval</span></div></figure>
</section>

<section id="when">
  <h2>2. When they leave and where they go</h2>
  <div class="two">
    <figure><h3>Training year when they left</h3>{bars(pgy_items, w=360, h=220, ymax=35)}<figcaption>Agarwal (2005–10) found 65% left in PGY-1–2; Renfrow (2000–09) 76% in PGY-1–3. We find {100 * early / K:.0f}% in PGY-1–2.</figcaption></figure>
    <figure><h3>What they did next</h3>{hbar([(TYPE[k], v) for k, v in types.most_common()], w=360, rowh=30, ml=190)}<figcaption>"Destination not found": gone from the program with no later trace online.</figcaption></figure>
  </div>
  <figure><h3>New specialty of the {types["switched_specialty"]} who switched</h3>{hbar(dest)}<figcaption>Radiology, anesthesiology and neurology account for most switches, as in Lynch and Agarwal.</figcaption></figure>
</section>

<section id="transfers">
  <h2>3. Moving to another neurosurgery program</h2>
  <p>{len(trans)} residents left their program but continued neurosurgery elsewhere. That is {tr_share:.0f}% of everyone who left a program, almost the same as Agarwal's 33.6%. We count these as transfers, not attrition; studies that count them report higher rates.</p>
</section>

<section id="trend">
  <h2>4. Change over time</h2>
  <div class="two">
    <figure><h3>Share leaving per year</h3><div class="scroll"><table><thead><tr><th>Period</th><th class="n">Per year</th></tr></thead><tbody>{per_rows}</tbody></table></div>
      <figcaption>Attrition dipped during the COVID years, as Kabangu (2023) also found in ACGME data (2.7% before vs 1.7% during, counting transfers), then returned to its earlier level.</figcaption></figure>
    <figure><h3>By entering class</h3><p>Finished classes range from {min(c["r"] for c in classes if c["fin"]):.1f}% to {max(c["r"] for c in classes if c["fin"]):.1f}% with overlapping confidence intervals, so there is no clear trend across 2011–2018.</p></figure>
  </div>
</section>

<section id="programs">
  <h2>5. Region, program size and individual programs</h2>
  <div class="two">
    <figure><h3>By region (2011–18 entrants)</h3><div class="scroll"><table><thead><tr><th>Region</th><th class="n">Left</th><th class="n">95% CI</th><th class="n">Residents</th></tr></thead><tbody>{reg_rows}</tbody></table></div></figure>
    <figure><h3>By program size (2011–18 entrants)</h3><div class="scroll"><table><thead><tr><th>Size</th><th class="n">Left</th><th class="n">95% CI</th><th class="n">Residents</th></tr></thead><tbody>{size_rows}</tbody></table></div></figure>
  </div>
  <p>The confidence intervals overlap, so neither region nor program size makes a clear difference. Agarwal likewise found no regional difference.</p>
  <figure><h3>Individual programs: share of 2011–18 entrants who did not finish</h3>{PCH}
    <div class="legend"><span><i style="background:var(--accent)"></i>Program's rate (label: left / entrants)</span><span><i style="background:var(--band)"></i>Range a program that size would reach by chance</span><span><i style="background:var(--hot)"></i>Above that range</span><span>Dashed line: {100 * p_fin:.1f}% overall</span></div>
    <figcaption>{NPCH} programs with at least 10 residents who entered 2011–2018. Most programs train only 1–3 residents a year, so one or two departures move a rate a lot; the grey band shows how far chance alone can push it. {len(outs)} program{"s" if len(outs) != 1 else ""} sit{"" if len(outs) != 1 else "s"} above {"their" if len(outs) != 1 else "its"} band{": " + ", ".join(e(r["name"].replace(" Program", "")) for r in outs) if outs else ""}; with {NPCH} programs, a few are expected there by luck.</figcaption></figure>
</section>

<section id="methods-compare">
  <h2>6. How our method compares with earlier studies</h2>
  <p>Earlier studies used match lists, society or board directories, or numbers reported by programs to ACGME or AAMC. We rebuilt every program's roster, year by year, from its own web pages (live and archived) and then checked each resident against an outside source. The table shows what each study used and what it found.</p>
  <figure><div class="scroll"><table><thead><tr><th>Study</th><th>Years</th><th class="n">Residents</th><th>Where the list of residents came from</th><th>How outcomes were confirmed</th><th>Transfers counted as attrition?</th><th>Attrition</th></tr></thead><tbody>{meth_rows}</tbody></table></div></figure>
  <h3>Our data, measured the other studies' way</h3>
  <ul class="plain">
    <li>Counting transfers and deaths as attrition, like Agarwal: {agarwal_style:.1f}% of 2011–18 entrants (Agarwal: 11.0% for 2005–10).</li>
    <li>Per year, counting transfers, like ACGME-based studies: {annual_incl_tr:.1f}% (published: 2.1–2.6%).</li>
    <li>Excluding transfers, like Haruno: {100 * KF / NF:.1f}% (Haruno: 10.4% for 2001–18; Agarwal recomputed: 7.7%).</li>
  </ul>
  <p class="note">The main difference from program-reported sources is coverage: a web roster shows only who a program chose to list, so we cross-checked the count against ACGME totals every year and every entering class against the national match. Gender could not be analysed because the rosters do not record it.</p>
</section>

<section id="limits">
  <h2>Methods and limits</h2>
  <ul class="plain">
    <li><b>Who is counted:</b> residents who entered an ACGME neurosurgery program in 2011–2024. Excluded: later entrants, pre-2011 entrants, fellows listed on rosters, and the military program (no public rosters).</li>
    <li><b>Attrition:</b> left neurosurgery without graduating by 30 June 2025. Transfers to another neurosurgery program, deaths and career changes after graduating are not attrition. A resident who transferred and then left is counted once, at the last program.</li>
    <li><b>Range:</b> if every "destination not found" resident had quietly transferred, attrition would be {100 * (K - types["left_destination_unknown"]) / N:.1f}% overall; if twelve matched residents we could not name had all left, {100 * (K + 12) / (N + 12):.1f}%. The main overall figure is {100 * K / N:.1f}%.</li>
  </ul>
  <details><summary>Roster confidence by program and year</summary>
    <p class="note" style="margin-block:8px">Green: roster seen. Yellow: filled in from surrounding years, with every resident and the intern class accounted for. Red: a resident could be missing. Full detail is in <code>program_year_confidence.xlsx</code>.</p>
    <div class="legend"><span><i class="c-lo"></i>Red</span><span><i class="c-me"></i>Yellow</span><span><i class="c-hi"></i>Green</span><span><i class="c-na"></i>Program not open</span></div>
    <div class="scroll" style="max-height:520px"><table class="hm"><thead><tr><th></th>{"".join(f"<th>{y[2:4]}</th>" for y in hm_years)}</tr></thead><tbody>{hm_rows}</tbody></table></div>
  </details>
</section>
</div>
"""
open(f"{R}/report.html", "w").write(page)
print(f"QS {QS:.1f} | fin {100 * KF / NF:.1f} | annual {annual_ours:.2f} (incl tr {annual_incl_tr:.2f}) | agarwal-style {agarwal_style:.1f} | transfers share {tr_share:.1f} | outliers {[r['name'][:25] for r in outs]} | programs {NPCH}")
