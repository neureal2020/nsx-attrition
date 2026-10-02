# Program 105: University of Tennessee College of Medicine Program (UTHSC / Semmes-Murphey, Memphis TN), Phase 1 gap report

The program is **7 years for classes entering in 2013 or later** and was **6 years for classes entering through 2012** (graduates 2012-2018). The site said "six-year ... two residents per year" until 2014 and "seven-year" from March 2015. There were no graduates in 2019, which fits the switch. The complement was 2 per year until 2018 (3 in 2010 and 2017) and has been 3 per year since 2019 (2 in 2021). The 2026-27 roster has 4 PGY-1s.

## Hosts / paths
| URL | From | To |
|---|---|---|
| www.utmem.edu/neurosurgery/ (old UT Memphis host) | 2008 | 2009-01. Before the window; no roster |
| uthsc.edu/neurosurgery/residents.php | 2010-06 | 2015-03. **Program description only, never a roster** |
| uthsc.edu/neurosurgery/residents/index.php, /residents/residents.php, /residents/resident-alumni.php | 2015-08 | 2017-03 (index.php runs to 2018-03 but has no roster) |
| uthsc.edu/neurosurgery/residency/current-residents.php (+ graduates.php 2019-08..2024-07, former-residents.php 2026-03..live) | 2019-10 | live 2026-09-27 |
| semmes-murphey.com/training.php (clinical partner practice) | 2007-09 | 2011-02. Only links to utmem.edu |
| semmes-murphey.com/resident-training-program | 2017-04 (Common Crawl); in Wayback from 2019-03 | 2019-12 |
| semmes-murphey.com/residency-training (+ /resident/&lt;name&gt; bios in 2020) | 2020-06 | 2026-07 |

## Year-by-year
| AY | Source | Status |
|---|---|---|
| 2011-12 | manual | **Reconstructed, low significance.** No capture exists. Bracketed by the UTHSC GME Neurosurgery house-staff list of Oct 2008 and May 2013 plus the alumni list |
| 2012-13 | Common Crawl CC-MAIN-2013-20 (2013-05-24), uthsc.edu/GME/staff_list.php?program=24 | Observed, 12. Alphabetical list with no PGY labels, so PGY comes from the graduation year. Same names as the reconstruction |
| 2013-14 | Common Crawl CC-MAIN-2013-48 (2013-12-06), same page | Observed, 12, as reconstructed |
| 2014-15 | Common Crawl CC-MAIN-2014-41 (2014-10-01), same page | Observed, 13, as reconstructed |
| 2015-16 | Wayback 2015-09-06 uthsc residents/index.php | Observed, 13 |
| 2016-17 | Wayback 2016-10-25 uthsc residents/residents.php | Observed, 12 |
| 2017-18 | Common Crawl CC-MAIN-2017-47 (2017-11-24), semmes resident-training-program | Observed, 13. No Wayback roster for this year |
| 2018-19 | Wayback 2019-03-29 semmes resident-training-program | Observed, 13 (same as CC 2018-10 and 2018-12) |
| 2019-20 | Wayback 2019-10-22 uthsc current-residents | Observed, 15 |
| 2020-21 | Wayback 2020-10-22 semmes residency-training | Observed, 16. No uthsc capture exists |
| 2021-22 | Wayback 2021-08-13 uthsc | Observed, 15 |
| 2022-23 | Wayback 2022-12-07 uthsc | Observed, 16 |
| 2023-24 | Wayback 2024-03-03 uthsc | Observed, 17 (same as semmes 2023-12-09) |
| 2024-25 | Wayback 2024-12-16 uthsc | Observed, 19. The 2024-07 capture's "Yagmurlu PGY-2" is a typo |
| 2025-26 | Wayback 2026-01-24 semmes residency-training | Observed, 20 (same as uthsc 2026-04-11) |
| 2026-27 | live, uthsc current-residents (page updated 2026-08-14) | Observed, 21. Advanced from 2025-26, 4 interns |

Reconstruction rule: PGY = track length − (graduation year − AY end year), using the 6-year track for graduates up to 2018 and the 7-year track after. Every reconstructed PGY matches the 2015-16 roster. Only alumni-listed people were reconstructed.

## Phase 2 (2026-09-28)
- **New source:** the UTHSC GME "Procedural Competence" house-staff list. `uthsc.edu/GME/staff_list.php?program=24` is Neurosurgery, `program=51` is Surgery-Preliminary and `program=25` is pediatric neurosurgery fellows. Wayback holds only 2008-05, 2008-10 (utmem.edu) and 2016-04/07. Common Crawl holds about 40 copies from 2013-05 to 2016-12. Those copies make 2012-13, 2013-14 and 2014-15 observed, and each matches the phase-1 reconstruction exactly. The 2015-09 copy matches the 2015-16 roster.
- **2011-12** is still unobserved: CC-MAIN-2012 has no staff_list record. It is **low** significance. The Oct 2008 list (Boehm, Broadway, Duntsch, Helms, Kimball, Oliver, Phillips, Van Poppel, Weimar, Winestone, Yam) and the May 2013 list together account for every 2006-2012 entrant who graduated. Every class 2009-2012 is complete on the 2013 list (2/3/2/2).
- **Class of 2014 (one graduate):** the Oct 2008 Surgery-Preliminary list names Bate, Goodwin and Walls. Neither Goodwin nor Walls ever appears on a neurosurgery list, the alumni page or a UT neurosurgery paper, so Bate was very probably the only neurosurgery intern in 2008. This is not an in-window loss.
- **Christopher Duntsch** is on the 2008 lists (in PubMed since 2004, so he entered around 2003-05) and is not on the alumni page. He is absent by May 2013 and is treated as a pre-window leaver, with Dallas practice from July 2011 (public record).
- PubMed (2008-2016) and Europe PMC per-author affiliation mining found no resident names beyond the known roster; the other names were alumni from before 2011, faculty, fellows or students. OpenAlex returned 429 and was skipped.
- The Semmes-Murphey site from 2010 to 2016 has only doctor and news pages with no resident content. UTHSC news has no neurosurgery resident items.
- `terminal_pgy_by_entry_year`: 6 for entrants through 2012, 7 from 2013.

## Departures (left before the terminal PGY)
- **Timothy Gooldy** (2017 intern class): last seen **2018-19 PGY-2** (semmes page until CC 2019-04-23). He is gone by 2019-06-17 and absent from every 2019-20 roster. **He transferred to Barrow** (program 4) as PGY-3 in 2019-20; program 4's training_history has him graduating from Barrow in 2024. This confirms the lead.
- **Jonathan Dvorak** (2017 class): last seen **2019-20 PGY-3**. He is on the semmes page and bio ("third-year") until 2020-08, and absent from 2020-10-22 on. He is not on the alumni page. The adjudicator's "switched specialty" rests on a weak NPI match (1912432386: enumerated 2017-04, "General Practice", Charlotte NC). **Outcome unknown**: PubMed has no record of him under any affiliation, so the NPI match is not used. training_history th_id 2983 (`unknown`).
- **Rachel Stein**: **joined in 2020-21 as PGY-2** (semmes 2020-10-22; bio of 2020-09-29 says "second-year"). She was still listed 2021-01-24 and gone by 2021-04-11, so she **left partway through 2020-21**. She is on no uthsc capture, because none exists for 2020-21. **Switched to radiology**: PubMed affiliation Dept of Radiology, UF College of Medicine-Jacksonville on papers received 2021-03-16 (PMID 34352049) and 2021-04-13 (PMID 34338815), through 2026. training_history th_id 2984 (`switched_specialty`). Gooldy's transfer is th_id 2982.

## Joiners (above PGY-1)
- **Rachel Stein**: 2020-21, PGY-2. The 2019-20 roster exists and does not list her. She was attached to the 2019 class.

## Class sizes by entry year (42 residents entering 2011+)
2011: 2 · 2012: 2 · 2013: 2 · 2014: 2 · 2015: 2 · 2016: 2 · 2017: 3 (Gooldy and Dvorak left; Roberts-Dacus graduated alone in 2024) · 2018: 2 · 2019: 3 + Stein · 2020: 3 · 2021: 2 · 2022: 3 · 2023: 3 · 2024: 3 · 2025: 3 · 2026: 4

## Alumni page
https://www.uthsc.edu/neurosurgery/residency/former-residents.php (live). Earlier versions: graduates.php 2019-2024 and residents/resident-alumni.php 2015-2016. I inserted 28 graduation rows (2012-2026) into training_history. **The class of 2014 has only Berkeley Bate.** A 2008 entrant who left may be hidden in the unobservable 2011-14 years or before them.

## Adjudication
28 COMPLETED, 21 IN TRAINING, 1 LEFT -> TRANSFERRED (Gooldy, Barrow), 1 LEFT -> SWITCHED SPECIALTY (Stein, radiology), 1 LEFT -> did not complete, outcome unknown (Dvorak).

## Problems
- 2011-12 is still unobserved. Its significance is low (see Phase 2).
- Dvorak's destination is unknown.
- OpenAlex was rate-limited (429). The phase-1 Common Crawl failures were not retried, because those years are now observed.
