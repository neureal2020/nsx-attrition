# Program 34: Loyola University Medical Center Program (Maywood, IL)

7-year program (PGY1-7). Takes 1 or 2 residents a year; recent classes alternate between 1 and 2.
**The recorded website is wrong:** it points to the neurology residency. The correct page is https://www.loyolamedicine.org/gme/residencies/neurosurgery (roster at /residents, graduates at /alumni).

## Hosts
| Host / path | From | To |
|---|---|---|
| luhs.org/depts/neurosurg/resident_staff.htm | 2003 | 2008-07 (last capture) |
| stritch.luc.edu/neurosurgery/node/6 ("Resident Staff", Drupal) | 2011 | 2016-02 (last capture; stale since 2014-15 content) |
| ssom.luc.edu/neurosurgery (no roster; links out) | 2016-01 | 2024-01 |
| loyolamedicine.org/gme/neuro-surgery-residency/residents | 2017-01 (section) / 2019-04 (first roster capture) | 2020-01 (last roster capture) |
| loyolamedicine.org/gme/residencies/neurosurgery/residents, /alumni | 2023-06 | live |
| luc.edu/stritch/neurosurgery (no roster) | 2025-07 | live |

## Years (after phase 2)
| AY | Status | Significance | Reason |
|---|---|---|---|
| 2011-12 | observed | none | stritch node/6 (content dated Aug 2011) |
| 2012-13 | reconstructed | low | All 10 bracketed or alumni-confirmed; 2011 class seen alone as PGY1 in 2011-12, 2012 class full at 2. Only Liniewski's exit year (2012 or 2013) is open. |
| 2013-14 | observed | none | stritch node/6 2013-09 |
| 2014-15 | observed | none | stale 2015-10 capture holding 2014-15 content |
| 2015-16 | reconstructed | low | All 11 of 2014-15 accounted for (2 alumni 2016, Ibrahim died summer 2016, Spencer at Loyola until Northwestern took him Aug 2016); 2015 class full at 2 |
| 2016-17 | reconstructed | low | All bracketed or alumni-confirmed; 2016 class of 1 fits the program's stated 1/2 alternation |
| 2017-18 | reconstructed | low | Bracketed; Jusue Torres seen on awards page (2018 TIGER); 2017 class full |
| 2018-19 | observed | none | residents page 2019-04 |
| 2019-20 | observed | none | residents page 2020-01 |
| 2020-21 | reconstructed | low | 4 on awards page (2021 recipients), 5 bracketed, Jani/Ng added as PGY1 (medical school at Pitt/Tufts through 2020) |
| 2021-22 | reconstructed | low | 3 on awards page (2022 recipients), rest bracketed, Frazzetta added as PGY1 (Stritch student through 2021). Small residual: a second 2021 intern who left within the year can't be excluded outright. |
| 2022-23 | observed | none | residents page 2023-06 |
| 2023-24 | reconstructed | low | 3 on awards page (2024 recipients), 7 bracketed, Choe added as PGY1 (Stritch MD) |
| 2024-25 to 2026-27 | observed | none | residents page / live |

The awards page (https://www.loyolamedicine.org/gme/residencies/neurosurgery/awards; Wayback 2024-11-21) lists recipients by the year each academic year ends. Jani's bio ("2021-2022 John F. Shea Award") matches the "2022" heading. These people are loaded as `source_type: other` partial captures.

## Departures and outcomes (training_history)
- **David Liniewski**: entered 2008 and was last seen 2011-12 at PGY4. He left in 2012 or 2013. Phase 2 found no papers and no page on any Loyola host. NPPES shows "Dawid Liniewski", Neurological Surgery taxonomy, Maywood address, enumerated 2008; this is not evidence of his outcome. Outcome unknown, and no row was added.
- **Drew Spencer**: entered 2010. **Transferred to McGaw/Northwestern (program 41).** He is absent from every Northwestern roster capture up to 2016-05-12 and is listed there at PGY7 from 2016-08-01; Northwestern alumni 2017. He left Loyola at the end of 2015-16 (PGY6), so he was added as reconstructed PGY6 in 2015-16. Rows: program 34 has completed='no', departure_type='transferred', end_year 2016; program 41 has a transfer-in row with start_year 2016 (PGY7).
- **Tarik Ibrahim**: entered 2010. **Died during residency in summer 2016, with a year left.** Sources: the TIGER fund page https://www.loyolamedicine.org/gme/residencies/neurology/tarik-ibrahim-education-fund, and his CV (residency 7/2010-8/2016). A certificate was given posthumously and the alumni page lists him under 2016. His training_history row was changed to completed='no', notes='died during training', with no departure_type. **He counts as neither a completion nor attrition.** 16_adjudicate has no "died" category and prints him as "LEFT -> did not complete".

## Joiners
None. Everyone first seen above PGY1 has now been placed at PGY1 in the gap years with supporting evidence (bracketing, alumni year, or pre-entry medical-school affiliation).

## Consistency
Every person has one entry year across all observations. Class sizes by entry year:

| Entry year | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Residents | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 2 |

**Residents entering 2011 or later: 25.**

## Alumni
The alumni page lists graduates for 2000-2026. The 21 graduates listed for 2012-2026 were inserted into training_history (source_type program_page). In phase 2, Ibrahim's row was changed to 'died during training' (completed='no'), which leaves 20 completions.

## Adjudication
| Outcome | Count |
|---|---|
| COMPLETED | 20 |
| IN TRAINING | 11 |
| LEFT -> TRANSFERRED (Northwestern) | 1 (Spencer) |
| LEFT, outcome unknown | 1 (Liniewski) |
| Died during training (printed "LEFT -> did not complete") | 1 (Ibrahim) |

## Phase 2 searches
- gapaudit over every Loyola host in each gap window.
- Full CDX listings of the stritch, ssom and loyolamedicine neurosurgery paths.
- Every stritch Drupal node, plus the graduation-2012/2013 pages (photos only).
- linkaudit on the department, SSOM and GME parent pages. The GME incoming/current-housestaff pages carry no names.
- Common Crawl retries of CC-MAIN-2014-42 and CC-MAIN-2020-50: both OK, 0 records.
- Awards pages and live bios.
- PubMed affiliation mining 2011-26 (599 PMIDs). It found no resident missing from the rosters; the extra Loyola-neurosurgery authors were Stritch students, research staff or other-department trainees.
- Northwestern roster captures for 2015-16.
- NPPES.

Scratch files: data/raw/extraction/p34/phase2/.

## Files
Scratch work is in data/raw/extraction/p34/: p34parse.py (Loyola layouts), build34.py, and the CC logs cc_a, cc_b, cc_s and cc_r.
