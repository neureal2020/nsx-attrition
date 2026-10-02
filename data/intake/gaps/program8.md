# Program 8: Carilion Clinic-Virginia Tech Carilion (Roanoke, VA): roster gaps

- Started in 2006 as an AOA (osteopathic) program with OGME labels. ACGME initial accreditation came in 2017, continued accreditation in 2019. It takes 1 resident a year (2 in 2008, 2010, 2022 and 2026). Program length is now 7 years. In the AOA era residents graduated after OGME-6: McNeal 2013, Marvin/Logan 2014 ("Graduate 20xx" on the 2014 page), Sawvel and Synkowski left at PGY6.
- Roster file: `data/intake/rosters_program8.json`, 17 captures: 10 observed and 7 manual. Scratch files, the decoder for the JSON-embedded Drupal roster (`decode.py`), `build.py` and the CC hits are in `data/raw/extraction/p8/`.

## Hosts
| host/path | dates |
|---|---|
| www.carilionclinic.org/Carilion/Neurosurgery+Residency, `_Residency` (roster subpage `_Our_People` never archived) | 2010-02 .. 2012-07 |
| www.carilionclinic.org/education/neurosurgery-residents | 2013-02 (1 capture) |
| www.carilionclinic.org/neurosurgery/residency/current-residents (**Common Crawl only**) | 2014-07 .. 2015-09 (stale after 2014-10) |
| www.carilionclinic.org/neurosurgery/residency (+ /residents, never archived) | 2016-08 .. 2017-10 (then 301) |
| www.carilionclinic.org/graduate-medical-education/resident-fellow-directory | 2017-06 (1 capture) |
| www.carilionclinic.org/neurosurgery-residency (Drupal; roster JSON-escaped in page from 2022) | 2019-09 .. 2024-07 (301 to gme) |
| gme.carilionclinic.org/neurosurgery-residency/residents, /graduates | 2024-07 .. live (residents archived only from 2026-06) |

## Years
| AY | source | status |
|---|---|---|
| 2011-12 | manual | **missing**: reconstructed 6 (seen 2012-13 + on the graduates list) |
| 2012-13 | Wayback 2013-02-18 | observed, 7 |
| 2013-14 | CC 2014-07-24 | observed, 8 (July capture, but the content is 2013-14) |
| 2014-15 | CC 2014-10-01 | observed, 7 |
| 2015-16 | manual | **missing**: CC 2015 copies are the stale 2014-15 list; reconstructed 7 |
| 2016-17 | Wayback 2017-06-16 GME directory | observed, 6 (no PGY7 because of AOA 6-year completion) |
| 2017-18 | news feature (partial, 2) + manual 3 | **missing / partial** |
| 2018-19 | manual 4 | **missing** |
| 2019-20 | manual 3 | **missing**: the 2019-09 and 2020-12 pages list faculty only |
| 2020-21 | manual 2 | **missing**: the 2021-08 and 2021-10 pages list no residents |
| 2021-22 | Wayback 2022-05-17 | observed, 7 |
| 2022-23 | Wayback 2022-10-06 | observed, 7 (no PGY2) |
| 2023-24 | Wayback 2023-12-04 | **incomplete**: no PGY3 or PGY5 group; Adhikari omitted |
| 2024-25 | manual 5 (bracketed) | **missing**: no capture of the gme residents page before 2026 |
| 2025-26 | Wayback 2026-06-12 | observed, 7 |
| 2026-27 | live 2026-09-27 | observed, 8. The heading still says "2025-2026", but the PGYs have advanced one year and 2 new PGY1s are listed |

Rule applied to reconstructions: only people bracketed by captures or confirmed by the graduates list. This leaves out the 2017-2020 entrants (Guilliams, Cuoco, Adhikari, Hoggarth) and Walker from 2017-18 through 2020-21, so those classes are unverified in those years.

## Departures and joiners
- **Stacy Hatcher**: PGY1 in 2021-22, gone in 2022-23 (there is no PGY2 group). The NPPES match suggests a specialty switch.
- **Brittany Stopa**: PGY1 in 2023-24 (Dec 2023 to Apr 2024), absent in 2025-26. She left in 2023-24 or 2024-25 and is not on the graduates list.
- **Evin Guilliams**: PGY7 chief in 2023-24 but **not on the graduates page**. He probably completed in 2024; this needs verifying.
- Srijan Adhikari: missing from the 2023-24 page only (page omission). He was PGY7 in 2025-26, so this is not a departure.
- Joiner **Thomas Frimpong**: first seen OGME-4 in 2013-14 and absent from the complete Feb-2013 list. Same class as Danison. Graduated.
- Joiner **Evan Courville**: first seen PGY3 in 2025-26 (entry year 2023) but not on the 2023-24 page. He probably joined in 2024-25 at PGY2, possibly as Stopa's replacement.
- **Blake C. Walker, MD**: on the graduates list between Busch and Benko, never on any captured roster. Probably a transfer in; entry and graduation years are unknown.

## Alumni → training_history (14 rows, program_page)
Graduation years were taken from the page where stated: McNeal 2013, Marvin 2014, Logan 2014, Cuoco 2025. Others were inferred from the terminal PGY on the rosters: Sawvel 2015, Danison 2016, Frimpong 2016, Synkowski 2017, Prickett 2018, Benko 2022, Klein 2023. Rogers, Busch and Walker are stored with end_year NULL (year unknown). Qandah (graduated 2010) was skipped because it is before 2012.

## Adjudication
15 completed, 8 in training, 1 left (switched specialty: Hatcher), 1 left with outcome unknown (Stopa). 19 residents entered in 2011 or later, plus Walker whose entry year is unknown.

## Phase 2 (2026-09-28)
- Walker = Blake Walker, Wayne State/DMC (program 125) PGY1-5 2014-19. His DMC affiliation was on a paper received Nov 2019, and he has a Carilion Neurosurgery affiliation from Nov 2020 (PMID 33322413). He transferred in at PGY7 in 2020-21 and graduated in 2021.
- Courville transferred in at PGY2 in 2024-25 (UNM surgery and research 2021-24; Carilion affiliation Feb 2025).
- Guilliams completed in 2024 (PGY7 on the roster; NPI now neurosurgery). Rogers graduated in 2019 (MD Anderson fellowship affiliation in 2020). Busch probably graduated in 2021.
- Hatcher left after PGY1 in 2021-22 and Stopa left after PGY1 in 2023-24. Both outcomes are unknown. Hatcher's NPI is a student record, so the "switch" in the phase-1 adjudication is wrong.
- A 2010 Carilion GME article shows one neurosurgery intern in 2010, so Frimpong was a transfer in.
- Reconstructed rows added: Guilliams 2017-21, Cuoco 2018-21, Walker and Busch 2020-21, Courville and Bhutada 2024-25. All are backed by PubMed affiliations or later rosters.
- Per-year status and significance are in the JSON. All gaps are now rated low: no roster exists for 2017-21 or 2024-25, but every class is accounted for.
- The Common Crawl 2015-2025 rerun with the fixed filter was still running at handback: log `data/raw/extraction/p8/phase2/cc_pairs_log.txt`, pid 57952, restarted after first run died at 3 pairs. The 2019-2021 pages are JS shells, so it is not expected to turn up a roster.
