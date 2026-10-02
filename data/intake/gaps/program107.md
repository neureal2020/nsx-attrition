# Program 107: UTHealth Houston (McGovern) Neurosurgery: roster gaps

7-year program with 3 residents per year now (2 per year up to entry 2015, plus added residents). The DB website is https://med.uth.edu/neurosurgery/. Baylor (5) and Houston Methodist (26) were not used.
Alumni page: https://med.uth.edu/neurosurgery/education/residency/former-residents/ (classes 2015-2026). 28 graduates were inserted into `training_history`.

## Hosts
| Host / path | From | To |
|---|---|---|
| www.uth.tmc.edu/schools/med/neurosurg/residency/current-residents.html | 2009 | 2011-05 (the 2010-11 list, before the study window) |
| www.uth.tmc.edu/schools/med/neurosurg/residency-fellowship/residency/current-residents.html | 2011-08 | 2012-01 |
| www.uth.tmc.edu/schools/med/neurosurg/education/residency/current-residents.html | 2013-05 | 2014-04 (Common Crawl) |
| med.uth.edu/neurosurgery/files/2014/03, 2014/11, 2015/09 brochure PDFs (each has a residents page) | 2014-03 | 2015-09 |
| med.uth.edu/neurosurgery/education/residency/current-residents/ (in 2016 the nav linked /neurosurgery/residency/current-residents/, which was never archived) | 2014-11 | live. Wayback has it only from 2021-11; Common Crawl has 2018-02 to 2018-09 |
| med.uth.edu/neurosurgery/education/residency/former-residents/ | 2018-02 | live |
| utphysicians.com | none | clinic pages only, no roster |

## Years
| AY | Source | n | Notes |
|---|---|---|---|
| 2011-12 | Wayback 2012-01-19 | 9 | no PGY6/7 residents that year |
| 2012-13 | Wayback 2013-06-24 | 10 | page titled "2012-2013" |
| 2013-14 | Common Crawl 2013-48 (2013-12-07) | 13 | same list as the 2013-14 brochure |
| 2014-15 | Brochure PDF (files/2014/11) | 15 | |
| 2015-16 | Brochure PDF (files/2015/09) | 15 | |
| 2016-17 | reconstructed (significance low) | 16 | no capture anywhere; all bracketed; Villarreal and Turkmani have unknown PGY |
| 2017-18 | Common Crawl 2018-09 (2018-02-24) | 18 | |
| 2018-19 | Common Crawl 2018-39 (2018-09-20) | 17 | |
| 2019-20 | reconstructed (low) | 17 | no capture; phase 2 added Lekka PGY2 (NPI Feb 2019); Divito and Kadipasaoglu left out (exit year unknown) |
| 2020-21 | reconstructed (low) | 18 | no capture; phase 2 added Chandra, O'Connor and Sheinberg as PGY1 (NPIs from Apr 2020) and Lekka as PGY3 |
| 2021-22 | Wayback 2021-11-29 | 20 | |
| 2022-23 | Wayback 2022-12-09 | 20 | Lekka off the roster this year |
| 2023-24 | Wayback 2024-04-24 | 20 | the Sep-2023 capture was stale (still the 2022-23 list) |
| 2024-25 | Wayback 2024-11-06 | 20 | |
| 2025-26 | Wayback 2025-09-10 | 21 | |
| 2026-27 | live 2026-09-27 | 16 | incomplete (low): no PGY-1 listed yet; Shentu absent |

Phase-1 significant gaps (all downgraded to low in phase 2; see the end of this file):
- 2016-17, 2019-20 and 2020-21 have no capture and were reconstructed.
- In 2019-21 two residents left (Divito, Kadipasaoglu) and one joined (Lekka), but the year of each cannot be pinned down.
- The 2026-27 roster has no interns.

## Departures (left before the terminal PGY)
- Adrian Smith: last seen 2011-12 at PGY5 (entered 2007); absent in 2012-13.
- Leon Chen: last seen 2014-15 at PGY1.
- Quoc-Bao Nguyen: last seen 2017-18 at PGY1; Mullarkey took the slot at PGY2 in 2018-19.
- Anthony Divito: last seen 2018-19 at PGY5; left 2019-21 and is not an alumnus. The NPI record suggests he switched specialty.
- Mehmet Cihan Kadipasaoglu: last seen 2018-19 at PGY1; left 2019-21.
- Kyle O'Connor: last seen 2022-23 at PGY3.
- Yujia Shentu: last seen 2025-26 at PGY3.

Other anomalies:
- Lekka was off the roster in 2022-23 and graduated a year late (2026).
- Villarreal and Turkmani each took one extra year (PGY6 in 2015-16, PGY7 in 2017-18, graduated 2018).

## Joiners (arrived above PGY-1)
- Edward Hsu: PGY2 in 2011-12.
- Ali Turkmani: PGY3 in 2013-14 (he had a prior residency at AUB).
- Anthony Divito: PGY2 in 2015-16.
- Matthew Mullarkey: PGY2 in 2018-19.
- Elvira Lekka: first seen PGY4 in 2021-22. She joined sometime in 2019-21, and the exact year was not observed.

## Totals
- 44 residents entered in 2011 or later; 51 people in total.
- Adjudication: 28 completed, 16 in training, 6 left with outcome unknown, 1 left and switched specialty.

## Problems
- Common Crawl crawls failed and need a retry: CC-MAIN-2018-30 (med.uth.edu); CC-MAIN-2015-40, 2017-34, 2019-22 and 2020-34 (old uth.tmc.edu prefix).
- The brochure years (2014-15 and 2015-16) use the PDF upload month as `captured_at`.

## Phase 2 (2026-09-28)
No gap stays significant. None of the three years has a roster anywhere, but the reconstructions are now tight, and every departure has a known destination.

Searched:
- Common Crawl rescan 2016-2021 of med.uth.edu with the fixed `cclocal.py`. All five failed crawls were retried and now work (2015-40, 2017-34, 2019-22, 2020-34, 2018-30); none holds a roster. med.uth.edu is missing from every crawl from 2016-30 to 2018-05, confirmed in the index itself.
- Wayback: the full URL list of med.uth.edu/neurosurgery, plus every changed version of the home, education and residency pages from 2016 to 2021. No news posts, no match posts, and no resident names.
- PubMed affiliation mining for 2016-2021, NPPES, Houston Methodist neurology rosters and the Hopkins anesthesiology site.

Found (all recorded in `training_history`, [phase2] rows):
- Leon Chen switched to dermatology at UT McGovern / MD Anderson (PubMed 2017-19). Left 2015.
- Quoc-Bao Nguyen switched to dermatology at UTHealth McGovern / MD Anderson (PubMed 2022-23). Left 2018.
- Anthony Divito switched to anesthesiology at Johns Hopkins (PubMed 2021-23), later Cleveland Clinic. Left in 2019 or 2020; 2019 assumed.
- Mehmet Cihan Kadipasaoglu switched to neurology. He is PGY-1 in 2021-22 on the Houston Methodist neurology roster, and PGY-4 in 2024-25. He left between 2019 and 2021; 2019 assumed.
- Kyle O'Connor switched to orthopaedic surgery (Medical City Denton UNT/TCU residency, PubMed 2024). Left 2023.
- Adrian Smith (2012) and Bart MacDonald (2011) transferred to UTMB (program 109).
- Yujia Shentu: outcome unknown.
- Transfer-in rows: Hsu (PGY2 2011), Turkmani (PGY3 2013), Divito (PGY2 2015), Mullarkey (PGY2 2018) and Lekka (PGY2 2019, inferred from her NPI of Feb 2019).
- Rosters: entry-2020 PGY1s were added to 2020-21. Lekka was added to 2019-20 and 2020-21.

Remaining (all low):
- Exit years of Divito and Kadipasaoglu.
- Villarreal and Turkmani's PGY in 2016-17.
- The 2026 interns are not posted yet.
- Shentu's outcome.

Adjudication after reload: 28 completed, 16 in training, 5 switched specialty, 1 transferred, 1 outcome unknown.
