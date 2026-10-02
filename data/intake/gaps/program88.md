# Program 88: University of Louisville School of Medicine (Louisville, KY), gap report (phase 1 + phase 2, 2026-09-28)

The program is now 7 years with 2 residents per year ("We accept two residents per year"). Classes up to 2012 took one resident a year and were on a **6-year track**: they graduated at PGY-6, as the alumni years for Baker, Rhee, Kinsman, Hall, Mansfield and Hruska show. The 7-year track starts with the 2013 class (Aljuboori, PGY-7 in 2019-20, graduated 2020).

## Hosts and paths
| URL | From | To |
|---|---|---|
| louisville.edu/medschool/neurosurgery/residency-program/current-residents.html (old Plone site) | 2011-05 | 2013-12 (Wayback only has 2011-05 and 2012-09; Common Crawl has 2013-05 and 2013-12) |
| louisville.edu/medicine/departments/neurosurgery/residency/current-residents | 2014-03 | 2014-09 (Common Crawl only) |
| louisville.edu/medicine/departments/neurosurgery/education/neuroresidency/current-residents | 2014-10 | 2014-10 |
| louisville.edu/medicine/departments/neurosurgery/residency/neuroresidency/current-residents | 2016-05 | 2019-09 |
| louisville.edu/medicine/departments/neurosurgery/neuroresidency/current-residents | 2018-10 | 2025-03 |
| louisville.edu/medicine/departments/neurosurgery/neuroresidency/graduates (alumni; also recent-graduates in 2019) | 2019-06 | 2025-10 |
| medicine.louisville.edu/academics-programs/Neurological%20Surgery/.../neurological-surgery-residency-meet-our-residents (new site) | 2026-04 | live |
| medicine.louisville.edu/search.html people directory, facet "Resident Program = neurological surgery" (live, 2 pages) | 2026 | live |

The old program URL in the DB (louisville.edu/medschool/neurosurgery/residency-program/program-overview.html) now returns 404. uoflhealth.org has no residency pages in Wayback, and uoflphysicians.com has no roster pages.

## Year by year (after phase 2)
| AY | Source | Status | Significance |
|---|---|---|---|
| 2011-12 | manual | Reconstructed (6) | **Low.** Every 1-per-year cohort slot is accounted for: 2006 Shah and Franklin (grad 2011), 2007 Baker, 2008 Rhee, 2009 Kinsman and Hall, 2010 Chojecka (left; Yale neurology later) replaced by Mansfield (PGY-2 in 2011-12, grad 2016), 2011 Hruska (NPI Apr 2011). Only someone who entered in Jul 2011 and left by Jul 2012, above complement, could be hidden. |
| 2012-13 | CC 2013-05-23 | Observed (7), PGY-1 not listed | **Low.** The "missing 2012 intern class" is explained: the 2012 recruit, Ryan Nazar, entered at **PGY-2**. He is absent from the Jul-2012 version and listed at PGY-2 by Apr 2013; his labels match Hruska's once the Oct-2014 slip is corrected. A 2012-13 PGY-1 would have been PGY-2 in 2013-14, and nobody was. The program already carried 7 residents, over 1 a year for 6 years. The alumni list has no 2018 or 2019 graduate. |
| 2013-14 | CC 2014-03-11 | Observed (6), PGY-1 not listed | **Low.** Only Aljuboori is omitted (PGY-2 in 2014-15, grad 2020); the complement is 1. |
| 2014-15 | **CC 2014-12-21** (phase 2) | Observed (7) | None. The Dec capture corrects Nazar from PGY-3 (Oct) to PGY-4. |
| 2015-16 .. 2022-23 | Wayback | Observed | None. |
| 2023-24 | Wayback 2024-06-14 plus manual supplement | Observed (10) plus 3 reconstructed | **Low.** The only version omits the PGY-1s and the PGY-6. Added: Leavitt and Walek at PGY-1 (complement 2; PGY-2 in Jan 2025; Leavitt's NPI Apr 2023), and Raja Jani at PGY-6 (Rutgers PGY-5 2022-23, Louisville affiliation from Feb 2023, PGY-7 2024-25). Common Crawl 2023-24 has no roster capture. The only open point is Pearson's exact exit date (see below). |
| 2024-25 .. 2026-27 | Wayback / live | Observed | None. |

Program length by entry cohort: 6 years through the 2012 cohort, 7 years from 2013 (`terminal_pgy_by_entry_year` in the JSON).

## Departures (training_history rows, phase 2)
- **Pola Chojecka** (th 3189): PGY-1 in Oct 2010. She probably left by Jul 2011, since Mansfield took the 2010-cohort slot. PubMed places her in Yale's Department of Neurology (2020-21). **Switched to neurology.** Pre-window.
- **Ryan Nazar** (th 3190): entered 2012 at PGY-2 (UK MD). Last seen PGY-5 in May 2016; not an alumnus. His 2022 affiliation is Norton Healthcare care management. **Did not complete; destination unknown.**
- **Jeffrey M. Rice** (th 3191): joined at PGY-4 in 2017-18 and was gone by Mar 2018. He trained earlier at the **University of Arizona Tucson** neurosurgery program (2014 paper; NPI enumerated Jul 2010). Later outcome unknown. *Lead for program 72: he is probably Arizona's unseen 2010 entrant.*
- **Muhammad Kandel / Abolfotoh** (th 3192): joined at PGY-3 in 2016 and left in 2020. He was a **UF Jacksonville Complex/MIS spine fellow in 2021-22**, then **SLU (60)** PGY-6 in 2023-24, graduating in 2025. **Transferred.**
- **Hyunchul Lee** (th 3193): PGY-3 in 2020-21, then gone. His UofL neurosurgery research affiliation continues to 2024. **Unknown.**
- **Luke Pearson** (th 3194): PGY-5 in 2022-23. He was dropped by the early-2023-24 page edit, so he most likely left in Jun 2023. He was a UF Jacksonville spine fellow from Jun 2024 to Dec 2025 (UFJ showed no fellows through Feb 2024), then **UMKC (95) PGY-4 in 2026-27.** Recorded as **transferred** (re-entry), end_year 2023.
- **Enzo Fortuny Viacava** (th 3195): PGY-3 in both 2022-23 and 2023-24, absent Jan 2025. His UofL research affiliations continue to 2025. **Unknown.**
- **Lydia Leavitt** (th 3196): PGY-2 in 2024-25, then gone. Her own NPI (enumerated Apr 2023) moved to a Salt Lake City trainee record in Jul 2025. She is not in Utah neurosurgery. **Unknown** (the NPI "switch" came from a namesake).

## Joiners
Mansfield (PGY-2 2011-12, hidden by the gap), Nazar (PGY-2 2012-13), Kandel (PGY-3 2016-17), Rice (PGY-4 2017-18), and **Raja Jani** (transfer from Rutgers in 2023 at PGY-6: th 3197; graduated 2025, PGY-terminal roster: th 3198).

## Not a Louisville resident
**Heegook Yeo** is a UofL MD. His NPI dates from 2018, when he was a student with a Louisville address. He was never on a Louisville neurosurgery roster: the Oct 2018, Jan 2020 and Sep 2020 rosters are complete, interns included. He was Henry Ford's 2020 intern, so there was no transfer.

## Other training_history rows
PGY-terminal graduations: Jani 2025, Dang 2026, Oxford 2026 (th 3198-3200). The alumni page has not been updated since 2024.

## Adjudication (after phase 2)
18 completed, 12 in training, 5 left and did not complete (Nazar, Rice, Lee, Fortuny Viacava, Leavitt), and 2 transferred (Kandel to SLU, Pearson to UMKC).

## Phase 2 searches
Phase 1's CC files were re-parsed; the 2013-14 didactics PDF has no names. CDX of every roster, graduates and news page version. gapaudit of the department for 2023-24, and of the GME and news hosts for 2011-14. Common Crawl 2023-2024 (15 crawls, none failed). PubMed affiliation mining for 2010-15 found no unlisted residents. Per-person PubMed, OpenAlex and NPPES. UF Jacksonville fellowship pages. UofL live directory. Cross-program rosters 24, 57, 60, 72, 95 and 111.
