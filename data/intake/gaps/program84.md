# Program 84: University of Illinois College of Medicine at Peoria (OSF Saint Francis / Illinois Neurological Institute)

- Length: 7 years now. Classes that entered through 2011 finished at PGY-6. Complement: about 2 per year, with only 1 in some years.
- Roster file: `data/intake/rosters_program84.json`. Scratch files: `data/raw/extraction/p84/` (`parse84.py`, `dir84.py`, `build84.py`, `txt/`, `cc/`).
- Residents entering 2011 or later: 26.

## Hosts
| Host / path | From | To |
|---|---|---|
| peoria.medicine.uic.edu/departments___programs/GME/residencies/NeurosurgeryRes/Residents/ (+ /Alumni/, bio pages whose left nav lists the full roster) | 2010-07 (2009-10 content) | 2017-03 |
| peoria.medicine.uic.edu/departments___programs/neurosurgery/ (department home; its residency link redirects to the GME path) | 2009 | 2014 |
| peoria.medicine.uic.edu/departments/neurosurgery/neurosurgery-residency/residents/ (WordPress) | 2017-09 | 2023-03 (301 by 2024-07) |
| Common Crawl CC-MAIN-2020-10 copy of that residents page | 2020-02-25 | |
| peoria.medicine.uic.edu/depts/academic/neurosurgery/directory/ ("Resident (Class of YYYY)") | 2024-03 | live 2026-09-27 |
| peoria.medicine.uic.edu/depts/academic/neurosurgery/residency/ (overview only, no names) | 2023-10 | live |
| osfhealthcare.org neurosciences residencies/fellowships pages | checked | no names |

## Years
- **Observed:** 2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18, 2019-20 (Common Crawl), 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27 (live, advanced).
- **Missing:** 2011-12 (no capture on any host between 2010-07 and 2013-02, nothing in Common Crawl). Phase 2 significance: low (see below).
- **Reconstructed:** 2018-19 now holds 10 residents: the 8 bracketed plus the 2018 interns Ivankovic and Sommer (Class of 2025). Villar is not hidden here, because he graduated in June 2018.
- **Incomplete-risk years:**
  - 2012-13: no PGY-1 is listed. There may have been no intern that year: Villar did his internship at UF.
  - 2015-16: the only source is the bio-page nav from 2016-05, and Ramanathan's PGY label did not advance.
  - 2020-21: the only capture is from 2021-04.

## Departures (left before terminal PGY)
- **Dinesh Ramanathan.** Last seen 2015-16 as PGY-3 (label repeated from 2014-15). Absent from 2016-17 while his classmate Villar continued. He had joined at PGY-2 in 2013-14.
- **Fahkry (Bavly) Dawoud.** PGY-1 in 2021-22 (Oct 2021 and May 2022 captures), absent in Dec 2022. His Class of 2028 slot was then held by Lara-Reyna.
- **Chris Villar (unresolved).** PGY-6 in 2017-18, then hidden by the 2018-19 gap and absent in Feb 2020. He probably graduated in June 2019.
- **Not attrition (6-year era graduates):** William Lee (2014), Vasilakis and Vachhani (2015), Issawi (2016), Martinez (2017). The adjudicator flags them LEFT because it assumes 7 years.

## Joiners (above PGY-1, with a prior-year roster that lacks them)
- Chris Villar: PGY-2 in 2013-14 (his bio says he did his intern year at UF Jacksonville).
- Dinesh Ramanathan: PGY-2 in 2013-14.
- Jacques Lara-Reyna: PGY-2 in 2022-23. He is not on the 2021-22 roster and replaces Dawoud.
- Tejas Sardar: PGY-2 in 2024-25 (Class of 2030). He is not on the Mar or Jun 2024 directory.

## Alumni
- The archived alumni page (last capture 2014-02-17) lists graduates up to 2013.
- The only 2012+ graduates on it are David Neils and Sadashiva Karanth (2013). Both were inserted into `training_history`.

## Adjudication
- 13 COMPLETED, 11 IN TRAINING, 8 LEFT.
- Of the 8 LEFT, only Ramanathan and Dawoud are real unexplained departures. Villar is unresolved, and the other 5 are 6-year graduates.

## Problems
- Program length changed from 6 to 7 years around the 2012-13 entry classes. The first PGY-7s seen are Johnson and MacMahon in 2019-20.
- Stephanie Salovesh's photo files are named "Menezes" (name change).
- Common Crawl finished all crawls from 2011 to 2020. Four index range requests failed (2016-07, 2017-39, 2018-51, 2020-29); retrying them returned 0 records.

## Phase 2 (2026-09-28)
**Program length by cohort:** entrants through **2012** finished at PGY-6, and entrants from 2013 finish at PGY-7 (`terminal_pgy_by_entry_year` in the JSON). Villar entered in 2012 (intern year at UF). He was PGY-6 in Jan 2018. NPPES 1366700361 (Christopher F. Villar MD, neurosurgery, mailing address OSF St Francis Peoria) was updated on 2018-07-25 with a Pensacola FL practice, so he graduated in June 2018.

| Year | Status | Significance | Why |
|---|---|---|---|
| 2011-12 | missing | low | Bracketed by the 2009-10 list and Feb 2013. Everyone except the 2010 graduate Rammos reappears. The 2010 and 2011 classes each show one entrant. Only a short-stay 2010/2011 entrant could be missed. |
| 2012-13 | observed | low | No PGY-1 is listed because the 2012 class joined at PGY-2 after outside internships (Villar at UF, Ramanathan at UW Seattle). |
| 2015-16 | observed | low | Bio-page nav lists all 9 and is bracketed. |
| 2018-19 | reconstructed | low | 10 residents: 8 bracketed plus Ivankovic and Sommer. The classes are full. |
| 2020-21 | observed | low | Spring capture only, but consistent with the years around it. |
| all other years | observed | none | |

**Outcomes recorded in training_history (10 rows):**
- COMPLETED at PGY-6: Lee 2014, Vasilakis 2015, Vachhani 2015, Issawi 2016, Martinez 2017, Villar 2018.
- Ramanathan: transferred out in 2016. He was at Peoria from 2013 (PGY-2) to 2016 (PGY-3). For 2016-19, UC Davis Dept of Neurological Surgery appears as his affiliation on 2018-19 PubMed papers (PMIDs 30459890, 31192094, 31393221). This was a non-resident post: he is not on the UCD residents roster or site. He joined Loma Linda (31) in 2019-20 at effective PGY-4 and graduated from LL in 2023.
- Dawoud: left after PGY-1 in 2022, destination unknown. NPPES lists diagnostic radiology in TN, but no program page confirms it: he is not on the Vanderbilt DR residents page in any capture from 2022 to 2026.
- Joiners: Lara-Reyna (PGY-2 in 2022-23; did neurosurgery research at Mount Sinai 2020-22) and Sardar (PGY-2 in 2024-25; NPPES trainee record in Peoria since 2023-03).

**Adjudication after phase 2:** 19 COMPLETED, 11 IN TRAINING, 1 TRANSFERRED (Ramanathan), 1 did not complete (Dawoud).

**Searched:** full-host gapaudit for both gap windows; full-host CDX grep for 2017-20; linkaudit; UICOMP press-release PDFs and news; Common Crawl (all crawls 2011-20 were done with the new filter in phase 1, and the failed ranges were retried with 0 records); PubMed "Peoria" neurosurgery affiliations for 2010-13 and 2017-20; PubMed and NPPES checks on each departing or joining resident; the UC Davis site; the Vanderbilt DR roster.

**Remaining (low):** the 2011-12 and 2018-19 rosters were never archived; Dawoud's destination; where Ramanathan was in 2016-17.
