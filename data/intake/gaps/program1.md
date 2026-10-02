# Program 1: Albany Med Health System Program (Albany, NY)

7-year program, 2 per year (2017 page: complement "recently increased to 2 residents a year"; the 2012 class had one entrant). Roster in DB: `data/intake/rosters_program1.json` (16 captures, 174 observations). Alumni graduations (20 rows, classes 2012 and 2016-2026) are in `training_history`.

## Hosts / paths
| URL | Dates | Roster? |
|---|---|---|
| www.amc.edu/Academic/GME/programs/Neurosurgery/residents_fellows.html, alumni.html | 2008-09 to 2012-02 | yes (PGY headings) |
| www.amc.edu/Academic/GME/programs/Neurosurgery/residents_fellows.cfm, alumni.cfm, index.cfm | 2012-07 to 2016-05 (roster), index to 2022-06 | yes to 2016-05 |
| www.amc.edu/academic/gme/programs/Neurosurgery/meet_us.cfm | linked 2022, never archived (301 in 2026) | not captured |
| amc.edu/academic/GMENew/Neurosurgery/index.cfm | 2021 (301), 404 by 2024 | no |
| amc.edu/Departments/neurosurgery/index.cfm | 2014 to 2022 | no (department page) |
| albanymed.org/Academic/GME/programs/Neurosurgery/index.cfm | 2016-04 mirror | no |
| www.amc.edu/education/residencies-fellowships/neurosurgery-residency/neurosurgery-residency-meet-us/ | 2023-12 to live | yes ("Class of" labels), plus alumni list |

## Years (phase 2, 2026-09-28)
| AY | Status | Significance | Reason |
|---|---|---|---|
| 2011-12 | observed | none | Plakas (left off the page) added as reconstructed PGY4. He is bracketed by PGY2 in May 2010 and PGY5 in 2012-13. |
| 2012-13 | observed | none | Complete PGY1-6 list. |
| 2013-14 | observed | none | No PGY7 expected: the class of 2013 finished after PGY6. |
| 2014-15 | observed | low | The only possible omission is Plakas (entry 2008) at PGY7. |
| 2015-16 | observed | none | The page had no PGY7 level. Calayag and Jeyamohan added as reconstructed PGY7 (alumni class of 2016). |
| 2016-17 to 2018-19 | reconstructed | significant | No roster anywhere. Every class has 2 members except 2016 (Field only). |
| 2019-20 to 2022-23 | reconstructed | low | 2020-22 entrants now placed (see below). The residual risk is the same unseen 2016 slot. |
| 2023-24, 2024-25, 2026-27 | observed | none | Complete, 14 each. |
| 2025-26 | observed | none | The page left out the class of 2026. Harland and Rogers added as reconstructed PGY7. |

## Phase 2: what was searched and what was found
- **Wayback full host audit (2016-2023)**
  - Hosts covered: amc.edu/academic, /education, /news, /PR, /about, /departments, GMENew, and albanymed.org.
  - No roster exists. residents_fellows.cfm and meet_us.cfm were never archived after 2016-05.
  - Under Neurosurgery/images, the only files are 2021 testimonial photos (Harland, Spurgas, Sweeney, Adamo).
  - Output: `data/raw/extraction/p1/phase2/gapaudit_ph2.txt`.
- **Link audit.** I read the archived index.cfm pages from 2017-07, 2017-11, 2021-08 and 2022-06.
  - The 2021-22 pages state a complement of "2-2-2-2-2-2" and quote Sweeney, Harland and Spurgas as residents.
  - The GME "Meet our residents" page (2017) shows no neurosurgery roster.
- **News.** None of these pages name neurosurgery residents: match day 2017, 2022 and 2023, and "welcomes new class of residents" (2021).
  - Field's 2023 hire notice says he "spent seven years training" at Albany (residency plus CAST fellowship). This confirms he entered in 2016.
- **Common Crawl rerun with the fixed filter** (see the JSON `problems` for crawls that did not finish).
  - Prefixes: gme/programs/neurosurgery, gmenew/neurosurgery, gme/meet, departments/neurosurgery, education/.../neurosurgery, and albanymed.org.
- **PubMed affiliations 2015-2024, plus NPPES.** No unlisted resident was found.
  - Every non-roster author was a student, research fellow, faculty member, or resident elsewhere: Haider (Henry Ford), Syed (Brown), Graffeo (Mayo), Heller (USF). Staudt was a functional fellow.
  - Amr Albakry (NPI 2016-08, Neurological Surgery, Albany department address, Egyptian neurosurgeon) is probably a research or functional fellow, so I did not add him.
- **2020-22 entrants placed in 2020-23 as reconstructed rows:** Custozzo, Sweeney, Prabhala, Rosoklija, Barr, Ogagan. The evidence is:
  - the Class-of labels on the 2023-24 page;
  - NPPES residency NPIs from March 2020, 2021 and 2022 at the Albany Department of Neurosurgery. Ogagan's NPI dates from May 2021 at a non-department Albany number; his neurosurgery entry is 2022, and the prior year is unknown.
- **Cross-program.** I matched every roster file against the Albany PubMed authors. Only Yim went from Albany to another program.

## Remaining significant gap
- **The 2016 class has only one known entrant (Nicholas Field) against a complement of 2.**
  - If a second 2016 intern existed and left before 2023, no available source shows it.
  - This leaves 2016-17 to 2018-19 significant. From 2019-20 on it is low.
- **Low:** a departure followed by a lateral replacement in 2016-22 would leave no trace. Plakas's graduation year (2014 or 2015) is not confirmed.

## Phase 2 problems
- **Common Crawl rerun was stopped after about 50 minutes.** Only 19 of 74 crawls from 2016-2023 finished (up to CC-MAIN-2017-43). Three prefix lookups failed. The JSON `problems` field lists every unfinished crawl.
  - Impact is probably small. Phase 1 already read the index for the main path in every crawl from 2012 to 2023 and found nothing after 2016-05. amc.edu also blocked Common Crawl's crawler by 2022.
- **USC transfer-in row for Yim not added.** It belongs to program 104, which is outside this agent's write scope.

## Consistency
- Through 2012-13 the site labelled residents PGY1-6 and they graduated after PGY6 (Gandhi 2012; Bahrassa and Jacobsen probably 2013; Plakas probably 2014).
- Classes of 2016 onward follow the 7-year pattern.
- Amilyn Taplin (PGY1 in 2011-12) graduated in 2017 after 6 listed levels.
- Alexandra Paul (same class) graduated in 2019, one year extended. Her reconstructed rows use PGY7 in both 2017-18 and 2018-19.
- Class sizes by entry year:

| Entry year | Size |
|---|---|
| 2011 | 3 (including Peris-Celda, who joined in 2014) |
| 2012 | 1 |
| 2013 | 2 |
| 2014 | 2 (Yim left) |
| 2015 | 2 |
| 2016 | 1 seen |
| 2017-2026 | 2 each |

## Departures (left the roster before the terminal PGY)
- **Benjamin Yim: TRANSFERRED to USC (program 104).**
  - At Albany he was PGY2 in 2015-16 (last capture 2016-05-20). He was PGY3 on USC's 2016-17 roster PDF and graduated from USC in 2021.
  - A 2019 PubMed paper lists both affiliations.
  - Recorded in `training_history`: completed=no, departure_type=transferred, end_year=2016.
- **Constantine Plakas** (entry 2008): last listed as PGY6 in 2013-14. He probably graduated in 2014 or 2015; no graduate list covers those years.
- **Farhad Bahrassa and Walter Jacobsen:** PGY6 (the final level at the time) in 2012-13, and in the Class of 2013 photo. Recorded as completed in 2013 ("PGY-terminal roster").
- **Mohammad Shaikh:** PGY3 in 2009-10. This is before the study window.

## Joiners (first seen above PGY1)
- **Walter Jacobsen:** transferred in from SUNY Upstate (program 63), where he was PGY4 in 2010-11. At Albany he was PGY5 in 2011-12 and was not on the May-2010 Albany roster. Confirmed against both rosters.
- **Maria Peris-Celda:** joined at PGY4 in 2014-15 and graduated in 2018.

## Adjudication (after phase 2)
| Outcome | Count | Who |
|---|---|---|
| Completed | 22 | |
| In training | 14 | |
| Transferred | 1 | Yim, to USC |
| Left, outcome unknown | 1 | Plakas, a pre-2011 entrant who probably graduated |

## Alumni
The live Meet Us page lists graduates for 2016-2026. The 2016 archived alumni.cfm names graduates for 2005-2012. Rows inserted into `training_history` for Gandhi 2012 and for the 2016-2026 graduates (20 rows).
