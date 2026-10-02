# Program 73 - University of Arkansas for Medical Sciences (UAMS), Little Rock AR

7-year program. The complement is not stated; observed intern classes are 1-3 (usually 2). JSON twin: `program73.json`. Scratch: `data/raw/extraction/p73/` (phase 2 in `phase2/`).

## Hosts
| Host / path | From | To |
|---|---|---|
| www.uams.edu/neurosurgery/ (static ASP) | 2005 | 2010-06 (before the window; no resident list) |
| neurosurgery.uams.edu/?id=NNNN&sid=29 (UAMS ASP CMS; Residents = ?id=8043) | 2012-01 | 2014-05. The residents page was never archived or crawled |
| neurosurgery.uams.edu WordPress v1 (homepage residents menu, /residents/<slug>/) | 2014-11 | 2017-09. The menu was never updated after ~May 2014 (same 11 names through 2016-05) |
| neurosurgery.uams.edu/residents/current-residents/ | 2017-10 | 2022-01 |
| medicine.uams.edu/neurosurgery/residents/current-residents/ (live) | 2022-08 | 2026-09-27 |

## Year status (phase 2)
| AY | Status | Significance | Reason |
|---|---|---|---|
| 2011-12 | missing (partial list) | significant | Feb-2012 sitemap: 7 names, no PGY. A 2011 entrant who left before mid-2014 would not be seen. |
| 2012-13 | reconstructed (partial) | significant | No capture anywhere. Elswick (PGY-2), Gandhi, Phillips, Dowdy are bracketed. The 2012 class shows only Burton. |
| 2013-14 | reconstructed (partial) | significant | As 2012-13 (Elswick is PGY-3). |
| 2014-15 | missing (partial list) | low | The 11-name menu mirrors the ~May-2014 profiles. Everyone on it is now traced except Gandhi and Phillips (pre-2011 entrants). |
| 2015-16 | reconstructed | significant | Elswick PGY-5 added. The 2015 class shows only Stephens, and when Paulson and Paullus arrived is not observed. |
| 2016-17 to 2026-27 | observed | none | Full rosters. |

## Phase 2 findings
- **Transfers out:**
  - **Michael Raber** left after 2011-12 for Brigham and Women's (p37), where he was PGY-4 (research) in 2012-13 and graduated in 2016.
  - **Matthew Burton** entered in 2012 and left after 2014-15 at PGY-3. He was PGY-4 at Missouri (p94) in 2015-16.
  - **Clay M. Elswick** entered in 2011 and left after 2015-16 at PGY-5. He was Year 6 at Wayne State (p125) in 2016-17. The 2016-17 UAMS roster has no PGY-5 because Elswick left the 2011 class and Burton left the 2012 class.
- **Transfers in (confirmed by the same medical school on both programs' pages):**
  - **Paullus** came from LSU Shreveport and started at UAMS as PGY-3 in 2016-17.
  - **Taylor Wilson** came from Wake Forest and started as PGY-4 in 2017-18.
  - **Paulson** came from UTMB, where he was a research PGY-6 in 2012-13. He published from the Swedish Neuroscience Institute in 2015-16 and was PGY-7 at UAMS in 2016-17.
- **Pre-2016 names resolved as not attrition:**
  - **Tabbosha** was an assistant professor by Aug 2012 (UAMS news).
  - **Dowdy:** a Jul-2017 UAMS news story calls him a former resident who is now a neurosurgeon in Hot Springs.
  - **Bahgat** is listed as an assistant professor on the Nov-2017 faculty page.
  - **Vasudevan** has a 2014 Stanford neurosurgery affiliation but is on no Stanford resident roster, so he was probably a fellow there.
- **Still unresolved:** Gandhi and Phillips. Both are pre-2011 entrants (NPPES enumeration dates 2009 and 2008). 16_adjudicate gives every name-only person a guessed entry year of 2011 or 2014; exclude all six (`pre2011_entrants_name_only` in the JSON) from the 2011+ cohort.

## Departures (left before PGY-7)
| Name | Last AY | Last PGY | Outcome / evidence |
|---|---|---|---|
| Michael Raber | 2011-12 | 3 (inferred) | Transferred to Brigham (p37) |
| Matthew Burton | 2014-15 | 3 | Transferred to Missouri (p94) |
| Clay M. Elswick | 2015-16 | 5 | Transferred to Wayne State (p125) |
| Elena Rose Milosavljevic | 2017-18 | 1 | Switched to radiology: Dept of Radiology, Loma Linda, 2023 (PMID 37941631) |
| Taylor Wilson | 2018-19 | 5 | Left mid-year. Probable switch to neurology: Loma Linda Dept of Neurology, 2024 (PMID 38468681) |
| Paul Lee | 2018-19 | 3 | Unknown. Affiliated with CHI St. Vincent Arkansas Neuroscience Institute in 2021-24; his role is not stated |
| Olusoji Afuwape | 2021-22 | 3 | Unknown |
| Kevin Thomas | 2022-23 | 2 | Switched to pediatrics (allergy/immunology): UNC (PMIDs 36134173, 40065718) |
| Austin Robbins | 2024-25 | 1 | Unknown. The NPI "switch" call is unsupported: NPPES has no record under this name |
| Alex Gilman | 2024-25 | 1 | Unknown. The NPI "switch" call is unsupported: NPPES lists him only as a student in training |

## Joiners
- David Paulson: PGY-7 in 2016-17, from UTMB.
- Patrick Paullus: PGY-3 in 2016-17, from LSU Shreveport.
- Taylor Wilson: PGY-4 in 2017-18, from Wake Forest.
- Kierany Shelvin: PGY-2 in 2025-26, origin not found.

## training_history (26 rows inserted, program 73)
- 11 PGY-terminal graduations, 2017-2026. Pinckard-Dover's 2020 graduation is sourced to a UAMS news story.
- 4 pre-2016 completions: Tabbosha, Dowdy, Bahgat, Vasudevan.
- 3 transfers out.
- 3 transfer-in rows: Paullus, Paulson, T. Wilson.
- 3 switches.
- 2 unknown outcomes: Gilman, Robbins. These override the NPI calls.

## Adjudication (after phase 2)
- 17 COMPLETED
- 12 IN TRAINING
- 3 TRANSFERRED
- 3 SWITCHED SPECIALTY. These now rest on publication affiliations, not on NPI.
- 6 outcome unknown: Gandhi and Phillips (pre-2011), Paul Lee, Afuwape, Gilman, Robbins.

Residents entering 2011 or later: 30.

## Problems
- CC-MAIN-2015-35, 2017-47 and 2019-43 were retried and read successfully. 2015-35 has 0 records.
- OpenAlex rate-limited the per-person queries (429), so PubMed was used for those.
- No capture of any kind exists for the 2011-14 residents page.
