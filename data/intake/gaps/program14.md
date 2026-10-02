# Program 14: Clinical Center at the National Institutes of Health Program (Bethesda, MD)

NINDS Surgical Neurology Branch neurosurgery residency. It is 7 years long with 1 position per year. The first intern was Gautam Mehta in July 2010, so `first_class_year` = 2010.
- Partners: University of Virginia. It was a joint NIH-UVA track, with PGY-1..3 and PGY-7 at UVA. From about the 2021 class the clinical partner is MedStar Georgetown (GUH, WHC, CNMC). Last UVA-track resident: Maxwell Laws, PGY-7 in 2026-27.
- No link to Walter Reed or the National Capital Consortium was found.

## Hosts
| Host / path | Dates | Content |
|---|---|---|
| clinicalcenter.nih.gov/training/gme/programs/neurological_surgery.html | 2010-05 .. 2016-01 | "Current Residents" section. Stale in 2012-13 and 2015-16; omits Weintraub from 2013-14. The roster was dropped in 2016. Later at www.cc.nih.gov/... with no roster; live returns 403. |
| neuroscience.nih.gov/ninds/ClinicalPrograms/... (NeurologicalSurgeryResidencyProgram.aspx etc.) | 2015 .. 2020 | Description only |
| neuroscience.nih.gov/neurosurgery/Home/Education/CurrentResidents.aspx, FormerResidents.aspx | 2019-07 .. 2020-08 | Single stale roster, content-dated 2018-19 |
| research.ninds.nih.gov/surgical-neurology-branch/education-training/{current-residents,alumni,residency-program} | 2021-10 .. 2025-04 | Roster and alumni. Retired Jun 2025 (301 to generic NINDS page); the host no longer resolves. |
| www.medicine.virginia.edu/clinical/departments/neurosurgery/residenttraining[/current-residents] (UVA) | 2010 .. 2015-11 | UVA roster; NIH residents marked "(NIH)" |
| med.virginia.edu/neurosurgery/resident-training/current-residents/ (UVA) | 2016-08 .. live | Same. No Wayback captures 2016-09..2019-07; Common Crawl has 2017-09 .. 2018-12. |
| www.medstarhealth.org/education/residency-programs/neurosurgery/current-residents (MedStar Georgetown) | 2024-04 .. live | NIH residents marked "(NIH)" |

## Years
All years from 2011-12 to 2026-27 are observed. The only reconstructed row is Pomeraniec at PGY-1 in 2016-17. Per-year status and significance are in `program14.json` under `year_status`.

**Phase 2: no significant gaps remain.**
- **2016-17 (low).** The only capture (UVA, Aug-2016) has no PGY-1 group.
  - No other capture exists. Wayback was audited 2016-06..2017-08 on the UVA, CC-GME, NINDS and cc.nih hosts. Common Crawl was checked across 21 crawls (2016-07..2017-51) with 0 failures.
  - Pomeraniec was added as a reconstructed NIH PGY-1 (`source_type: manual`). He appears as PGY-2 '(NIH)' in 2017-18 and graduated in 2023 per the alumni page.
  - With 1 position per year and his class filled, only an extra, over-complement intern could be missed.
- **2013-14 (none).** The NIH CC page omits Weintraub. He is bracketed at PGY-4 (2012-13) and PGY-6 (2014-15) and is listed on the UVA page as '(NIH)'.
- **2017-18 and 2018-19 (none).** These come from Common Crawl captures of the UVA page, and all NIH classes are present.
- **2025-26 and 2026-27 (none).** MedStar and UVA partner pages together cover all 7 classes.
  - Wayback CDX 2025-26 of www.ninds.nih.gov and www.cc.nih.gov/training shows no NIH roster.

## Classes (entry year: resident, outcome)
| Entry | Resident | Outcome |
|---|---|---|
| 2009 | David Weintraub | Joined at PGY-3 in 2011-12, moving from UVA. PGY-7 in 2015-16, graduated 2016 |
| 2010 | Gautam Mehta | Graduated 2017 (alumni page) |
| 2011 | Winson Ho | Graduated 2018 (alumni page) |
| 2012 | Alexander Ksendzovsky | Graduated 2019 (alumni page) |
| 2013 | Dominic Maggio | Graduated 2020 (alumni page) |
| 2014 | none | No 2014 entrant |
| 2015 | Panagiotis Mastorakos | Graduated 2022 (alumni page) |
| 2016 | Jonathan Pomeraniec | Graduated 2023 (alumni page) |
| 2017 | Leonel Ampie | Graduated 2024 (PGY-terminal roster) |
| 2018 | David Asuzu | Graduated 2025 (PGY-terminal roster) |
| 2019 | Joshua Diamond | Graduated 2026 (PGY-terminal roster) |
| 2020 | Maxwell Laws | PGY-7 in 2026-27 |
| 2021 | Joseph McAbee | In training |
| 2022 | Amanda Roehrkasse | In training |
| 2023 | Evan Der | In training |
| 2024 | Jessica Chen | In training |
| 2025 | Mark Mizrachi | NIH PGY-1 2025-26, **transferred** to Loma Linda (program 31) as PGY-2 2026-27 |
| 2026 | Peyton Presto | In training |

Every person has one consistent entry year. Class size is 1 in every year except 2014, which had 0.

## Departures before terminal PGY
- **Mark Mizrachi transferred out after PGY-1 (2025-26).** This is confirmed.
  - The MedStar Georgetown page lists him as "Mark Mizrachi, MD, PhD (NIH)" PGY-1 in the Jan, Feb and Jun 2026 captures. He is absent from Sep 2026 on.
  - The live Loma Linda residents page (program 31) lists "Mark Mizrachi, MD, PhD PGY-2" in 2026-27, with a Hofstra/Northwell MD. His PubMed Hofstra/Northwell/Feinstein MD-PhD affiliations (2021-2025) fit.
  - It is the same rare name and credential, and the PGY is continuous. `crossmatch.json` also paired these two records.
  - `training_history` th_id 3380 records the transfer out (`completed=no`, `departure_type=transferred`, `end_year=2026`). Program 31 inserted the matching transfer-in row (th_id 2723).
  - The NIH PGY-2 slot is empty in 2026-27.

## Joiners above PGY-1
- **David Weintraub** joined at PGY-3 in 2011-12. He entered UVA in 2009 and is on the UVA lists of Sep 2010 and Mar 2011 with no marker.
  - The NIH CC page first lists him in Apr 2012 as "PGY3". The Oct 2011 and Jan 2012 captures show only Ho and Mehta.
  - UVA shows "Weintraub, David(at NIH)" from May 2012.
  - This was an internal move within the NIH-UVA track. Program 113 excludes him for all years, which is consistent with this program, so there is no UVA-side departure.
  - He was PGY-7 in 2015-16 and graduated in 2016 (th_id 3376, start_year left null so his entry cohort stays 2009).

## Alumni page and training_history
The alumni page is research.ninds.nih.gov/.../alumni (Wayback 2022-05..2023-09; the same list is embedded in residency-program until 2025-04). It covers graduation years 2017-2023. Six rows were inserted into `training_history`:
- Mehta 2017
- Ho 2018
- Ksendzovsky 2019
- Maggio 2020
- Mastorakos 2022
- Pomeraniec 2023

## Terminal PGY
PGY-7 for every cohort (entry years 2009-2026). This is recorded as `terminal_pgy_by_entry_year` in the JSON.

## Phase 2 training_history rows (2026-09-28)
- Graduations from PGY-terminal rosters: Weintraub 2016, Ampie 2024, Asuzu 2025, Diamond 2026.
- Transfer out: Mizrachi 2026.

## Adjudication
Result: COMPLETED 10, IN TRAINING 6, LEFT -> TRANSFERRED 1 (Mizrachi -> Loma Linda).

## Problems
- NINDS and CC live sites return 403 to automated fetches. This was not bypassed.
- The NIH alumni list stops at 2023.
- **Common Crawl 2017-2018 pass:** completed, 24 crawls, 0 failures.
- **Common Crawl 2025-26 pass:** started and then stopped, because partner pages already covered those years.
