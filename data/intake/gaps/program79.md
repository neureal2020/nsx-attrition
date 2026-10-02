# Program 79: University of Cincinnati Medical Center/College of Medicine Program (Cincinnati, OH)

**Length:** 7 years now. Entrants through 2012 were on a 6-year track (PGY1-6, chiefs were PGY6; the last 6-year class graduated in 2018). The 7-year track starts with the 2013 entry class (first PGY7 chiefs in 2019-20). This is recorded in the JSON as `terminal_pgy_by_entry_year`: 6 for entry years up to 2012, 7 from 2013.
**Complement:** 3/yr for the 2009-2013 entrants, then 2/yr for 2014-2017. The first year had 1 resident in 2018 and 2019: Gaulden's March-2020 transfer used a temporary complement increase, "bringing the first year program to a total of two residents". In June 2020 the ACGME approved one extra resident every other year, so classes since 2020 are 2-3.
**Residents entering 2011+:** 36 (roster file: `data/intake/rosters_program79.json`, 16 captures).

## Hosts
| URL | from | to |
|---|---|---|
| mayfieldclinic.com/DNS/R_OurRes.htm (UC department pages on the Mayfield Clinic site) | 2007-12 | 2012-10 (the Oct-2012 capture is still the 2011-12 list) |
| med.uc.edu/neurosurgery/education/residency/residents.aspx, plus directory/directory.aspx and alumni/alumni.aspx | 2013-01 | 2015-03 |
| med.uc.edu/neurosurgery/residency/current-residents and /directory/residents (Wayback, plus Common Crawl copies) | 2017-03 | 2018-07 |
| med.uc.edu/neurosurgery/education/residency/current-residents (Common Crawl and Wayback) | 2018-08 | 2019-12 |
| med.uc.edu/depart/neurosurgery/education/residency/current-residents | 2020-08 | live 2026-09-27 |

## Year status (phase 2)
| AY | status | significance | reason |
|---|---|---|---|
| 2011-12 | observed | none | full PGY-labelled roster |
| 2012-13 | reconstructed | low | Every 2011-12 resident is accounted for. The 2012 interns (Carroll, Kosty, Vuong) fill the complement of 3; all are on the Oct-2013 directory, and Carroll and Kosty have UC Neurosurgery affiliations in 2012-13 |
| 2013-14 | observed (names only) | low | Oct-2013 and Feb-2014 directories list every resident; PGY inferred consistently |
| 2014-15 | observed | none | full roster |
| 2015-16 | reconstructed | low | All PGY1-4 of 2014-15 reappear in 2016-17. The 2016 Dunsker (Gogela) and Tew (Kosty) awards confirm presence. The 2015 interns (Plummer, Robinson) fill the complement of 2. Harwell, Tackla and York completing in 2016 is inferred |
| 2016-17 | observed (spring) | low | 5 identical captures Mar-Jun 2017; nobody from 2015-16 is missing |
| 2017-18 | observed | none | **closed:** 8 Common Crawl captures Aug-2017 to Jul-2018, all the same 14 |
| 2018-19 | observed | none | **closed:** 14 Common Crawl captures Aug-2018 to Aug-2019, all the same 12. Shah was the sole 2018 intern all year |
| 2019-20 to 2026-27 | observed | none | in-year rosters |

## Phase 2: what was done
- Re-read the phase-1 raw files: the cc/ pages and the Oct-2012, Dec-2014, Mar-2015 and Jul-2017 captures. They held no new roster.
- Ran gapaudit for 2012-2019 over mayfieldclinic.com, med.uc.edu/neurosurgery (both casings), /depart/neurosurgery, /gme, healthnews.uc.edu, magazine.uc.edu and uc.edu/news. I also ran a CDX keyword scan over uchealth.com and uc.edu/news. Result: per-resident profile and Pubs pages only, with no new people.
- Read ten Mayfield Standard newsletter PDFs (2012-2017). They contain no rosters. The Winter-2016 issue calls Harwell a "fifth-year resident" at the May-2015 award.
- **Ran Common Crawl over all 55 crawls from 2015 to 2019** with the new filter, and none failed. The crawls hold full in-year rosters for 2017-18 and 2018-19; both years now use these CC captures as their source. They have nothing for Aug-2016 to Feb-2017, and nothing for 2015-16.
- Read the live award pages: the 2016 Dunsker Award went to Gogela and the 2016 Tew Award to Kosty.
- Mined PubMed affiliations for 2012-2019 (658 PMIDs). Everyone with a UC Neurosurgery affiliation who never appears on a roster turned out to be a fellow, visitor or student: Kurbanov, Jimenez, Poczos, Woodhouse, Evans and Hoang.
- **Stanley Hoang** was a UC Neurosurgery *fellow* ("Instructor" on directory/fellows, Oct and Dec 2019), not a resident. I recorded no row for him at 79.
- crossmatch.json had one entry for this program: a false pairing of Myers with Dan Myers at AHN.

## Departures (left before the terminal PGY)
- **Katie Myers** (2011 entrant, Missouri MD): last seen 2013-14 at PGY3. Destination unknown. training_history: completed='no', departure_type='unknown', end_year 2014.
- **Christopher Cutler** (2024 entrant): last seen 2025-26 at PGY2 and missing from the live 2026-27 page. Destination unknown. training_history: completed='no', departure_type='unknown', end_year 2026.

## Completions recorded in training_history (phase 2)
- **PGY-terminal roster (6-year track):** Bixenmann, King and Magner (2015); Gogela and Gozal (2017); Carroll, Kosty and Vuong (2018).
- **Inferred (not observed), end_year 2016:** Harwell, Tackla and York. The evidence: all three were PGY5 in 2014-15, and on the 6-year track they would finish in 2016. York has a Swedish Neuroscience Institute affiliation in 2016. Tackla was on the UC directory in 2017, but not as a resident. All three hold NPPES neurosurgery taxonomy.

## Joiners (transfer in; rows added at 79)
- **Amber Gaulden:** transferred from Wayne State/DMC (program 125, which lost accreditation). She joined in March 2020 as PGY1 and was PGY2 in 2020-21 (UC news, 2020-06-10). Her row has start_year 2020.
- **Abhijith Matur:** joined at PGY2 in 2023-24, arriving from the University of Kentucky: his PubMed affiliations are General Surgery in 2020-21 and Radiology in 2022-23. His row has start_year 2023.

## PGY anomalies
- Staarmann (2014 entrant) was PGY4 in both 2017-18 and 2018-19, and finished in 2022.
- Saleh (2014 entrant) was PGY5 in both 2018-19 and 2019-20. He is missing only from the Nov-2019 capture, was PGY7 chief in 2020-21, and finished in 2021.
- Chiefs are labelled "Chiefs" with no number from 2016-17 to 2020-21, so I assigned their PGY by cohort.

## Adjudication (after phase 2)
32 completed, 15 in training, 2 left (Myers and Cutler). The transfer-in start_year rows put Gaulden in the 2020 cohort, although she began residency at Wayne State in 2019.

## Remaining / problems
There is still no archived roster for 2012-13 or 2015-16; both are rated low significance because the brackets and full complements cover them. The completions of Harwell, Tackla and York are inferred. Where Myers and Cutler went is unknown. The NPPES API was unreachable, so I used the local NPPES copy.
