# Program 99: University of Oklahoma Health Sciences Center Program (Oklahoma City, OK)

7-year program. It took 1 resident a year until 2016 and 2 a year from 2017 (except 2019 and 2021, which took 1). Roster file: `data/intake/rosters_program99.json`. Scratch files: `data/raw/extraction/p99/`.

## Hosts
| URL | From | To |
|---|---|---|
| www.oumedicine.com/neurosurgery/academic-information/current-residents | 2012-06 | 2016-05 |
| www.oumedicine.com/department-of-neurosurgery/academic-information/current-residents | 2016-08 | 2019-02 (frozen at the 2015-16 list from 2015-11 to 2017-08) |
| www.oumedicine.com/department-of-neurosurgery/neurosurgery/academic-information/residency/current-residents | 2019-05 | 2019-08 |
| www.oumedicine.com/department-of-neurosurgery/academic-information/residency/current-residents (+ neurosurgery-alumni) | 2019-10 | 2020-02 |
| medicine.ouhsc.edu/academic-departments/neurosurgery/residency-program/residents (+ /alumni) | 2020-08 | live 2026-09-27 |
| www.oumedicine.com/body.cfm?id=… (old ColdFusion site) | ≤2011 | 2012-03 (not mapped: it predates the study window) |

No neurosurgery roster pages turned up on ouhsc.edu/neurosurgery or ouhealth.com.

## Years
- **Observed (13):** 2011-12 (June 2012; the page has no PGY labels, so PGYs were derived), 2013-14 (**incomplete: no PGY-1**), 2015-16, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22 (May 2022 capture), 2022-23, 2023-24, 2024-25, 2025-26, 2026-27 (live).
- **Reconstructed (3):**
  - 2012-13: no capture exists.
  - 2014-15: no capture exists. Randhawa was not reconstructed.
  - 2016-17: the page was stale (it kept showing the 2015-16 list).
  - Each reconstructed person is either bracketed by the years before and after, or confirmed by the alumni graduation year.
- **Missing:** none. After phase 2 no gap is significant (see the Phase 2 section).

## Departures
- **Pal Randhawa** (entered 2009): last seen 2013-14 at PGY-5. He is absent from 2015-16 and from the alumni list, so he left some time in 2014-16.
- **Alison Westrup** (entered 2022): seen only in 2022-23 at PGY-1. Giancarlo Mignucci-Jimenez joined her class at PGY-2 in 2023-24.

## Joiners
- **Zoya Voronovich:** PGY-7 in 2020-21. She was first listed in January 2021 and was absent in October 2020 and 2019-20. The alumni page lists her as a 2021 graduate.
- **Giancarlo Mignucci-Jimenez:** PGY-2 in 2023-24. He was absent in 2022-23. Before joining he did a research fellowship at Barrow.
- **Graham Mulvaney:** PGY-6 in 2024-25. He was absent in 2023-24.

## Alumni
The alumni page is https://medicine.ouhsc.edu/academic-departments/neurosurgery/alumni and lists graduates only through 2024. I inserted 14 graduations from 2012 to 2024 into training_history.

## Adjudication
18 completed, 13 in training, 2 left (phase 2: 1 transferred [Randhawa], 1 did not complete [Westrup]). 27 residents entered in 2011 or later (by entry year, including the 3 joiners).

## Problems
- Two Common Crawl indexes could not be read and should be retried in phase 2:
  - CC-MAIN-2012 (the cluster.idx size request failed).
  - CC-MAIN-2017-09 for the department-of-neurosurgery prefix (a range request failed).
- The 2013-14 roster leaves out the intern.

## Phase 2 (2026-09-28)

### Year status
| Year | Status | Significance | Reason |
|---|---|---|---|
| 2011-12 | observed | low | June 2012 page has no PGY labels; PGYs derived; every 1/yr slot accounted for |
| 2012-13 | reconstructed | low | No capture anywhere (CC-MAIN-2012 now read: home page only). All 7 bracketed; intern Strickland PGY2 2013-14 (NPI 2012-06) |
| 2013-14 | observed | none | Intern Smitherman added as reconstructed PGY-1: NPI enumerated 2013-05-16 in Oklahoma City, PGY3 2015-16, alumni 2020 |
| 2014-15 | reconstructed | low | No capture (Wayback on all hosts, link audit, CC incl. retried 2014-42/49). 1/yr (residency page 2014-08); intern Tullos NPI 2014-06. Only open point: Randhawa's exit date |
| 2015-16 | observed | none | |
| 2016-17 | reconstructed | low | Stale page; CC 2016-40..2017-09 (2017-09 retried OK) home page only. All bracketed; Palejwala NPI 2016-05; 1 and 2 alternate (page 2016-11), 2017 class = 2, so 2016 = 1 |
| 2017-18 .. 2026-27 | observed | none | |

Terminal PGY is 7 for every entry cohort (2005-2026).

### Outcomes recorded in training_history (8 rows, th_id 2985-2992)
- **Pal Randhawa:** transferred (end_year 2014) to Colorado (80), PGY4 2015-16, graduated 2019. His exit falls between 2014-06 and 2015-06 because OU's 2014-15 roster is unobserved.
- **Alison Westrup:** left after PGY1 2022-23; departure_type unknown. Her last PubMed affiliation is OU (2023-06). Destination not found.
- **Zoya Voronovich:** joined at PGY7 in 2020-21 from UNM (97), which closed on 2020-06-30. Graduated 2021.
- **Giancarlo Mignucci-Jimenez:** joined at PGY2 in 2023-24 in Westrup's class. His OU profile gives a UPR MD and a 15-month research fellowship at Barrow; PubMed shows a Barrow affiliation in 2022-23. He appears on no program roster, so where his PGY1 credit came from is unknown.
- **Graham Mulvaney:** joined at PGY6 in 2024-25 from Carolinas (9), where he was PGY1-6 from 2018-19 to 2023-24. Graduated 2026 (PGY-terminal roster).
- **Graduations seen only on the PGY-terminal roster:** Shi and Villeneuve (2025), Stephens (2026). The alumni page, rechecked 2026-09-28, still stops at 2024.

### Searched
- p99 scratch: the cc hits files are all empty, so there were no unparsed captures.
- gapaudit for 2012-2017 on both oumedicine prefixes, ouhsc.edu/neurosurgery and the GME paths.
- Faculty-and-staff and residency pages from 2013-2017, and department home pages from 2012-2017. None carries resident names.
- Link audit.
- Common Crawl retries: CC-MAIN-2012, 2014-42, 2014-49, 2016-40, 2016-44, 2016-50, 2017-04 and 2017-09. All read OK; none holds a roster URL.
- PubMed affiliation mining for 2011-2018, plus author histories.
- NPPES enumeration dates.

### Remaining
All remaining items are low significance:
- Randhawa's exit date within 2014-15.
- Westrup's destination.
- Mignucci-Jimenez's PGY1 origin.
- Program 9 has no training_history row for Mulvaney's transfer out. That row belongs to program 9's owner.
