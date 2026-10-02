# Program 56: Rush University Medical Center Program (Chicago, IL)

7-year program (entrants through 2012 finished in 6 years: 2010-11 PGY1s graduated 2016, 2012 entrants 2018; 2013 entrants graduated 2020 after PGY7; no 2019 graduates). Complement 2 per year before ~2014, 3 per year since (residency landing page 2019-2022: "two or three positions each year").
Roster file: `data/intake/rosters_program56.json` (loaded; 17 captures, 246 observations incl. 2010-11 for bracketing). Alumni graduations 2012-2026: 31 rows in `training_history`, plus 11 phase-2 event rows (2026-09-28). Redo of an interrupted run: every roster capture re-parsed and checked by eye, live pages re-fetched 2026-09-28, the roster-block searches redone.

## Hosts / paths
| URL | Dates | Note |
|---|---|---|
| http://www.rush.edu/professionals/gme/neurosurgery/residents-fellows.html | 2001 to 2011-06 | roster (2010-11 content) |
| http://www.rush.edu/professionals/gme/neurosurgery/index.html | 2011-12 to 2013-04 | meta-refresh stub to rushu servlet |
| http://www.rushu.rush.edu/servlet/Satellite?c=RushUnivLevel3Page&cid=1249914457241 | 2012-05 to 2016-06 | GME > Neurosurgery; no roster |
| http://www.rushu.rush.edu/servlet/Satellite?c=RushUnivLevel4Page&cid=1306073857793 (also cid=1320161224476) | 2013 to 2016 | Faculty & Housestaff; links roster block cid=1307369094954, never archived |
| https://www.rushu.rush.edu/education-and-training/graduate-medical-education/residency-programs/neurosurgery-residency | 2016-07 to 2024-05 | no roster |
| https://www.rushu.rush.edu/education-and-training/graduate-medical-education/residency-programs/neurosurgery-residency/meet-our-residents | 2019-08 to 2024-06 | roster |
| https://www.rushu.rush.edu/education-and-training/.../neurosurgery-residency/alumni-where-are-they-now (-> alumni-where-did-they-go-after-graduating) | 2022-08 to 2024-07 | alumni |
| https://www.rushu.rush.edu/education-training/graduate-medical-education/residency-programs/neurosurgery-residency/meet-our-residents | 2024-08 to 2026-09-28 (live) | roster |
| https://www.rushu.rush.edu/education-training/graduate-medical-education/residency-programs/neurosurgery-residency/alumni-where-did-go-after-graduating | 2024 to 2026-09-28 (live) | alumni 2001-2026 |
| https://www.rushu.rush.edu/rush-medical-college/departments/department-neurological-surgery | 2016-06 to live | department page (DB website); no roster |

Checked and empty: rushneurosurgery.com/.org/.net, rushneuro.com (no captures); www.rush.edu Drupal site (patient pages only); live rush.edu and rushu.rush.edu sitemaps.

## Years (phase 2, 2026-09-28)
Program length by entry year: 6 years for entrants to 2012, 7 years from 2013 (`terminal_pgy_by_entry_year` in the JSON). Exception: Khanna (entry 2016) graduated after PGY6.

| AY | status | significance | reason |
|---|---|---|---|
| 2011-12 | reconstructed | low | All 2010-11 residents are accounted for by the alumni list. The 2011 class (Munich, Ahuja) matches the complement of 2. Kasliwal's entry year is inferred. |
| 2012-13 | reconstructed | low | The 2012 class is Wewel plus **David Wallace** (from his UTHSA bio), so it matches the complement of 2. |
| 2013-14 | reconstructed | low | The 2013 class (Kerolus, Kochanski) matches the complement, and both graduated in 2020. DiLorenzo arrived in 2013-14 or 2014-15. |
| 2014-15 | reconstructed | low | All 3 of the 2014 class graduated in 2021. Wallace left after this year. |
| 2015-16 | reconstructed | low | Adogwa's transfer in at PGY4 is documented. The 2015 class (2) fits the alternating 3/2 pattern. |
| 2016-17 | reconstructed | low | All 3 of the 2016 class graduated. |
| 2017-18 | reconstructed | low | The 2017 class (2) fits the pattern. Nobody with a Rush neurosurgery affiliation in 2016-19 is unaccounted for. |
| 2018-19 | observed | low | Content-dated from the Aug 2019 capture. |
| 2019-20 | observed | none | Dec 2019 capture. |
| 2020-21 | reconstructed | low | Every 2019-20 resident is on the 2021-22 roster or graduated. The 2020 class (3) fits the pattern. Joshi's start (2020 or 2021) is unresolved. |
| 2021-22 | observed | none | |
| 2022-23 | observed | low | The capture omits the PGY-1 class. The 2022 class (Otun, Richards, Olson) of 3 fits the pattern, and all three are on 2023-24. |
| 2023-24 .. 2026-27 | observed | none | Sakakura is PGY-1 in two years. |

**Why 2011-18 is now "low":** the resident list for those years (FatWire content block cid=1307369094954) was never archived. Phase 2 re-audited the hosts for 2011-2019: all 4,074 Wayback content_block captures (the target cid is absent, and the nearby cids are unrelated pages), 134 level-4 pages, the old rush.edu/professionals/gme/ tree (resident photo files return 404 from 2013), the rushu GME and department paths, and rush.edu/news. None holds a roster. The years are closed with independent evidence instead:
- the alumni list, complete for 2001-2026;
- PubMed affiliation mining for 2010-2019 (737 papers, every non-faculty name followed up) and for 2020-26;
- a cross-check of every Rush name against the other programs' rosters.

That search found one unseen departure (Wallace) and one misplaced reconstruction (Adogwa). Every entry class now matches the complement: 2 per year to 2013, then alternating 3/2 (2014: 3, 2015: 2, 2016: 3, 2017: 2, ... 2023: 2). Residual risk: a 2015-17 entrant who never published with a Rush affiliation and left before Aug 2019 would still be invisible.

Common Crawl: phase 1 scanned every crawl from 2012 to 2022 with no failures, so there was nothing to retry.

## Departures (left before the terminal PGY)
- **David Wallace** (NEW): entry 2012, left after PGY3 (2014-15). His UTHSA bio reads "Residency - Rush University Medical Center, Department of Neurosurgery (2012-2015)". **Transferred to UT Health San Antonio (108)**: PGY4 in 2016-17, graduated 2020.
- **Ravi Nunna**: entry 2015, last seen 2018-19 at PGY4. PubMed shows UIC neurosurgery research in 2020-22. **Transferred to Missouri (94)**: PGY5 in 2022-23, graduated 2025.
- **Ayodamola Otun**: entry 2022, left after PGY2 (2023-24). Outcome unknown. NPPES lists anesthesiology in Milwaukee, but that is the NPI only and is not confirmed.
- **Joseph Morrison**: entry 2018, left after PGY6 (2023-24). Outcome unknown. NPPES shows a trainee in Aurora CO, but he is not on the Colorado neurosurgery roster. **The adjudicator's "TRANSFERRED (Buffalo)" is wrong**: it matched him to John Morrison by initial and surname.
- **Mychael Delgardo**: left after PGY1 (2024-25). Outcome unknown.

**Completed from the roster only:** John Paul Kolcun, 2026. He was PGY7 through May 2026 and his papers carry a Rush affiliation in 2026, but he is not yet on the alumni page.

## Joiners
- **Owoicho Adogwa** (NEW): Duke PGY1-3 (2012-15), joined Rush at PGY4 in 2015-16, graduated 2018. Phase 1 had reconstructed him as a 2012 Rush entrant; that is now corrected.
- **Krishna Joshi**: first seen at PGY5 in 2021-22. He had a Rush research affiliation in 2018-20. Graduated 2024.
- **Vitor Salviato Nespoli**: PGY2 in 2024-25, after prior training at the University of Sao Paulo.
- **Daniel DiLorenzo**: UTMB (109) 2011-12, then Houston Methodist (26) in 2013, then Rush from 2013-14 or 2014-15. PGY unknown. Graduated 2016.
- **Manish Kasliwal**: Rush spine fellow in 2010-11, then resident from about 2011-12 (inferred). Graduated 2016.

Residents entering 2011+: 42. That is 37 seen on Rush rosters plus 5 never on one: Munich, Ahuja and Wewel (alumni list), Adogwa (alumni list; 2015 transfer-in) and Wallace (his UTHSA bio). DiLorenzo and Kasliwal are not counted.

## training_history (phase 2)
Eleven rows, th_id 2756-2766:
- **Transfers out:** 2 (Wallace, Nunna).
- **Transfers in:** 5 (Adogwa, Joshi, Nespoli, DiLorenzo, Kasliwal). The graduates among them carry completed=yes so they do not override the alumni rows.
- **Completion from a PGY-terminal roster:** 1 (Kolcun).
- **Departures with unknown outcome:** 3 (Otun, Morrison, Delgardo).

The destination-side rows for Wallace (108) and Nunna (94) are left to those programs.

## Adjudication
31 COMPLETED, 17 IN TRAINING, 2 LEFT -> outcome unknown (Ruban and Smith, 2011 graduates before the window), 2 LEFT -> did not complete (Otun, Delgardo), and 3 TRANSFERRED: Wallace to UTHSA and Nunna to Missouri are correct; **Morrison to Buffalo is wrong**.

## Problems
- 2011-12 to 2017-18 remain reconstructed.
- The adjudicator's initial+surname fallback misattributes Joseph Morrison. The shared script was not edited.
- A transfer-in start_year is read as the entry year (Adogwa shows 2015, Nespoli 2024).
- OpenAlex was over its daily rate limit and was not used.
- Sakakura is listed as PGY-1 in two consecutive years.
