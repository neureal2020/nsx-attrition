# Program 58: Sidney Kimmel Medical College at Thomas Jefferson University / TJUH (Philadelphia, PA)

7-year program. Normal complement is 3 a year; the 2019, 2022, 2023 and 2025 classes had 4. JSON twin: `program58.json`.

## Hosts
| Host / path | From | To |
|---|---|---|
| `jefferson.edu/neurosurgery/staff/index.cfm` (old ColdFusion site; also `/neurosurgery/residency/documents/Blockrotationschedule2011.12.doc`) | 2008-07 | 2012-05. Wayback captured the roster only in 2010-05/06; the 2012 roster comes from Common Crawl |
| `jefferson.edu/jmc/departments/neurosurgery/Education/staff.html` | 2013-02 | 2014-03. Wayback never captured the roster; it is in Common Crawl 2013-20, 2013-48 and 2014-10. Redirects to `/university/jmc/...` by 2014-08 |
| `jefferson.edu/university/jmc/departments/neurosurgery/education/staff.html` (+ `education/fellow-alumni.html`) | 2014-10 | 2021-01 |
| `jefferson.edu/academics/colleges-schools-institutes/skmc/departments/neurosurgery/education/residency/residents.html` (+ `residency/alumni.html`) | 2021-01 | live |
| jeffersonhospital.org/neurosurgery, hospitals.jefferson.edu, jeffersonhealth.org | clinical sites | no roster |

## Years
- **Observed (15):** 2011-12 through 2025-26.
  - 2011-12, 2012-13 and 2013-14 come from Common Crawl (`source_type: other`).
  - 2014-15 through 2025-26 come from Wayback.
- **Reconstructed:** none.
- **Missing:** 2026-27. The live page (2026-09-27) is not advanced and matches the 2025-26 roster: PGY-7 is still the Andrews class, there are no 2026 interns, and the alumni page has no 2026 class.

### Capture notes
- **2011-12:** CC-MAIN-2012, 2012-02-09. The names match the 2011-12 Block Rotation Schedule .doc.
- **2012-13:** CC-MAIN-2013-20, 2013-05-18. The page heads the Atsina/Pendleton/Stricsek group "PGY II" twice, which is a typo for PGY I, so they are stored as PGY 1.
- **2013-14:** CC-MAIN-2013-48, 2013-12-18. CC-MAIN-2014-10 has the same content.
- **2014-15 is incomplete (significant).** PGY VII lists only Krieger, Williams and Salas. Sonia Teufack (Geschwindt) and Chengyuan Wu are missing, although both were PGY VI in 2013-14 and the alumni page lists them as 2015 graduates.
- **The site updated late in three years.** In each case I used the first capture whose content matched the year:
  - 2015-16: 2016-05 (the 2015-10 capture was stale)
  - 2018-19: 2019-02 (the page was stale until 2019-01)
  - 2024-25: 2025-05 (the Aug-2024 captures were stale)
- **2022-23:** used 2022-11. The Sep-Oct captures had no PGY-1 section.

## Departures (left before the terminal PGY)
| Name | Last AY | Last PGY | Note |
|---|---|---|---|
| Kofi-Buaku Atsina | 2014-15 | 3 | Entered 2012. Absent from 2015-16 and from the alumni page. NPI shows a specialty switch |
| Erika Dillard | 2017-18 | 4 | Entered 2014. Absent from 2018-19 (Feb 2019) and from the alumni page. NPI shows a specialty switch |
| Edward M. Marchan | 2009-10 | 4 | Pre-window: left between 2010-06 and 2011-07. Not loaded |

**Joiners:** none.

## Alumni
The live alumni page lists graduates 2005-2025. I inserted 35 rows for graduation years 2012-2025 into `training_history`. Two alumni-page issues:
- **Madineni and Philipp are missing from the alumni page.** Ravichandra Madineni was PGY-7 in 2016-17 and Lucas Philipp was PGY-7 in 2024-25, but neither appears. Their completion is unconfirmed.
- **Two people changed their names.** Shannon Hann became Shannon Clark, and Sonia Teufack appears as Sonia Geschwindt.

## Counts
- **Residents entering 2011 or later:** 49.
- **Adjudication:** 37 completed, 25 in training, 2 left (switched specialty).

## Other issues
- **Salas's entry year is inconsistent.** Sussan Salas was PGY VI in both 2012-13 and 2013-14, then PGY VII in 2014-15. This extra year (probably research) means her entry year computed from PGY comes out as 2007 in some years and 2008 in others.

## Phase 2 (2026-09-28)
| Year | Status | Significance | Reason |
|---|---|---|---|
| 2011-12 .. 2013-14 | observed (Common Crawl) | none | complete rosters |
| 2014-15 | observed + 2 reconstructed | none | Teufack/Geschwindt and Wu spent PGY7 as enfolded Jefferson fellows (Skull Base, Functional): the archived alumni page (Wayback 2017-09-01) lists them as both 2015 residency graduates and 2015 fellows, so they were on the fellow list, not the resident list. Added as reconstructed PGY7 rows. |
| 2015-16 .. 2025-26 | observed | none | complete rosters |
| 2026-27 | missing | low | live page re-fetched 2026-09-28 is still the 2025-26 roster; only the 2025-26 -> 2026-27 transition is unseen |

**Outcomes recorded in `training_history` (4 rows):**
- **Madineni:** completed 2017. The archived alumni page (2017-2021) lists "Ravi Madineni, MD, Clinical Instructor, TJU". The live page later dropped him.
- **Philipp:** completed 2025. He was PGY-7 in 2024-25 and is absent from 2025-26. Supporting evidence: NPPES shows him as a neurosurgeon in Independence, MO.
- **Atsina:** left after 2014-15 (PGY3) and switched to radiology. PubMed affiliations show TJU Radiology 2017-20 (PMIDs 27657929, 31093804), then Penn neuroradiology / NIR 2020-22. He is not Yale's Komli-Kofi Atsina.
- **Dillard:** left after 2017-18 (PGY4); destination unknown. There are no publications after she left. The NPPES name match is not evidence.

**Salas:** repeated PGY VI, so she trained 8 years (entered 2007, graduated 2015). She is not a departure. All cohorts are 7 years (`terminal_pgy_by_entry_year`).

**Adjudication after reload:** 37 completed, 25 in training, 1 switched specialty, 1 did not complete.
