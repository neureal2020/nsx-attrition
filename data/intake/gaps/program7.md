# Program 7 — Beth Israel Deaconess Medical Center Program (BIDMC/BMC Neurosurgical Residency), Boston MA

- 7-year program, combined BIDMC + Boston Medical Center (PD James Holsapple, BMC). ACGME RRC approval April 2016; first resident July 2016; 1 resident/year (two PGY1s listed in 2026-27).
- **first_class_year: 2016.** 2011-12 .. 2015-16 are not applicable (program did not exist).
- Residents entering 2016+: **13** (incl. one PGY5 transfer-in).

## Hosts / paths
| URL | Dates | Notes |
|---|---|---|
| bidmc.org/Medical-Education/Departments/SurgicalEducation/Training-Programs/Neurosurgery.aspx | 2016-09 .. 2018-01 | roster from 2017-07; 302 from 2018-04; DB `programs.website`, now 404 |
| bidmc.org/medical-education/medical-education-by-department/surgery/surgery-training-programs/neurosurgery | 2019-07 .. 2025-05 | roster; lost roster by 2025-09; 301 2026-03 |
| research.bidmc.org/surgery-gme/neurosurgical-residency | 2025-09 .. live | current roster + alumni list |
| bidmc.org/education-training/graduate/residencies/neurosurgical | live | stub linking to research.bidmc.org |
| bmc.org/neurosurgery/team | 2019-08 .. 2021-04 | partner site, flat resident list (cross-check only) |
| bmc.org/neurosurgery/neurosurgery-residency | 2021-05 .. 2023-03 | description only |

## Years
| AY | Source | Capture | n |
|---|---|---|---|
| 2016-17 | **reconstructed** (significance none) | – | 1 (Filippidis PGY1) |
| 2017-18 | wayback .aspx | 2017-10-15 | 2 |
| 2018-19 | wayback new path | 2019-07-22 (content-dated 2018-19) | 3 |
| 2019-20 | wayback | 2019-10-14 | 4 |
| 2020-21 | wayback | 2020-10-31 | 6 |
| 2021-22 | wayback | 2021-09-24 | 7 |
| 2022-23 | wayback | 2023-01-17 | 8 |
| 2023-24 | wayback | 2024-04-15 (page stale until then) | 7 |
| 2024-25 | wayback | 2024-12-07 | 7 |
| 2025-26 | wayback research.bidmc.org | 2026-02-19 | 7 |
| 2026-27 | live | 2026-09-27 | 8 |

Missing years: none. Reconstructed: 2016-17.

## Gap details
- **2016-17 (significant, low risk):** no roster published. Program-page captures 2016-09-21, 2017-04-06, 2017-04-29, 2017-06-09 have no resident list; "Meet Our Residents" first appears 2017-07-10. gapaudit 2016-07..2018-08 over bidmc.org Surgery/Neurosurgery, SurgicalEducation and bmc.org/neurosurgery: no other roster page. Common Crawl phase-1 pass hit HTTP 403; **phase 2 retry succeeded** over all 21 crawls of 2016-17 (see below). Filippidis reconstructed as PGY1 (PGY2 in 2017-18, alumni graduation 2023). With 1 slot/year, the only way an unseen person could hide is a 2016 intern who left before July 2017 — not observable.
- **2018-19:** no capture between 2018-01 and 2019-07 (site migration); the 2019-07-22 capture is content-dated 2018-19 (Mackel PGY1, Powers absent; 2019-09 capture adds Powers).
- **2023-24:** page not updated until spring 2024 (Oct 2023 capture still shows 2022-23); the 2024-04-15 capture is used.

## Alumni page
research.bidmc.org/surgery-gme/neurosurgical-residency: 2023 Filippidis, 2023 Harris, 2024 Penumaka, 2025 Mackel, 2026 Powers — all 5 inserted into `training_history`.

## Consistency
Every person has a single entry year (year − PGY + 1). Class sizes: 1 per entry year 2016-2025 (2016 has Filippidis + Harris-by-arithmetic), 2 in 2026.

**Departures before terminal PGY:** none. Every resident seen is either a graduate on the alumni list or on the live 2026-27 roster.

**Joiners above PGY-1:** Dominic Harris — transferred in July 2020 at PGY5 from University of New Mexico (program 97, accreditation withdrawn effective 2020-06-30); PGY7 2022-23, graduated 2023. training_history th_id 3232 (transfer-in) + 775 (alumni).

## Adjudication
5 COMPLETED (Filippidis, Harris, Penumaka, Mackel, Powers), 8 IN TRAINING, 0 left.

## Problems
- `programs.name` carries ACGME PDF footer junk; `programs.website` is dead (404). The live roster is research.bidmc.org.
- 2026-27 lists two PGY1s (Jha, Serrato): the complement may have increased.
- Enriquez-Marulanda (BIDMC postdoc, BMC clinical fellow) and Filippidis (BMC pre-residency fellow) entered at PGY1. They are not transfers.
- Common Crawl 403 of 2026-09-27 resolved on retry 2026-09-28.

## Phase 2 (2026-09-28)
- **2016-17 closed (significance none).** CC retry, all 21 crawls 2016-17 OK (`phase2/cc1617.log`, `phase2/ccneuro.log`). BIDMC program page (CC 2017-06-24) still has no roster. bmc.org/neurosurgery/team captures 2016-09-28, 2016-10-26, 2017-02-24, 2017-05-26 list Filippidis (headed "Neurosurgical Fellows") as the only continuing trainee; Tabbara, Thaci, Tschoe appear only 2016-09/10 (pre-existing non-ACGME fellows). With complement 1/yr and Filippidis graduating 2023 after 7 years, no other 2016 entrant is possible. PubMed 2016-18 BMC/BIDMC/BU neurosurgery affiliations (`phase2/pubmed_2016_2018.txt`) show mostly Ogilvy-lab research fellows and no other resident.
- **Harris** transfer-in from UNM recorded (th_id 3232).
- **BMC research affiliates, not residents:** Omofoye (2017-18; absent from the 2017-18 roster), Hamade (2023-25, BU/St Elizabeth's; absent from 2023-24 and 2024-25 rosters), Wetsel (2025; absent from every roster). None were BIDMC/BMC residents, so there are no departures from program 7.
- Remaining significant gaps: none.
