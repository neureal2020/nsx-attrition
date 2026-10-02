# Program 83: University of Illinois College of Medicine at Chicago Program (Chicago, IL)

7-year program, complement 2/yr (1 intern in 2013, 2016, 2020, 2022, 2023; 3 in 2021 and 2025). Roster: `data/intake/rosters_program83.json`; scratch/parsers: `data/raw/extraction/p83/` (build.py, nameyear.py, classof.py, booklet PDFs/texts, cc/, cc2/). Not mixed with UIC Peoria (program 84).

## Hosts / paths
- chicago.medicine.uic.edu/departments___programs/departments/neurosurgery/ (old CMS; residency page had no resident list 2011-13; medical_education/residency/current_residents/ roster from 2014-02): 2008-08 to 2017-06 (roster page last 2016-10)
- chicago.medicine.uic.edu/UserFiles/Servers/Server_442934/File/Neurosurgery_Chicago/Documents/ (residency booklets UIC_Residency_2010.pdf, Residency_Booklet_12.pdf, Residency_Booklet_2015.pdf with 'Current Residents' lists; Residency_Booklet_13.pdf linked but never archived): 2010 to 2015
- chicago.medicine.uic.edu/departments/academic-departments/neurosurgery/medical-education/residency/current-residents/ (+ previous-graduates/, current-recent-fellowship-graduates/): 2017-08 to 2024-03 (content frozen at 2022-23 from Dec 2022)
- chicago.medicine.uic.edu/neurosurgery/people/residents/ (+ /page/2/; WordPress wp-json/wp/v2/profile API; live): 2024-03 to 2026-09-27
- medicine.uic.edu/departments/neurosurgery, neurosurgery.uic.edu (no captures; neurosurgery.uic.edu does not resolve): None to None

## Years
- Observed: 2012-2013, 2013-2014, 2014-2015, 2015-2016, 2016-2017, 2017-2018, 2018-2019, 2019-2020, 2020-2021, 2021-2022, 2022-2023, 2023-2024, 2024-2025, 2025-2026
- Reconstructed: 2011-2012 (significance LOW after phase 2)
- Missing: 2026-2027 (SIGNIFICANT: stale live site)
- 2023-2024: observed, significance LOW after phase 2

## Gap / capture details
- **2011-2012**: SIGNIFICANT. No 2011-12 roster anywhere: the old CMS had no resident page before Feb 2014 (full prefix listing of departments___programs/departments/neurosurgery), the residency page only linked a booklet (UIC_Residency_2010.pdf = 2010-11 list; Residency_Booklet_12.pdf = 2012-13 list). Reconstructed the 6 people listed in both 2010-11 and 2012-13 (Munson PGY6, Hage/Hari Krishna PGY4, Ivanov PGY3, Birk/Oh PGY2) plus Arnone/Khan PGY1 (PGY2 in 2012-13, alumni page graduation 2018). Sebastian Herrera (2010-11 booklet only, probably PGY6 then) not reconstructed; his completion is unconfirmed. 2010-11 booklet shows no PGY4 (2007 class empty) and 2012-13 no PGY6 - consistent. Common Crawl (cclocal, one pass): 2011-2013 on departments___programs/.../neurosurgery found only alumni pages (captures 2013-05, 2013-12), no roster; CC-MAIN-2012 and CC-MAIN-2013-20 FAILED in phase 1 (retried OK in phase 2). 2023-2024 on new-site people/ and old-site medical-education/residency found only the same frozen 2022-23 old-site page and 2024-05+ new-site pages already in Wayback; CC-MAIN-2023-06 and CC-MAIN-2024-42 failed in phase 1 (retried OK in phase 2).
- **2012-2013**: Residency_Booklet_12.pdf (PDF created 2012-11-20, Wayback 2014-12-29). 'Chief' = PGY7 (Munson). Complete (10 names, consistent with neighbours).
- **2013-2014**: Only capture of the roster in 2013-14 is Feb 2014 (first capture of current_residents page). Residency_Booklet_13.pdf never archived. Only one PGY1 (Dash).
- **2018-2019**: Captured July 2019, but page heading '(2018-2019)' and modified 2018-10-23; content is 2018-19.
- **2020-2021**: Page heading still '(2019-2020)', but PGYs advanced and 2020 intern (Pierce) added: content is 2020-21 (Oct 2020 - May 2021 captures identical).
- **2021-2022**: Sept 2021 capture had new interns but un-advanced PGYs; used Jan 2022 capture.
- **2023-2024**: Moderately significant: old-site page frozen at 2022-23 content (Dec 2022 - Mar 2024); new site's first capture is Apr 2024 (spring). A 2023-24 departure before April 2024 would be unseen. Peter Theiss (PGY6 in 2022-23) is not on the residents list; his new-site profile (Sept 2024 capture, wp-json) says 'Fellow, Endovascular Neurosurgery Fellowship', category class-of-2025. 2024 'Class of' labels for Khalid/Patel (2027) and Marotta (2028) are one year early relative to their entry years and were corrected to 2028/2029 in Jan 2025; PGYs computed from entry year.
- **2024-2025**: Oct 2024 capture still the unchanged Apr 2024 list; used Jan 2025 (page 1) + Apr 2025 page 2 (Tiefenbach) as a separate 'other' entry, plus Theiss profile as 'other' (pgy null).
- **2025-2026**: Page 1 Jan 2026 (identical Sept 2025 and May 2026). Page 2 never archived in 2025-26; used the live page 2 (unchanged, fetched 2026-09-27; Rios Zermeno profile created 2025-08-21) as an 'other' entry.
- **2026-2027**: SIGNIFICANT. Live page (fetched 2026-09-27) is identical to the 2025-26 roster: Peng/Souter (Class of 2026) still listed, no Class of 2033 interns, no profile created after 2025-10-30 in wp-json. Not loaded as 2026-27.

## Alumni page
https://chicago.medicine.uic.edu/departments/academic-departments/neurosurgery/medical-education/residency/previous-graduates/ (archived 2020-08..2023-12; not on the live site). Graduates 2016-2022 inserted into training_history (11 rows): Ivanov 2016; Oh, Birk 2017; Arnone, Khan 2018; Barks, Esfahani 2019; Behbahani, Chaudhry 2021 (page says 2020, see problems); Kwasnicki, Stone McGuire 2022. No 2012-2015 graduates listed.

## Departures (left roster before PGY-7)
- Debadutta Dash: last seen 2014-2015 PGY-2. SWITCHED to emergency medicine (PubMed: Stanford Dept of Emergency Medicine 2023-26; NPPES EM + clinical informatics).
- Justin Scheer: last seen 2017-2018 PGY-2. TRANSFERRED to UCSF (program 76), PGY3 2018-19, UCSF alumni 2023.
- Charles Pierce: last seen 2020-2021 PGY-1. sole 2020 intern; absent from Sept 2021 and Jan 2022 rosters. Destination unknown (2022 neuroradiology review with UIC hospital address hints at radiology; unconfirmed).
- Peter Theiss: NOT attrition. Dropped from residents list 2023-24 because re-categorised as in-program endovascular fellow (profile created 2024-01-02, 'Year: PGY-6', class-of-2025); UIC affiliation continuous 2019-2026. Expected completion 2025, not directly confirmed.

## Joiners (above PGY-1)
- Nauman Chaudhry: first seen 2015-2016 PGY-2 (2014-15 roster exists and lacks him)

## Consistency
Every person has one entry year across observations. Entry classes: 2006 Munson; 2008 Hage, Hari Krishna; 2009 Ivanov; 2010 Birk, Oh; 2011 Arnone, Khan; 2012 Barks, Esfahani; 2013 Dash; 2014 Behbahani (+Chaudhry joined PGY-2 2015); 2015 Kwasnicki, Stone McGuire; 2016 Scheer; 2017 Almadidy, Theiss; 2018 Bram, Sadeh; 2019 Peng, Souter; 2020 Pierce; 2021 Khalid, Patel, Brunozzi; 2022 Marotta; 2023 Gonzales-Portillo; 2024 Kurker, Tiefenbach; 2025 Madapoosi, Abou Mrad, Rios Zermeno. Residents entering 2011+: 27.

## Adjudication summary
{"COMPLETED": 17, "IN TRAINING": 12, "LEFT -> outcome unknown": 3, "LEFT -> SWITCHED SPECIALTY": 1, "note": "LEFT unknown = Scheer, Pierce, Theiss (Theiss probably extended as in-program fellow); Dash switched-specialty from NPI, unverified. Pre-2011 entrants included: Munson, Hage, Hari Krishna, Ivanov, Birk, Oh."}

## Problems
Behbahani/Chaudhry listed under 2020 on the alumni page but rosters show them PGY-7 through May 2021 (inserted training_history end_year 2021). 2024 new-site 'Class of' labels wrong for 3 residents (fixed 2025). Theiss status 2023-25 ambiguous. Herrera (2010-11) outcome unknown. Common Crawl (cclocal, one pass): 2011-2013 on departments___programs/.../neurosurgery found only alumni pages (captures 2013-05, 2013-12), no roster; CC-MAIN-2012 and CC-MAIN-2013-20 FAILED in phase 1 (retried OK in phase 2). 2023-2024 on new-site people/ and old-site medical-education/residency found only the same frozen 2022-23 old-site page and 2024-05+ new-site pages already in Wayback; CC-MAIN-2023-06 and CC-MAIN-2024-42 failed in phase 1 (retried OK in phase 2).

## Phase 2 (2026-09-28)
Per-year significance: 2011-12 reconstructed/LOW; 2012-13..2025-26 observed/none except 2023-24 LOW; 2026-27 missing/SIGNIFICANT.

- **2011-12 -> LOW.** Retried CC-MAIN-2012 (now readable: dept home + 3 faculty pages) and CC-MAIN-2013-20 (alumni page only); booklet folder empty in CC-MAIN-2013-20/2013-48. Wayback prefix listing of the booklet folder: no 2011 or 2013 booklet. PubMed 2011-13 UIC neurosurgery affiliations: no unknown resident. Bracketing: every 2010-11 booklet name except graduating chief Chan and Herrera reappears in 2012-13; the 2011 class (Arnone, Khan) fills the complement of 2 and both graduated 2018. Only Herrera (probably 2005 class, PGY7 2011-12, graduating 2012; NPPES neurological surgery TX) is unconfirmed; he is a pre-2011 entrant.
- **2023-24 -> LOW.** wp-json resident profiles created 2023-12-20/2024-01-02 match the Apr 2024 roster exactly; Theiss added as a 2023-24 'other' entry (in-program endovascular fellow). CC-MAIN-2023-06 and CC-MAIN-2024-42 retried OK: no new roster (2024-10-12 residents page = Apr 2024 list). Only a 2023 intern leaving Jul-Dec 2023 could be unseen.
- **2026-27 remains SIGNIFICANT.** Live page and wp-json unchanged on 2026-09-28 (newest resident profile 2025-08-21); no posts; Wayback 2026 captures identical.
- **training_history rows added (11, notes prefixed '[phase2 p83]'):** Scheer transfer out (83, end 2018) + transfer in (76, PGY3 2018-19); Dash switched specialty (end 2015); Pierce left, departure_type unknown (end 2021); Theiss completed='unknown' (expected 2025); PGY-terminal roster completions Munson 2013, Hage 2015, Hari Krishna 2015, Almadidy 2024, Bram 2025, Sadeh 2025.
- **Not a UIC resident:** Ravi Nunna (Rush, program 56) appears in UIC neurosurgery affiliations 2020-22 as a research fellow.
- Adjudication after reload: COMPLETED 17, IN TRAINING 12, SWITCHED 1 (Dash), TRANSFERRED 1 (Scheer), did not complete 1 (Pierce), outcome unknown 1 (Theiss: not attrition).
- Remaining: 2026-27; Herrera; Pierce destination; Theiss completion; Chaudhry's origin (not in any loaded roster).
- Files: data/raw/extraction/p83/phase2/ (cc/, cc.log, ccrun.py, pubmed_*.txt, gapaudit_*.txt, ns_prof.json, theiss_live.html, rosters_program83.phase1.json backup).
