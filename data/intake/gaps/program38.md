# Program 38: Mayo Clinic College of Medicine and Science (Jacksonville) Program (Jacksonville, FL)

- The residency is new. The first resident started in July 2012 ("One resident will begin this program annually"). It was advertised as six years until Oct 2015 and seven years from Nov 2015. Yoon (2012 entrant) finished in 2018 after 6 years; everyone after him trains 7 years (`terminal_pgy_by_entry_year` in the JSON).
- The complement is 1. Classes of 2 PGY-1s: 2019 (Ravindran, Stein), 2021 (Montaser, Goyal), 2026 (Garner, Mohamed). The 2018 class was empty.
- Only Florida-specific pages are used (none of the Rochester or Arizona pages).

## Hosts
| Host/path | Dates | Notes |
|---|---|---|
| www.mayo.edu/msgme/residencies-fellowships/neurologic-surgery/neurologic-surgery-residency-florida | 2012-10 to 2017-02 | Program page and subpages. No residents listed |
| www.mayo.edu/msgme/about/resident-profiles/neurologic-surgery | 2016-09 to 2017-01 | Roster with inline PGY (Jacksonville only) |
| www.mayo.edu/mayo-clinic-school-of-graduate-medical-education/.../neurologic-surgery-residency-florida/resident-profiles | 2017-03 to 2018-06 | Renamed path. 301 from Jul 2018 |
| college.mayo.edu/academics/residencies-and-fellowships/neurologic-surgery-residency-florida/ (resident-profiles/, graduate-outcomes/) | 2019-09 (WB) to live | Testimonials 2019-2022, full PGY roster from 2023, alumni page |

## Years (after phase 2)
| AY | Status | Significance | Basis |
|---|---|---|---|
| 2012-13..2015-16 | reconstructed | low | No page existed. Each single class slot held by a resident who finished on schedule; PubMed 2012-16 (129 papers) shows no other resident |
| 2016-17, 2017-18 | observed | none | Full rosters with PGY |
| 2018-19 | reconstructed | low | All bracketed. 2018 class empty in every later source; PubMed mining and a Florida NPI screen found no unaccounted PGY-1 |
| 2019-20 | partial + reconstructed | low | Testimonials (Stein, Ebot, Gassie) + bracketed. Stein corrected to PGY-1 |
| 2020-21 | reconstructed | low | Clifton, Gassie, Akinduro, Ravindran, Lee (added). Ebot's exit falls in or at the end of this year |
| 2021-22 | observed (effectively complete) | none | Sep-2021 page names every expected resident except the departed Ebot |
| 2022-23 | observed | none | Full roster |
| 2023-24 | reconstructed | low | Bracketed + Goyal (PGY-3, PubMed affiliations) + Perez Vega (PGY-1: NPI 2023-03, 2024 paper footnote "Resident ... Jacksonville") |
| 2024-25 | reconstructed | low | Bracketed + Perez Vega 2, Bendfeldt 1 (NPI 2024-03), Goyal 4 (paper received Nov 2024, Mayo-Jax neurosurgery) |
| 2025-26, 2026-27 | observed | none | Full rosters |

No year remains significant for roster coverage.

## Departures and outcomes (training_history)
- **Rachel Stein** (th_id 2510): entered **2019**, not 2018. Evidence: NPI enumerated 2019-04; VCOM student affiliation on papers submitted Jun-Aug 2018; first Mayo-Jax affiliation on a paper submitted 2019-07-24. **Transferred** to Tennessee/Semmes-Murphey (program 105) as PGY-2 for 2020-21 (Semmes bio, 2020-09-29). She left Tennessee by Apr 2021; PubMed shows UF-Jacksonville Radiology 2021-26 (belongs to program 105's record).
- **James Ebot** (th_id 2511): entered 2017. Mayo-Jax neurosurgery affiliation on papers published up to Sep-Nov 2020; absent from Sep 2021 on. Left between mid-2020 and Sep 2021 (end_year 2021, approximate). Johns Hopkins Bloomberg School of Public Health in 2023. No NPI. Outcome unknown.
- **Ansh (Anshit) Goyal** (th_id 2512, completed=unknown): entered 2021. Mayo-Jax neurosurgery affiliation to Nov 2024. Off the 2025-26 and 2026-27 rosters (classmate Montaser is PGY-6). His bio mentions an enfolded clinician-investigator program. A 2026 paper lists him under Anesthesiology and Perioperative Medicine (Mayo-Jax co-authors), but he is not on the Mayo Florida anesthesiology resident page. NPI (FL, neurosurgery) was updated 2025-12. Research leave vs departure is unresolved.
- Graduates on the alumni page: Yoon 2018, Grewal 2020, Clifton 2021, Gassie 2022, Akinduro 2023, Ravindran 2026 (th_id 1086-1091).
- Adjudication (16): 8 in training, 6 completed, 1 transferred (Stein), 1 left without completing (Ebot), 1 left with outcome unknown (Goyal).

## Phase 2 searches
Gap audit (2018-2025) of the college.mayo.edu program path, the old GME path and the headshot asset folder (only known residents; photo files dated 2020-06 for Lee, 2021-06 for Montaser and Goyal). Wayback CDX for resident-profiles/ (no new captures), Doximity (none) and semmes-murphey.com/resident/. PubMed affiliation mining 2012-16 and 2017-26. PubMed, OpenAlex and Europe PMC author searches. NPPES entry-year checks and a Florida neurosurgery NPI screen for 2017-19. The live Mayo Florida anesthesiology resident page. Files: `data/raw/extraction/p38/phase2/`.

## Problems
- Common Crawl (`data.commoncrawl.org`) returned 403 on 2026-09-28 (shared-IP throttle). CC-MAIN-2023-23 is still unread. Its value is now low, since 2023-24 is covered by other evidence.
- A 2018 entrant who left within a year cannot be fully excluded; the evidence against one is indirect.
- Goyal's status needs a program contact or a later capture to settle.
