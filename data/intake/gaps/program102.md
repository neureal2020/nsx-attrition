# Program 102 - University of Rochester (URMC) Neurosurgery - roster gaps

7-year program, complement 2/year. Built 2026-09-28 (phase 1).

## Hosts / paths
All rosters are on the GME "prospective-residents" pages; the department site (`urmc.rochester.edu/neurosurgery/`, education.cfm -> education.aspx -> /education 302) only links there.

| Path (under `urmc.rochester.edu/education/graduate-medical-education/prospective-residents/neurosurgery/`) | Dates |
|---|---|
| `our-residents/current-residents.cfm` | 2011-10 .. 2015-09 (stale 2014-15 list from Mar 2015 on) |
| `our-residents/current-residents.aspx` | 2016-02 .. 2016-06 |
| `our-residents.aspx` | 2016-07 .. 2024-12 |
| `our-residents` (live) | 2025-01 .. 2026-09 |
| `our-residents/recent-graduates{.cfm,.aspx,}` (alumni page) | 2012 .. live |

## Year-by-year captures
| AY | Source | Captured | n | Notes |
|---|---|---|---|---|
| 2011-12 | Wayback current-residents.cfm | 2012-01-14 | 13 | only one chief (Boev, 2005 class of one) |
| 2012-13 | Common Crawl CC-MAIN-2013-20 | 2013-05-22 | 13 | no Wayback capture Jan 2012-May 2014 |
| 2013-14 | Common Crawl CC-MAIN-2013-48 | 2013-12-05 | 14 | same list as Wayback 2014-05-17 |
| 2014-15 | Wayback | 2015-03-01 | 13 | Srinivasan gone |
| 2015-16 | Wayback current-residents.aspx | 2016-06-20 | 12 | = CC Feb 2016; Montoya gone |
| 2016-17 | Common Crawl CC-MAIN-2016-44 | 2016-10-22 | 13 | no Wayback roster capture |
| 2017-18 .. 2023-24 | Wayback our-residents.aspx | Sep-Nov | 13-14 | |
| 2024-25 | Wayback | 2024-09-13 | 14 | complete (phase 2: George was listed as 'PGY- 5') |
| 2025-26 | Wayback our-residents | 2025-09-15 | 14 | |
| 2026-27 | live | 2026-09-27 | 14 | advanced; new PGY-1 Green, Jalal |

Observed: all 16 years. Reconstructed: none. Missing: none. **Phase 2: every year significance = none** (per-year reasons in the JSON `year_status`).

## Phase 2 (2026-09-28)

### 2024-25 closed: Derek George was never absent
Every 2024-25 capture (Sep 2024 to May 2025) lists "Derek D. George is a PGY- 5 resident", with a space after the hyphen. The phase-1 regex `PGY[- ]?(\d)` missed it. The fixed parser is `data/raw/extraction/p102/phase2/parse102p2.py`, and the build script is `phase2/build102p2.py`. George was PGY1-7 continuously from 2020-21 to 2026-27, so he had no research year. No other capture changed when re-parsed.

### Leavers, resolved with program pages (URMC's other residency programs) and publications
| Name | Left after | Outcome | Evidence |
|---|---|---|---|
| Michael Moravan | 2011-12 PGY1 | **Switched: radiation oncology** (URMC, class of 2016; then Duke) | URMC Rad Onc recent-graduates page, "2016: Michael Moravan, MD PhD"; PubMed Rad Onc URMC 2016, Duke 2017-21 |
| Vasisht Srinivasan | 2013-14 PGY5 | **Switched: emergency medicine** (URMC EM PGY1 2015-16, class of 2018; then a neurocritical care fellowship at Cincinnati; now UW EM) | URMC EM roster: PGY-1s (Jun 2016), PGY-3s (Nov 2017, May 2018); EM recent-graduates page, class of 2018. His 2014-15 year is unaccounted for. |
| Simone Montoya | 2014-15 PGY4 | **Switched: diagnostic radiology** (URMC R1 2015-16 to R4 2018-19) | URMC Radiology roster: first year (Jun 2016), third year (Nov 2017), fourth year (2019); PubMed Imaging Sciences URMC 2016-20 |
| Clifford Pierre | 2018-19 PGY5 | **Did not complete; outcome unknown** (not a switch) | PubMed/OpenAlex: Dept of Neurosurgery URMC until May 2019, then Swedish Neuroscience Institute / Seattle Science Foundation, Seattle, Oct 2019-2026 (spine and cerebrovascular neurosurgery papers). Not on the URMC alumni list or on any other program's roster in the DB. His NPI still carries the 2014 student taxonomy. |
| Rahim Ismail | 2020-21 PGY3 | **Switched: diagnostic radiology** (URMC R1 2021-22 to R4 2024-25; now UTSW) | URMC Radiology roster: first year (Sep 2021), second (Nov 2022), third (Nov 2023), fourth (Nov 2024, Apr 2025); PubMed Imaging Sciences URMC 2023-26 |

The adjudicator's NPI-only "switched" label was right for 4 of the 5, and program pages now support those 4. It was wrong for Pierre.

### Joiner
Simone Montoya joined in 2013-14 at PGY3; her PGY places her in the 2011 cohort, in Moravan's slot. She is absent from the 2012-13 roster (May 2013). Where she spent 2011-13 is unknown: her bio, PubMed and OpenAlex are all silent. Her `training_history` transfer-in row uses start_year 2013.

### Program length
The program is 7 years for every cohort: all graduates from 2012 to 2026 finish at PGY-7. `terminal_pgy_by_entry_year` = 7 for all years.

### Cross-program
`data/intake/crossmatch.json` has no pair involving program 102. None of the 5 surnames appears on any other program's roster in the DB.

### training_history rows added (6)
Moravan, Srinivasan, Montoya and Ismail: `completed='no'`, `departure_type='switched_specialty'`. Pierre: `completed='no'`, `departure_type='unknown'`. Montoya also has a transfer-in row (start 2013, PGY3).

### Adjudication after phase 2
25 COMPLETED, 14 IN TRAINING, 4 LEFT -> SWITCHED SPECIALTY, 1 LEFT -> did not complete (Pierre).

### Remaining (not significant for the roster)
- Pierre's status after 2019: research fellow or non-ACGME training? This is unconfirmed.
- Montoya's whereabouts in 2011-13.
- Srinivasan's 2014-15 year.

## Problems
None blocking. The NPPES API could not be reached in phase 2 (it was not needed). Europe PMC full text returned 503 for 3 of the 5 PMC ids.
