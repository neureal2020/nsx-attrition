# Program 85: University of Iowa Health Care Medical Center Program (Iowa City, IA)

7-year program, complement 2 per year (3 in the 2014 and 2026 classes). Rosters: `data/intake/rosters_program85.json`. Scratch: `data/raw/extraction/p85/`.

## Hosts
| Host / path | From | To |
|---|---|---|
| www.uihealthcare.com/depts/med/neurosurgery/residents/current.html (old UIHC dept site; frozen at the Jan-2011 = 2010-11 roster) | 2006-05 | 2012-08 |
| www.uihealthcare.org/neurosurgeryresidency/ -> /GME/ResProgInsidePages.aspx?id=236125&taxid=226497 ("Current Residents") | 2012-11 | 2016-07 |
| www.medicine.uiowa.edu/neurosurgery/residency/, medicine.uiowa.edu/neurosurgery/education/residency-training (links only, no roster) | 2013-05 | 2025-07 |
| gme.medicine.uiowa.edu/neurological-surgery-residency/our-people/current-residents (+ alumni-residents from 2022); Wayback only from 2020-10, earlier via Common Crawl | 2016-09 | 2025-04 |
| neurosurgery.medicine.uiowa.edu/education/neurological-surgery-residency/our-people/residents and /alumni-residents (live; old hosts 301 here) | 2025-08 | live |

Labels: through 2018-19 "Fellow Associates" = R7 and "Chief Residents" = R6. From 2019-20 the pages use PGY-n headings.

## Years
- **Observed (15):** 2012-13, 2013-14 (CC, phase 2), 2014-15 (CC, phase 2), 2015-16, 2016-17 (CC), 2017-18 (CC), 2018-19 (CC), 2019-20 (CC), 2020-21 through 2025-26 (Wayback), and 2026-27 (live). A 2010-11 anchor (Wayback Jul 2011) is also loaded.
- **Reconstructed (1), significance low:**
  - **2011-12:** no roster exists in any archive. The old uihealthcare.com current.html stayed frozen at the Jan-2011 list, and the UIHC GME neurosurgery pages were created later in 2012 (first capture Nov 2012; CC-MAIN-2012 has no uihealthcare.org/GME records). The 10 bracketed residents (R2-R6) are reconstructed. Low because every 2010-11 R1-R5 reappears in 2012-13 at the expected PGY, the 2011 class (Abode-Iyamah, Smietana) fills the complement of 2, and the R7 fellow associates of that year are 2011 alumni.
- **Missing:** none.

## Phase 2 (2026-09-28)
- **2013-14 and 2014-15 closed.** Phase 1 searched `ResProgInsidePages.aspx?id=236125`. From mid-2013 the same roster was served at `www.uihealthcare.org/GME/InsidePages.aspx?id=236125&taxid=226497`. Common Crawl has it in every crawl from CC-MAIN-2013-48 to 2015-35 (about 40 records), and Wayback has it on 2015-09-24. Loaded CC 2013-12-07 (2013-14) and CC 2014-12-18 (2014-15). Both are complete, with 14 residents each.
- **Smietana:** listed R3 through Apr 2014, absent from Jul 2014 on. She left at the end of 2013-14, after PGY-3. Destination unknown: NPPES shows a New York psychiatry taxonomy, but NPPES alone is not used as evidence.
- **Liesl Close is a joiner.** She is absent from every capture from 2014-07-25 to 2014-11-01 and is listed under R1 from 2014-11-23, so she joined mid-year 2014-15. This explains the 3-person 2014 class and her finishing one year ahead of it (PGY-7 in 2019-20, graduated 2020). Prior training is unconfirmed: NPPES shows a 2012 NPI with an Arizona surgery resident license.
- **Haselden:** 2026 papers (received Nov 2025) list him in the Department of Neurology, University of Iowa Health Care. He is not on the Iowa neurology residency directory (classes 2027-2030), so his role is unknown and he is not classified as a switch.
- **PubMed affiliation mining** ("neurosurgery" AND "University of Iowa", 2011-2016) found no unlisted residents. `crossmatch.json` has no entries for program 85.
- **training_history rows inserted:** 3100 Smietana (no, unknown, 2011-2014), 3101 Haselden (no, unknown, 2023-2025), 3102 Close (joined 2014 at R1, completed 2020), 3103/3104 Teferi and Woodiwiss (PGY-terminal roster, completed 2026).
- **Terminal PGY:** 6 for entrants through 2012 (R7 was a post-graduation "Fellow Associate" year), 7 from the 2013 entrants. This is recorded in the JSON as `terminal_pgy_by_entry_year`.
- **Grossbach:** the live alumni page gives 2017 and the archived 2022 page gives 2016. His classmate Abel is listed at 2016, and both were Fellow Associates (R7) in 2016-17. So 2016 is the end of the chief year under the old convention and 2017 is the end of R7. His completion is not in doubt.
- Scratch files: `data/raw/extraction/p85/phase2/` (gapaudit, CC pass `cc_2013_2016/`, `pubmed_aff_2011_2016.txt`, backups of the phase-1 roster and gap file).

## Consistency
Every resident has a single entry year. Class sizes are 2 each year from 2006 to 2025, 3 in 2014 (Close joined mid-year) and 3 in 2026. Close was printed under "Chief Residents" in the 2016-17 capture, which is a page error, so she is stored without a PGY for that year.

## Departures (left before the terminal PGY)
- **Janel Smietana:** 2011 entrant, last seen 2013-14 as R3 (Apr 2014), absent from Jul 2014 on. She left at the end of 2013-14. Destination unknown.
- **William Haselden:** 2023 entrant, last seen 2024-25 as PGY-2, absent Sep 2025. He left in summer 2025. Destination unknown (Iowa neurology affiliation on 2026 papers).

## Joiners above PGY-1 / mid-year
- **Liesl Close:** joined mid-year 2014-15 at R1 (Nov 2014) and graduated 2020, accelerated by one year.

## Alumni page
Live page: https://neurosurgery.medicine.uiowa.edu/education/neurological-surgery-residency/our-people/alumni-residents. It lists graduates from 1975 to 2025. 26 graduates with graduation years 2012-2025 were inserted into `training_history`. There are no 2019 graduates: until the 2012 entrants, graduation came at the end of R6 (chief), and from the 2013 entrants it comes at the end of PGY-7. For Grossbach, the live page gives 2017 and the 2022 archived page gives 2016; both are noted. The 2026 graduates (Teferi, Woodiwiss) are not listed yet.

## Adjudication
30 COMPLETED, 14 IN TRAINING, 3 LEFT (outcome unknown), 2 LEFT (did not complete). Three of the LEFT (Dahdaleh, Vogel, Lindley) are 2011 alumni, recorded before the 2012 cut-off, so they are not attrition. The real departures are Smietana and Haselden. 34 residents entered in 2011 or later.

## Problems
Phase-1 Common Crawl failures (2015-35, 2017-30 uihealthcare.com; 2018-13, 2019-09 gme; 2020-24 uihealthcare.org) were retried in phase 2 and all succeeded. They held no new roster (only a Mar-2018 gme current-residents record inside observed 2017-18). The phase-2 CC passes (2012, 2013-2016) had no failures.
