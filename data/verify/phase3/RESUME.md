# Resume point (updated 2026-09-29, second session, limit 30,000)

**Nothing has been written to the database yet.** Full detail: RUNLOG.md (lines after "RESUMED").

## User decisions in force (see memory: attrition-definition, program-procedure)
- Attrition = failing to graduate a neurosurgery residency. Not attrition: transfers that completed elsewhere, deceased, exits after completion.
- Evidence = program website + external validation. Gold = a current bio page actually opened. Directory listings never gold; Doximity silver only with board cert shown.
- Publication affiliations do not count. in_training requires the program's CURRENT resident page.
- Only WebSearch for searching; no other engines; no CAPTCHA/login bypass; no curl/scripted fetch; no health.usnews.com (except u_002 redo).
- Parallel agents: each must use a private scratchpad subfolder and write only its own output file (shared add.py collision happened in city sweep).

## Status: VERIFICATION COMPLETE, AWAITING SIGN-OFF (2026-09-29 evening)
- All passes done, plus targeted reconcile checks recon/r_1, r_2 (13 items) and proper re-open of the curl-fetched pages (both confirmed).
- User decisions applied (see memory attrition-definition): cutoff = status as of 30 June 2025; T. Wilson attrition at UAMS / Wake transfer; Wetsel transfer; Klein attrition.
- `python3 scripts/tools/phase3_final_merge.py` -> merged_final.json (fields outcome_2025 / attrition_2025) + FINAL_REVIEW.md.
- **As of 30 June 2025: 3,407 residents in cohort (543 later entrants excluded); attrition 230 (6.8%), not attrition 3,177, unresolved 0.**

## Status (2026-09-30): gold pass complete for every in-scope resident; REPORT PUBLISHED
- Report: https://claude.ai/artifact/UA4UMfKkZ11kFSsNvjFY4X (rebuild: phase3_final_merge.py -> confidence_heatmap.py -> attrition_analysis.py -> build_report_v2.py, then republish report.html)
- Excel heatmap: data/verify/report/program_year_confidence.xlsx
- Final (v3, 2026-09-30): cohort 3,387 (entrants 2011-24 only), attrition 221 (6.5%); finished classes 7.1% (6.0-8.4); program-years green 1215 / yellow 279 / red 63. Final red-year search done (data/verify/programs/red_1..5_out.json). Lit full texts in data/verify/lit/fulltext.

## Remaining
1. User: answer whether X posts read in their logged-in browser count as gold (58 records; grades only).
2. DONE: PDFs downloaded and verified (Agarwal on our definition = 7.7%). Optional: paywalled program histories for MCG (Viers 2014 Neurosurgery 75:295) and MCW (PMID 30660875) might name missing 2011/2013 interns.
3. Optional: class-by-class NRMP reconciliation (not approved); entry-year fixes logged in RUNLOG not applied.
4. User sign-off, then DB load.
