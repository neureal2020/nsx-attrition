# Program 50: NYU Grossman School of Medicine (New York, NY): gap report

7-year program. Complement: 3 a year since 2015. Earlier classes had 2 to 3 (the 2012 class shows only 1). State as of 2026-09-28 (phase 2).

## Hosts / paths
| URL | span | note |
|---|---|---|
| www.med.nyu.edu/neurosurgery/education/current_residents.html | 2007 to 2012-05 | old static site. Its list was frozen at about 2007-09, so it is stale for all years. `trainees/list.html` lists academic alumni. |
| neurosurgery.med.nyu.edu/education-training/meet-our-residents | 2012-12 to 2015-02 | Drupal subdomain, flat name list. First archived 2014-01. |
| (www.)med.nyu.edu/neurosurgery/education-training/meet-our-residents | 2015-03 to 2020-10 | https without www from 2017. Wayback has nothing 2017-01 to 2019-07, so Common Crawl filled the gap. |
| med.nyu.edu/neurosurgery/research/residents-research | 2014-07 to 2019-12 | mirrors the roster |
| med.nyu.edu/departments-institutes/neurosurgery/education/residency/current-residents-alumni | 2021-09 to 2024-10 | no PGY labels |
| .../residency/neurosurgery-residents-alumni | 2025-01 to live | PGY-labelled, plus alumni by graduation year |

## Years
| AY | source | n | note |
|---|---|---|---|
| 2011-12 | **manual (reconstructed)** | 14 | No roster exists. Only people confirmed by the alumni list are included. |
| 2012-13 | **manual (reconstructed)** | 14 | No roster capture. Same approach as 2011-12. |
| 2013-14 | Wayback 2014-01-18 | 15 | flat list |
| 2014-15 | Wayback 2014-11-17 | 15 | |
| 2015-16 | Wayback 2015-10-11 | 15 | |
| 2016-17 | Wayback 2016-11-10 | 16 | |
| 2017-18 | Common Crawl CC-MAIN-2017-47, 2017-11-20 | 15 | Wayback has no capture this year |
| 2018-19 | Wayback 2019-07-23 | 17 | Content dates to 2018-19: Brunswick is still listed and there are no 2019 interns. |
| 2019-20 | Common Crawl CC-MAIN-2020-24, 2020-06-06 (residents-research) | 18 | **Phase 2: observed.** The sidebar list is the 2018-19 list plus the 2019 interns Orillac and Liu. Brunswick is omitted because he is stale (graduated 2019). |
| 2020-21 | Wayback 2020-10-25 | 18 | |
| 2021-22 | Wayback 2021-10-26 | 19 | |
| 2022-23 | Wayback 2022-11-29 | 20 | The 2023-10 capture is identical to this one, so it is stale. |
| 2023-24 | Wayback 2024-05-22 | 21 | first 2023-24 version |
| 2024-25 | Wayback 2025-01-19 | 20 | PGY labels |
| 2025-26 | Wayback 2025-10-08 | 20 | PGY labels |
| 2026-27 | **missing** | – | The live page is still identical to 2025-26 (re-fetched 2026-09-28). |

PGY labels appear only from 2025 on. For earlier years, PGY = AY minus the entry year, plus 1. The entry year comes from the alumni graduation year minus 7, or from the year first listed as intern. These values agree across every year and with the 2025 labels.

## Gap status after phase 2
| AY | status | significance | reason |
|---|---|---|---|
| 2011-12 | reconstructed | low | Entry classes 2006-2011 are at complement (2-3) and bracketed by 2013-14. Anyone hidden is likely a non-academic 2012 graduate, which is not attrition. |
| 2012-13 | reconstructed | **significant** | The 2012 class shows only Brunswick against the handbook's "2 residents per year". A second 2012 intern who left before Jan 2014 would be invisible. |
| 2013-14 to 2018-19 | observed | none | |
| 2019-20 | observed (partial list) | low | The CC 2020-06-06 list names both 2019 interns and everyone bracketed. |
| 2020-21 to 2025-26 | observed | none | |
| 2026-27 | missing | **significant** | Right-censored: the page has not been updated. |

## Phase 2 searches (2026-09-28)
- **Host audit** (gapaudit), 2011-06 to 2013-09, over the old www.med.nyu.edu/neurosurgery site, the neurosurgery.med.nyu.edu Drupal site, GME, education, surgery and nyulangone.org/news. Nothing new. The Drupal education-training page (captured 2012-12 and 2013-02) already linked to meet-our-residents, but that page has no capture before 2014-01-18. The 2013-08 Drupal resident-alumni page is academic-only and ends at the class of 2010.
- **Link audit** of the old residency/education pages (CC 2012): the only roster link goes to the stale current_residents.html.
- **Common Crawl 2020** (new), all crawls. It found the **2020-06-06 residents-research capture**, which now serves as the observed 2019-20 roster. CC-MAIN-2020-05 failed twice (cluster.idx). It is not needed.
- **PubMed affiliation mining.** For 2010-2014 there is no unidentified NYU neurosurgery resident, except Matthew M. Kang: NYU/Bellevue neurosurgery 2007-2012, then Regions Hospital, St Paul, from 2013. He is probably a non-academic graduate of 2011 or 2012. I did not add him because his year is unknown. The other unknown authors were students or scientists (C. R. Lee, a PhD at NYU then Rutgers; T. Ma, an NYU student who became a Penn resident). For 2019-2021, no third 2019 intern turned up. For 2026, 17 of the 18 residents at PGY 1-6 in 2025-26 have 2026 NYU neurosurgery papers; the exception is Huell.
- **Cross-program:** Phillips is confirmed on the UCLA roster (program 67) as PGY3 in 2017-18.

## Departures (left before PGY-7)
- **Harold Westley Phillips** (2015 entrant): **TRANSFERRED to UCLA**. He was NYU PGY2 in 2016-17 and UCLA PGY3 in 2017-18 (Wayback 2017-12-07), and graduated from UCLA in 2022. Recorded in training_history as transferred, end_year 2017.
- **Mohamed Khattab** (2016 entrant): **SWITCHED SPECIALTY to radiation oncology**. His PubMed affiliation is Vanderbilt Radiation Oncology for 2018-2022 (PMID 30622928), then Minneapolis Radiation Oncology. Recorded as switched_specialty, end_year 2017.

## Joiners (entered above PGY-1)
- **Roee Ber:** joined at PGY2 in 2018-19 from Tel Aviv Sourasky (not a US program) and graduated in 2024. His transfer-in row has start_year 2018. He took the vacancy Phillips and Khattab left, so the 2017 class had 4 members and the 2019 class had 2.

## Alumni page
It lists graduation years for academically employed alumni. I inserted 31 graduations for 2012-2025 into `training_history`.

Two people on it were **not** inserted: Marian M. Bercu (2017) and Aryan M. Ali (2020). Neither appears on any roster that covers their would-be years. Bercu's 2020 PubMed affiliation is NYU pediatric neurosurgery, so I treated both as fellows.

## Counts
- Residents entering 2011 or later: 41 (classes of 2011 through 2025).
- Adjudication: 31 completed, 20 in training, 1 transferred (Phillips, to UCLA), 1 switched specialty (Khattab).
- Program length: 7 years for every cohort (`terminal_pgy_by_entry_year` = 7).
- Phase 2 added 5 training_history rows: Phillips (transferred), Khattab (switched specialty), Ber (transfer in), and Orillac and Liu (completion taken from the PGY-terminal roster, 2026).
