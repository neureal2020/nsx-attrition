# Program 51: Ohio State University Hospital Program (Columbus, OH)

This is a 7-year program (PGY-1 to PGY-7). It took 2 residents per year for the 2005-2015 entry classes, 3 per year for 2016-2023 (the 2020 class was listed with only 2), and 4 per year from the 2024 class on. A graduates list (1954-2026) sits at the bottom of the live residents page.

## Hosts
| Host / path | Dates | Content |
|---|---|---|
| neurosurgery.osu.edu/education/residency/current_residents/ (index.cfm), former_residents/ | 2010-06 .. 2016-01 | Roster ("Program Year n") and alumni. Returns 404 from 2016-02; the host 301s to wexnermedical from 2016-12. |
| wexnermedical.osu.edu/.../department-neurosurgery/neurosurgery-residency/our-residents (+/past-residents) | 2016-10 .. 2018-12 | Roster (PGY n) and alumni |
| .../department-neurosurgery/education-and-training/neurosurgery-residency/our-residents (+/past-residents) | 2020-01 .. 2020-10 | Roster and alumni |
| medicine.osu.edu/departments/neurosurgery/education/residency/residents | 2021-01 .. live | Roster and graduates list (/past-residents existed until 2024-07) |

## Years
| AY | Status | Significance | Reason |
|---|---|---|---|
| 2011-12 | observed | none | Nov 2011 roster |
| 2012-13 | reconstructed | low | See below. No one could have entered or left unseen. |
| 2013-14 | observed | none | April 2014 capture; every class complete |
| 2014-15 | observed | none | March 2015 capture; every class complete |
| 2015-16 .. 2025-26 | observed | none | Roster captures |
| 2026-27 | observed | none | Live page (PGYs advanced, 4 new interns) |

## 2012-13 (reconstructed, low significance)
There is no roster capture between 2012-01 and 2014-04. Phase 2 searched again:
- Host-wide Wayback audits of neurosurgery.osu.edu, medicalcenter.osu.edu, medicine.osu.edu and osumc.edu paths.
- Link audit of the home, news, RSS, article and lab pages from 2012-13.
- Common Crawl 2012-2014 over the whole neurosurgery host with the new filter (11 crawls, none failed).

None of these holds a roster or resident news.

The gap still hides nobody:
- Everyone who entered in 2011 or earlier is on both bracketing rosters.
- The 2012 class (complement 2) is David Dornbos plus **Nishanta Baidya**. Phase 2 found that Baidya entered in 2012: his NPI was issued on 2012-04-03 (Match season), he was already at OSU publishing from the Dardinger skull-base lab in 2011-12, and all his PGY labels from 2013 to 2017 give an entry year of 2012. He is now reconstructed at PGY1 for 2012-13 and is not a transfer in.
- PubMed affiliation mining for 2012-13 (97 papers) turned up only roster residents, fellows and visiting scholars.

## Departures (evidence found in phase 2)
| Name | Last AY / PGY | Outcome | Evidence |
|---|---|---|---|
| Nishanta Baidya | 2016-17 / 5 | **Switched to radiology** | Department of Radiology, University of Wisconsin, 2018-19 (PubMed 31183841). NPI (nuclear medicine/radiology) agrees but is used only as corroboration. |
| Candice Carpenter | 2018-19 / 3 | Did not complete; destination unknown | No publication after 2019. Her NPI is trainee-only, so phase 1's NPI "switch" call is withdrawn. |
| Orel Zaninovich | 2019-20 / 1 | Did not complete; destination unknown | Last paper is from OSU neurosurgery in 2020. His NPI says anesthesiology (Arizona), but NPI is not counted as evidence. He is not on the University of Arizona anesthesiology residents or alumni pages. |
| James Mossner | 2021-22 / 2 | **Transferred** to McGaw/Northwestern (program 41) at PGY3 in 2022-23 | Northwestern rosters list him from 2022-23 through 2025-26, and he has Northwestern affiliations 2024-26. The destination row is th_id 429. |
| Ahmed Jorge | 2023-24 / 3 | Unknown | Still listed as PGY4 in Jun/Jul 2024, gone by Nov 2024. No later paper or roster. A hidden research leave cannot be ruled out. |
| Christen O'Neal Swann | 2025-26 / 4 | Unknown | Listed through Apr 2026, absent from the live 2026-27 page. She has OSU papers from 2026 and is not on OU's 2026-27 roster. This is too recent to resolve and may be a research year. |

**Absence, not a departure: Daniel Kreatsoulas.** He was off the roster from 2019-20 through 2022-23, but he published continuously from OSU Neurological Surgery in 2020-23 (PubMed 32019726, 35365316, 36871221). He returned at PGY6 and graduated in 2025. This shows that OSU leaves research years off its roster, which is why Jorge and O'Neal Swann are left as "unknown" rather than "did not complete".

**Joiners:** none.

## Counts
- 45 residents entered in 2011 or later.
- Adjudication: 32 completed, 20 in training, 1 switched specialty, 1 transferred, 2 did not complete (outcome unknown), 2 left with outcome unknown.
- training_history rows added in phase 2: 6 (Baidya, Mossner, Carpenter, Zaninovich, Jorge, O'Neal Swann).

## Remaining
- The destinations of Carpenter, Zaninovich, Jorge and O'Neal Swann are unknown.
- Recheck Jorge and O'Neal Swann on the 2027-28 roster, in case they were on hidden research years.

## Problems
Europe PMC returned 503 errors throughout, so PubMed and OpenAlex were used instead. Common Crawl finished all 11 crawls with no failures.
