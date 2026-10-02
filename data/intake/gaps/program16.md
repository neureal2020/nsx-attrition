# Program 16: Corewell Health Grand Rapids / Michigan State University (formerly Spectrum Health / MSU, GRMEP), Phase 1 gap report

This is a new 7-year program with 1 resident per year. The first class started in summer 2018. In 2017-03 the grmep.org page said it was "seeking ACGME approval". The 2019 spectrumhealth.org page says "Beginning in the summer of 2018, a single resident per year". Years 2011-12 to 2017-18 come before the program existed, so they are not gaps.

Note: `programs.website` in the DB points to neurology.msu.edu. The neurosurgery page is https://corewellhealth.org/graduate-medical-education/west-michigan/residencies/neurological-surgery.

## Hosts / paths
| URL | From | To |
|---|---|---|
| grmep.org/programs/neurological-surgery/ (+ /resident-bios/, empty) | 2016-08 | 2017-12 |
| www.spectrumhealth.org/medicaleducation/residencies/neurological-surgery (+ /neurological-surgery-resident-bios) | 2018-10 (CC) / 2019-10 (Wayback) | 2022-01 |
| www.spectrumhealth.org/medical-education/residencies/neurological-surgery-residency (+ -bios) | 2022-01 | 2025-03 (then 301 to Corewell) |
| corewellhealth.org/graduate-medical-education/west-michigan/residencies/neurological-surgery (+ /bios, page-data.json) | 2025-02 | live |

The program page itself carries the full roster. The separate bios page never listed Nina Shank.

## Year-by-year
| AY | Source | Status |
|---|---|---|
| 2018-19 | Common Crawl CC-MAIN-2018-47, 2018-11-17 (program page) | Observed, 1 (Verhey). There is no Wayback capture |
| 2019-20 | Wayback 2019-10-18 | Observed, 2 |
| 2020-21 | Wayback 2020-10-26 | Observed, 3 |
| 2021-22 | Wayback 2021-11-04 | Observed, 4 |
| 2022-23 | Wayback 2023-03-25 | Observed, 5 (the Sep 2022 capture had not yet added the intern) |
| 2023-24 | Wayback 2023-09-29 | Observed, 6 |
| 2024-25 | Wayback 2024-12-02 | Observed, 7 |
| 2025-26 | Wayback 2025-10-07 (Corewell) | Observed, 7 |
| 2026-27 | live 2026-09-27 | Observed, 5 (no PGY-3, no PGY-5) |

## Entry classes (9 residents, 1 each year 2018-2026)
Verhey 2018, Restrepo Orozco 2019, Abouelleil 2020, Montenegro 2021, Shank 2022, Madhani 2023, Farooq 2024, DeGroot 2025, Looman 2026. Entry years are consistent across all observations.

## Alumni
The "Learn About Our Graduates" PDF lists Verhey (Class of 2025) and Restrepo Orozco (Class of 2026). Both were inserted into `training_history`.

## Departures (resolved in phase 2)
- **Nina Shank** (2022 class, Tulane MD): last seen PGY-4 in 2025-26 (still listed 2026-05-20). **Switched specialty to general surgery.** The live Carilion Clinic General Surgery residents page (https://gme.carilionclinic.org/general-surgery-residency/residents, 2026-09-28) lists "Nina Shank, MD, Medical School: Tulane University School of Medicine" under PGY1 Residents. She is not on the Carilion neurosurgery (program 8) roster. training_history th 3387 (switched_specialty, end 2026).
- **Jeffrey Farooq** (2024 class, USF Morsani): last seen PGY-2 in 2025-26 (still listed 2026-05-20). **Transferred to UChicago (program 78) at PGY-3 in 2026-27** (UChicago live roster and June 2026 newsletter). training_history th 3388 (transferred, end 2026).

## Joiners
None.

## Problems
- No year is missing. The CC index failed for CC-MAIN-2017-39 and CC-MAIN-2018-34 on the broad prefixes, which is irrelevant here. The shared cclocal.py roster filter skips '/residencies/<program>' URLs, so a narrow-prefix copy (p16/cc_ns.py) was used.
- Both departures are now confirmed at their destinations (see above).

## Phase 2 (2026-09-28)
- **Completeness:** complement is 1 per year, 7-year program. Counts 1,2,3,4,5,6,7,7 for 2018-19 to 2025-26 equal the number of active classes, and 2026-27 (5) is 7 minus the two departures. None of the known parser misses apply: the pages use PGY/"Class of" headings, with no Chiefs heading, no inline "Name, PGY" entries and no suffix names. Every year: status observed, significance none.
- **Common Crawl rerun with the fixed filter:** all 84 crawls 2018-2026 over the three program-page prefixes (spectrumhealth /medicaleducation/, /medical-education/, corewellhealth). 41 captures saved in `data/raw/extraction/p16/phase2/cc_all/` and parsed. Every capture agrees with the roster, and no unknown resident appears (the extra names are faculty). The CC-MAIN-2026-39 /bios copy (2026-09-12) is stale.
- **Terminal PGY by entry year:** 7 for every cohort 2018-2026.
- **Outcomes recorded:** 2 training_history rows (Shank switched_specialty, Farooq transferred). Adjudication: 5 in training, 2 completed, 1 switched specialty, 1 transferred.
- **Remaining:** none.
