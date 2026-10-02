# Program 28: Indiana University School of Medicine Program (Indianapolis, IN)

- Length: 7 years for 2013+ entrants; 2009-2012 entrants finished in 6 (alumni 2015-2018, no PGY7 on the 2015-16 to 2017-18 rosters). Pre-2009 entrants did 7.
- Complement: 2 or 3 in alternating years until about 2019, then 3 a year.
- Goodman Campbell Brain and Spine was IU's neurosurgery faculty group from 2010. Its site hosted the IU rosters from 2011-12 to 2016-17. These are **not** the Ascension St. Vincent program (program 3), which starts in 2025.

## Hosts
| Host/path | Dates | Notes |
|---|---|---|
| goodmancampbell.com/residencies-and-fellowships.cfm, /medical-education.cfm | 2010-2015 | Link roster files: 2011-2012 PDF (stale until 2013-11), ResidentRoster20142015.jpg |
| goodmancampbell.com/residency-and-fellowships | 2015-2019 | Links ResidentRoster2015-2016.jpg and Residents_16_17.png |
| medicine.iu.edu/neurosurgery/ (concrete5) residency-program/overview | 2012-2016 | Links index.php/download_file/view/73 (2012-13, never archived), 82 (2013-14), 85 (2014-15), 86 (2015-16) |
| medicine.iu.edu/departments/neurological-surgery/education-programs/residency/(current-)residents/ | 2016-11 to 2019-12 | No names in 2017. The 2017-18 roster stayed up, stale, until 2019-08. There is a proper list from 2019-11 |
| medicine.iu.edu/neurological-surgery/education/residency/residents | 2020 to live | Name + "Neurological Surgery, PGY n" layout (parser: data/raw/extraction/p28/parse_iu.py) |
| .../residency/alumni (and residency-alumni) | 2023 to live | Graduates 2013-2026 |

## Years
| AY | Source | n | Note |
|---|---|---|---|
| 2011-12 | GC PDF (Wayback 2012-03-04) | 14 | |
| 2012-13 | reconstructed (significance: low) | 13 | The roster PDF was never archived. Bracketed by 2011-12 and 2013-14; Bohnstedt confirmed PGY6 by news (Sep 2012, Jan 2013). Hill left after 2011-12 |
| 2013-14 | IU download_file 82 image PDF (created 2013-09) | 14 | |
| 2014-15 | GC ResidentRoster20142015.jpg | 14 | Fellows excluded |
| 2015-16 | GC ResidentRoster2015-2016.jpg | 14 | |
| 2016-17 | GC Residents_16_17.png | 15 | |
| 2017-18 | IU current-residents (Wayback 2019-08, the same page in CC 2018-05 to 2019-08) | 15+1 | Page omits Brandon Lane (PGY5); added as a reconstructed row (significance: none) |
| 2018-19 | reconstructed (significance: low) | 15 | The page stayed stale all year (CC 2018-11, 2019-04 retried). Berry had left for Miami; Priddy (entry year uncertain) not reconstructed |
| 2019-20 | Wayback 2019-11-20 | 18 | |
| 2020-21 | Wayback 2021-01-03 | 18 | |
| 2021-22 | Wayback 2021-12-08 + the PGY7s from 2021-07-25 (other) | 16+3 | |
| 2022-23 | Wayback 2023-05-11 | 19 | The fall captures omit the PGY7s |
| 2023-24 | Wayback 2024-01-16 | 19 | |
| 2024-25 | Wayback 2025-01-17 | 19 | |
| 2025-26 | Wayback 2025-11-16 | 20 | |
| 2026-27 | live 2026-09-27 | 20 | Advanced, with new interns |

Missing years: none. Reconstructed: 2012-13, 2018-19, both now **low** significance (see Phase 2).

## Departures (left before the terminal PGY)
- **Jason Hill**: last seen 2011-12 at PGY4. Absent in 2013-14 and not on the alumni list; last IU PubMed affiliation 2012. Left after 2011-12 (possibly during 2012-13), destination unknown.
- **Katherine Berry**: PGY1 2017-18, then **transferred** to University of Miami (program 90), 2018 class. Recorded in training_history.
- **Blake Priddy**: 2018 entrant, listed PGY2 in both 2019-20 and 2020-21. Absent from July 2021 onward and not an alumnus. Left in 2021. The NPI data suggests he switched specialty.

## Joiners
- **Ahmed Belal**: first seen 2021-22 at PGY2. The 2020-21 roster exists and does not list him. He moved to the 2019 class in 2024-25 (PGY6) and graduated in 2026 with Huh and Patel.

## Alumni
31 graduation rows were inserted into training_history (2013-2026). "Steven Wakeman" (2023) was not inserted: he never appears on an IU roster and is a VCU (program 118) resident who probably did an IU fellowship. The 2026 post-graduate fellows (Aljabari, Garg) were excluded. Dodd and Wilden (2012 graduates) are before the start of the alumni list.

Residents entering 2011+: 44. Adjudication (after phase 2): 33 completed, 20 in training, 2 left and did not complete (Hill, Priddy; destinations unknown), 1 transferred (Berry).

## Program length by entry year
`terminal_pgy_by_entry_year` in the JSON: 2008 and earlier = 7, 2009-2012 = 6, 2013+ = 7. The IU overview page (2013-03) calls it a "fully-approved 6-year" residency. PGY6 finishers from the 2009-2012 classes are graduates, not departures.

## Phase 2 (2026-09-28)
- Searched: Wayback host audits (2012-05 to 2013-08 and 2018-05 to 2019-10) over medicine.iu.edu/neurosurgery, /departments/neurological-surgery, /residents (GME), /gme, /news and goodmancampbell.com; the IU 2013 overview, welcome and award pages; Goodman Campbell news stories from 2012-13; Common Crawl (the phase-1 2012-14 and 2018-19 runs had finished; the failed CC-MAIN-2018-47 and 2019-18 were retried and succeeded); PubMed affiliation mining for 2012-14 and 2018-20; author checks for Hill, Priddy, Berry and Belal.
- Found: no 2012-13 or 2018-19 roster. Every 2018-19 capture shows the stale 2017-18 page, Berry included. Bohnstedt is confirmed as PGY6 in 2012-13. PubMed shows no residents missing from the rosters in either window.
- **2012-13: low significance.** It sits between two observed rosters. Both 2012 interns (Ansari and Kovanda, whose bios say they joined July 2012) appear in 2013-14. Hill's departure is recorded. The only thing that could be missed is a third 2012 intern who left within a year.
- **2018-19: low significance.** It sits between two observed rosters. Berry's transfer is recorded. The 2018 class of 3 (Budnick, Ordaz, Priddy) is complete in 2019-20.
- training_history rows added (4): Berry (transferred to Miami 2018), Hill (left 2012, unknown), Priddy (left 2021, unknown), Belal (joined PGY2 2021, graduated 2026).
- Remaining: Hill's exact departure date and the destinations of Hill and Priddy.
