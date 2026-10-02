# Program 71: University of Arizona College of Medicine - Phoenix (Banner - UMC Phoenix) neurosurgery

The DB website (college.mayo.edu ... arizona) is Mayo Clinic Arizona (program 39) and is wrong for this program. The real host is phoenixmed.arizona.edu. Barrow/St Joseph's (program 4) is not included here.

- Program length: 7 years. Complement: 1 per year (single PGY-1 in 2024, 2025, 2026). An extra PGY-2 (Carter) joined in 2026-27.
- **New program. First class: 2024.** The neurosurgery-banner-contact page said "does not have a UACOM-P sponsored residency or fellowship program" in every capture from 2023-12 to 2024-08-03. By 2024-09-27 it announced the new residency. The residency hub was first captured 2024-08-11. Barbagli's bio says he was the "first resident hired once they started the program in June 2024".
- Alumni page: none, because there are no graduates yet (ACGME status: Continued Accreditation without Outcomes).

## Hosts
- https://phoenixmed.arizona.edu/neurosurgery-banner-contact: from 2023-12 (states 'does not have a UACOM-P sponsored residency' through 2024-08-03) to 2024-09-27 onward announces the new residency
- https://phoenixmed.arizona.edu/neurosurgery-residency (+ /curriculum, /how-apply, /who-we-are, /who-we-are/faculty): from 2024-08-11 (first capture, Wayback and CC-MAIN-2024-33) to live 2026-09-27
- https://phoenixmed.arizona.edu/programs/graduate-medical-education/residency-programs/neurosurgery/who-we-are/neurosurgery (training sites): from 2024-08-11 to live
- https://phoenixmed.arizona.edu/neurosurgery-residency/who-we-are/current-residents: from linked from hub between 2025-07-15 and 2025-11-07; first capture 2026-01-25 to live 2026-09-27
- bannerhealth.com: the domain-wide CDX filter for neuro*surg*(resid|train|fellow) found 0 URLs. The academic-medicine page only links to phoenixmed.

## Rosters
| AY | source | PGY1 | PGY2 | PGY3 | PGY4 | PGY5 | PGY6 | PGY7 |
|---|---|---|---|---|---|---|---|---|
| 2024-25 | reconstructed (no roster published) | Barbagli* | | | | Nosova* | | |
| 2025-26 | Wayback 2026-01-25 (same in 2026-06-10) | Bauer | Barbagli | | Wetsel | | Nosova | |
| 2026-27 | live 2026-09-27 | Davidar | Bauer, Carter | Barbagli | | Wetsel | | Nosova |

## Gaps
- **2024-25 (reconstructed, significance none):** program's first year (June 2024); no roster was ever published. Only two residents: Barbagli PGY-1 (bio: "first resident hired once they started the program in June 2024"; NPPES 207T AZ Feb 2024) and Nosova PGY-5 (PGY-6 in 2025-26; Banner/UACOM-P affiliation continuous since early 2023). Complement 1/yr and the first Match intern was Bauer (2025). PubMed affiliation mining (neurosurgery + Banner/UA + Phoenix, 2024-25) shows only these two plus faculty, spine research fellows and students, so nobody could have entered and left unseen. Wetsel was at Boston Medical Center in 2024-25.
- 2025-26 and 2026-27: observed.

## Consistency, departures and joiners
- Departures: none.
- Joiners (training_history rows 3078-3080, program 71):
  - Nosova: from UC Davis (program 77, PGY-1..5 2018-19..2022-23). At Banner from early 2023 (before accreditation); in the program at PGY-5 2024-25, PGY-6 2025-26, PGY-7 2026-27. Lost one PGY level in the move.
  - Wetsel: from UMMC Mississippi (program 93, PGY-1..3 2019-22), then a research interval at Boston Medical Center/BU (PubMed 2024-12..2025-09). Joined at PGY-4 in 2025-26.
  - Carter: EVMS MD 2025, PGY-1 2025-26 in UACOM-P General Surgery (PMID 41804424), then joined neurosurgery at PGY-2 in 2026-27.

## Phase 2
Searched: phase-1 raw captures, live bios, PubMed per name and by affiliation 2024-25, local NPPES, program 77/93 rosters. Remaining: none.

## Problems
Program DB website was wrong (Mayo Clinic Arizona, program 39); real host is phoenixmed.arizona.edu/neurosurgery-residency. Common Crawl CC-MAIN-2025-08 failed for prefix edu,arizona,phoenixmed)/neurosurgery-residency (cluster.idx range request failed); low value since no roster page existed until after 2025-07. No graduates yet (ACGME 'Continued Accreditation without Outcomes'). Nosova's 2023-24 status at Banner (pre-accreditation) is unclear. Program 77 has no transfer-out row for Nosova (left to that agent). NPPES API unreachable; used local db/nppes.db.
