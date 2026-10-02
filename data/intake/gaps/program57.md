# Program 57: Rutgers Health/New Jersey Medical School (Newark NJ), formerly UMDNJ-NJMS

7-year program. Native classes 1 to 4 per year (2 in most years, 3 to 4 since 2020). No new-program issue.

## Hosts
| URL | from | to |
|---|---|---|
| njms.umdnj.edu/departments/neurosurgery/CurrentResident.cfm, FormerResidents.cfm | 2008-10 | 2009-04 (before the study window) |
| njms.umdnj.edu/departments/neurosurgery/resident.cfm | 2010-05 | 2013-06 (still showing the 2009-10 list) |
| njms.rutgers.edu/departments/neurosurgery/resident.cfm | 2014-01 | 2021-01 (HTML table until 2018, then a PNG image) |
| njms.rutgers.edu/departments/neurosurgery/resident.php + images/*Housestaff*.png | 2021-09 | live 2026-09-27 |
| sites.rutgers.edu/rbhs-neurological-surgery/type/residents/ (paginated WordPress) | 2021-10 | 2024-03 (404 now) |

## Years
- **Observed:** 2013-14, 2016-17, 2019-20, 2020-21, 2021-22, 2023-24, 2024-25, 2025-26
- **Reconstructed (bracketed residents only):** 2011-12, 2012-13, 2014-15, 2015-16, 2017-18, 2018-19, and 2022-23 (page 1 of the listing is partial; the lower PGYs are reconstructed)
- **Missing:** 2026-27. The live page still shows the 2025_2026 image.
- **Significant gaps:** every reconstructed year. The page was left unchanged for years at a time (2009-10 list served until 2013, 2013-14 list until 2016-08, 2016-17 list until 2018-11). Common Crawl copies are identical.

See program57.json `gap_details` for what was tried in each year.

## Departures and joiners (updated in phase 2)
- **Patrick Reid** (NEW): a 2010 entrant (classmate of Fernholz) who is on no roster, because 2011-13 were stale. UMDNJ-NJMS neurosurgery affiliation in 2011 (PMID 21959746) and on Feb 2013 Stroke abstracts. **Transferred to USC (104)**: PGY5 there in 2014-15, graduated 2017. Left after 2012-13 (PGY3).
- **Raja Jani**: **transferred to Louisville (88)** in 2023, not 2024. A paper received 2023-02-09 carries a Louisville affiliation, he is absent from the official 2023-24 NJMS image, and he is PGY7 at Louisville in 2024-25. The sites.rutgers listing that still showed him in 2024-03 was stale, so his row was removed from that capture.
- **Elena Solli**: left after 2019-20 (PGY3). **Switched specialty**: Mount Sinai neurology 2021-22, then NYU ophthalmology 2023-25.
- **Ryan Radwanski**: left during or after 2022-23 (PGY2). Later affiliations are Weill Cornell / Brain and Spine Group, then Cornell biomedical engineering. Outcome unknown.
- **Gap artefacts resolved as completions** (later neurosurgery affiliations): Assina 2015, Quinn 2016, Crisman 2018, Meleis 2019, Say 2019.
- **Gap artefacts still unresolved**: Sinclair (his NPI "switch" is only the default student taxonomy), Cohen, Slottje.
- **2020-21 joiners**: Shafiq PGY7, Cummock PGY6, Arzumanov PGY5, Zhao PGY5, Talbot PGY4 and Jani PGY3 came from the **Saint Barnabas Medical Center (Livingston NJ, RWJBarnabas) AOA osteopathic neurosurgery residency**. It was ACOS-approved and affiliated with Hackensack. PD Ira Goldstein's bio describes SBMC osteopathic residents rotating at University Hospital, then "the unification of the residency programs of SBMC and NJMS". Their SBMC starts were 2014-2018, and all SBMC cohorts carried a 7-year terminal PGY.
  - **No SBMC resident was found to have been lost in the merger.** Every SBMC neurosurgery resident in PubMed and Europe PMC 2012-21 moved to NJMS. SBMC never published a roster, though, and nobody joined at PGY2 in 2020, so an SBMC 2019 intern (if there was one) cannot be observed.
  - **Manan Shah** (PGY5 2020-21) is not from SBMC: he is an MD who transferred from **Wayne State/DMC (125)** when it closed. He is the "Kevin Shah" of the notes.

## Alumni page
Only umdnj FormerResidents.cfm, captured 2009, with pre-2012 graduates. No training_history rows were added.

## Numbers
42 residents entering 2011 or later (43 with Reid, a 2010 entrant). Phase-2 adjudication: see below.

## Problems
- From 2019-20 on, rosters are PNG images, transcribed by eye.
- Name variants were canonicalised: Caminucci -> Carminucci, Hershman -> Herschman, "Nick" -> Robert Hernandez, Meybodi-Tayebi -> Tayebi Meybodi.
- Trong Huynh has an off-cycle promotion (Oct 1).
- Common Crawl index failures: CC-MAIN-2013-48, 2016-40, 2017-04, 2019-04, 2020-05, 2021-43, 2023-14.

## Phase 2 (2026-09-28)
Year significance: all observed years are `none`. 2011-13, 2014-16, 2017-19 and 2022-23 are reconstructed and `low`. 2026-27 is missing and `low`. The per-year reasons are in program57.json `year_status`.
- 2011-13 was a real risk: the stale page hid Reid's departure. PubMed affiliation mining over 2010-2024 (1065 PMIDs) turned up no other unlisted resident, only students and research fellows.
- Residual risks: the 2015 and 2017 classes each have one resident, so an unseen second matchee cannot be excluded; the 2022 interns' PGY1 year is unseen.
- Common Crawl: no new roster content was found. CC-MAIN-2022-49 has njms resident.php at 2022-11 and it still shows Housestaff21.png. The crawls that still fail are listed under `problems`.
- training_history: 31 rows. 21 are PGY-terminal graduations (including the absorbed SBMC residents and the Manan Shah transfer-in). 5 are inferred completions. Reid and Jani are transfers, Solli is a switch, Radwanski is unknown, and Sinclair has an unknown row.
- Adjudication: 24 COMPLETED, 18 IN TRAINING, 3 LEFT unknown (Sinclair, Cohen, Slottje), 2 transferred, 1 switched, 1 left (Radwanski).
