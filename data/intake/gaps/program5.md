# Program 5 - Baylor College of Medicine (Houston, TX): Phase 1 gap report

7-year program. Complement 3/yr for classes through 2018 ("We accept three residents per year", 2015 site), 4/yr from the 2019 class on.

## Hosts / paths
| URL | From | To |
|---|---|---|
| http://www.bcm.edu/neurosurgery/index.cfm?pmid=5799 (old ColdFusion "Current Residents") | 2010 | last capture 2013-02; 301 by 2016 |
| http://www.bcm.edu/neurosurgery/residencyoverview | 2012 | 301 by 2016 |
| https://www.bcm.edu/departments/neurosurgery/index.cfm?pmid=5799 (same ColdFusion site, moved; Common Crawl only, not in Wayback) | 2013 | 2014-04; 302 to new site by 2015-03 |
| https://www.bcm.edu/departments/neurosurgery/education/neurosurgery-residency/{residents,alumni} | 2015-10 (linked) | 2021-09 |
| https://www.bcm.edu/departments/neurosurgery/education/neurological-surgery-residency/{residents,alumni} | 2021-12 | live |

No other hosts found (neurosurgery.bcm.edu etc. have no captures). The /residents page existed from 2015-10 per links but was first archived 2019-08.

## Year-by-year
| AY | Source | Status |
|---|---|---|
| 2011-12 | manual (alumni) | **Reconstructed**. No capture (Wayback, CC-MAIN-2012). 18 alumni-confirmed names |
| 2012-13 | Wayback 2012-10-12 | Observed, 19 |
| 2013-14 | Common Crawl CC-MAIN-2014-10 (2014-03-11) | **Observed (phase 2)**, 21, incl. Zheng Lan PGY-3 |
| 2014-15 .. 2017-18 | manual (alumni + phase-2 evidence) | Reconstructed, **low** significance (see Phase 2) |
| 2018-19 | Common Crawl CC-MAIN-2019-04 (2019-01-16) + 2019-05-20 supplement | Observed, 22+1 |
| 2019-20 | Wayback 2019-08-19 | **Incomplete**: PGY-1 group missing (Sharma, Jackson, McGinnis, Snyder) |
| 2020-21 .. 2025-26 | Wayback (Aug-Jan captures) | Observed, complete |
| 2026-27 | live 2026-09-27 | Observed, 28 |

Reconstruction only uses alumni-page graduates at PGY = AY - (grad-7) + 1, which matches every observed entry year. It leaves out anyone who left or joined inside the gap: Zheng Lan, Derek Lu, Venita Simpson and Patrick Cotton are not reconstructed there.

## Departures (left before PGY-7)
- **Zheng Lan**: last seen 2012-13 PGY-2 (2011 class). Not an alumnus. He left sometime in 2013-2018 (unobserved). A 2015 PubMed paper has a BCM neurosurgery affiliation.
- **Derek Lu**: last seen 2018-19 PGY-3 (CC 2019-01-16), gone by 2019-03-22. Not an alumnus. 2016 class.
- **Miller Douglas**: 2022-23 PGY-1 only. Replaced in his class by Apokremiotis.
- **Jackson Allen**: 2023-24 PGY-1 only (through 2024-06). Replaced by Varela.

## Joiners (above PGY-1)
- **Venita Simpson**: first seen 2018-19 PGY-7, graduated 2019. Not a 2012-13 PGY-1, so she joined at an unknown date in 2013-2018.
- **Patrick Cotton**: 2018-19 PGY-2, first listed May 2019 (absent Jan/Mar 2019). Graduated 2024.
- **Panayotis Apokremiotis**: 2023-24 PGY-2.
- **Samantha Varela**: 2024-25 PGY-2.

## Class sizes by entry year (2011+; 60 residents)
2011: 3 (Cherian, Sen, Lan) / 2012: 3 + Simpson / 2013-2015: 3 each / 2016: 3 (Lu left) / 2017: 3 + Cotton / 2018: 3 / 2019-2021: 4 / 2022: 4 + Apokremiotis (Douglas left) / 2023: 4 + Varela (Allen left) / 2024-2026: 4.

## Alumni
https://www.bcm.edu/departments/neurosurgery/education/neurological-surgery-residency/alumni lists graduates from 1995 to 2026. 44 graduations for 2012-2026 were inserted into training_history. Name variants were canonicalised: Hudin Jackson-Sarnor to Hudin Jackson, JP McGinnis to John McGinnis, "Rita Synder" to Rita Snyder, A. Basit Khan to Abdul Khan, Ben Larkin to Michael Larkin.

## Adjudication (16_adjudicate)
44 COMPLETED, 28 IN TRAINING, 4 LEFT (Lan, Lu, Douglas, Allen). The adjudicator gives Simpson entry year 2012 by PGY arithmetic, but she was actually a late joiner.

## Problems
The gap in 2013-14..2017-18 means any 2013-2017 attrition or transfer that is not visible on the alumni list or the 2018-19 roster cannot be seen. Only Lan's and Simpson's cases are known to fall inside it. 2019-20 is incomplete. Scratch files: data/raw/extraction/p5/ (build.py, cc_pmid.py, cc/).

## Phase 2 (2026-09-28)
**Closed:** 2013-14 is now observed. The old ColdFusion roster (pmid=5799) had moved to `/departments/neurosurgery/index.cfm`. Wayback never captured that path, and phase 1 scanned only `/departments/neurosurgery/education` in CC. CC-MAIN-2014-10/2014-15 hold it ("Last modified July 09, 2013"; complete, 21 residents).

**Still reconstructed but low significance: 2014-15..2017-18.** Every CC crawl 2013-2018 was rescanned on `edu,bcm)/departments/neurosurgery` and `edu,bcm)/neurosurgery`, with the fixed filter and pmid URLs, and the failed crawls (2015-18, 2017-13, 2019-22, 2012) were retried successfully. The Wayback gapaudit ran over the dept, education, GME and surgery hosts. From 2015-03 the new residency page (which links /residents) is crawled almost monthly, but /residents itself never is. No resident could have entered or left unseen, for three reasons:
- Every class (2007-2017 entrants) is complete on both sides of the gap: the 2013-14 roster, the 2018-19 roster and the alumni list.
- The BCM people-profile links on the 2019-01 roster are time-based UUIDs. Their creation dates match intern start for each class: 2014-07-03, 2015-06-24, 2016-06-24 and 2017-04-29.
- Complement stayed 3/yr.

The only residual risk is an above-complement resident who both entered and left inside the gap.

Rows added to the reconstruction:
- Lan: 2014-15 PGY-4 (PMID 25800940, received Nov 2014, BCM neurosurgery).
- Simpson: PGY-4..6 for 2015-18.
- Lu: 2016-17 PGY-1 and 2017-18 PGY-2 (PGY-3 Jan 2019; PMID 30230171, received Apr 2018).

**Low significance:**
- 2011-12: no capture. CC-MAIN-2012 and 2009-10 were checked on both paths.
- 2019-20: the missing PGY-1 group is a full class of 4, seen as PGY-2 in 2020-21.

**Outcomes (training_history, 7 rows inserted):**
- Zheng Lan left after 2014-15 (end 2015, switched_specialty). He was at MD Anderson cancer biology from 2016, then in neurocritical care at Emory (2020) and critical care/neurology at Montefiore (2025).
- Derek Lu (end 2019), Miller Douglas (2023) and Jackson Allen (2024): completed=no, departure type unknown.
- Joiner rows for Cotton (2019, PGY-2), Apokremiotis (2023, PGY-2) and Varela (2024, PGY-2).
- **Venita Simpson arrived Oct 2015 at PGY-4.** Her profile UUID was created 2015-10-13. She filled Lan's slot. Her transfer rows (Upstate end 2015, Baylor start 2015) were already inserted by the program-63 agent (th 2783/2784), so no duplicate was added.

**Leads:** Varela was probably UNM's (program 97) PGY-1 in 2023-24. She has UNM neurosurgery affiliations in 2023, UNM's 2023-24 roster is unobserved, and UNM has no 2023 entrant seen at PGY-2. This is unconfirmed.

Adjudication after reload: 44 completed, 28 in training, 3 left (did not complete), 1 switched specialty.

Scratch: data/raw/extraction/p5/phase2/ (cc_scan.py, cc_scan.log, cc/, cc2012/, update_rosters.py, gapaudit.log).
