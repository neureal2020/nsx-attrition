# Program 119: Wake Forest University Baptist Medical Center (Winston-Salem, NC)

**Length:** 6 years for entrants through 2012, 7 years from the 2013 entrants (`terminal_pgy_by_entry_year` in the JSON). **Complement:** 2 per year (3 in the 2025 and 2026 classes). **Residents entering 2011 or later:** 36.

Phase 2 (2026-09-28): no significant gap remains. 2019-20 is now observed from a full roster PDF, and 2018-19 is reconstructed with low significance.

## Hosts and paths
| URL | From | To |
|---|---|---|
| www.wakehealth.edu/School/Neurosurgery/Resident-Profiles.htm | 2011 | 2014-09 (Common Crawl only) |
| www.wakehealth.edu/School/Neurosurgery/Current-Neurosurgery-Residents.htm | 2014-09 | 2018-06 (301 from 2018-07-29) |
| school.wakehealth.edu/.../neurosurgery-residency (alumni "Where Are They Now?") | 2018-09 | live |
| school.wakehealth.edu/-/media/.../Neurosurgery-Residency/NEUROLOGICAL-SURGERY-RESIDENTS-2019-2020.pdf | 2019-09 | single capture (**new in phase 2**) |
| school.wakehealth.edu/residents-and-fellows/&lt;initial&gt;/&lt;slug&gt; (per-resident profiles showing the PGY) | 2019-12 | live |
| school.wakehealth.edu/.../neurosurgery-residency/current-residents (roster loaded by Coveo JS) | 2020-05 | live |

## Years
| AY | Status | Significance | Basis |
|---|---|---|---|
| 2011-12 .. 2017-18 | observed | none | Full roster pages |
| 2018-19 | reconstructed | low | See below |
| 2019-20 | observed | none | Full roster PDF (Wayback 2019-09-24): 14 residents, grouped Interns/Junior/Senior/Chief with "Class of" years. It matches the profile-built list exactly |
| 2020-21 .. 2025-26 | observed | low | Assembled from per-resident profile pages. Every class is at complement, and the classes run unbroken between the full 2019-20 and 2026-27 rosters. All ~2,485 archived profile slugs are identified. The phase-1 Common Crawl failures (2020-16, 2024-51) were retried and turned up no new slug |
| 2026-27 | observed | none | Live roster (Coveo API) |

**2018-19:** there is still no roster. The old page returns 301 from 2018-07-29. The new residency page (Common Crawl copies 2018-09 to 2019-06) has no roster and no roster link. Wayback has nothing under school.wakehealth.edu/Education-and-Training before 2019-06. The neurosurgery media folder holds only the 2019-20 PDF. Profile pages did not exist yet: the retried crawls CC 2019-04 and 2019-09 have no profile records.

The year is reconstructed from 12 residents:
- the 10 residents who appear on both the 2017-18 roster and the 2019-20 roster;
- Oravec and T. Wilson as PGY-1 ("Class of 2025", PGY-2 in 2019-20).

The 2018 class fills the 2-slot complement. PubMed authors with a Wake Forest neurosurgery affiliation in 2018-19 include no unexplained trainee.

## Departures before the terminal PGY (recorded in training_history)
| Name | Last AY / PGY | Outcome |
|---|---|---|
| Phillip Dagostino | 2014-15 / 4 | Left. Destination unknown (th 3285) |
| Chetak Patel | 2014-15 / 4 | Left. Destination unknown (th 3286). The crossmatch candidates (Hiren and Nitesh Patel) are different people |
| Taylor Wilson | 2016-17 / 3 | **Transferred** to UAMS (program 73) at PGY-4 in 2017-18 (th 3283). The UAMS side is already recorded |
| James West | 2017-18 / 4 | Left. He is absent from the 2019-20 PDF and from the alumni list. His e-mail on papers changed from wakehealth.edu (received Jun 2018) to gmail (received Nov 2018), so he most likely left in June 2018. Later affiliations are Loma Linda (2020) and Mayo Jacksonville (2021); he is on neither program's resident roster. Destination unknown (th 3284) |
| Kristen Pawlowski | 2024-25 / 2 | Left. Her profile was last seen 2024-10-11 and is missing from every later crawl (the slug now returns 301). Destination unknown (th 3287). The NPI "switch" call is not evidence. A 2026 University of Michigan neurology affiliation predates her residency, so it does not show a switch |

## Joiners above PGY-1
- **Hector Soriano-Baron**, PGY-3 in 2015-16. MD from UNAM (Mexico) in 2005, then a Barrow research fellow (th 3288).
- **Taylor Wilson**, PGY-2 in 2015-16. Where he came from is not identified.

## Alumni-page conflicts (resolved)
- **Kim and Nechtman:** the alumni page gives 2023, which is wrong; they graduated in **2022**. Four sources agree on 2022: the 2019-20 PDF says "Class of 2022", the profiles say "Projected Graduation Date: 2022", both were PGY-7 in 2021-22, and both profiles disappear after May 2022. Rows 2383 and 2384 are corrected.
- **Soriano-Baron:** 2019 is kept. The PDF also says "Class of 2019", but he was still chief resident in Sep-Dec 2019, so he finished off-cycle, probably around Dec 2019. He then did a Hopkins spine fellowship.

## Other outcomes added
- **Amponsah and Cochran:** graduated in 2012, according to the "Recent Graduates" list on the 2018 residents page.
- **Graduations seen only on rosters** (PGY-terminal, not on the alumni list):
  - Coffman and Williams: 2024
  - Oravec and T. Wilson: 2025
  - Marcet and Venkataraman: 2026

In total, 14 training_history rows were inserted and 3 were corrected.

## Adjudication
- 26 completed
- 15 in training
- 4 left, did not complete
- 1 transferred

## Problems
- None outstanding: every phase-1 Common Crawl failure was retried successfully.
- The University of Michigan neurology site returned 403. It was not bypassed.
