# Program 54: Rhode Island Hospital / Brown University Health neurosurgery (Providence, RI)

7-year program. Complement was 1 per year for the entry classes of 2005-2013 (plus transfers). It has been 2 per year since about 2016, with 14 residents from 2022-23 on. Roster file: `data/intake/rosters_program54.json` (16 captures). JSON twin: `program54.json`.

## Hosts
| Host / path | Dates | Notes |
|---|---|---|
| www.brownneurosurgery.com/education/residents.asp | 2010-11 to 2012-04 | Names in seniority order, no PGYs. Content frozen at the Apr-2012 version until Mar-2018, then 301. |
| www.brownneurosurgery.com/residents/residents.asp | 2014-04 to 2018-04 | The /residents/ section was created around Sep-2012, but this page was first captured Apr-2014. PGY labels appear from Feb-2015. It kept the 2014-15 list until it was retired. |
| brownneurosurgery.com/our-team/residents/ (WordPress) | 2018-04 to 2025-10 | JS vc_grid. Names appear in the captured HTML only from Jul-2019. Showed stale 2024-25 content after the site moved. |
| brownneurosurgery.com/education/residency-program/current-residents-and-alumni/ | 2019-06 to 2024-05 | Roster with a year heading, plus the alumni list. |
| neurosurgery.med.brown.edu/people (Residents section), …/current-residents-alumni | 2025-11 to live | The live residency page lists only PGY3-7. The people directory is complete. |
| brown.edu/academics/medical/about/departments/neurosurgery | 2011-2019 | School directory page only. |
| rhodeislandhospital.org …/neurosurgery/residency-program*.html, lifespan.org/centers-services/neurosurgery/residency-program* | 2014-2023 | No names. |

## Years
- **Observed:** 2011-12, 2013-14 (both with PGYs inferred from list order and alumni graduation years), 2014-15, and 2018-19 through 2026-27.
- **Reconstructed (significant gaps):**
  - **2012-13:** No roster capture exists. The old page was frozen and the new page was not archived until Apr-2014.
  - **2015-16, 2016-17, 2017-18:** The residents page kept serving the 2014-15 list. Wayback digests and Common Crawl CC-MAIN-2017-22, 2017-30 and 2018-05 all show that list. The Apr-2018+ WordPress grid is unrendered in Wayback and in CC 2018.
  - Only people who are bracketed, or confirmed by the alumni list and seen later, were reconstructed. Xun Li, Morrison and Baker were **not** reconstructed.
- **Missing:** none.

## Alumni page
https://neurosurgery.med.brown.edu/education/residency-program/current-residents-alumni lists graduates from 1990 to 2024.
- There is no 2016 graduate.
- The 2025 graduates (Sastry, Ali) and 2026 graduates (Shao, Abdulrazeq) have not been added yet.
- 13 graduates from 2012-2024 were inserted into `training_history`.

## Departures (left before the terminal PGY)
- **Benjamin Jacobson:** Last seen 2010-11 at about PGY-2 (pre-window). He is on the May-2011 list but gone by Jul-2011, and not on the alumni list. Not loaded.
- **John Morrison:** Last seen 2014-15, labelled PGY-5. He transferred in in Jul-2011. He is absent in 2018-19 and not on the alumni list. The departure year (2015-2018) is hidden by the stale page.
- **Amanda Baker:** Last seen 2014-15 as PGY-1. She is absent in 2018-19 and not on the alumni list. Departure year 2015-2018 unknown.

## Joiners (above PGY-1)
- **John Morrison:** Joined 2011-12. He is absent from the May-2011 list. PGY unresolved: seniority order suggests PGY-3, while the 2014-15 label implies PGY-2.
- **Hael Abdulrazeq:** Joined 2020-21 as PGY-2. He is absent from all 2019-20 captures. Graduated 2026.
- **Santos E. Santos Fontanez:** Joined 2021-22 as PGY-2. His profile lists a prior residency at the University of Puerto Rico.
- **Xun Li:** First seen 2018-19 as PGY-5 (entry class 2014, graduated 2021). He was absent from the 2014-15 roster. Because 2015-18 was unobserved he cannot be strictly classified. His bio ("after more detours … arrived in Providence") points to a transfer in during 2015-2018.

## Counts and adjudication
- 33 residents were observed from 2011-12 on. 27 of them entered in 2011 or later.
- Adjudication: 17 COMPLETED, 14 IN TRAINING, 2 LEFT with outcome unknown (Morrison, Baker).

## Problems
- The CC-MAIN-2018-13 lookup failed for `com,brownneurosurgery)/`. Retry it in phase 2, though it probably won't help.
- The 2011-12 and 2013-14 PGYs are inferred.
- Morrison's PGY is inconsistent between the seniority order and the 2014-15 label.

## Phase 2 (2026-09-28)

### Year status
| Year | Status | Significance | Reason |
|---|---|---|---|
| 2011-12 | observed | none | PGYs inferred from order; Morrison now PGY-2 (from the printed 2014-15 PGY-5 label) |
| 2012-13 | reconstructed | low | 2011-12 and 2013-14 lists bracket everyone; 1/yr complement (Pucci = 2012 class); PubMed 2012-14 shows no unlisted resident |
| 2013-14, 2014-15 | observed | none | |
| 2015-16 | reconstructed | low | every 2014-15 resident accounted for (Aghion grad, Morrison at Brown to Feb-2016, Baker -> radiology); only a hidden second 2015 intern could be missed |
| 2016-17 | reconstructed | none | near-complete independent roster (see below) |
| 2017-18 | reconstructed | low | all Mar-2017 residents seen later or graduated; Match-week 2017 added only Shaaya |
| 2018-19 to 2026-27 | observed | none | |

### Key finding: the 2016-17 roster from the new WordPress site
The new site was built in Feb-May 2017 but went live only in Apr-2018. Its resident profile posts keep their creation dates (Yoast `datePublished`, post IDs, and `wp-content/uploads/2017/02-03` headshots):
Choi (2017-02-25), Torabi (02-25), Pucci (03-16), Moldovan (03-17), **Xun Li (03-18)**, Anderson (03-20), Poggi (03-21), and the incoming intern Shaaya (03-22, Match week).
Syed has no 2017 post, but PMID 28564664 (Jun-2017) calls him "Resident, Department of Neurosurgery, Alpert Medical School of Brown University".
Morrison and Baker have no posts.

### Outcomes recorded in training_history
- **John Morrison** (row 2908): transferred to Buffalo (69). His papers received in Feb-2016 still give Brown (PMID 27259283, 27213112), so he was PGY-6 in 2015-16 (added as a reconstructed row). He was at Buffalo as PGY-6 by Sep-2016 and graduated from Buffalo in 2018. He joined Brown in Jul-2011 at PGY-2; where he came from is unknown.
- **Amanda Baker** (row 2909): switched to radiology/neuroradiology at Brown. Her PubMed affiliations are Radiology (2018), Neuroradiology (2019) and Diagnostic Imaging RIH (2020). Her NPI 1790198125 carries both Neurological Surgery (RI limited licence LP03216, Jun-2014) and Neuroradiology (CA). She most likely left in 2015.
- **Xun Li** (row 2910): transfer in from UVM (112) during 2016-17, at PGY-3. Added as reconstructed rows for 2016-17 (PGY-3) and 2017-18 (PGY-4). Graduated 2021.
- **Hael Abdulrazeq** (row 2912): probable closure transfer from Wayne State/DMC (125). PMID 31406942, received May-2019, gives Wayne State Dept of Neurosurgery. The WSU 2019 intern class was never listed. He joined Brown at PGY-2 in 2020-21 and graduated in 2026 (PGY-terminal roster).
- **Santos E. Santos Fontanez** (row 2911): closure transfer from UPR (101) at PGY-2 in 2021-22. Still in training.
- PGY-terminal graduations: Sastry and Ali (2025, rows 2913-2914) and Shao (2026, row 2915).
- Adjudication: 17 COMPLETED, 14 IN TRAINING, 1 TRANSFERRED (Morrison), 1 SWITCHED SPECIALTY (Baker).

### Searched
- Wayback full-URL inventories of brownneurosurgery.com (2012-19) and of /our-team/ and /wp-content/uploads/ (2017-26).
- The old resident-news, residents/index and pgy7 pages (no new names).
- gapaudit over brown.edu, lifespan.org, rhodeislandhospital.org and npniri.org for 2012-18 (no rosters).
- linkaudit for 2015-18.
- The CC-MAIN-2018-13 retry succeeded: 24 records, no roster.
- PubMed affiliation mining for 2012-19 (557 PMIDs) found no unlisted resident.
- NPPES. OpenAlex was rate-limited.

### For other programs (not edited here)
- UVM (112) row 2801: Xun Li's end_year should be 2016.
- Wayne State (125): add Abdulrazeq as a 2019 intern who left at the closure.
