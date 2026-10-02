# Program 68: UMass Chan Medical School Program (Worcester, MA)

This is a new 7-year program with 1 resident per year. The first resident (Rrita Daci) started in July 2019, so `first_class_year` = 2019 and the years 2011-12 through 2018-19 are pre-program, not gaps. Neurosurgery was a division of the Department of Surgery until 2012, when it got department status. The roster is in `data/intake/rosters_program68.json`. Scratch files are in `data/raw/extraction/p68/` (build.py, cc/, cdx_prefix.txt).

## Hosts / paths
- www.umassmed.edu/Surgery/Neurosurgery_*.aspx: the division under Surgery, with only faculty and contact pages. Captured 2010-05 to 2010-11.
- www.umassmed.edu/surgery/divisions-and-programs/neurosurgery_aboutus/: division pages, redirected (301) by 2015-09.
- www.umassmed.edu/neurosurgery/: the department site, 2015-10 to live. The live site returns a Cloudflare 403 challenge.
- /neurosurgery/residency: the residency page, 2019-01 to 2021-10. It announced and listed residents and was redirected (301) by 2024-07.
- /neurosurgery/neurosurgery-residency/who-we-are/our-residents/: captured 2024-04 to 2025-02.
- /neurosurgery/neurosurgery-residency/who-we-are/aans-student-chapter/: lists every resident with their PGY as "resident advisors". Captured 2022-12 to 2025-06.
- umassmemorial.org: no neurosurgery residency pages were found.

## Years
- **Observed:** 2019-20, 2020-21 (weak, from Common Crawl), 2021-22, 2022-23, 2023-24, 2024-25
- **Reconstructed (partial):** 2025-26
- **Missing:** 2026-27

## Gap details
- **2020-21:** Wayback has no capture of any roster page between Dec 2019 and Oct 2021. I used a Common Crawl capture of the residency page (CC-MAIN-2020-29, 2020-07-12). It lists Daci as the first resident and announces that Owusu-Adjei "will join us in July 2020". The PGYs are inferred.
- **2022-23:** The roster page itself was not captured. I used the AANS chapter page (Wayback, 2022-12-21), which lists all 4 residents with their PGYs, so the year is complete.
- **2023-24:** The only captures are from April 2024. They are consistent with neighbouring years.
- **2025-26 (significant):** No roster capture exists after Feb 2025 in Wayback or in any of the 72 Common Crawl crawls from 2019 to 2026. The 2025 intern is unseen, and so is Daci's PGY-7 year.
- **2026-27 (significant):** The live page is blocked by Cloudflare (403), and I did not bypass it.

## Departures and joiners
There are none. Each class from 2019 to 2024 has exactly one resident, and each is seen every year through 2024-25.

## Adjudication
All 6 residents are "in training". Residents entering 2011+: 6. There is no alumni page (no graduates yet), so no `training_history` rows were inserted.

## Problems
- The Cloudflare block on the live site means 2026-27 needs a browser or a manual check.
- Name variants were merged: "Brittany Owusu-Adjei Thomson" is stored as Brittany Owusu-Adjei, and "Jeewoo 'Chelsea' Lim" as Chelsea Jeewoo Lim.
- There were no Common Crawl failures.

## Phase 2 (2026-09-28)
- **2025-26, partly closed.** The department's "Recent Publications" news page (Wayback 2025-09-10, with the same text in Dec 2025 and Mar 2026) prints "Rrita Daci, MD, PGY-7, and Brittany Owusu-Adjei, MD, PGY-6". This is loaded as a partial capture (`other`). Mietus (PGY-5), Lambert (PGY-4) and Qureshi (PGY-3) are reconstructed from UMass-neurosurgery-affiliated papers entered in PubMed between Oct 2025 and Sep 2026. Lim (expected PGY-2) is **not confirmed**: her last UMass paper is from June 2025. **The 2025 intern was not identified.** Several routes found nothing: the UMass Match Day 2025 and 2026 articles name no one by program; the new UMass-neurosurgery PubMed authors are students or lab staff; and cross-matching 1,480 Worcester-area student NPIs against all UMass-neurosurgery authors from 2019-2026 found no new resident. Still **significant**.
- **2026-27, still missing (significant).** Daci graduated in June 2026: NPPES was updated on 2026-06-05 to Neurological Surgery at 300 Longwood Ave (Boston Children's). A `training_history` row was inserted (completed=yes, end_year 2026). Qureshi (Sep 2026) and Mietus (Jul 2026) are still UMass-affiliated on PubMed. The 2026-27 roster needs a manual browser check of the live our-residents page.
- **Adjudicator error:** Chelsea Jeewoo Lim is shown as "LEFT -> SWITCHED SPECIALTY" from an NPI name match. The "Chelsea Lim" NPIs belong to an OT in TX and a peer specialist in OK. Her own NPI, 1801646757, is a Worcester student NPI and has been unchanged since 2024. There is no evidence that she left.
- Scratch files: `data/raw/extraction/p68/phase2/`.
