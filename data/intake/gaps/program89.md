# Program 89: University of Maryland Program (Baltimore, MD)

7-year program, 2 residents per year. Checked 2026-09-28.

## Hosts
| URL | From | To |
|---|---|---|
| neurosurgery.umaryland.edu/residents.asp (UMSOM dept ASP site, roster with a PGY per name) | 2007-07 | 2016-10. Not captured 2010-06 to 2014-11. The "~ 2014-2015" list stayed frozen 2014-11 to 2016-10, then 404 |
| neurosurgery.umaryland.edu/default.asp (Ektron homepage, no residents link) | 2012-09 | 2016-05 |
| neurosurgery.umaryland.edu/Neurosurgery-Residency-Program/Neurosurgery-Residents/ | 2017-03 | 2019-08 (updated late, about once a year) |
| www.umm.edu/neurosciences/residency_program.htm (description only) | 2008-05 | 2012-09 |
| umm.edu/programs/neurosciences/professionals/neurosurgery-residency (description only) | 2013-07 | 2017-12 |
| www.umms.org/ummc/pros/gme/residency/neurosurgery/current-residents | 2020-09 | 2023-02 |
| www.umms.org/ummc/pros/gme/residency/neurosurgery/residents (+ /bios, /alumni) | 2023-06 | live |
| medschool.umaryland.edu/neurosurgery/ (faculty bios only) | 2002 | 2008 |

## Years
- **Observed (12):** 2014-15, 2016-17 (Apr 2017 capture), 2017-18 (May 2018 capture), and 2018-19 through 2026-27 (2026-27 from the live page, which has advanced).
- **Reconstructed (significant gaps):**
  - **2011-12, 2012-13, 2013-14:** no residents.asp capture between 2010-06-12 and 2014-11-22. The years were rebuilt from the 2009-10 roster, the 2014-15 roster and the alumni page.
    - The 2009-10 roster was captured 2009-07-22 and 2010-06-12 (same content).
    - Tried: prefix CDX on neurosurgery.umaryland.edu, medschool.umaryland.edu/neurosurgery, umm.edu/neurosurgery, umm.edu/neurosciences, umm.edu/programs/neurosciences/professionals and umm.edu/professionals/gme; year-by-year filtered scans of medschool.umaryland.edu and umm.edu; the Ektron linkit redirects (all go to medschool pages); Common Crawl 2012-2016 (30 crawls, no roster URL, none failed).
  - **2015-16:** every capture from 2015-05 to 2017-03 still shows the "2014-2015" list. All 14 residents are bracketed by the 2014-15 and 2016-17 rosters.
- **Missing:** none. A resident who both joined and left within 2010-2014 could not be seen.

## Alumni
www.umms.org/ummc/pros/gme/residency/neurosurgery/alumni lists graduates up to 2024 and has no 2025 or 2026 entries. I inserted 25 graduates (2012-2024) into training_history.

## Departures
- **Abdul-Kareem Ahmed:** left before PGY-7, destination unknown. Last seen at PGY-6 in 2023-24 (class of 2025), on the bios page 2024-04-21. He is absent from every residents capture from 2024-07-13 on, and Olexa was the sole PGY-7 in 2024-25. His last UMSOM Neurosurgery PubMed affiliation is July 2024, and no later neurosurgery affiliation exists anywhere. His NPPES record has not been updated since 2018. training_history: completed=no, departure_type=unknown, end_year 2024.
- **Adam Hunt:** left after PGY-1 in 2025-26, destination unknown. He is absent from the live 2026-27 page, has no 2025+ PubMed affiliation, and is on no other program's roster. training_history: completed=no, departure_type=unknown.
- **Ryan Nowak (pre-window):** switched to radiation oncology. The UNMC "Meet the Residents" page (Wayback 2013-10-29) lists him as rad-onc PGY-4, so he left Maryland by June 2011 at the latest. That is outside the window, so he is not loaded.

## Joiners
- **Ujwal Boddeti:** transfer in at PGY-2 for 2026-27. The live bios page says he "completed his PGY-1 neurosurgery year at Upstate University Hospital" (SUNY Upstate, program 63, 2025-26). Program 63 has no 2025-26 roster, so the transfer out should also be recorded there. training_history row added.

## Graduations recorded from rosters
Olexa (2025), Shea and Stokum (2026) were PGY-7 on the final roster. The alumni page has no entries after 2024. These were recorded as PGY-terminal roster graduations.

## Phase 2 (2026-09-28)
Year status and significance are in the JSON under `years`.
- **2011-12 to 2013-14:** still reconstructed; significance **low**.
  - No roster exists. Searched: gapaudit over dept/UMMC/medschool/GME/news hosts 2010-16; link audit; Common Crawl 2011-16 on the UMMC and medschool neurosurgery paths (description page only); PubMed affiliation mining 2010-16 (no unlisted resident).
  - Transfer-in ruled out: NPPES enumeration dates match the inferred PGY-1 years for Hersh (2011-05), Hayman and Jones (2012-04), Kole and Mushlin (2013-04), and Lewis and Patel (2010).
  - Elizabeth Le has no NPPES record. She was a UMSOM MD and is in class 2018 with Hersh.
  - Every class held the complement of 2 on both bracketing rosters.
  - Residual risk: only an over-complement resident who entered and left inside the gap.
- **2015-16:** still reconstructed; significance **low**. The page was frozen. Everyone is bracketed by the adjacent rosters, and NPPES confirms 2015 entry for Cannarsa and Chryssikos.
- **Other checks:** crossmatch.json has no program 89 entries. OpenAlex was over its daily budget, so it was not used.
- **Adjudication after reload:** 28 completed, 14 in training, 2 left (Ahmed, Hunt).
