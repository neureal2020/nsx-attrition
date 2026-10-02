# Phase 3 overnight run: summary (2026-09-29)

**Nothing has been written to the database.** Everything below is in files for review.

## What ran
- All 3,950 residents (124 programs; 2011+ entrants, plus earlier entrants whose outcome was open or weak) got:
  - (A) a Google search including faculty and program bios: found for 3,934
  - (B) their Doximity page opened in Chrome: 3,038 profiles found
- US News: about 200 people done. It blocked us twice ("automated behavior"), the second time apparently for this whole connection, so it is **paused**. The remaining ~3,450 are in `usnews_todo.json` and `usnews/u_005..u_091_in.json`.
- A deep pass (up to 8 searches per person) on the 108 people still "unknown" resolved 38.

## Files
- `final.json`: one record per person (input + finding, with deep-pass overrides)
- `merged.json`: the same, before the deep pass
- `REVIEW.md`: disagreements, QA flags, weak identities (re-run `python3 scripts/tools/phase3_merge.py` to regenerate)
- `RUNLOG.md`: batch-by-batch notes and every case flagged for review
- `deep/d_*_out.json`, `usnews/u_*_out.json`: raw deep and US News results

## Final outcome counts (final.json)
| outcome | all | tier 1 (open departures) | tier 2 (weak departure records) | tier 3 (everyone else) |
|---|---|---|---|---|
| completed | 1915 | 34 | 0 | 1881 |
| in training | 1689 | 14 | 0 | 1675 |
| switched specialty | 155 | 68 | 10 | 77 |
| transferred | 105 | 2 | 11 | 92 |
| left medicine | 15 | 12 | 1 | 2 |
| died in training | 1 | 1 | 0 | 0 |
| unknown | 70 | 58 | 0 | 12 |

**Main finding: 48 of 189 recorded departures (tier 1) had not left.** 34 completed and 14 are still in training, mostly because roster pages were incomplete or the person was on a research year. Using roster disappearance alone would have overstated attrition.

## Decisions needed from you
1. **Deceased residents.** Yimo Lin (OHSU) died during residency in 2018. For Ebot and Grewal, agents saw death notices but, per the brief, did not record details. Should these go under the database's `deceased` status and be excluded from voluntary attrition?
2. **US News.** Retry later at 1 agent with long gaps, or skip it? You said dates are secondary. So far it has mostly confirmed Doximity.
3. **US News batch u_002** was collected with scripted in-page `fetch()` calls. That method is now banned in the brief. Keep the data or redo the batch?
4. **Post-completion exits** (Wetzel: hair restoration; Marcellino: anesthesiology after neurosurgery; Sivaganesan: orthopaedic spine): these are not residency attrition. Track them separately?
5. **Program closures:** many transfers cluster around Wayne State (~2020), the old UNM program and UPR. Report them separately, as the handoff planned?

## Needs a check before loading
- **Identity:** 408 probable, 14 ambiguous, 10 not found. See REVIEW.md.
- **Conflicting records to reconcile:**
  - Rachel Stein: path is Tennessee → Mayo Jacksonville → radiology; batch 046 had the direction reversed.
  - Fang: phase 1 said radiology; a Healthgrades listing says neurosurgeon.
  - Jimenez: the same MCW Doximity record was used for two different programs.
- **Entry years:** 70 cases where Doximity's residency start is 2+ years from the recorded entry year. Research or preliminary years may be counted in entry_year; check how it is derived.
- **Cross-program transfers found** (each should count as a departure from the origin program): Loma Linda → UC Irvine ×2, → Utah, → Brigham; Nebraska → Chicago, → Baylor, → Northwestern (Mossner was Ohio State); Emory → Baylor; Buffalo → Barrow; Upstate → Maryland, → WVU ×2; UW → Nebraska; Pitt → UCSF, → Upstate; Wayne State → many; UNM → Colorado, → Oklahoma, → Northwell. Full list in RUNLOG.md.

## Still unknown (70)
58 are tier-1 departures. Many are simply absent from current rosters with no public trace. Some are likely June 2026 graduates without a public record yet (Munier, Gaulden, M. Johnson, R. Turner, Fleming, Marcet). The list is in final.json (`finding.outcome == "unknown"`).
