# Program 48: New York Presbyterian Hospital (Columbia Campus) Program (New York NY)

- 7-year program, 2-3 residents per year (3 per year since 2022). Cornell (program 49) not included.
- Hosts:
  - `www.columbianeurosurgery.org/education/residents/current-residents/`, 2010-01 to 2021-05 (`/residents/current-residents/` redirected here with a 301 in 2010; graduates at `/education/residents/recent-graduates/`)
  - `www.neurosurgery.columbia.edu/education/residency-program/current-residents` (plus `/graduates`), 2021-07 to the live page
  - Checks: CDX prefix scans of both hosts for 2010-2026 and the live sitemap.xml. No other roster pages were found.
- Parser: `data/raw/extraction/p48/p48.py`. The PGY comes from the heading descriptor, not from the "NS n" number. In 2011-12 the headings ran "NS 6 - Chief" to "NS 1 - Lab Year". From 2013 they changed to "Chief", "NS 6 - Senior" ... "NS 2 - Lab Year". Both map to PGY 7..2, and class continuity confirms it.

| AY | Capture | n | Note |
|---|---|---|---|
| 2011-12 | WB 20120111 | 16 | Aug 2011 capture still showed 2010-11 |
| 2012-13 | WB 20121028 | 16 | |
| 2013-14 | WB 20131009 | 15 | |
| 2014-15 | WB 20141216 | 15 | Page was stale Jul-Nov 2014. Gupta and De Rojas were removed by 2015-04 |
| 2015-16 | WB 20151021 | 14 | |
| 2016-17 | WB 20161221 | 13 | |
| 2017-18 | WB 20171223 | 12 | Only capture with 2017-18 content |
| 2018-19 | WB 20181221 | 14 | |
| 2019-20 | WB 20191223 | 14 | Sep 2019 capture was stale |
| 2020-21 | WB 20201029 | 14 | Phase 2: Boyett added as PGY1 (parser miss). In Mar 2021, Sisti and Joiner were moved up a PGY |
| 2021-22 | WB 20211028 | 14 | New host |
| 2022-23 | WB 20221014 | 14 | |
| 2023-24 | WB 20231208 | 15 | The Oct 2023 capture was half-edited |
| 2024-25 | WB 20241014 | 16 | |
| 2025-26 | WB 20251009 | 16 | CreveCoeur listed as "Enfolded Fellow" and excluded |
| 2026-27 | Live 2026-09-27 | 18 | PGYs advanced and 3 new interns |

- **Observed:** every year from 2011-12 to 2026-27.
- **Missing:** none. **Reconstructed:** none. Common Crawl was not needed.
- **Departures (4):**
  - Gaurav Gupta: last seen 2014-15 at PGY4. He left mid-year and is not on the graduates list.
  - Joaquin De Rojas: last seen 2014-15 at PGY1. He left mid-year; NPI data suggests he switched specialty.
  - Paul McCormick: last seen 2016-17 at PGY1.
  - Anna Filley: last seen 2021-22 at PGY4. She is not on the graduates list.
- **Joiners:** none. (Phase 1 listed Deborah Boyett as a PGY2 joiner in 2021-22; phase 2 found her on the Oct 2020 roster as a PGY1 intern.)
- **Accelerated to 6 years:** Higgins (graduated 2021), Sisti (2023), Joiner (2024) and CreveCoeur (2025). Because a PGY was skipped, the computed entry year for each of them differs by one across rosters.
- **Alumni page:** https://www.neurosurgery.columbia.edu/education/residency-program/graduates
  - It lists graduates from 1997 to 2026. The archived recent-graduates page (2020) matches it.
  - Its only mismatch: it lists CreveCoeur under 2026, but department news from 2025-06-10 names him a 2025 graduating joint chief. I recorded end_year 2025.
  - 30 rows for graduation years 2012-2026 were inserted into training_history.
- **Adjudication (after phase 2):** 30 COMPLETED, 18 IN TRAINING, 2 LEFT (did not complete, outcome unknown), 2 LEFT (switched specialty).
- **Residents entering 2011 or later:** 38.
- **Significant gaps:** none. Two things to know:
  - The 2014-15 roster is from December, and two residents left later that year.
  - Residents who left between captures are counted from the next capture.

## Phase 2 (2026-09-28)

**Completeness check.** I re-read the raw text of all 16 captures (`data/raw/extraction/p48/phase2/text_*.txt`). I checked every heading ('Chief'/'Chiefs', 'Enfolded Fellow') and looked for comma-less or inline names.
- The only parser miss was in 2020-21: "Deborah Boyett MD, MS" under PGY 1 - Intern Year. She is now added, so that year has 14 names.
- Boyett is therefore not a joiner. She entered in 2020 with a Columbia MD (2020) and is PGY7 in 2026-27.
- Every entry cohort from 2005 to 2026 has 2 or 3 residents, and every short year is explained by a recorded departure.
- The 2025 intern class of 2 is confirmed by the department news post "Welcome to Our 2025 Columbia Neurosurgery Matches" (Dadario, Savage).

**Departures.** The four rows below were written to training_history as th_id 3392-3395.
- **Gaurav Gupta** (PGY4, left spring 2015): outcome UNKNOWN.
  - He is not on any other roster, and his PubMed papers show a Columbia affiliation in 2013-14 only.
  - The Rutgers-RWJ neurosurgeon of the same name is a different, older person (a Cleveland Clinic resident in 2003).
- **Joaquin De Rojas** (PGY1, left spring 2015): SWITCHED SPECIALTY to ophthalmology.
  - PubMed shows Harkness Eye Institute at Columbia 2016-19, the Wilmer cornea division in 2021, then Center for Sight, Sarasota.
- **Paul McCormick Jr.** (PGY1 2016-17): left after PGY1. Outcome UNKNOWN.
  - He is identified from the Match Day 2016 and Nov 2016 welcome posts.
  - PubMed and OpenAlex cannot separate him from his father, Paul C. McCormick.
- **Anna Filley** (PGY4 2021-22): SWITCHED SPECIALTY to orthopaedic surgery.
  - Her ORCID 0009-0005-6964-9152 links her IU and Columbia neurosurgery papers to UCSF Orthopaedic Surgery spine papers (2023-26) and Denver Health Orthopedics (2026).
  - Whether her UCSF role was resident or research fellow is not stated.
- **Research years and enfolded fellowships:** none of the four departures is one. Columbia lists its lab years (PGY2, PGY5) on the roster, and none of the four ever reappears. The only enfolded fellow is CreveCoeur, after he graduated in 2025.

**Terminal PGY.** It is 7 for every entry cohort from 2005 to 2026. Higgins, Sisti, Joiner and CreveCoeur finished in 6 years by skipping a PGY label. They are not departures and do not mark a change in program length.

**crossmatch.json:** it has no entries for program 48.

**Significance:** none for every year. 2014-15 is rated low because two residents left mid-year, and both are resolved. There are no remaining significant gaps.
