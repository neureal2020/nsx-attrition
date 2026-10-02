# Program 12: Cleveland Clinic Foundation Program (Cleveland, OH)

7-year program, 3 per year (4 interns in 2019, 2025, 2026). Roster: `data/intake/rosters_program12.json`; parser and scratch: `data/raw/extraction/p12/` (p12parse.py, build.py, cclocal_p12.py).

## Hosts / paths
- my.clevelandclinic.org/neurological_institute/education/neurosurgeryfellows.aspx ("Current Residents"; parent neurological_institute/education/neurosurgery/*.aspx): 2009-03 to 2013-05
- my.clevelandclinic.org/neurological_institute/for-medical-professionals/residencies/neurosurgery-residency.aspx: 2013-12 to 2014-07
- my.clevelandclinic.org/services/neurological_institute/education/residencies/neurosurgery-residency: 2014-11 to 2017-01 (301 by 2017-06)
- my.clevelandclinic.org/departments/neurological/medical-professionals/residencies/neurosurgery (Current Residents tab; live): 2017-02 to 2026-09-27
- www.clevelandclinic.org/education/gme/ (old GME host; program links only, no rosters): 2009 to 2010
- portals.clevelandclinic.org/gme/ (GME portal; training-program directory only, no rosters): 2011 to 2018
- my.clevelandclinic.org/departments/neurological/medical-professionals/alumni (and older neurological_institute alumni.aspx paths) - alumni association page, no graduate list: 2011 to live

## Years
- Observed: 2012-2013, 2013-2014, 2014-2015, 2015-2016, 2016-2017, 2017-2018, 2018-2019, 2019-2020, 2020-2021, 2021-2022, 2022-2023, 2023-2024, 2024-2025, 2025-2026, 2026-2027
- Reconstructed: 2011-12 (partial, 9 bracketed people)
- Missing: none fully missing; 2021-22 observed but incomplete (no PGY-1 group)

## Gap details
- **2011-2012**: SIGNIFICANT. No capture of any roster page between 2009-03-30 and 2013-02-27 (Wayback exact + prefix audits of my.clevelandclinic.org/neurological_institute 2011-06..2013-12; GME hosts; Common Crawl 2011-2013: CC-MAIN-2012 has no CDXJ index, 2013 crawls only 2012-13 content). Reconstructed only the 9 people listed both in 2008-09 (Wayback 20090330083704) and 2012-13: PGY-4 Kelly/Kshettry/Rosenbaum, PGY-5 A. Khalil/Lobo/Vadera, PGY-6 Hughes/Liu/Matheus. PGY-1..3 (2009-2011 entrants) and PGY-7 (2005 entrants) unknown. The 2009 class shows only 2 residents (Brennan, Torre-Healy) in 2012-13, so a 2009 entrant may have left before 2012-13 unseen.
- **2012-2013**: Only captures are Feb and May 2013 (identical); Feb 2013 used. Complete (20 names).
- **2014-2015 / 2015-2016**: Nov 2014 content stayed on the page until Nov 2015 (stale); 2015-16 taken from Dec 2015 capture.
- **2017-2018**: No Wayback captures Mar 2017 - Jul 2019. Observed from Common Crawl CC-MAIN-2017-51 (2017-12-17), complete; confirmed by CC-MAIN-2018-13/22/30.
- **2018-2019**: Wayback 2019-07-18 capture content-dated to 2018-19 (interns Achey/Barnett/Sharma); identical to Common Crawl 2018-09-22, 2018-11-15, 2019-01-23.
- **2021-2022**: (phase 1; CLOSED in phase 2, see below) observed but INCOMPLETE. All captures (Wayback/CC Sep 2021, Jan 2022, May 2022) lack a 'Year One' group; 2021 entrants (Glauser, Nelson, Trivedi, seen as PGY-2 in 2022-23) are missing. Not reconstructed (not bracketed).
- **2022-2023**: Sep/Nov 2022 captures list only Glauser at PGY-2; Feb 2023 capture (used) adds Nelson and Trivedi.
- **2024-2025**: Nov 2024 capture lists 2 interns; Feb 2025 capture (used) adds Colin Lamb (possible mid-year start).
- **2020-2021**: Aug 2020 capture still showed 2019-20; Oct 2020 lists 2 interns; Jan 2021 (used) lists 3.

## Departures (left roster before PGY-7)
- Muhammad Z. Memon: last 2012-2013 PGY-2 (absent from 2013-14 roster onward)
- Sara Bourne: last 2013-2014 PGY-1 (absent from 2014-15 onward)
- Adam Khalil: last 2015-2016 PGY-2 (absent from 2016-17 onward)
- Austin Barnett: last 2018-2019 PGY-1 (absent from 2019-20 onward)
- Charlie Nelson: last 2023-2024 PGY-3 (absent from 2024-25 onward (Nov 2024 and later))
- Colin Lamb: last 2024-2025 PGY-1 (first listed Feb 2025, absent from 2025-26 onward)

## Joiners
- Louis Ross: first 2013-2014 PGY-2 (4th PGY-2; not on 2012-13 intern list. PGY-5 in 2016-17 then PGY-7 in 2017-18 (skipped PGY-6; finished with 2011 class))
- Vikram Chakravarthy: first 2017-2018 PGY-4 (not on 2016-17 PGY-3 list (Grabowski, Otvos only); fills slot left by Adam Khalil)
- Colin Lamb: first 2024-2025 PGY-1 (absent in Nov 2024 capture, listed Feb 2025)

## Adjudication
40 completed, 21 in training, 4 left -> switched specialty (NPI-based, unverified), 2 left -> unknown. Residents entering 2011+: 53.

## Problems
Common Crawl crawls that failed (range/size errors) and should be retried in phase 2: CC-MAIN-2012 (no cluster.idx - old format), CC-MAIN-2017-43, CC-MAIN-2019-13, CC-MAIN-2021-25. No program-side graduates list exists, so no training_history rows were inserted. Name variants canonicalised: Rupa Gopalan -> Rupa Gopalan Juthani; Elizabeth Bennett (2015-16+) -> Elizabeth Abbott (same MCW graduate, same class slot). Cleveland Clinic Florida's separate neurosurgery residency (my.clevelandclinic.org/florida/...) is NOT this program.

## Phase 2 (2026-09-28)
Year status / significance:
- 2011-12: reconstructed (PGY4-6 only), significance LOW: the 2010 and 2011 classes are complete (3 each) in Feb 2013, so no 2011+ entrant could leave unseen; only the 2009 class (2 of 3 seen) and 2012 graduates remain unobservable. Wayback gapaudit 2010-06..2013-02 (6 hosts) and CC-MAIN-2012 (now queryable, 46 records under neurological_institute/) found no roster page.
- 2021-22: now observed and COMPLETE. Year One = Gregory Glauser, Remi Kessler, Charlie Nelson (written "Name, PGY 1", missed in phase 1).
- 2015-16..2020-21: William Kemp, III, MD added (Year Two 2015-16 -> Year Seven 2020-21; gen-surg intern at Beaumont; dropped by the phase-1 parser because of "III").
- All other years observed, significance none. CC retries: 2017-43 and 2021-25 had 0 records; 2019-13 identical to 2018-19.

Outcomes recorded in training_history (11 rows, program 12):
- Transfers: Sara Bourne -> MGH 2014 (Sarah Bick); Vikram Chakravarthy <- Loma Linda PGY-4 2017 (completed 2021).
- Joiners: Louis Ross PGY-2 2013 (probably from CC general surgery; completed 2018), William Kemp PGY-2 2015 (completed 2021), Megh Trivedi PGY-2 mid-2022-23 (from CC pediatrics/research; in training).
- Specialty switches (publication affiliations, not NPI): Memon -> neurology (after 2012-13 PGY2), Adam Khalil -> radiology/IR (after 2015-16 PGY2), Austin Barnett -> emergency medicine (after 2018-19 PGY1), Remi Kessler -> probably anesthesiology (after 2021-22 PGY1; MUSC 2023 + NPPES).
- Unknown: Charlie Nelson (after 2023-24 PGY3), Colin Lamb (Feb-Jul 2025 PGY1).

Adjudication after reload: 41 completed, 21 in training, 4 switched, 1 transferred, 2 did not complete (unknown). Residents entering 2011+: 55.
Scratch: data/raw/extraction/p12/phase2/ (ccp12.py, cc/, gapaudit_2010_2013.txt, wbyears.py, au.py, oa*.py; phase-1 backups *.phase1.bak.*).
