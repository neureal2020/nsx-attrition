# Program 81 - University of Connecticut School of Medicine Program (Farmington CT)

- Length 7 yrs, complement 1/yr. **First class 2020** (Erica Shen, 'our inaugural neurosurgery resident'). 2011-12..2019-20 are not gaps: the program did not exist (UConn GME sponsored-program list 2012-2018 has no neurosurgery residency; residency home page first archived 2019-09-19).
- Residents entering 2020+: 7. Observed years: 2020-21 .. 2026-27 (all). Reconstructed: none. Missing: none.

## Hosts
- https://health.uconn.edu/graduate-medical-education/neurological-surgery-residency-program/ (program home; no roster until the Current Residents subpage) (2019-09-19 (first capture) -> live 2026-09-27)
- https://health.uconn.edu/graduate-medical-education/neurological-surgery-residency-program/current-residents/ (WP page created 2021-10-18; linked from Jan 2022) (2024-07-08 (first capture) -> live 2026-09-27)
- https://health.uconn.edu/neurosurgery/our-team/ (dept Our Team page, 'Residents' section with PGY) (2021-07-03 (first capture with residents; 2019 captures have no residents; no 2020 captures) -> live 2026-09-27)
- https://health.uconn.edu/neurosurgery/ (dept home: 'Welcome' news items per new resident) (2020-08-01 (Shen inaugural-resident item) -> live 2026-09-27)
- http://gme.uchc.edu/programs/sponsored.html (old GME host: sponsored-program list, 2012-2018, no neurosurgery residency) (2012-05 -> 2018-02)

## Year by year
- **2011-2012..2019-2020**: Program did not exist. UConn GME sponsored-program list (gme.uchc.edu/programs/sponsored.html, 27 captures 2012-2018) lists Neurology, Neuromuscular, Neurovascular but no neurosurgery residency; gapaudit 2010-2020 on neurosurgery.uchc.edu, uchc.edu/neurosurgery, health.uconn.edu/neurosurgery, gme.uchc.edu/programs/neuro* found no neurosurgery residency pages. Residency home page first archived 2019-09-19 (recruiting for 2020); dept home Aug 2020 welcomes Erica Shen as 'our inaugural neurosurgery resident'.
- **2020-2021**: No roster page captured (our-team: captures 2019-09 then 2021-07; GME current-residents page not yet created). Year taken from dept home-page news item (2020-11-01 capture): Erica Shen, inaugural (sole) resident; PGY-1 inferred from PGY2 in 2021-22. Common Crawl 2020-2021 checked for our-team/GME pages (see problems).
- **2021-2022**: Our Team 2021-10-29: Diaz PGY1, Shen PGY2.
- **2022-2023**: Our Team 2022-11-26: Shen PGY3, Diaz PGY2, Burch PGY1.
- **2023-2024**: Our Team 2023-12-10: Shen PGY4, Diaz PGY3, Burch PGY2, Patil PGY1.
- **2024-2025**: Our Team 2024-12-07 (= GME current-residents 2024-07-08): Diaz PGY4, Shen PGY4 (second year at PGY4), Burch PGY3, Patil PGY2, Nwankwo PGY1.
- **2025-2026**: Our Team 2025-11-11 (= GME 2026-02-12): Diaz 5, Burch 4, Patil 3, Nwankwo 2, Venero 1. GME page 2025-08-09 still listed Shen PGY4 (stale carry-over); she is absent from every later list.
- **2026-2027**: Live GME current-residents 2026-09-27 (advanced, new intern): Rao 1, Venero 2, Nwankwo 3, Patil 4, Burch 5, Diaz 6. Dept Our Team live and 2026-06-13 capture agree.

## Class sizes (entry year)
2020 Shen; 2021 Diaz; 2022 Burch; 2023 Patil; 2024 Nwankwo; 2025 Venero; 2026 Rao - one per year, matches complement.

## Departures
- **Erica Shen** (entry 2020, inaugural resident). Listed PGY4 in 2023-24 AND 2024-25 (consistent with a research year). The GME page of 2025-08-09 had been updated for 2025-26 but still showed her at PGY4, not advanced. She is gone from the dept page by 2025-11-11 and from the GME page by 2026-02-12, and absent in 2026-27.
  - **Phase 2 evidence:** a July 2025 bioRxiv GLASS preprint (doi 10.1101/2025.07.11.664189, PMID 40791422) lists her at the Department of Neurosurgery, Yale University. This is the Verhaak lab.
  - **Identity:** she is the same OpenAlex author (A5062832120) as on her UConn/JAX papers, and her 2022 paper is co-authored with Verhaak and Bulsara.
  - **Not a transfer:** she is on no Yale NS residency roster (program 123, 2024-27), so the Yale link is a research affiliation.
  - **Outcome:** LEFT, did not complete. Destination and specialty are unknown. The NPPES "switch" is a different person (respiratory therapist, CA) and is not used.
  - **Recorded:** a training_history row (th_id 3389): completed='no', departure_type='unknown', end_year 2025. Evidence: `data/raw/extraction/p81/phase2/shen_evidence.json`.
  - **Significance:** real attrition in the 2020 cohort, now evidenced. The small residual uncertainty is whether she was nominally enrolled into early 2025-26.

## Joiners
None. (Taylor Burch did a pre-residency fellowship at Lahey before entering as PGY1 in 2022.)

## Adjudication
6 IN TRAINING; 1 LEFT -> did not complete (Shen, from the phase-2 training_history row; the wrong-person NPI switch call is superseded).

## Program length
terminal_pgy_by_entry_year: 2020-2026 all 7 (ACGME 7-yr program since founding; no length change, not AOA).

## Problems
Common Crawl pass 2020-2021 (our-team and GME residency prefixes) found no 2020-21 roster page, only GME program home/application/contact pages; failed crawls to retry: CC-MAIN-2020-24 (our-team prefix), CC-MAIN-2021-39 (GME residency prefix) - range request failures. 2020-21 rests on the inaugural-resident news item (single resident, PGY inferred). Name variant: 'Aliana Rao' (GME bio, NPPES 1750194445 Farmington CT) vs 'Alina Rao' (dept page) - canonicalised to Aliana Rao. The former SWITCHED SPECIALTY call for Shen is superseded by the training_history row. No alumni page; no graduates yet (first possible graduation June 2027). Phase-1 failed CC crawls (CC-MAIN-2020-24, 2021-39) not retried: 2020-21 can hold only the single inaugural resident, so they cannot change any count. Hartford Hospital is listed only as a clinical site; it hosts no separate program roster.

## Year status and significance (phase 2)
| Year | Status | Significance | Reason |
|---|---|---|---|
| 2011-12..2019-20 | not_applicable | none | The program did not exist. |
| 2020-21 | observed | none | No roster page, but the department news names the sole inaugural resident. With a complement of 1, and the 2021-22 roster, there is no room for an unseen resident. |
| 2021-22 | observed | none | 2 residents, PGY1-2. |
| 2022-23 | observed | none | 3 residents, PGY1-3. |
| 2023-24 | observed | none | 4 residents, PGY1-4. |
| 2024-25 | observed | none | 5 residents. Shen was held at PGY4 alongside Diaz PGY4; no PGY5 cohort exists. |
| 2025-26 | observed | none | 5 residents (entries 2021-25). Shen had left; her only trace is the unadvanced GME listing of Aug 2025. |
| 2026-27 | observed | none | 6 residents, PGY1-6. There is no PGY7 because the only 2020 entrant left. |

Every year's count equals the number of classes times the complement of 1.

## Phase 2 completeness audit
I re-read all the parsed captures (`wb_rosters.txt`), the live pages and the unparsed `cc/` captures. None of the phase-1 parser misses occur here:
- no 'Chiefs' heading
- no residents on a faculty menu
- no inline 'Name, PGY' entries
- no suffixed names such as 'III' or 'Jr'

The `cc/` files are GME program home, application, contact and clinical-sites pages, plus one faculty bio. None of them lists residents.

## Phase 2 searches
Searches that found nothing new:
- **UConn sites:** WordPress search on the neurosurgery and GME sites. The GME hits for 'Shen' are other people.
- **Archived dept home:** Wayback captures of 2025-02, 2025-06, 2025-09 and 2026-01 (saved in `phase2/`).
- **UConn Today:** the 2025-08-21 residency feature does not mention her.
- **Yale:** her profile page returns 404, and she is not on the Yale rosters.
- **Cross-program:** crossmatch.json has nothing for program 81.

Searches that found evidence:
- **PubMed and OpenAlex:** these found the Yale affiliation described under Departures.

## Remaining
Shen's clinical status after 2025 is not public on the allowed sources. This is not significant for the roster: the departure itself is established.
