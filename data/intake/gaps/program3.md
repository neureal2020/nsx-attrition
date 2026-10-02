# Program 3: Ascension St. Vincent Hospital Program (Indianapolis, IN)

- Length 7 years (PGY-7 enfolded fellowship, per Program Overview). ACGME complement 1/yr in DB; actual classes: 2025 = 2, 2026 = 1.
- **New program: first class entered July 2025** (Goodman Campbell news post 2025-04, "our inaugural resident class"). The years 2011-12 to 2024-25 are before the program started. They are not gaps.
- Faculty and web host: Goodman Campbell Brain and Spine.

## Hosts
| Host/path | Dates | Notes |
|---|---|---|
| www.goodmancampbell.com/ascension-st-vincent-hospital-indianapolis-neurological-surgery-residency-program/, /current-residents/ | 2024-11 to live | Roster page. It said "More information coming soon" in 2024-11 and 2025-01 |
| medicaleducation.ascension.org/.../home/neurological-surgery (DB website) | 2025-09 to 2025-10 captures; 404 live | Welcome text and contact only, no roster |
| goodmancampbell.com pre-2017 (.cfm pages, ResidentRoster 2011-12..2016-17 jpg/pdf) | 2010-2017 | These rosters are **Indiana University's (program 28)**, from when GCBS was IU faculty. Not used |

## Observed years
- 2025-26: Wayback 20251015085242 current-residents: Anthony Dragun PGY1, Geoffrey O'Malley PGY1.
- 2026-27: live 2026-09-27: Dragun PGY2, O'Malley PGY2, Pratheek Makineni PGY1. A 2026-07 news post confirms three residents in total.

Reconstructed: none. Missing: none. 2011-2024: program did not exist.

## Consistency
Entry years are consistent: Dragun 2025, O'Malley 2025, Makineni 2026. No departures and no joiners. Alumni page: none, because there are no graduates yet. No training_history rows.

## Problems
The DB `programs.website` link now returns 404, and the roster is on goodmancampbell.com. The complement of 1 in the DB does not match the 2-person inaugural class.

## Phase 2 (2026-09-28)
- **Completeness.** Both observed years are complete:
  - 2025-26 = 2 PGY1. This matches the inaugural class of 2 named in the 2025-04 post. All 5 distinct captures of current-residents from 2025-04 to 2026-06 are identical in Wayback and in CC.
  - 2026-27 = 2 PGY2 + 1 PGY1. The 2026-07 post says "third resident".
  - No resident appears once and then vanishes.
- **History.** This is a new ACGME program (ID 1601700001), and its 2026 status is "Continued Accreditation without Outcomes". The associate PD appointment dates from 2024, and the first class started 2025-07. It is not ex-AOA: there is no earlier St. Vincent neurosurgery residency on any host or in PubMed affiliations. 2011-2024 = not_applicable.
- **Terminal PGY.** 7 for the 2025 and 2026 cohorts (PGY-6 chief, PGY-7 enfolded fellowship). The first graduation is expected 2032, so there are no training_history rows.
- **Complement.** The DB complement is 1. The 2025 class of 2 is above complement but confirmed.
- **Searches.**
  - Wayback digests of all roster, faculty and program pages.
  - Common Crawl with the fixed filter, over all 2024-2026 crawls for both hosts. There were 0 failed crawls.
  - PubMed affiliations.
  - crossmatch (none).
  - Checks for the known parser misses (none apply).
- **Significance.** None for every year. Nothing remains.
