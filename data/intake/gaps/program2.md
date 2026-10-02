# Program 2: Allegheny Health Network (AGH) Neurosurgery, Pittsburgh PA

7-year program. The complement was 1 per year on the 2009 page, then "1-2 per year" (2014-17 pages), and is now 2 per year (ACGME). No alumni or graduates page exists on any host. Roster file: `data/intake/rosters_program2.json`. Scratch folder: `data/raw/extraction/p2/` (`build.py`, `aem.py`, `cc/`).

## Hosts
| URL | Dates | Content |
|---|---|---|
| wpahs.org/agh/education/graduate/agh_neurosurgres.html | 2005-03 to 2009-09 | Description only (6 years, 1 per year). No roster. |
| wpahs.org/education/graduate-medical-education/residencies/neurosurgery-residency-program | 2011-09 to 2014-03 | Program pages. No roster. |
| wpahs.org/education/graduate-medical-education/residencies/neurosurgery/residents | 2013-02 to 2014-04 | Roster |
| ahn.org/education/graduate-medical-education/residencies/neurosurgery/residents | 2015-03 to 2015-09 | Roster (Common Crawl Mar to Jul 2015, Wayback Sep 2015 only) |
| ahn.org/education/residencies/neurosurgery/residents | 2018-04 to 2019-07 | Roster (Common Crawl 2018-04 and 2019-02, Wayback 2019-07) |
| ahn.org/health-care-professionals/education/graduate-medical-education/residencies/neurosurgery/residents(.html) | 2020-05 to live | Roster (AEM layout, "PGY n" headings) |

## Years (after phase 2, 2026-09-28)
| AY | Status | Significance | Why |
|---|---|---|---|
| 2011-12 | missing | low | There was no roster page before Feb 2013. The May 2012 overview says "one residency position for each of the seven years", and every entry class from 2006 to 2011 is filled on the 2012-13 roster. The 2011 class already has two residents: Dupre, and Castellvi, whose NPI was issued Oct 2011 in Pittsburgh. |
| 2012-13 to 2015-16 | observed | none | 2013-14 is consistent: Yu graduated 2013, and Castellvi had one extra year. 2014-15 comes from Common Crawl only but is complete. |
| 2016-17 | reconstructed | low | 11 of 11 placed: 9 bracketed residents, plus Jho at PGY7 (Penn State Health bio: AGH residency 2017) and Myers at PGY1 (PGY2 in 2017-18; NPI Apr 2016). The only remaining risk is an unseen second 2016 intern who quit within PGY1 (the program took "1-2 per year"). |
| 2017-18 to 2025-26 | observed | none | 2017-18 and 2018-19 come from Common Crawl. For 2023-24 the complete May 2024 capture was used. |
| 2026-27 | missing | significant | The live page and Sep 2026 captures are stale and half-edited: the 12 names of 2025-26, PGYs not advanced, no 2026 interns. Under the harmonised rule this is not an observation, so the capture was removed from the roster file. Apr and Jul 2026 captures still list all 12. Recheck when the page updates. |

Program length: 7 years for every 2008+ entry class. The 2007 entrant Yu graduated after PGY6 (2013). Dabecco, a transfer-in, graduated after AGH PGY6 with credit for earlier training. The JSON records this as `terminal_pgy_by_entry_year`.

## Departures and joiners (resolved in phase 2)
| Name | Last seen | Outcome | Evidence | th_id |
|---|---|---|---|---|
| Alexander Yu | 2012-13 PGY6 | **Graduated 2013** (not attrition) | AHN findcare: residency graduation 2013, internship 2008 | 3049 |
| Nihar Gala | 2014-15 PGY3 | Left 2015, destination unknown | NPI anesthesiology is not evidence; only Rutgers NJMS research papers | 3057 |
| Diana Jho | 2016-17 PGY7 (recon.) | **Graduated 2017** | Penn State Health profile | 3050 |
| Andrea Alonso | 2020-21 PGY2 | **Switched to vascular surgery** (moderate confidence) | Boston Medical Center vascular surgery publications 2023-25 | 3055 |
| Kevin Sexton | 2020-21 PGY2 | Left 2021, destination unknown | NPI radiology is not evidence; no later papers | 3056 |
| Rocco Dabecco | 2021-22 PGY6 | **Graduated 2022** | findcare: AGH residency 2022, CCF skull base fellowship 2023; now AHN faculty | 3051 |
| Lance Valls | 2022-23 PGY2 | Unknown; possibly a research leave | Still an AHN-neurosurgery author on papers from 2023 and 2026 (the 2026 one received Jun 2025); Barcelona IDIBAPS abstract 2023 | 3058 |

| Joiner | Joined | From | th_id |
|---|---|---|---|
| Rocco Dabecco | PGY3 2018-19 | Saint Barnabas Medical Center neurosurgery (AOA; not in the DB) | 3051 |
| Jose Sandoval Consuegra | PGY4 2021-22 | UPR (101) closure; graduated 2025 | 3053 |
| Alejandro Matos Cruz | PGY5 2021-22 | UPR (101) closure; graduated 2024 | 3052 |
| Bhavika Gupta | PGY2 2024-25 | Filled the 2023 slot. Research at Cleveland Clinic Florida 2023-24; PGY1 site unknown | 3054 |

Rejected crossmatches (name-only): Raghav Gupta (USC) is not Bhavika Gupta, and Katie Myers (Cincinnati) is not Dan Myers.

## Adjudication (after reload)
22 completed, 12 in training, 3 left with outcome unknown (Gala, Sexton, Valls), and 1 switched specialty (Alonso). All four departures are 2011+ entrants.

## Phase 2 searches
- Unparsed phase-1 `cc/` files: nothing new (program pages and duplicate 2014 rosters).
- Common Crawl rerun with the fixed filter: CC-MAIN-2012 (wpahs.org), all 2016-17 crawls (ahn.org and wpahs.org neurosurgery paths, ahn neuroscience), and all 2026 crawls. No failures; the crawls that failed in phase 1 (2016-30, 2016-50, 2017-43) now return 0 roster records.
- Wayback gapaudit: wpahs.org 2010-2013 and ahn.org 2016-17. The 2016 program page links to /neurosurgery/residents, but that page was never captured.
- PubMed affiliation mining for 2010-13 and 2016-19: every author with an AGH neurosurgery affiliation is a known resident, faculty member, foreign fellow, student or other-specialty resident.
- Files: `data/raw/extraction/p2/phase2/`.

## Problems
- There is no alumni page. 2026-27 cannot be observed until AHN updates the page.
- Alcindor's repeated PGY7 in 2013-14 is unexplained (he entered before 2011).
- Saint Barnabas is not in the programs table, so no departure row was written there.
