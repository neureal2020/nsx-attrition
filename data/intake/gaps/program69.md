# Program 69: University at Buffalo (Buffalo, NY): roster gaps

- Program length: 7 years. It was 6 years (PGY-6 chief) through the 2011 entering class; 7-year numbering starts with the 2012 class, first visible in 2016-17.
- Complement: 2 per year to about 2015, then 3 (4 in 2024 and 2025).
- The residency pages have sat on four different sites. The University at Buffalo Neurosurgery (UBNS) practice site at ubns.com was always the most current. The medical school's department pages on medicine.buffalo.edu often lagged by one to three years.
- Residents entering 2011 or later: **49**. Adjudication (phase 2): 33 completed, 21 in training, 3 transferred, 1 switched specialty, 1 left (destination unknown).

## Hosts
| Host / path | From | To |
|---|---|---|
| ubns.com / ubneurosurgery.com `handler.cfm?cpid=N` (ColdFusion). `ubns.com/residency` is a text-only page with no resident list | 2005 | 2012-10 |
| ubns.com (+ ubneurosurgery.com mirror) `/residency-and-fellowship/residency-program/current-residents` (Concrete5) | 2012-12 (roster first archived 2014-03) | 2016-09 |
| ubns.com `/residency-fellowship/residency-program/current-residents/` (WordPress). Wayback never archived it; Common Crawl has 2018-12, 2019-02 and 2019-04 copies | 2017-06 | 2019-12 |
| medicine.buffalo.edu `/departments/neurosurgery/education/residency/residents/current.html` | 2019-08 | live (shows 2025-26) |
| ubns.com `/current-residents-fellows/` | 2021-01 | live |
| Alumni: medicine.buffalo.edu `.../residents/alumni.html` (graduates to 2022). ubns.com `/former-residents-fellows/` (Former Chief Residents to 2025) | 2021/2022 | live |

## Years
| AY | Status | Source | n | Significance |
|---|---|---|---|---|
| 2011-12 | reconstructed | alumni + 2013-14 PGYs | 12 | **low**: no roster page ever existed; PubMed 2007-14 shows no unlisted resident. Residual: the 2008 class shows only Sorkin, so a 2008-class departure before 2013 can't be ruled out. |
| 2012-13 | reconstructed | alumni + 2013-14 PGYs | 12 | **low**: same evidence as 2011-12. |
| 2013-14 | observed | Wayback 2014-03-28 | 12 | none |
| 2014-15 | observed | Wayback 2015-05-12 | 13 | none |
| 2015-16 | observed | Wayback 2015-11-15 | 14 | none |
| 2016-17 | observed | Wayback 2016-09-27 | 16 | none (Bregy printed as PGY-1, stored as PGY-2) |
| 2017-18 | **observed (phase 2)** | WordPress profile publish dates + former-fellows text; Morrison reconstructed | 16 | **low**: see below |
| 2018-19 | observed | Common Crawl 2018-12-14 | 17 | none |
| 2019-20 | observed | medicine.buffalo.edu 2019-08-17 | 17 | none |
| 2020-21 | observed | ubns.com 2021-01-15 | 18 | low: omits Sonig, a 2021 graduate (outcome already known) |
| 2021-22 | observed | ubns.com 2021-10-16 | 19 | none |
| 2022-23 | observed | medicine.buffalo.edu 2022-10-14 | 19 | none |
| 2023-24 | observed | ubns.com 2024-04-17, plus Shallwani reconstructed | 18 | none: see below |
| 2024-25 | observed | ubns.com 2025-02-16 | 19 | none |
| 2025-26 | observed | ubns.com 2026-01-12 | 19 | none |
| 2026-27 | observed | live ubns.com | 21 | none |

**Program length by entry year** (`terminal_pgy_by_entry_year` in the JSON): 6 years for 2005-2011 entrants, 7 years from 2012. Exceptions:
- Morr (2010) and Shakir (2011) took 7 years, with an enfolded endovascular fellowship.
- Becker (2018) and Hess (2019) left after PGY-6 but are listed as Former Chief Residents, so they are counted as completed.

## Phase 2 (2026-09-28)

### 2017-18: now observed
The 2019 Common Crawl copies of the ubns.com WordPress resident profiles carry their publish dates (`article:published_time`):
- **2017-07-06**, site-launch batch (post ids 988-1028): Meyers, Winograd, Kogan, Vakharia, Agyei, Bregy, Jowdy, McPheeters, Sonig, Smolar.
- **2017-08-15** (ids 1241-1250): O'Connor, Cappuzzo, Recker, Housley. These are exactly the 2017-18 newcomers.
- **2018-07-02**: the 2018 class.

Other 2017-18 evidence:
- The former-fellows page (CC 2018-12) still prints Shakir as "PGY-7 Resident" and Sonig as "PGY-4 Resident". That text was written in 2017-18.
- Thind and Loya appear on the UC Davis and Wayne State rosters in 2017-18.
- The 2017 site says the program "accepts two residents per year", so the 2 interns (Housley, Recker) make a full class.

Only Morrison (PGY-7, 2018 graduate) is still reconstructed.

Residual: one deleted post (id 996) was created on 2017-07-06 between Vakharia and Agyei. It is probably Thind's profile, removed after he left. All 24 Common Crawl crawls for 2017-18 were listed for the whole ubns.com host, and they hold no roster, profile or news page beyond these.

### 2023-24: Shallwani
Every 2023-24 capture omits Shallwani. He is bracketed (PGY-5 in 2022-23, PGY-7 in 2024-25), and a paper first published online 2024-04-13 (PMID 38613377) gives his affiliation as UB Neurosurgery. Added as a reconstructed PGY-6 row.

### 2011-13
Searched with no new roster found:
- gapaudit on ubns.com, ubneurosurgery.com, smbs.buffalo.edu (GME and Surgery pages) and buffalo.edu/news.
- Common Crawl 2011-2013.

PubMed affiliation mining for 2007-2014 surfaced only faculty, fellows (per the former-fellows list), students and known residents.

### Failed Common Crawl requests from phase 1
All four were retried, all succeeded, and none held anything new.

## Outcomes recorded (training_history th_id 3036-3048, program 69)
Transfers out:
- **Joti Thind** -> UC Davis (77), PGY-4 2017-18. end_year 2017.
- **Joshua Loya** -> Wayne State (125), Year 3 2017-18; then UCSD (75) PGY-6 2020-21 after the Wayne State closure. end_year 2017.
- **Alex Aguirre** -> Barrow (4), PGY-2 2025-26. end_year 2025.

Other departures:
- **Neil Almeida**: switched to radiation oncology. Roswell Park profile: "Resident Physician, PGY 5, Department of Radiation Medicine". end_year 2023.
- **Kenan Rajjoub**: left after PGY-2 (end_year 2022), outcome unknown. A 2025 paper lists him at Mayo Clinic Radiology, role unknown.

Joiners (rows with start_year):
| Resident | Joined | From |
|---|---|---|
| Morrison | PGY-6, 2016 | Brown (54) |
| Sonig | PGY-3, 2016 | UB endovascular fellowship (trained at NIMHANS, India) |
| O'Connor | PGY-4, 2017 | Florida (82) |
| Cappuzzo | PGY-2, 2017 | MGH general-surgery internship |
| Starling | PGY-6, 2020 | UNM (97), after its closure |
| Singh | PGY-2, 2022 | unknown |

PGY-terminal graduations (no alumni row): Lim and Shallwani, 2025.

## Remaining
- 2011-12 and 2012-13 are still reconstructed (low significance).
- Singh's origin is unknown.
- Rajjoub's destination is unconfirmed.

## Alumni and training_history
Inserted 31 graduation rows:
- 2012-2022 from the medicine.buffalo.edu placements page.
- 2023-2025 from the ubns.com Former Chief Residents list.

The ubns.com year is the **chief year**, which is not always the graduation year:
- Ghannam is listed under 2025 but was PGY-7 in 2025-26. Her row is stored with end_year 2026 and a note.
- Lim and Shallwani (PGY-7 in 2024-25) are not listed at all, so they have no alumni row.

## Problems
- None blocking.
- All four phase-1 failed Common Crawl index requests succeeded on retry.
- Live ubns.com was rebuilt, so the old WordPress post ids return 404 and deleted post 996 cannot be identified.
