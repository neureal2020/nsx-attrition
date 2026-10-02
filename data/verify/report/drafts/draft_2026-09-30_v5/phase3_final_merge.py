#!/usr/bin/env python3
"""Layer every phase-3 verification pass onto final.json and apply the attrition definition.

    python3 scripts/tools/phase3_final_merge.py

Layer order (later wins, with the exceptions below):
    final.json <- deep <- ident <- unk2 <- recheck <- manual_resolutions <- dest (x_*, then city y_*) <- gold <- recon

- An "unknown" from a later layer does not erase a more specific departure outcome from an earlier one.
- Gold changes the outcome only when the gold record states a disagreement AND its outcome differs from its own input;
  otherwise it only sets the evidence level.
- City-sweep outputs are filtered to their own input keys (shared-helper collision, see RUNLOG).
- COORDINATOR overrides and evidence DOWNGRADES below are applied last and listed in the review.

Writes data/verify/phase3/merged_final.json and FINAL_REVIEW.md. Nothing is written to the database.
"""
import glob, json, os, re
from collections import Counter, defaultdict

D = "data/verify/phase3"

NORM = {"died_in_training": "deceased", "completed_nonclinical": "completed",
        "unresolved_current_page_unavailable": "unknown", "not_on_current_page_possible_research_year": "possible_research_year",
        "in_training_research_year": "in_training", "not_at_program": "not_a_resident"}
ATTRITION = {"switched_specialty", "left_medicine", "left_destination_unknown", "left_other"}
UNRESOLVED = {"unknown", "possible_research_year"}

# Coordinator decisions from this session's reports. Marked pending where the user has not confirmed.
OVERRIDES = {
    "93:zac:wetsel": ("transferred", "UMMC -> EM residency -> back in NS, PGY-5 Arizona COM-Phoenix/Banner current page (g_034). User confirmed 2026-09-29"),
    "61:ruk:taiwo": ("completed", "Stanford chief 2025-26, off current page; alumni 2026 class not posted (x_7). Inferred."),
    "119:tay:wilson": ("transferred", "Wake -> UAMS NS (transfer); attrition counted once, at UAMS (73:tay:wilson). User confirmed 2026-09-29"),
    "11:ash:patel": ("transferred", "Cedars -> Geisinger NS; attrition counted at Geisinger (last NS program), per user rule"),
    "63:han:polavarapu": ("transferred", "Upstate roster 2024-25 (PGY-1), WashU PGY-3 2026-27 (bio) -> transfer, not a DB error (g_126 said not_at_program)"),
    "125:eli:klein": ("left_other", "WSU NS 2011-16, then MPH + PA; now NS physician assistant (g_047 gold)."),
}
# Evidence grades that break the gold brief, by key: (new level, reason). Keys resolved from the gold files.
DOWNGRADES = {
    "46:ada:sandler": ("program_only", "doctor.com only"),
    "67:giy:prashant": ("program_only", "Healthgrades only"),
    "69:jai:lim": ("program_only", "doctor.com only"),
    "85:jan:smietana": ("silver", "directory listing, not a bio"),
    "99:gri:ernst": ("program_only", "Doximity without board cert"),
    "111:far:laiwalla": ("program_only", "2020 news page"),
    "116:ric:thomas": ("program_only", "news article"),
    "119:jac:renfrow": ("silver", "bio under different surname, link inferred"),
    "119:sid:venkataraman": ("silver", "team page, not a bio"),
    "2:rid:mitha": ("program_only", "snippet of 404 page"),
    "4:sir:gandhi": ("program_only", "program's own resident bio"),
    "4:ale:greven": ("program_only", "program's own resident bio"),
    "4:nic:rabah": ("program_only", "program's own resident bio"),
    "4:sid:srivastava": ("program_only", "program's own resident bio"),
    "10:tia:xiao": ("silver", "personal X post"),
    "18:eva:bond": ("silver", "conference profile"),
    "25:rox:beladi": ("silver", "read behind login overlay"),
    "53:ama:brisco": ("program_only", "LinkedIn snippet"),
    "60:nic:musgrave": ("program_only", "LinkedIn snippet"),
    "51:hoa:nguyen": ("silver", "bio under a different name (Alex N. Hoang); link by residency + MD year"),
    "57:pur:patel": ("silver", "bio under a different surname (Panchmatia); link by MD school + residency"),
    "70:eli:alford": ("silver", "bio under a different name (Elizabeth Kuhn)"),
    "117:cam:liles": ("silver", "bio under a different first name (David Liles), no residency stated"),
    "10:min:huerta": ("program_only", "Cureus profile"),
    "20:sar:newman": ("program_only", "pre-match article (hoped to match), not a confirmation"),
    "30:jos:materi": ("silver", "outside local news, not a program/school source"),
    "32:ale:oderhowho": ("silver", "outside local news, not a program/school source"),
    "117:sor:jonzzon": ("silver", "undergraduate athletics team post, not the program/school"),
    "38:jam:ebot": ("program_only", "insurer network profile (directory)"),
    "36:amy:wang": ("program_only", "snippet; live page no longer lists her"),
}


def load(pattern, exclude=("v1_shallow", ".bak", "_in.json")):
    for f in sorted(glob.glob(f"{D}/{pattern}")):
        if any(x in f for x in exclude):
            continue
        for r in json.load(open(f)):
            if isinstance(r, dict) and r.get("key"):
                yield f, r


GOLD_IN = {r["key"]: NORM.get(r.get("outcome"), r.get("outcome"))
           for f in glob.glob(f"{D}/gold/g_*_in.json") for r in json.load(open(f))}
base = {r["key"]: r for r in json.load(open(f"{D}/final.json"))}
people = {}
for k, r in base.items():
    o = NORM.get(r["finding"].get("outcome"), r["finding"].get("outcome"))
    people[k] = {k2: r.get(k2) for k2 in ("key", "name", "program_id", "program", "entry_year", "first_seen", "last_seen",
                                           "last_pgy", "recorded_outcome", "tier")}
    people[k].update(outcome=o, outcome_source="final", evidence_level=None, trail=[("final", o)], notes=[])

# People found by the roster-hole checks (data/verify/programs/holes_*_out.json) who were missing from final.json,
# and entry-year corrections from the same checks. Sources are recorded in those files.
ADDITIONS = [
    # key, name, program_id, entry_year, first_seen, last_seen, last_pgy, outcome, note
    ("4:sam:kalb", "Samuel Kalb", 4, 2012, "2012-2013", "2018-2019", 7, "completed", "on Barrow rosters PGY-2 Jan 2014 to PGY-7 2018-19; adjudication had misdated entry to 2010 (holes_1)"),
    ("45:dan:felbaum", "Daniel Felbaum", 45, 2011, "2011-2012", "2016-2017", 6, "completed", "Georgetown 2011 class, graduated 2017 (6-yr program then); misdated to 2010 (holes_1)"),
    ("45:jos:ryan", "Joshua Ryan", 45, 2011, "2011-2012", "2016-2017", 6, "completed", "Georgetown 2011 class, graduated 2017 (holes_1)"),
    ("30:jos:porras", "Jose Porras", 30, 2018, "2018-2019", "2023-2024", 6, "left_medicine", "Hopkins rosters Sep 2019-Feb 2024, gone Aug 2024, not in 2025 alumni; now surgical-AI startup (holes_1)"),
    ("30:saf:alomari", "Safwan Alomari", 30, 2023, "2023-2024", "2024-2025", 2, "transferred", "Hopkins PGY-1/2; transferring to Cleveland Clinic Florida June 2025 (holes_1)"),
    ("29:rob:sterner", "Robert C. Sterner", 29, 2023, "2023-2024", "2023-2024", 1, "left_destination_unknown", "Inova resident Feb 2024 (Spine Summit page); no PGY-2 in Jan 2025 guide; probable (holes_1)"),
    ("55:chr:wong", "Christopher Wong", 55, 2024, "2024-2025", "2026-2027", 3, "in_training", "Riverside 2024 matchee, on current Arrowhead Neurosurgical resident page (holes_2)"),
    ("97:jor:davies", "Jordan Davies", 97, 2018, "2018-2019", "2018-2019", 1, "transferred", "UNM intern 2018-19, then UC Irvine PGY-2 2019, completed 2025 (holes_2; UCI record 74:jor:davies)"),
    ("21:ash:patel", "Ashish Patel", 21, 2011, "2013-2014", "2019-2020", None, "switched_specialty", "Cedars 2011-13 -> Geisinger NS (May 2019 release lists him as NS resident) -> Geisinger neurology 2021-25; attrition counted at Geisinger (red_4). Geisinger start year approximate"),
    ("101:fre:beato", "Freddie Rodriguez Beato", 101, 2019, "2019-2020", "2020-2021", 2, "transferred", "UPR 2019 matchee, to UC Davis PGY-3 2021 at UPR closure (holes_2; UC Davis record 77:fre:beato)"),
]
ENTRY_FIX = {  # key: (entry_year, first_seen) corrections from the roster-hole checks
    # UCSF Breshears/Osorio/Rutkowski: 2012 fix REVERTED (red_3 opened bios: UCSF 2011-2018)
    "45:tus:jha": 2012, "45:jas:mcgowan": 2012,  # Georgetown: pre-2013 classes were 6 years
    "39:dev:patra": 2020,
    "50:osa:choudhry": 2012,  # NYU: MD 2012, NYU NS internship 2012-13, completed 2020 (red_2)  # Mayo Phoenix: started 2020 after 2018-20 fellowship
}
# people named by the final red-year search (data/verify/programs/red_*_out.json)
import re as _re
for _f in sorted(glob.glob("data/verify/programs/red_*_out.json")):
    for _r in json.load(open(_f)):
        for _np in _r.get("new_people", []):
            _t = _re.sub(r"[^A-Za-z \-]", " ", _np.get("name", "")).split()
            if len(_t) < 2 or not _np.get("entry_year"):
                continue
            _k = f'{_r["program_id"]}:{_t[0][:3].lower()}:{_t[-1].lower()}'
            ADDITIONS.append((_k, _np["name"], int(_r["program_id"]), int(_np["entry_year"]), _np.get("first_seen") or f'{_np["entry_year"]}-{int(_np["entry_year"]) + 1}',
                              _np.get("last_seen") or f'{_np["entry_year"]}-{int(_np["entry_year"]) + 1}', _np.get("last_pgy"), _np.get("outcome") or "left_destination_unknown",
                              f'red-year search: {(_np.get("fate_detail") or "")[:200]}'))
for k, n, pid, ey, fs, ls, pgy, o, note in ADDITIONS:
    if k in people:
        continue
    people[k] = dict(key=k, name=n, program_id=pid, program=next((p["program"] for p in people.values() if p["program_id"] == pid), None),
                     entry_year=ey, first_seen=fs, last_seen=ls, last_pgy=pgy, recorded_outcome="ADDED (roster-hole check)", tier=None,
                     outcome=o, outcome_source="addition", evidence_level=None, trail=[("addition", o)], notes=[f"[addition] {note}"])
for k, ey in ENTRY_FIX.items():
    if k in people:
        people[k]["notes"].append(f"[entry_fix] entry_year {people[k]['entry_year']} -> {ey}")
        people[k]["entry_year"] = ey

unknown_keys = Counter()


def apply(layer, f, r, gold=False):
    k = r["key"]
    p = people.get(k)
    if p is None:
        unknown_keys[layer] += 1
        return
    o = NORM.get(r.get("outcome"), r.get("outcome"))
    p["trail"].append((layer, o))
    if gold:
        lvl = r.get("evidence_level")
        if lvl:
            p["evidence_level"] = lvl
            p["gold_file"] = os.path.basename(f)
            p["gold_evidence"] = (r.get("evidence") or "")[:300]
            p["gold_url"] = r.get("external_url")
        # gold inputs were built before the dest/city passes: only a change the gold agent itself made counts
        if not (r.get("disagreement") or "").strip() or not o or o == p["outcome"] or o == GOLD_IN.get(k):
            return
    if not o:
        return
    if o in UNRESOLVED and p["outcome"] not in UNRESOLVED | {"in_training"}:
        return
    p["outcome"], p["outcome_source"] = o, f"{layer}:{os.path.basename(f)}"
    for fld in ("destination", "destination_program", "outcome_detail", "evidence", "disagreement", "note"):
        if r.get(fld):
            p["notes"].append(f"[{layer}] {fld}: {str(r[fld])[:240]}")


for f, r in load("deep/d_*_out.json"): apply("deep", f, r)
for f, r in load("ident/i_*_out.json"): apply("ident", f, r)
for f, r in load("unk2/k_*_out.json"): apply("unk2", f, r)
for f, r in load("recheck_in_training_out.json"): apply("recheck", f, r)
for f, r in load("manual_resolutions.json"): apply("manual", f, r)
for f, r in load("dest/x_*_out.json"): apply("dest", f, r)
for f in sorted(glob.glob(f"{D}/dest/city/y_*_out.json")):
    if ".bak" in f:
        continue
    own = {r["key"] for r in json.load(open(f.replace("_out.json", "_in.json")))}
    for r in json.load(open(f)):
        if r.get("key") in own:
            apply("city", f, r)
gold_seen = defaultdict(list)
for f, r in load("gold/g_*_out.json"):
    gold_seen[r["key"]].append(os.path.basename(f))
    apply("gold", f, r, gold=True)

# Targeted reconcile checks (recon/r_*_out.json), applied after gold. Keys starting "reopen:" or not in final.json are notes only.
for f in sorted(glob.glob(f"{D}/recon/r_*_out.json")):
    for r in json.load(open(f)):
        k = r.get("key", "")
        if k in people and r.get("answer_outcome") and r["answer_outcome"] != "unresolved":
            apply("recon", f, {"key": k, "outcome": r["answer_outcome"], "evidence": r.get("evidence")})
            if r.get("evidence_level"):
                people[k]["evidence_level"] = r["evidence_level"]

applied = []
for k, (o, why) in OVERRIDES.items():
    if k in people:
        people[k]["trail"].append(("coordinator", o))
        people[k].update(outcome=o, outcome_source="coordinator")
        people[k]["notes"].append(f"[coordinator] {why}")
        applied.append((k, o, why))
    else:
        applied.append((k, "KEY NOT FOUND", why))

down = []
for k, (lvl, why) in DOWNGRADES.items():
    p = people.get(k)
    if p is None or not p.get("evidence_level"):
        down.append((k, "KEY NOT FOUND / no gold record", None, lvl, why))
        continue
    down.append((k, p["name"], p["evidence_level"], lvl, why))
    p["evidence_level"] = lvl

# Analysis cutoff (user, 2026-09-29): status as of 30 June 2025 (end of academic year 2024-25).
# Cohort = residents first seen by 2024-25. Anyone still on a 2025-26 or later roster was in training at the cutoff,
# whatever happened afterwards.
CUTOFF_AY = "2024-2025"
for p in people.values():
    o = p["outcome"]
    p["attrition"] = True if o in ATTRITION else (None if o in UNRESOLVED else False)
    if p["program_id"] == 47:  # National Capital Consortium (military match, no public rosters): out of scope (user 2026-09-30)
        p["outcome_2025"], p["attrition_2025"] = "excluded_program_out_of_scope", None
    elif o == "not_a_resident":  # fellow / research fellow / prelim intern listed on a roster (recon checks)
        p["outcome_2025"], p["attrition_2025"] = "excluded_not_a_resident", None
    elif p.get("entry_year") and p["entry_year"] < 2011:  # pre-2011 entrants were only captured if they left (worklist tiers 1-2): biased, exclude
        p["outcome_2025"], p["attrition_2025"] = "excluded_entered_before_2011", None
    elif (p["first_seen"] or "") > CUTOFF_AY:
        p["outcome_2025"], p["attrition_2025"] = "excluded_entered_after_cutoff", None
    elif (p["last_seen"] or "") > CUTOFF_AY and o not in UNRESOLVED:
        p["outcome_2025"], p["attrition_2025"] = "in_training", False
    else:
        p["outcome_2025"], p["attrition_2025"] = o, p["attrition"]

out = sorted(people.values(), key=lambda p: (p["program_id"] or 0, p["key"]))
json.dump(out, open(f"{D}/merged_final.json", "w"), indent=1)

oc = Counter(p["outcome"] for p in out)
ev = Counter(p["evidence_level"] or "none" for p in out)
att = Counter(p["attrition"] for p in out)
oc25 = Counter(p["outcome_2025"] for p in out)
att25 = Counter(p["attrition_2025"] for p in out if not p["outcome_2025"].startswith("excluded"))
changed = [p for p in out if p["trail"][0][1] != p["outcome"]]
dups = {k: v for k, v in gold_seen.items() if len(v) > 1}
by_prog = defaultdict(Counter)
for p in out:
    if p["outcome_2025"].startswith("excluded"):
        continue
    by_prog[(p["program_id"], (p["program"] or "")[:45])][{True: "attrition", False: "ok", None: "unresolved"}[p["attrition_2025"]]] += 1

L = ["# Phase 3 final merge (auto-generated by scripts/tools/phase3_final_merge.py)", "",
     f"People: {len(out)}. Layer records with keys not in final.json: {dict(unknown_keys) or 'none'}", "",
     "## Outcomes", *[f"- {k}: {v}" for k, v in oc.most_common()], "",
     f"## Attrition (definition: failed to graduate NS residency): yes {att[True]}, no {att[False]}, unresolved {att[None]}", "",
     f"## AS OF 30 JUNE 2025 (analysis cutoff): attrition {att25[True]}, not {att25[False]}, unresolved {att25[None]}",
     *[f"- {k}: {v}" for k, v in oc25.most_common()], "",
     "## Evidence level (gold pass)", *[f"- {k}: {v}" for k, v in ev.most_common()], "",
     f"## Coordinator overrides: {len(applied)}", *[f"- {k} -> {o}: {w}" for k, o, w in applied], "",
     f"## Evidence downgrades: {len(down)}", *[f"- {n} ({k}): {a} -> {b} ({w})" for k, n, a, b, w in down], "",
     f"## People in several gold batches: {len(dups)}", *[f"- {k}: {v}" for k, v in dups.items()], "",
     f"## Outcome changed from final.json: {len(changed)}",
     *[f"- {p['name']} ({(p['program'] or '')[:40]}): {' -> '.join(f'{l}:{o}' for l, o in p['trail'])}" for p in changed], "",
     "## Per program, as of 30 June 2025 (attrition / ok / unresolved)",
     *[f"- {pid} {name}: {c['attrition']} / {c['ok']} / {c['unresolved']}" for (pid, name), c in sorted(by_prog.items(), key=lambda x: x[0][0] or 0)], ""]
open(f"{D}/FINAL_REVIEW.md", "w").write("\n".join(L) + "\n")
print(f"AS OF 2025-06-30: {dict(oc25)}; attrition {dict(att25)}")
print(f"people {len(out)}; outcomes {dict(oc)}; attrition {dict(att)}; changed {len(changed)}; downgrades {len(down)}; "
      f"overrides {len(applied)}; unknown-key layer records {dict(unknown_keys)}")
