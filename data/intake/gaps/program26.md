# Program 26: Houston Methodist Hospital (Medical Center) Program (Houston, TX)

7-year program, 2 per year (complement 14). There were 3 interns in 2018, 2019, 2025 and 2026, and only 1 in 2021 and 2024. Roster: `data/intake/rosters_program26.json`. Parser and scratch files: `data/raw/extraction/p26/` (p26parse.py, build.py, cdxq.py, cc_a/, cc_b/, api_res.json, api_alu.json).

## Program start
The program pages give no start date. The 2010 page already describes a "seven-year residency program beginning in the PGY1 year". The earliest alumni class is 2013 (Krishna, Rangel-Castilla), so the first entry was about 2006. The program was active throughout 2011-2026, so `first_class_year` is null.

## Hosts / paths
- methodisthealth.com/tmhs/nineurosurgery.do?channelId=-98384...: program description only, 2010-01 to 2010-02
- methodisthealth.com/nineurosurgery.cfm?id=34950 (Residency Program): 2010-04 to 2013-06. By Jun 2013 it linked "Current Residents" = nineurosurgery.cfm?id=43099, which was **never archived**.
- houstonmethodist.org/current-residents-43099 ("Current Residents 2013-2014 / 2014-2015"): 2013-12 to 2015-03
- houstonmethodist.org/education/gme-postgraduate/graduate-medical-education/neurosurgery-residency/our-residents: 2015-07 to 2015-09
- houstonmethodist.org/1285_houstonmethodist/2623_education/2647_.../2685_education_neurosurgeryresidency/2689_education_ourresidents: 2015-10 to 2016-03
- same with `gme%20programs/` inserted: 2016-04 to 2016-11
- houstonmethodist.org/1285_houstonmethodist/2623_education/medical-education/graduatemedicaleducation/gme-programs/gme_neurosurgeryresidency/2689_education_ourresidents: 2017-02 to 2018-08
- houstonmethodist.org/education/medical/graduate-medical-education/neurosurgery-residency/our-residents/ (+ /alumni/): 2017-11 to 2024-10
- houstonmethodist.org/academic-institute/gme/neurosurgery-residency/ (Our Residents + Alumni with class years): 2024-11 to live. Server-rendered until about 2025-10. After that the lists load via JS from POST /api/faculty/directory/ (residents scope "fellow", alumni scope "alumni").
- houstonmethodist.org/neurosurgery-residency/ (vanity URL): 2021-12 to 2026-05, 404 live (it is the DB `programs.website`)

## Years
- Observed: 2013-14 (Common Crawl), 2014-15 through 2017-18, 2018-19 (Common Crawl), 2019-20 through 2025-26, 2026-27 (live)
- Reconstructed: 2011-12 (8 people), 2012-13 (10 people). Only alumni-confirmed graduates are included, with PGY back-projected from the 2013-14 roster.
- Missing: none fully, but 2011-12 and 2012-13 are still **significant** gaps after phase 2.

## Gap details
- **2011-12 / 2012-13**: SIGNIFICANT. No roster capture anywhere. Tried: Wayback exact/prefix/domain-regex CDX 2008-2016, gapaudit on both hosts 2011-07..2014-09, and Common Crawl 2012-2014 for id=43099 and current-residents (0 records). The reconstruction covers alumni graduates only. The 2007-2010 entry classes show just one resident each from 2013-14 on, so a second member of each class could have left unseen. The residents image folder held photos "Dilorenzo.jpg" and "Moisi.jpg" in Nov 2013, next to Krishna and Livingston. Those two surnames never appear on any archived roster or on the alumni list. **Phase 2:** those photos were uploaded on 9 Aug 2007, so they show 2007-08 residents. DiLorenzo left in 2010. Moisi left in 2011 or 2012 (see Departures). Neither is loaded.
- **2013-14**: Common Crawl CC-MAIN-2014-10 (2014-03-08) was used. The Dec 2013 crawl had the same list without the PGY-1s (Boghani, Steele).
- **2018-19**: No Wayback capture May 2018 to Jul 2019. Taken from CC-MAIN-2018-43 (2018-10-23), which is identical to the Dec 2018 and Feb 2019 crawls.
- **2020-21**: The Dec 2020 content stayed up until Nov 2021.
- **2021-22**: The only 2021-22 content is the May 2022 capture.
- **2022-23**: Amanda Jenson was still shown as PGY-7, but she is in the alumni Class of 2022. Stale entry, excluded.
- **2023-24**: The Sep 2023 capture lacks Ismail Mohiuddin. The Jun 2024 capture (used) lists him as PGY-1.
- **2025-26**: Sibi Rajendran is labelled PGY6 while his classmates are PGY7. The alumni API says he completed in 2026 at PGY-7.

## Departures (left before PGY-7)
- Chuan Liang: last seen 2014-15, PGY-1. Outcome unknown (NPPES hints radiology; NPI-only, not recorded as a switch).
- Ryan Jafrani: last seen 2016-17, PGY-3. **Transferred** to Penn State (53) at PGY-4 in July 2017, graduated 2021.
- Michael Ghali: last seen 2018-19, PGY-1 (Common Crawl roster only). Outcome unknown; he is on no other program's roster.
- Bradley Daniels: last seen 2021-22, PGY-5. Outcome unknown (NPPES hints anesthesiology in Dallas; NPI-only).
- Marc Moisi (not on any archived HM roster): HM resident (2007 photo; HM affiliation on a paper e-published Jul 2011). Then UTMB neurosurgery research fellow (~2012-14), Swedish fellowships 2014-16, Wayne State (125) Year 6 2016-17, graduated 2017. **Transfer**; he left HM in 2011 or 2012 (training_history end_year 2012, marked uncertain).
- Pre-window: Daniel DiLorenzo left HM for UTMB in 2010 (HM affiliation Jan 2010; the UTMB bio says "joined UTMB in 2010 for his senior and Chief years"), then Rush, graduated 2016. Nothing shows a return to HM in 2012-13.

## Joiners
None. Kadipasaoglu (UTHealth neurosurgery) joined the Houston Methodist **neurology** residency as a PGY-1 in 2021-22, which is a different department, so he is not a joiner here.

## Phase 2 (2026-09-28)
- **Photo dating:** the residents-folder photos (Dilorenzo, Moisi, Krishna, Livingston, TopNeurosurgeryResidents) carry an original Last-Modified date of 9 Aug 2007. They come from a 2007-08 residents page and are not evidence for 2011-13.
- **The id=43099 "Current Residents" page** was created around fall 2012, going by the CMS id sequence (ids about 42700 in Aug 2012 and about 44450 by Jun 2013). Neither Wayback nor Common Crawl ever captured it. The CC-MAIN-2013-20 and CC-MAIN-2014-10 retries found nineurosurgery.cfm pages but not id=43099.
- **Common Crawl retries:** CC-MAIN-2014-10 and CC-MAIN-2018-17 both succeeded. The 2018-17 capture (Apr 2018) matches the 2017-18 roster.
- **PubMed affiliation mining** (Methodist neurosurgery, 2008-2014, 145 PMIDs) found no residents that were not already known.
- **Still significant: 2011-12 and 2012-13.** No roster exists for either year. Anyone who left from the 2008-2010 entry classes would be invisible, and Moisi's presence in 2011-12 is unconfirmed.
- **training_history:** 6 rows added. Two are transfers (Jafrani, Moisi), one is a pre-window transfer (DiLorenzo), and three are unknown outcomes (Liang, Ghali, Daniels).

## Extended training
Virendra Desai was PGY-6 in both 2017-18 and 2018-19 and graduated in 2020 (the API shows "PGY-8").

## Adjudication
After phase 2: 22 completed, 14 in training, 3 did not complete (Liang, Ghali and Daniels; outcomes unknown) and 1 transferred (Jafrani, to Penn State). 34 residents entered 2011 or later. I inserted 22 alumni graduations (Class of 2013 to 2026) into training_history.

## Problems
The phase-1 Common Crawl failures (CC-MAIN-2014-10 and CC-MAIN-2018-17) were retried in phase 2 and both succeeded. Neither turned up a new roster.

CC-MAIN-2012 has no index. Names were canonicalised, for example John D./"Jd" Patterson → John Patterson and William J. Steele III → William Steele. Nancy Mize-Gonzalez (PGY-1 in 2026-27) has completion year 2032, one year earlier than the other interns' 2033.
