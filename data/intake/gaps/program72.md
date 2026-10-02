# Program 72: University of Arizona College of Medicine - Tucson Program (Tucson, AZ)

ACGME accredited 2003 (first residents 2004). Six-year program through the class of 2017 (Palejwala, entry 2011, graduated after PGY6); seven-year from the 2012 entrants on (Martirosyan, entry 2012, graduated 2019). One resident per year until 2024; two PGY-1s per year from 2025 (Brown and Hayat in 2025, Skelton and Wilson in 2026). Roster in DB: `data/intake/rosters_program72.json` (16 captures: 10 page captures, 1 live, 6 reconstructed; 109 observations). Alumni graduations 2012-2026 (13 rows) are in `training_history`.

## Hosts / paths
| URL | Dates | Roster? |
|---|---|---|
| www.surgery.arizona.edu/neurosurgery/residency (+ /alumni, /team/neurosurgery) | 2010-06 to 2011-08 | no (program text, faculty, alumni landing page only) |
| surgery.arizona.edu/residency/neurosurgery, /team/neurosurgery, /unit/division/neurosurgery | 2011-10 to 2016-07 | no (linked /residents/neurosurgery from 2012 onward) |
| surgery.arizona.edu/residents/neurosurgery (+ /current-residents/neurosurgery/<name> profiles) | 2014-10 to 2016-07 (404 from 2016-08) | yes (PGY headings) |
| surgery.arizona.edu/alumni/neurosurgery | 2014-10 to 2016-03 | alumni list |
| surgery.arizona.edu/education/residency-programs/neurosurgery/current-residents, /alumni | 2016-09 to 2018-10; 301 from 2018-11 (target never archived) | yes |
| neurosurgery.arizona.edu (Department of Neurosurgery site) | homepage 2019-12, 2020-10, 2021-03; /residency/current-residents and /residency/alumni 2021-10 to 2025-04 | yes |
| medicine.arizona.edu/neurosurgery/residency-program/current-and-past-residents (neurosurgery.arizona.edu/residency now 301s here) | 2025-08 to live | yes, plus alumni table |

## Years
- **Observed:** 2014-15 (Wayback 2014-10-12), 2015-16 (2015-11-30), 2016-17 (2016-10-08), 2018-19 (2018-10-16), 2021-22 (2021-10-27), 2022-23 (2023-01-28), 2023-24 (2024-06-23), 2024-25 (2024-09-07), 2025-26 (2025-10-14), 2026-27 (live page, fetched 2026-09-27/28; it has advanced from 2025-26).
- **Reconstructed:** 2011-12, 2012-13, 2013-14, 2017-18, 2019-20, 2020-21. These include only people confirmed by the alumni list or bracketed by observed years.
- **Missing:** none in full. After phase 2 only 2011-12 to 2013-14 remain significant (the 2010-entry class cannot be observed); 2017-18, 2019-20 and 2020-21 are low. See the phase 2 section at the end.

## Significant gaps
- **2011-12 to 2013-14.** No resident list was ever archived:
  - The 2010-11 site had no roster.
  - The Drupal site linked /residents/neurosurgery from 2012, but Wayback first captured it in 2014-10.
  - Common Crawl 2011-2014 returned nothing for surgery.arizona.edu/residents or /residency/neurosurgery.
  - A 2013-14 applicant slide deck (NS Residency Welcome '13-14.ppt) has no names.
  - Whitney Sheen James (PGY3 in 2014-15, never on the alumni list) could not be reconstructed under the rule.
  - **Class of 2010:** there was no PGY5 in 2014-15 and no 2016 graduate, so a 2010 entrant who left before 2014 would be invisible. The same applies to a 2007 entrant (no 2013 graduate).
- **2017-18.** The page was not updated all year. Wayback captures from 2017-09, 2017-10, 2018-07 and 2018-08, and Common Crawl captures from 2017-09, 2017-11 and 2018-01, all show the 2016-17 list. Whitney Sheen James's status in 2017-18 is therefore unknown.
- **2019-20 and 2020-21.**
  - From 2018-11, surgery.arizona.edu residency pages return a 301 whose target was never archived.
  - neurosurgery.arizona.edu has only homepage captures before 2021-05 (they link /residency/current-residents, which was not captured until 2021-10-27).
  - Common Crawl 2019-2021 has no current-residents page.
  - Not reconstructed: Ryan Palsma (PGY1 2020-21, still in training) and Andres Monserrate Marrero (arrival year unknown).
- **Incomplete observed year, handled:** the 2023-12-05 capture has no PGY-1 section. The 2024-06-23 capture (same people plus Farhadi PGY-1) was used for 2023-24 instead.
- **Stale captures skipped:**
  - 2015-08 to 2015-10 captures still show 2014-15.
  - The 2022-08-12 capture still shows 2021-22.

## PGY labels
"Chief Resident" is a heading that repeats someone listed elsewhere, so its PGY varies by year:
- PGY7: Brasiliense in 2021-22.
- PGY6: Palejwala (2016-17), Bina (2018-19), Burket (2022-23), Aguilar Salinas (2023-24), Joshi (2024-25) and Palsma (2025-26).
- PGY5: Sheldon in 2026-27.

Each person was assigned their own PGY from the neighbouring years.

## Consistency
- Every person has a single entry year across all observations.
- Class sizes by entry year:

  | Entry years | Residents per class |
  |---|---|
  | 2006, 2008 | 1 |
  | 2009 | 2 |
  | 2011 | 1 |
  | 2012 | 2 (Martirosyan, Sheen James) |
  | 2013-2016 | 1 |
  | 2017 | 2 (Burket, plus Monserrate Marrero, who joined later) |
  | 2018-2024 | 1 |
  | 2025, 2026 | 2 |

- No entrant is seen for 2007 or 2010.

## Departures (left before terminal PGY)
- **Whitney Sheen James** (entry 2012)
  - Last observed in 2016-17 at PGY5. The 2017-18 page was stale.
  - Absent in 2018-19, when her classmate Martirosyan was PGY7.
  - Not on any alumni list: 2019's only graduate is Martirosyan, and there is no 2018 graduate.
  - She left in 2017-18 or at its end.
  - NPPES: Whitney James, NPI 1144582248, Neurological Surgery taxonomy, Prescott AZ. Possibly the same person.
- **Andres Monserrate Marrero** (effective entry 2017)
  - PGY5 in 2021-22 and PGY6 in 2022-23.
  - Absent in 2023-24, when his classmate Burket was PGY7.
  - Not on the alumni list: 2024's only graduate is Burket.
  - He left at the end of 2022-23.
  - NPPES 1962852517: Neurological Surgery taxonomy, Guaynabo PR and Pittsburgh addresses, updated 2024-03. The adjudicator's "SWITCHED SPECIALTY" call looks doubtful, and phase 2 should check it.

## Joiners (above PGY1)
- **Andres Monserrate Marrero**
  - First seen in 2021-22 at PGY5.
  - He arrived sometime between 2019-20 and 2021-22, a window hidden by the gap. The 2018-19 roster exists and does not list him at PGY2.
  - Before this he held a University of Puerto Rico MD, an NPI from 2016 and a 2017 UPMC co-authored paper, which suggests prior training elsewhere.

## Alumni pages
- Old: surgery.arizona.edu/alumni/neurosurgery (2014-16) and /education/residency-programs/neurosurgery/alumni (2018).
- neurosurgery.arizona.edu/residency/alumni (2021-25).
- Live: medicine.arizona.edu/.../current-and-past-residents (shows only 2023-2026).
- Graduates 2009-2026: Valdivia 2009, Rivero 2010, Serxner 2011, Ansay 2012, Stidd 2014, Fennell and Skoch 2015, Palejwala 2017, Martirosyan 2019, Bina 2020, Ramey 2021, Brasiliense 2022, Avila 2023, Burket 2024, Aguilar Salinas 2025, Joshi 2026.
- 13 rows (2012+) were inserted into `training_history`.

## Problems
Common Crawl run on 2011-2021 (84 crawls). The following crawl/prefix pairs still failed after a retry:
- CC-MAIN-2015-48 and 2016-40, surgery)/residents: observed years.
- CC-MAIN-2017-17, surgery)/education/residency-programs/neurosurgery: observed year.
- CC-MAIN-2019-35, surgery)/alumni/neurosurgery.
- CC-MAIN-2020-50, surgery)/education/residency-programs/neurosurgery: that path had redirected since 2018.
- CC-MAIN-2021-43, surgery)/residency/neurosurgery.

None is likely to fill a missing year. The retries of neurosurgery)/residency for 2015-11, 2018-05, 2018-51 and 2021-25 returned 0 records.


## Phase 2 (2026-09-28)

### Gap status after phase 2
| Year | Status | Significance | Reason |
|---|---|---|---|
| 2011-12 | reconstructed | significant | No roster anywhere. A 2010 entrant who left before 2014-15 would be invisible. |
| 2012-13 | reconstructed | significant | Same reason. Sheen James added at PGY1 (entry 2012; NPI enumerated 2012-06). |
| 2013-14 | reconstructed | significant | Same reason. Sheen James added at PGY2 (PMID 25019458, received 2014-04, UA Division of Neurosurgery). |
| 2017-18 | reconstructed | low | Page stale all year. Every class is bracketed. Sheen James added at PGY6. |
| 2019-20 | reconstructed | low | All 2013-2019 entrants are bracketed, and PubMed 2019-21 shows no unknown neurosurgery resident. The Dept of Surgery directory (Wayback and Common Crawl) is weak evidence: it omits Joshi and Palsma. |
| 2020-21 | reconstructed | low | As 2019-20. Palsma added at PGY1 (entry 2020). Monserrate Marrero was still at UPR. |
| Other years | observed | none | |

### Findings
- **Whitney Sheen James (entry 2012)** was still in Tucson during 2017-18:
  - A World Neurosurgery paper received 2018-05-12 (PMID 30144619) and a 2018 Cureus paper (PMID 30443448) list her at the Division of Neurosurgery, Banner-UMC Tucson.
  - Her surgery.arizona.edu "Resident/Fellow" profile was still up in 2018-08/09.
  - From 2018-06 she is affiliated with High Desert Surgery Center, Prescott (neurosurgery): PMID 30026140, 30771777, 31225517.
  - NPPES 1144582248: Neurological Surgery, full Arizona license, Prescott.
  - She left in **June 2018 after PGY6**. She is not on any alumni page (the fall-2018 alumni page has no 2018 graduate).
  - She may have completed a 6-year track (the 2011 entrant Palejwala finished in 6), or left one year short of a 7-year track. Recorded as completed='unknown', departure_type='unknown'.
  - The phase-1 note "left after 2016-17" is superseded.
- **Andres Monserrate Marrero:**
  - He was at UPR (program 101) through 2020-21 (PMID 33334750, 34900470), so he arrived at Arizona in **2021-22 at PGY5** as a closure transfer.
  - He left after 2022-23 at PGY6, which was 7 years of training counting from 2016. He is not on the alumni pages.
  - NPPES 1962852517 is still Neurological Surgery (Arizona resident licence R78987; Pittsburgh address, updated 2024-03).
  - The adjudicator's earlier "switched specialty" call was unsupported. It now reads "LEFT -> outcome unknown".
  - Outcome after 2023: unknown.
- **Ryan Palsma:** reconstructed at PGY1 in 2020-21. He was a UA College of Medicine student with Dept of Neurosurgery affiliations (2019-20 papers) and was PGY2 on the 2021-22 roster.
- **Stale captures:** Common Crawl captures of current-residents from 2017-11, 2018-01 and 2018-05 all show the 2016-17 list.
- **Composite PDF:** the 2015-16 division composite (surgery.arizona.edu/.../2015-16_neuro_comp_final.pdf) matches the observed 2015-16 roster.
- **Department of Surgery newsletters** (2009, 2010, 2011-12, 2012-13):
  - They name the neurosurgery graduates Rivero (2010), Serxner (2011) and Ansay (2012).
  - They name no other neurosurgery residents.
  - The 2012-13 issue names no 2013 neurosurgery graduate.
- **Unknown names from PubMed:** Gravbrot, Nisson, Telemi, Zeller, Johnstone, Alvarez Reyes, Root and Rice were all checked. Each is a medical student, research staff, or a resident elsewhere.

### training_history
Two rows were added (th_id 2830 Sheen James, 2831 Monserrate Marrero). Both have completed='unknown' and departure_type='unknown'.

### Program length
`terminal_pgy_by_entry_year`: 6 for entrants 2006-2011, 7 from 2013. The 2012 cohort is uncertain (Martirosyan PGY7, Sheen James left after PGY6).

### Remaining
- The 2010-entry class (and a 2007 entrant) cannot be observed in 2011-14. No roster, newsletter, Common Crawl or PubMed evidence exists either way.
- Whether Sheen James completed training is unresolved.
- Monserrate Marrero's outcome after 2023 is unknown.

### Problems
- Every Common Crawl failure from phase 1 and phase 2 was retried successfully except CC-MAIN-2018-34 surgery)/education/residency-programs/neurosurgery, which falls in 2018-19, an observed year. None of the retries produced a new roster.
- OpenAlex was over its daily IP budget, so PubMed and Europe PMC were used instead.
- Search files are in `data/raw/extraction/p72/phase2/`.
