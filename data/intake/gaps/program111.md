# Program 111: University of Utah Health Program (Salt Lake City, UT)

This is a 7-year program. It took 2 residents a year until 2014, and 2-3 a year from 2015. The 2007 class (Mumert, Sayama) finished after PGY-6 (`terminal_pgy_by_entry_year` in the JSON).
- Roster file: `data/intake/rosters_program111.json`
- Phase 1 scratch: `data/raw/extraction/p111/`
- Phase 2 scratch: `data/raw/extraction/p111/phase2/`

## Hosts
| URL | From | To |
|---|---|---|
| medicine.utah.edu/neurosurgery/academic/residency/current.htm (+ academic/alumni.htm, teachingrounds/, newsletters/). Old static site; inline "Name, M.D. / PGY-n". | 2008 | 2012-06 (last roster capture; the site was still linked in 2013-09) |
| uuhsc.utah.edu/neurosurgery/ (301 redirects only) | 2010 | 2013 |
| medicine.utah.edu/neurosurgery/current-residents/index.php (PGY tabs) + name.php profiles | 2014-07 (roster first archived 2015-02) | 2016-06 |
| medicine.utah.edu/neurosurgery/residency/current-residents.php (+ res-profiles/, never archived). Returned 301 in every capture from 2018-05 to 2019-09. | 2016-07 | 2021-04 |
| medicine.utah.edu/neurosurgery/residency/current-residents + /pgy1..pgy7 + /residents/slug + /residency/alumni | 2022-11 | live 2026-09-27 |
| healthcare.utah.edu/neurosurgery, neurosurgery.utah.edu, neurosurgery.utahhealth.acsitefactory.com, healthcare.utah.edu/gme, uuhsc.utah.edu/gme | no captures | |

## Years
| Year | Status | Significance | Reason |
|---|---|---|---|
| 2011-12 | observed | none | Full roster (Oct 2011). Paul Park's mid-year departure is visible. |
| 2012-13 | reconstructed | **significant** (narrowed) | Every 2011-12 resident is accounted for, and Eskandari is confirmed as chief in June 2013. But Jamil joined the 2012 class at PGY-2 in 2013-14 after an outside internship, so an unseen 2012 intern who left after one year (a vacancy he may have filled) cannot be ruled out. |
| 2013-14 | reconstructed | low | Everyone is bracketed. The 2013 class of 2 fills the complement of 2 for that era. Jamil (PGY-2) is placed from his profile. |
| 2014-15 | observed | none | Lin was removed (UVM visitor). |
| 2015-16 to 2017-18 | observed | none | |
| 2018-19 | reconstructed | low | The 2018 interns are placed. Shah's and Colwell's departures are known; only their exit year (2018 or 2019) is uncertain. Agnoletto was in Jacksonville. |
| 2019-20, 2020-21 | observed | none | |
| 2021-22 | reconstructed | low | Every 2020-21 non-graduate is on the 2022-23 roster. The 2021 class of Kim and Nguyen fits the alternating 2/3 class sizes of 2019-2023. |
| 2022-23 to 2026-27 | observed | none | Adams was removed from 2023-24 (UVM visitor). 2026-27 is the live site. |

## Phase 2 searches
- **Raw folder:** re-read all Common Crawl captures (cc, cc_b, cc_c) and the profile dumps.
- **Wayback host audits:**
  - Windows: 2012-06..2014-09, 2018-03..2019-11 and 2021-03..2023-03.
  - Hosts: every host in the table above, plus medicine.utah.edu/gme and medicine.utah.edu/surgery.
  - Prefix CDX: news, about, residency, residents, academic, newsletters, res-profiles, and current-residents.
- **Link audit:** checked the residency index, newsletters, teaching rounds (2012, 2013), events and alumni captures inside the gaps.
  - Teaching rounds lists "Ramin Eskandari, M.D., Chief Resident" on 2013-06-12.
  - Match Day 2022 names only the 2022 interns.
  - No other page names residents.
- **Common Crawl:** ran the whole `edu,utah,medicine)/neurosurgery` prefix over every crawl in 2012-2014 (11), 2018-2019 (24) and 2021-2022 (15). No crawl failed, and no roster was found apart from the known 2019-10/12 and 2022-11 pages.
- **PubMed affiliation mining:** ran for each gap window. It found no unknown resident. Per-person affiliation histories settled several outcomes (below).

## Roster changes (phase 2)
- **Added:**
  - Osama Jamil, PGY-2 in 2013-14. His profile says he did a general-surgery internship at Harlem Hospital before joining Utah.
  - Baker, Gamboa and Sherrod, PGY-1 in 2018-19. All three are 2025 alumni, and Gamboa and Sherrod are on a Utah Neurosurgery paper received in 2019-03.
  - Sarah Nguyen, PGY-1 in 2021-22 (Utah Neurosurgery affiliation on a paper received in 2021-07).
- **Removed:**
  - Chih-Ta Lin (2014-15). The UVM roster lists him as "PGY5: Utah Resident".
  - Dylan Adams (2023-24). The UVM roster lists him in every year from PGY-1 in 2020-21 to PGY-7 in 2026-27, so he was a UVM resident spending that year at Utah.
- **Not placed:**
  - Leo Kim, 2021-22. He was in the Case Western MSTP until 2021-22, and his PGY-1 location is undocumented.
  - Aatman Shah and Nicole Colwell, 2018-19.

## Departures (training_history rows, "[phase2 p111]")
| Name | Last seen | Outcome | Evidence |
|---|---|---|---|
| Paul Park | 2011-12 PGY-4 | unknown | Pre-2011 entrant, left Oct-Nov 2011. |
| Osama Jamil | 2014-15 PGY-3 | switched to neurology | First-author paper received 2016-03 with a Utah Department of Neurology affiliation (PMID 27113401). |
| Farah Laiwalla | 2014-15 PGY-1 | left medicine (judgement) | Papers only from Brown School of Engineering, 2019-2024. |
| Aatman Shah | 2017-18 PGY-2 | switched to dermatology | Utah Dermatology 2019-20, then Stanford, Mount Sinai and Cincinnati Dermatology. end_year 2019 (latest possible). |
| Nicole Colwell | 2017-18 PGY-1 | unknown | Later research affiliations at Rutgers NJMS Neurosurgery and NYU Ophthalmology. She is not on the Rutgers roster. end_year 2019. |
| Philip Tatman | 2024-25 PGY-1 | unknown | |
| Maren Loe | 2025-26 PGY-1 | transferred to BWH (program 37), mid-year | The MGB brochure dated 2026-01-05 lists her as a BWH PGY-1. |

## Joiners
| Name | First seen | Origin |
|---|---|---|
| Osama Jamil | PGY-2, 2013-14 | Outside general-surgery internship. |
| Nam Keun Yoon | PGY-4, 2015-16 | Transfer from Loma Linda (31); graduated 2019. |
| Guilherme Agnoletto | PGY-3, 2019-20 | International: neurosurgery residency at INC Curitiba (Brazil), then a Baptist/Lyerly Jacksonville fellowship. |
| Othman Bin-Alamer | PGY-3, 2026-27 | Transfer from Loma Linda (31). |
| Georgios Skandalakis | PGY-2, 2026-27 | His PGY-1 was at no program in this study (location unconfirmed). He was earlier a research fellow at Dartmouth-Hitchcock and UNM. He filled Loe's slot. |

## Excluded visitors (UVM)
Lin (2014-15), Ducis (2015-16), Akture (2016-17), Limoges (2019-20), Muse (2020-21) and Adams (2023-24).

## Counts
- 43 residents entered in 2011 or later.
- Class sizes by entry year:

| Entry year | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Residents | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 4 | 4 | 2 |

- Adjudication: 29 completed, 18 in training, 3 left (did not complete), 2 switched specialty, 1 left medicine, 1 transferred.

## Problems and consolidation notes
- **2012-13 is still significant.** No roster for that year exists anywhere.
- **Entry years for joiners.** The adjudicator takes a joiner's entry year from the start_year in their transfer-in row. The roster's PGY arithmetic gives an earlier year in each case:

| Name | Entry year shown | Entry year by PGY arithmetic |
|---|---|---|
| Jamil | 2013 | 2012 |
| Yoon | 2015 | 2012 |
| Agnoletto | 2019 | 2017 |
| Bin-Alamer | 2026 | 2024 |
| Skandalakis | 2026 | 2025 |

- **Program 37 (BWH):** needs a transfer-in row for Maren Loe.
- **Program 112 (UVM):** should note that Dylan Adams spent 2023-24 at Utah.
- **NPI records:** used only as supporting evidence. None of the NPI "switch" calls were used as evidence.
