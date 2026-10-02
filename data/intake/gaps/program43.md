# Program 43 - Medical College of Wisconsin Affiliated Hospitals Program (Milwaukee, WI)

7-year program; "one or two new residents each year" (complement 2; 3 interns in 2023 and 2026). No alumni/graduates page exists on any program host. Phase 2 added graduations to `training_history` from PGY-terminal rosters. Every roster lists each resident's completion year ("Residency Completion" / "Class of"), and PGY is derived from it.

## Hosts
| Host / path | From | To |
|---|---|---|
| www.mcw.edu/neurosurgery/education/residentroster.htm (old static MCW site) | 2010-01 | 2014-10. Content frozen at the 2011-12 list from about Jun 2011 |
| neurosurgery.mcw.edu/extranet/ (research-update blog; "Fellows/Residents" posts) | 2013-10 | 2014-10 |
| neurosurgery.mcw.edu/education/residency-program/residents/ (+ /faculty/residents/, /team/residents/) | 2015-02 | 2019-02 |
| www.mcw.edu/departments/neurosurgery/people/residents (neurosurgery.mcw.edu now 301s here) | 2019-10 | live 2026-09-27 |

## Years (phase 2, 2026-09-28)
| Year | Status | Significance | Why |
|---|---|---|---|
| 2011-12 | observed | none | Dec 2011 roster |
| 2012-13 | reconstructed | low | Frozen page (CC May 2012 copy identical). Cochran, Eckardt, Sharma in dept extranet posts Dec 2012-Jun 2013 (source `other`); Lozen, Oni-Orisan, Nguyen, Doan bracketed; intern Arocho-Quinones from her bio ("MD 2012, then began her residency at MCW") |
| 2013-14 | reconstructed | low | Extranet posts plus bracketed residents; Arocho-Quinones PGY2, Gelsomino PGY1 (MD 2013, class of 2020) |
| 2014-15 | observed | none | Feb 2015 roster |
| 2015-16 | observed (+2 reconstructed) | low | Janich and Montoure (MD 2015, class of 2022) added as PGY-1 |
| 2016-17 to 2021-22 | observed | none | complete rosters |
| 2022-23 | observed (+2 reconstructed) | low | MacKinnon and Palmer (MD 2022, class of 2029, live bios) added as PGY-1 |
| 2023-24 to 2026-27 | observed | none | complete rosters |

2012-13 and 2013-14 are low, not none: no real roster exists in either archive. But every resident on either side is accounted for, both intern classes are known from bios, and PubMed MCW-neurosurgery affiliation mining for 2011-16 turned up no one unlisted. Vedantam was a research fellow who went on to Baylor. Mohit Patel was an MCW student who went on to Case.

`terminal_pgy_by_entry_year`: 7 for all cohorts.

## Departures (left before PGY-7)
| Name | Last AY | Last PGY | Outcome |
|---|---|---|---|
| Amos Ladouceur | 2011-12 | 5 | Unknown. Class of 2014, entered 2007 (pre-cohort). Missing from the 2014-15 roster, which also fits graduating in 2014. No evidence either way (the NPI Family Medicine listing is not evidence). No row. |
| Amber Retzlaff | 2017-18 | 2 | **Switched to Radiation Oncology.** PubMed: MCW Radiation Oncology 2020 (PMID 31525486, 32599030); Abbott Northwestern 2025 |
| Fatu Conteh | 2019-20 | 2 | **Transferred to Loma Linda (program 31).** On the LL roster PGY3 2024-25 to PGY5 2026-27, with the same Rutgers RWJ MD and Princeton BA. PubMed 37059361 (LLU Neurosurgery, 2023) |
| Jose Sanchez Jimenez | 2022-23 | 4 | Left in 2023. Destination unknown: his MCW bio returns 410, there are no later publications, he is on no other roster in the DB, and his NPI has not changed since 2021 |

## Joiners (above PGY-1)
- Daniel Aaronson: 2018-19 at PGY-2 (MD Sackler 2016; prior program unknown). Completed 2024.
- Jose Sanchez Jimenez: 2021-22 at PGY-3, from UPR (program 101, closure dispersal).

## training_history (22 rows)
- 18 PGY-terminal graduations (Hoyt 2012 through Hussain 2026).
- Aaronson (transfer in, completed 2024).
- Sanchez Jimenez (transfer in 2021; left 2023, departure_type unknown).
- Retzlaff (switched_specialty, 2018).
- Conteh (transferred, 2020). The transfer-in row at Loma Linda is left to program 31.

## Counts
- Adjudication: 19 completed, 15 in training, 1 switched specialty (Retzlaff), 1 transferred (Conteh), 1 did not complete with destination unknown (Sanchez Jimenez), and 1 outcome unknown (Ladouceur, pre-cohort).

## Problems
- Phase 2 retried all four failed Common Crawl lookups, and all succeeded. CC-MAIN-2012 has residentroster.htm from 2012-05-24, showing the same frozen list. CC-MAIN-2014-23, 2015-22 and 2016-40 hold only spinecare and robots pages.
- Wayback was briefly "Temporarily Offline" during the audit.
- Remaining: where Sanchez Jimenez went, and Ladouceur's outcome.

Phase-2 files are in `data/raw/extraction/p43/phase2/`.
