# Program 20: Emory University School of Medicine Program (Atlanta, GA)

7-year program, 2-4 per class (recently 4). Phase 1 completed 2026-09-27; phase 2 completed 2026-09-28. JSON twin: `program20.json`.

## Hosts
| Host / path | From | To |
|---|---|---|
| www.neurosurgery.emory.edu/Residency/residents.htm (old static site, PGY headings) | 2007-06 | 2008-07 (shows 2007-08 roster) |
| www.neurosurgery.emory.edu/Residency/residents.html + secure.web.emory.edu/neurosurgery/Residency/currentresidents.html (linked, never archived; only orphan captures 2015-12, old alumni list ends with 2011 grads) | c.2009 | c.2015 |
| neurosurgery.emory.edu/residency-education/education/current-residents.html (+ alumni.html, resident-bios/) | 2015-10 | 2020-02 |
| med.emory.edu/departments/neurosurgery/education/residency/current_residents.html (+ alumni.html); live | 2020-11 | 2026-09-27 |
| emoryhealthcare.org/neurosurgery/residency-program.html (no names) | 2009 | 2016 |

## Years
- **Observed:** 2015-16 through 2025-26 (Wayback, one capture each, content-dated by PGY-1 class), and 2026-27 (live, advanced). Significance: none.
- **Reconstructed (manual):** 2011-12, 2012-13, 2013-14, 2014-15. After phase 2, all four are rated **low** significance (reasons below).
- **Missing:** none.

### Why 2011-2015 cannot be observed
Wayback has no capture of any residency page on neurosurgery.emory.edu from 2008-09 to 2015-10. secure.web.emory.edu/neurosurgery and web.emory.edu/neurosurgery have no captures at all. Common Crawl first indexes the host in CC-MAIN-2015-40/48. In phase 2 the two failed crawls (CC-MAIN-2015-06 and 2016-18) were retried and succeeded, but found no roster. A gap audit of the GME, education and news hosts for 2009-15 also found nothing.

### Phase-2 changes to the reconstruction
- **Jeremy Wetzel** is now reconstructed as PGY1 in 2013-14 and PGY2 in 2014-15. His Oct-2015 bio gives an MD from UTHealth in 2013 and PGY-3 status. His NPI was enumerated in GA in April 2013. The Oct-2015 alumni page lists "Joe Quillin, Jeremy Wetzel" under 2020. The entry-2013 class is therefore 2, and both members are accounted for.
- **David Laborde** is now reconstructed as PGY7 in 2011-12. He was PGY3 on the 2007-08 roster (entry 2005, the same class as Raore). He has Emory Neurosurgery PubMed affiliations in 2011-12, including a clinical case received 2011-09. He is not on any alumni list, and his NPI has not been updated since 2008. His outcome is **unknown**, and a training_history row records that.
- **Nasrin Aldawoodi** (PGY1 in 2007-08) left before 2011. She has a UNC Anesthesiology affiliation in 2012 and is now in Moffitt anesthesiology. She falls outside the study window.

### Significance
| Year | Status | Significance | Reason |
|---|---|---|---|
| 2011-12 | reconstructed | low | The 2009-2012 entry classes (3, 4, 3, 3) are intact on the 2015-16 roster or the alumni list. The 2005-2008 classes are anchored by the 2007-08 roster. Laborde is the only open case, and it is recorded. |
| 2012-13 | reconstructed | low | Same anchors. Every entrant from 2006-2012 is either an alumnus or on the 2015-16 roster. |
| 2013-14 | reconstructed | low | The 2013 class is Quillin plus Wetzel. Classes of 2 are normal here (2015, 2020 and 2022 were observed at 2). An entrant who left before Oct 2015 without trace cannot be fully excluded. PubMed mining turned up no unexplained resident. |
| 2014-15 | reconstructed | low | The total is 21, the fixed complement on every observed roster from 2015-16 to 2022-23. In 2015-16 the program took only 2 PGY-1s and no PGY-2 joiner, so there was no vacancy to backfill and hence no departure in 2014-15. |
| 2015-16 .. 2026-27 | observed | none | Complete PGY1-7 rosters. |

The program is 7 years for every cohort (the 2007-08 roster already ran to PGY7). `terminal_pgy_by_entry_year` = 7 throughout.

## Alumni page
https://med.emory.edu/departments/neurosurgery/education/residency/alumni.html. 40 graduation rows (2012-2026) were inserted into `training_history`.

## Departures and outcomes (phase 2)
- **Hosniya Zarabi: TRANSFERRED.** She was last at Emory in 2017-18 as PGY2. She then went to UC Davis (program 77) as PGY-3 in 2018-19, and to Temple (program 64) as PGY-3 in 2023-24. The training_history row has completed=no, departure_type=transferred and end_year 2018. The earlier NPPES "switch" call was wrong.
- **Jeremy Wetzel: COMPLETED 2020 (resolved).** He was PGY-7 on the Dec-2019 and Feb-2020 rosters, and the Jan-2020 alumni page lists him under 2020. The med.emory.edu alumni page added the 2020-22 classes only in 2022-06, and it lists Quillin alone for 2020. That page also drops confirmed graduates: Bryan Barnes and Patrick Tomak (2005) are on the old alumni list but not the new one. So his absence is an omission, not evidence of non-completion. He has Emory Neurosurgery affiliations on papers through 2021, a 2022 affiliation "JW Neurosurgery Consulting, Atlanta", and an active GA NPI (updated 2023). Recorded as completed=yes, end_year 2020, "PGY-terminal roster".
- **David Laborde: outcome unknown** (see above).

## Joiners (all at PGY2)
- **Juanmarco Gutierrez** (2017-18): MD Mexico 2010, then an Emory MSc in 2014 (Boulis lab). His July-2017 bio header still said PGY-1, so his PGY-1 year in 2016-17 was outside the neurosurgery roster. He filled the 2016 class and graduated in 2023. Not a transfer; no new row.
- **Kwanza Warren** (2021-22): PGY-1 in surgery at NYP-Columbia in 2020-21 (PubMed), a preliminary-year entrant. Row recorded (start 2021).
- **Sukreet Raju** (2023-24): came from a Tulane general-surgery residency (upper-level award 2019; Tulane Surgery affiliation 2021). His bio lists the SNS neurosurgery boot camp in July 2015 and a 2017 Ochsner Neurosurgery affiliation, so he may have done an earlier neurosurgery PGY-1 in New Orleans. Program 66's roster does not list him, which leaves this as a lead for that program. Row recorded (start 2023).
- **J. Manuel Revuelta-Barbero** (2023-24): **transfer in** from the Medical College of Georgia (program 42, listed there as "Manuel Revuelta", PGY-1 2022-23). He had been an Emory skull-base research fellow in 2021-22. Row recorded (start 2023).

## Class sizes (entry year: n)
2011:3, 2012:3, 2013:2 (Quillin, Wetzel), 2014:4, 2015:2, 2016:4 (incl. Gutierrez), 2017:3, 2018:4, 2019:3, 2020:3 (incl. Warren), 2021:3, 2022:4 (incl. Raju, Revuelta-Barbero), 2023-2026:4 each. **54 residents entered 2011+.**

## Adjudication (after phase 2)
41 COMPLETED (including 14 pre-2011 entrants, and Wetzel via training_history), 26 IN TRAINING, 1 LEFT -> TRANSFERRED (Zarabi), 1 LEFT -> outcome unknown (Laborde, entry 2005).

## Phase 2 searches (2026-09-28)
- **Common Crawl retries:** CC-MAIN-2015-06 through 2015-48 (3 prefixes) and all 2016 crawls (secure and web hosts). All succeeded. The only hits were the emoryhealthcare residency-program.html page and the old Residency/ index, neither of which has names.
- **Gap audit 2009-2015:** neurosurgery.emory.edu (with and without www.), the secure and web hosts, emoryhealthcare.org/neurosurgery, med.emory.edu/gme and /education, whsc news, and news.emory.edu 2012. No roster was found.
- **Old-site orphan pages from 2015-12:** alumni list to 2011 and six old bios, none with a PGY. The neuro-oncology track pages have no resident names.
- **Alumni pages:** every version on both hosts, 2015-10 to 2025-04.
- **Resident bios:** Wetzel, Gutierrez, Warren, Raju and Revuelta-Barbero.
- **PubMed affiliation mining:** "Emory AND neurosurg" for 2010-16 (487 PMIDs). Output is in `data/raw/extraction/p20/phase2/pubmed_2010_2016.txt`.
- **Other sources:** NPPES, Europe PMC and OpenAlex checks for the people above. The OpenAlex daily budget ran out after one query.
- **Phase-1 copies:** kept in `data/raw/extraction/p20/phase2/*.phase1.*`.

## Name canonicalisation
- Neal → Nealen Laxpati
- Krish → Krishanthan Vigneswaran
- Chris → Christopher Holland
- "Han Tao" (2024-07 typo) → Hao Tan
- Marshall A. Smith-Cain (2007-08) = Marshall A. Cain (alumni)

## Scratch
Scratch files are in `data/raw/extraction/p20/`: parse20.py strips HTML comments before calling roster_extract; build.py; gap.py.
