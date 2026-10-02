# Program 123: Yale-New Haven Medical Center Program (New Haven, CT)

The program runs 7 years and takes 2 residents per year (3 in 2019 and 2020). The recorded website (`www.medicine.yale.edu/neurosurgery/education`) is the department's education page. The roster has moved between several pages on the same host.

Phase 2 (2026-09-28) closed both significant gaps. No year is missing now.

## Hosts and paths
| Path | Dates |
|---|---|
| www.med.yale.edu/neurosurgery/ (old host) | Only 302s are archived (2010-07). No roster. |
| medicine.yale.edu/neurosurgery/education/index.aspx and people/index.aspx | 2010-10 to 2014. No resident list. |
| education/114813_HB 2012 v master.doc (Resident Handbook 2012) | Saved 2012-01-12, archived 2013-04. Has a "Current Residents" table. |
| education/residents.aspx | 2012-10 (Common Crawl) to 2017. Stale from 2015-09 in Wayback. |
| education/graduates.aspx (past graduates) | 2013-2018 |
| education/copy_of_index.aspx (roster embedded) | 2015-12 to 2016-01 |
| (www.)medicine.yale.edu/neurosurgery/education/residencyprogram.aspx (roster embedded) | 2016-04 to 2019-06. Wayback stops at 2018-02; Common Crawl covers 2018-05 to 2019-06. |
| education/currentresidents.aspx, then education/currentresidents/ | 2019-07 to 2025-07 |
| education/residencyprogram/currentresidents/ | 2026-02 to live |
| education/residencyprogram/alumni/ | 2022-11 to live. Lists graduates from 2008 to 2023 only. |
| Resident Handbook PDFs (Sept 2014, Oct 2016) | Their rosters match the 2014-15 and 2016-17 web rosters. |

neurosurgery.yale.edu, info.med.yale.edu/neurosurg and yalemedicine.org/departments/neurosurgery have no roster captures.
| website-api-data/feed-organization-member-listing/?organizationId=108855 | Live department directory feed (people-by-department/neurosurgery); gives the 2026-27 roster |
| medicine.yale.edu/news-article/... and /neurosurgery/news-article/<id>/ | Match Day 2020/2021, Change of Chiefs 2022/2026, 2026 NENS news |

## Years
| Academic year | Status | Significance | Source |
|---|---|---|---|
| 2011-12 | observed | none | Wayback 2013-04-03: the 2012 Resident Handbook .doc (content from Jan 2012), 14 residents |
| 2012-13 | observed | none | Common Crawl CC-MAIN-2013-20: residents.aspx headed "October 2012" |
| 2013-14 | observed | none | Wayback 2013-12-03, residents.aspx "October 2013" |
| 2014-15 | observed | none | Wayback 2014-10-10, residents.aspx "October 2014" |
| 2015-16 | observed | none | Wayback 2015-12-17, copy_of_index.aspx |
| 2016-17 | observed | none | Wayback 2016-09-08, residencyprogram.aspx |
| 2017-18 | observed | none | Wayback 2017-10-17, residencyprogram.aspx |
| 2018-19 | observed | none | Common Crawl CC-MAIN-2018-43, residencyprogram.aspx |
| 2019-20 | observed | none | Wayback 2019-11-13, currentresidents/ (Common Crawl 2020-01 capture is identical) |
| **2020-21** | reconstructed | **low** | No roster capture. All 14 people are evidenced (see below) |
| 2021-22 | observed | none | Wayback 2021-10-17 |
| 2022-23 | observed | none | Wayback 2022-11-14 |
| 2023-24 | observed | none | Wayback 2023-07-25 (already 2023-24 content) |
| 2024-25 | observed | none | Wayback 2024-11-14 |
| 2025-26 | observed | none | Wayback 2026-02-25, residencyprogram/currentresidents/ |
| **2026-27** | observed | **low** | Live department directory feed, 2026-09-28. PGY is inferred |

## 2020-21 (reconstructed, low significance)
- No roster capture exists. Phase 2 re-scanned all 18 Common Crawl crawls from 2020 to 2021 over the whole `medicine.yale.edu/neurosurgery` prefix. That includes the previously failed CC-MAIN-2020-05, and 2020-10, 2020-40 and 2021-21 were retried. It also fetched every archived news, awards and education page on the host in the window.
- **The 2020 class is closed.** The 2020 Match Day news (neurosurgery/news-article/23436, 2020-03-26) names exactly three new residents: Andrew Koo, Kelsey Anne Templeton and Brianna Carusillo Theriault. All three have archived Yale profiles from Aug 2020 to Jan 2021 that say "Hospital Resident" or "a resident in neurological surgery at Yale-New Haven". All three are PGY-2 in 2021-22. I added them as PGY-1 rows (reconstructed, with the evidence in `context`).
- Program news from Feb 2021 calls Antonios "a second-year neurosurgical resident". News from Dec 2020 calls Lamsam a Yale neurosurgery resident.
- Only open point: **Cikla** left either at the end of 2019-20 or during 2020-21. This changes his end year, not the head count.

## 2026-27 (observed from the live directory, low significance)
- The residency page `currentresidents/` is still stale. The department directory feed behind `myysm/people/people-by-department/neurosurgery/` (187 members) lists 15 people with the title "Hospital Resident":
  - The 13 continuing residents.
  - Two 2026 interns: **Oleksandr Strelko** (MD Loyola 2026) and **Allison Toth** (profile created 2026-07-01, Dept Neurosurgery).
- Antonios and Lamsam are gone. Department news from 2026-06-29 confirms they graduated in June 2026, and says Theriault is a "rising PGY7" and Alvarez Reyes a "rising PGY4". Craft is absent.
- The directory prints no PGY, so PGY is set by entry year.

## Departures (outcomes recorded in training_history)
- **Komli-Kofi Atsina** (2011 entrant). Left after 2013-14 as PGY-3; outcome unknown. **He is not the Jefferson (58) Atsina.** Kofi-Buaku Atsina was Jefferson PGY-1 to PGY-3 in 2012-15, at the same time Komli-Kofi was at Yale, and they have different NPIs. There was no transfer from Yale to Jefferson.
- **Gabriel Sneh** (2018 entrant). Left after 2018-19 as PGY-1. He probably switched to neurology: a 2024 paper lists his affiliation as the Dept of Neurology, Johns Hopkins (PMID 37921930).
- **Ulas Cikla** (2019). A foreign-trained attending neurosurgeon who held a supernumerary third PGY-1 spot (his bio calls him an "Associate Scientist"). Recorded end year: 2020, completed=no, departure type unknown.
  - His profile kept the "Hospital Resident" title until Feb 2021 but listed no Neurosurgery department.
  - Later: UW-Madison Cerebrovascular Fellow in 2023-24. His NPI is Neurological Surgery (Florida), and his 2025-26 papers give a UF-Jacksonville affiliation.
- **Samuel Craft** (2024). Left after 2024-25 as PGY-1. He probably switched to internal medicine. The July-2025 roster shows him as "Postdoctoral Associate". His Yale profile lists the Neurosurgery department in Mar 2025 and Internal Medicine now (live), with the title still "Hospital Resident".

## Joiners
- **Brett Gu** joined at PGY-2 in 2025-26 and filled Craft's slot. He has a Yale MD (2024). In Aug 2024 his Yale profile said "Hospital Resident" with the Surgery department, so he probably did a Yale preliminary surgery PGY-1 year in 2024-25.

## Cross-program checks
- **Robert C. Sterner** (Inova, 29) was **not** a Yale neurosurgery resident or research fellow. His Yale affiliation (Dept of Cell Biology) dates from his UW MSTP-era research:
  - PMID 41299044 (published 2025) was received in June 2022.
  - PMID 34882648 (2022) already carries the same affiliation.
  - He is on no Yale roster from 2023-24 to 2026-27 and not in the live department directory, and his Yale profile returns 404.
- The Atsina chain (Yale -> Jefferson) in PHASE2_NOTES is wrong (see above).

## Counts
- 35 residents entered in 2011 or later.
- The adjudicator's outcomes: 28 completed, 15 in training, 2 left without completing (Atsina, Cikla), 2 switched specialty (Sneh, Craft).
- training_history holds 23 alumni-page graduations from phase 1. Phase 2 added 10 rows:
  - 4 departures (Atsina, Sneh, Cikla, Craft).
  - 1 joiner (Gu).
  - 5 graduations: Robert and Sujijantarat (2024) and Elsamadicy (2025) from PGY-terminal rosters; Antonios and Lamsam (2026) from the 2026-06-29 news.

## Problems
- The alumni page stops at the class of 2023.
- The 2026-27 PGY levels are inferred.
- CC-MAIN-2015-18 and 2018-09 were not retried, because those years are observed.
