# Program 52: Oregon Health & Science University (OHSU Health) Program (Portland, OR)

7-year program. Complement 3/yr now; 2/yr for most classes before 2016. Every academic year from 2011-12 to 2026-27 is observed from the program's own roster pages. Nothing is reconstructed and nothing is missing.

## Hosts
- http://www.ohsu.edu/xd/education/schools/school-of-medicine/departments/clinical-departments/neurosurgery/academics-residency/residency/current-residents.cfm (xd CMS; single roster page, 'Nth Year Residents' headings; alumni at academics-residency/alumni.cfm) (2009-04 to 2019-05)
- https://www.ohsu.edu/school-of-medicine/neurosurgery/residents (Drupal; hub linking seven per-PGY pages: 1st-year-residents-intern-neurological-surgery ... 7th-year-residents-chief; 5th/6th renamed -senior-research / -research-clinical 2021-02) (2019-05 to 2021-05)
- https://www.ohsu.edu/school-of-medicine/neurosurgery/current-residents (single page, 'PGY-n (...)' accordions; links yearly roster PDF under /sites/default/files/) (2021-06 to live 2026-09-27)
- https://www.ohsu.edu/school-of-medicine/neurosurgery/neurological-surgery-residency-program-alumni (alumni by year 2000-2025; earlier alumni-2007-2011 / alumni-2012-2016 pages 2019-2021) (2019-08 to live 2026-09-27)
- Note: the xd path is .../clinical-departments/neurosurgery/, not .../neurological-surgery (that prefix has no captures).

## Year-by-year sources
- **2011-2012**: No Wayback capture of current-residents.cfm between 2010-06-07 and 2012-12-23. Common Crawl CC-MAIN-2012 capture 2012-02-12 used (source_type other). Complete, 14 names PGY1-7.
- **2012-2013**: Wayback 2012-12-23. Complete (15).
- **2013-2014**: No Wayback capture 2013-01..2015-01 (CDX all statuses). Common Crawl CC-MAIN-2013-48 2013-12-09 used; identical list in CC 2014-03..2014-09. Complete (15).
- **2014-2015**: Wayback 2015-01-30 (also in CC 2014-10..12). Complete (16).
- **2015-2016**: Wayback 2015-11-16. Complete (16).
- **2016-2017**: Wayback 2016-10-13. Complete (17).
- **2017-2018**: Wayback 2017-12-06. Complete (17). Yimo Lin (PGY3) dropped between 2018-03-14 and 2018-05-20 captures.
- **2018-2019**: Wayback 2018-11-22, last xd-era roster. Mantovani listed under 1st Year (joined 2018, prior residency in Italy).
- **2019-2020**: Roster split across seven per-PGY pages; all seven captured 2019-11-23 and loaded as seven entries. Complete (18).
- **2020-2021**: Per-PGY pages captured 2020-11-24 (seven entries). Complete (20).
- **2021-2022**: Wayback /current-residents 2021-09-30. Complete (21).
- **2022-2023**: Wayback 2022-11-17. Complete (22).
- **2023-2024**: Wayback 2023-10-16. Complete (21).
- **2024-2025**: Wayback 2024-10-08 (21). Stedelin removed by 2024-11-02; Greisman added by 2025-03-20 (partial 'other' entry with his row only).
- **2025-2026**: Wayback 2025-09-09; matches live PDF 'Neurosurgery Resident and Fellow Roster 2025-26'. Complete (21).
- **2026-2027**: Live page fetched 2026-09-28: advanced (new PGY1 Khalifeh/Lim/Tang-Tan). Complete (21). Page still links the 2025-26 PDF.

## Per-year status (phase 2)
Every year 2011-12 to 2026-27: **observed, significance none**. Every capture of every roster host was re-read with an independent name detector (xd page 42 captures 2009-2019; 17 Common Crawl captures 2012-2014; ~90 captures of the seven per-PGY pages 2019-2021; 68 captures of /current-residents 2021-2026). Within each year all captures list the same people, apart from the departures and joiners below. Class sizes follow the cohorts exactly: 2 per year for entrants 2005-2011, 2013 and 2015; 3 for 2012, 2014 and 2016 onward; plus Mantovani in 2018. Details per year are in the JSON `years` block.

## Program length
7 years for every cohort (`terminal_pgy_by_entry_year` = 7 for 2005-2026).

## Departures (left before PGY-7), all recorded in training_history as completed=no, departure_type=unknown
- **Paul McMahon** (entered 2014): PGY3 in 2016-17. Listed through the 2017-06-13 capture and absent from 2017-12-06 on. Not on the alumni list. PubMed and OpenAlex show no neurosurgery or medical affiliation after 2015, and he is on no other program's roster. The phase-1 NPI "switched specialty" hint is discarded because NPI is not evidence. Destination unknown.
- **Yimo Lin** (entered 2015): PGY3 in 2017-18. Listed through 2018-03-15 and gone by 2018-05-20. Not on the alumni list. Her only publications are OHSU neurosurgery papers (the last in 2021), with no later training affiliation, and she is on no other roster. Destination unknown. Her class slot was later filled by Moon.
- **Brittany Stedelin** (entered 2023): PGY2 in 2024-25. Listed on 2024-10-08 and gone by 2024-11-02. Papers from 2025-11 and 2026-08 still give an OHSU Department of Neurological Surgery affiliation, but she is not listed as a resident. She is on no other roster. Destination unknown. Her slot was filled by Greisman.

## Joiners
- **Alessandra Mantovani** (training_history start 2018, end 2023): foreign-trained, with advanced standing. She completed a neurosurgery residency in Modena, Italy, and fellowships at UW, UF, Stanford and BCH, and "joined the program in 2018 from Boston Children's". Listed as a 4th intern in 2018-19, then PGY5 2019-20, PGY6 in both 2020-21 and 2021-22, and PGY7 2022-23. Alumni 2023. She was not a transfer from a US program.
- **Seong-Jin Moon** (training_history start 2020 at PGY6, end 2022): transferred in from Wayne State/DMC (program 125) after it lost accreditation. The WSU rosters list him from PGY1 2015-16 to Year 4 2018-19, and PubMed gives him a WSU neurosurgery affiliation in 2018-19. He is absent from OHSU pages through 2020-02-25 and on the 6th-year page from 2020-08-25. Alumni 2022. The WSU-side row (3274) already existed; the OHSU-side row was added in phase 2.
- **Jacob Greisman** (training_history start 2024 at PGY2, in training): joined mid-year into Stedelin's vacancy and was first listed 2025-03-20. His bio gives his intern year as "Tulane University Neurosurgery/General Surgery", but he is not on Tulane's neurosurgery PGY1 roster, so this was likely a preliminary year. PubMed gives a Buffalo neurosurgery research affiliation in 2024-25. PGY4 in 2026-27.

## Graduations
There are 33 alumni rows for 2012-2025 from phase 1. Phase 2 added three "PGY-terminal roster" rows for the 2026 graduates (Lopez Ramos, Shahin, Yamamoto), who were PGY7 in 2025-26, are absent from the live 2026-27 roster, and are not yet on the alumni page.

## Crossmatch
`data/intake/crossmatch.json` has no pair involving program 52. The only cross-program transfer, Moon (125 -> 52), is recorded on both sides.

## Counts
- Adjudication: 36 COMPLETED, 21 IN TRAINING, 3 LEFT with destination unknown (McMahon, Lin, Stedelin).
- Phase-2 training_history rows: 9 (3 departures, 3 joiners, 3 graduations for 2026).

## Significant gaps
None.

## Remaining
The destinations of McMahon, Lin and Stedelin are unknown.

## Problems
None blocking. 2011-12 and 2013-14 rest on Common Crawl captures, which agree with the neighbouring years.
