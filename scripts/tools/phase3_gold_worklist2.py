#!/usr/bin/env python3
"""Build gold-pass batches g_065+ for every in-cohort resident not yet in a gold batch.

    python3 scripts/tools/phase3_gold_worklist2.py

In-cohort = first seen by 2024-25 (30 June 2025 cutoff). Uses merged_final.json for the current outcome,
final.json for prior sources and program_sources.json for the program-website part. Same record format as
gold/g_001..g_064. Writes data/verify/phase3/gold/g_NNN_in.json (25 per batch). Nothing is written to the DB.
"""
import glob, json, os

D = "data/verify/phase3"
merged = {p["key"]: p for p in json.load(open(f"{D}/merged_final.json"))}
final = {r["key"]: r for r in json.load(open(f"{D}/final.json"))}
sites = json.load(open(f"{D}/program_sources.json"))
done = {r["key"] for f in glob.glob(f"{D}/gold/g_*_in.json") for r in json.load(open(f))}
last = max(int(os.path.basename(f)[2:5]) for f in glob.glob(f"{D}/gold/g_*_in.json"))

rows = []
for k, p in merged.items():
    if k in done or p["outcome_2025"] == "excluded_entered_after_cutoff":
        continue
    f = final[k]["finding"]
    obs = [s["url"] for s in sites.get(k, []) if s.get("url") and not s["url"].startswith("reconstructed")]
    site = obs[-3:] or [s.get("url") for s in sites.get(k, [])][-2:]
    rows.append({
        "key": k, "name": p["name"], "program_id": p["program_id"], "program": p["program"],
        "entry_year": p["entry_year"], "last_seen": p["last_seen"], "outcome": p["outcome"],
        "outcome_detail": (f.get("outcome_detail") or "")[:400], "current": f.get("current"),
        "program_site": site,
        "prior_sources": [{k2: s.get(k2) for k2 in ("url", "type", "evidence")} for s in (f.get("sources") or [])][:4],
        "task": "EXTERNAL_TRAINING" if p["outcome"] == "in_training" else "CURRENT_BIO",
    })
rows.sort(key=lambda r: (r["task"], r["program_id"] or 0, r["key"]))
n = 0
for i in range(0, len(rows), 25):
    n += 1
    json.dump(rows[i:i + 25], open(f"{D}/gold/g_{last + n:03d}_in.json", "w"), indent=1)
print(f"{len(rows)} people -> batches g_{last + 1:03d}..g_{last + n:03d}; "
      f"CURRENT_BIO {sum(r['task'] == 'CURRENT_BIO' for r in rows)}, EXTERNAL_TRAINING {sum(r['task'] == 'EXTERNAL_TRAINING' for r in rows)}")
