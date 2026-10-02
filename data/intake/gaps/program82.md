# Program 82: University of Florida Program (Gainesville, FL)

7-year program, usually 3 residents a year (2 in the 2005-06 classes, 4 in 2019). All 16 academic years 2011-12 through 2026-27 were observed. No year was reconstructed and none is missing. Several years are **incomplete** because the PGY-7 (or extended PGY-8) residents were left off the page. The alumni graduation rows cover those residents.

## Hosts
| Host / path | From | To |
|---|---|---|
| http://www.neurosurgery.ufl.edu/residency/current-residents.shtml (+ alumni.shtml, per-resident `<slug>.shtml` bios); static, flat list, no PGY | 2009-06 | 2012-09 |
| http://neurosurgery.ufl.edu/residency/current-residents/ (WordPress; /residency/alumni/) | 2012-11 | 2017-04 (301 to https) |
| https://neurosurgery.ufl.edu/residency/current-residents/ (+ /residency/alumni/) | 2017 | live 2026-09-27 |

Wayback has no 200 capture on the host between 2017-01 and 2019-07. Common Crawl (2017-01 to 2019-04) fills that gap. The live site has no sitemap.xml (404).

## Year by year
| AY | Source | Notes |
|---|---|---|
| 2011-12 | WB 2011-10-13 .shtml | 20 names, no labels; PGY from bio start/finish dates |
| 2012-13 | WB 2013-01-13 | flat list; **Rahman (PGY8, alumni 2013) not listed** |
| 2013-14 | WB 2013-11-27 | flat; Fargen/Vasquez-Castellanos = Chief (PGY6); **Cox, Sporrer (PGY7) not listed** |
| 2014-15 | WB 2014-12-17 | headings; Fargen under Fellows (enfolded ESN), added as PGY7; **Vasquez-Castellanos not listed** |
| 2015-16 | WB 2015-12-15 | Titsworth's stale "(PGY5)" tag -> PGY6; **Hooten (PGY7) not listed** |
| 2016-17 | WB 2016-12-26 | **Weaver (PGY7) not listed** |
| 2017-18 | CC-MAIN-2017-34 2017-08-24 | **Hartman, Rokicki (PGY7) not listed** |
| 2018-19 | CC-MAIN-2018-43 2018-10-20 | **Hilliard, Sindelar (PGY7) not listed** |
| 2019-20 .. 2022-23 | WB Sep-Nov captures | complete; Adamczak PGY8 in 2021-22 |
| 2023-24 | WB 2023-10-05 | **Laurent (alumni 2024, extra year) not listed** |
| 2024-25, 2025-26 | WB 2024-10-13, 2025-10-12 | complete |
| 2026-27 | live 2026-09-27 | advanced, 3 new interns |

## Departures (left before the terminal PGY)
| Name | Entry | Last AY / PGY | Evidence |
|---|---|---|---|
| John Bandela | 2006 | 2011-12 / 6 | gone by 2012-09; not an alumnus (NPI: switched specialty) |
| Muhammad Abd-El-Barr | 2009 | 2011-12 / 3 | gone by 2012-09; not an alumnus |
| Nathan Kohler | 2009 | 2011-12 / 3 | gone by 2012-09; not an alumnus (NPI: switched specialty) |
| Orrin Dayton | 2012 | 2015-16 / 4 | listed 2016-05, gone 2016-07 |
| Timothy O'Connor | 2014 | 2016-17 / 3 | listed CC 2017-06, gone 2017-08 |
| Mishti Chakraborty | 2011 | 2016-17 / 6 | listed CC 2017-06, gone 2017-08; not an alumnus (her class graduated 2018) |
| Carl Brophy | 2017 | 2018-19 / 2 | listed CC 2019-03, gone 2019-07 (NPI: switched specialty) |
| Rasheedat Zakare-Fagbamila | 2019 | 2023-24 / 5 | listed 2024-06, gone 2024-08 |
| Patricia Miller | 2021 | 2023-24 / 3 | listed 2024-06, gone 2024-08 |
| Derrick Lewis | 2023 | 2025-26 / 3 | listed 2025-10, gone by 2026-02 (mid-year) |

Joiners above PGY-1 (2011+): none.

## Consistency
- Every person has a single entry year across all observations.
- 49 residents entered from 2011 on.
- Graduation outside the usual 7 years: Reichwage (2006 entrant, finished 2012); Karuppiah (entered 2008 at PGY2 after an outside internship, finished 2013); Titsworth and Wilson (2010 entrants, finished 2016); Rahman, Adamczak and Laurent each took 8 years.
- Kaitlyn Barkley is the same person as Kaitlyn Melnick (name change). Abe Alvarado is Abraham Alvarado.

## Alumni
The live alumni page (https://neurosurgery.ufl.edu/residency/alumni/) lists graduates through 2025. The 2026 class (Christie, Still, Yan) is not on it yet. I inserted 34 graduation rows for 2012-2025 into training_history.

## Adjudication
37 completed, 19 in training, 7 left with unknown outcome, 3 left and switched specialty.

## Problems
The Common Crawl run finished (36 crawls, 2017-2019). Cluster.idx range requests failed for CC-MAIN-2018-05, CC-MAIN-2019-22 and CC-MAIN-2019-47. None of them is needed: neighbouring crawls cover 2017-18 and 2018-19, and Wayback covers 2019-20.


## Phase 2 (2026-09-28)

**Key finding: UF lists its PGY-7 chief residents on the "Our Faculty" site menu during their final year.** The menu is on the same captures. Cox and Sporrer (2013-14), Vasquez-Castellanos (2014-15), Hooten (2015-16), Weaver (2016-17), Hartman and Rokicki (2017-18), and Hilliard and Sindelar (2018-19) are all there. I added 9 observed PGY-7 rows, so those years are now complete.

| AY | Status | Significance | Reason |
|---|---|---|---|
| 2011-12 | observed | low | No PGY labels. PGY is taken from the bios' start/finish dates, which agree with the later labelled rosters and the alumni years. |
| 2012-13 | observed | none | Only Rahman (PGY-8) is unlisted. A UF PubMed affiliation and the 2013 alumni entry place her there. Kimball is listed as PGY-7, so Bandela's absence is real. |
| 2013-14 .. 2018-19 | observed | none | PGY-7s recovered from the faculty menu. |
| 2019-20 .. 2022-23 | observed | none | Complete. |
| 2023-24 | observed | low | Only Laurent (PGY-8) is unlisted. UF PubMed affiliations in 2023-24 and the 2024 alumni entry place him there. |
| 2024-25 .. 2026-27 | observed | none | Complete. The stale Derrick Lewis row was removed from 2025-26. |

**Terminal PGY:** 7 for every entry cohort from 2005 to 2026. Individual exceptions:
- Reichwage (2006 entrant) and Titsworth and Wilson (2010 entrants) finished at PGY-6.
- Karuppiah entered at PGY-2.
- Rahman, Adamczak and Laurent each took 8 years.

### Departures resolved
| Name | Last AY / PGY | Outcome | Evidence |
|---|---|---|---|
| Abd-El-Barr | 2011-12 / 3 | transferred to BWH (37), PGY-4 2012-13 | Both programs' rosters; BWH alumni 2016 |
| Kohler | 2011-12 / 3 | switched to radiology | PubMed: Florida Hospital radiology 2016-17, UMD interventional neuroradiology 2018. Bio identity (UW PhD, Brown MD) matches. |
| Bandela | 2011-12 / 6 | left, destination unknown | Classmate Kimball is listed as PGY-7 in 2012-13 and Bandela is not. Not on the alumni list. |
| Dayton | 2015-16 / 4 | switched to radiology | PubMed: UF Radiology 2019-2023 |
| O'Connor | 2016-17 / 3 | transferred to Buffalo (69), PGY-4 2017-18 | Both programs' rosters; UB alumni 2021 |
| Chakraborty | 2016-17 / 6 | left, destination unknown | Classmates Hartman and Rokicki are on the 2017-08 faculty menu as PGY-7s and she is not. Not on the alumni list. |
| Brophy | 2018-19 / 2 | left, destination unknown | Absent from 2019-07 on. Not in the 2024 alumni class. |
| Zakare-Fagbamila | 2023-24 / 5 | left, destination unknown | Bio emptied 2024-07. Absent from 3 later rosters, so this is not a research year. |
| P. Miller | 2023-24 / 3 | left, destination unknown | Absent from 3 later rosters |
| D. Lewis | **2024-25 / 2** | transferred to UW (114) as PGY-3 on 2025-07-01 | UW newsletter Aug 2025. The UF Oct-2025 listing was stale. |

I inserted 10 rows into training_history (3 transferred, 2 switched_specialty, 5 unknown).

Crossmatch: I confirmed the 37, 69 and 114 matches. Maryam Rahman vs Shayan Rahman (UCLA) and Patricia Miller vs Michelle Miller (Tulane) are different people.

The adjudication now gives: 37 completed, 19 in training, 5 left (did not complete), 2 switched specialty, 3 transferred.

**Remaining:** The destinations of Bandela, Chakraborty, Brophy, Zakare-Fagbamila and Miller are unknown. Their departure years are certain. No year remains significant.
