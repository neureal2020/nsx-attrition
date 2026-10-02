# Program 23: Hackensack Meridian Health Program (Hackensack University Medical Center, Hackensack NJ)

**Status: new program, no residents on record.** ACGME 1603300001, Initial Accreditation effective 07/01/2026, PD Ira M. Goldstein (from ACGME list, DB notes). Not linked to any earlier neurosurgery residency at HUMC.

## Site history checked
- `hackensackumc.org` (Wayback, 8,810 URLs, 2013-2021): GME pages under `/health-professionals/education-training/residencies/`, `/health-professionals/residencies/`, `/health-professionals/graduate-medical-education/`. No neurosurgery residency URL. The 2019 "Graduate Medical Education Programs" page lists ACGME programs EM, General Surgery, IM, Pediatrics, Urology (plus Palisades programs), with no neurosurgery.
- `hackensackmeridianhealth.org/en/healthcare-professionals/humc/` (live and 260 Wayback URLs): 33 HUMC programs, including neurology, ortho, surgery and urology, but no neurosurgery. Guessed paths (`neurosurgery-residency`, `neurological-surgery-residency`, etc.) return 404. Live sitemaps (`sitemap_default`, news, services, locations) have no neurosurgery residency page and no news item on its accreditation.
- `hmsom.org` / `hmsom.edu` (2,226 / 1,477 Wayback URLs) and `hmhn.org`: no neurosurgery URLs.
- System GME contacts PDF (live): no neurosurgery entry.

## Years
- 2011-12 .. 2025-26: pre-program (not missing).
- 2026-27: accreditation year. No roster or page on the live site. Most likely the first class starts July 2027 (2027 Match), but this is **unconfirmed**. If a PGY-1 did start in July 2026, they are not visible anywhere on program-side pages.
- Observed / reconstructed / missing: none / none / none.

## Roster, alumni, attrition
- `data/intake/rosters_program23.json` = `[]` (loaded; 0 observations). No alumni page, no departures, no joiners, 0 residents entering 2011+.

## Problems / follow-up
- Complement and first class year unknown. Re-check the HUMC GME hub after the 2027 Match for a neurosurgery residency page.
- Common Crawl not run: there is no candidate host/path to scan.

## Phase 2 (2026-09-28)
- **No observed years exist.** All of 2011-12..2025-26 are pre-program (`not_applicable`, significance none). 2026-27 is the accreditation year (significance low). Rosters file stays `[]`. There are no classes to count against a complement, nobody who appears once and vanishes, no graduations and no training_history rows.
- **First class:** unconfirmed, most likely July 2027. The live HUMC GME hub (re-checked 2026-09-28) lists only `neurology-residency`, and the guessed neurosurgery paths all return 404. The 2025-26 PubMed authors with an HMH neurosurgery affiliation are HMSOM students or attendings, and none is a resident.
- **Terminal PGY:** 7 for every cohort (ACGME, entry 2026+).
- **JFK / NJ Neuroscience Institute (Edison, Seton Hall affiliate):** it had a neurology residency only, so it is not a predecessor. Evidence: njneuro.org PGME 2005; the jfkmc.org NJNI "Fellows, Residents and Students" page of 2014-05, which lists neurology residents and fellows; and jfkmc.org neuroscience-institute-education/residency 2020, the "ACGME-accredited Neurology Residency", with 8 per year. No neurosurgery residency URL appears across jfkmc.org (8,395 Wayback URLs), jfkhealth.org or njneuro.org.
- **Saint Barnabas Medical Center AOA neurosurgery (Livingston):** this is the closest lineage. Its program pages (2012, 2019) say it was "affiliated with Hackensack University Medical Center", and it merged into Rutgers NJMS (57) in 2020 under PD Ira Goldstein, now PD here. It is not a legal predecessor of program 23. In the DB, its 2014-18 entrants appear under 57 (as 2020-21 joiners) and Dabecco's 2018 transfer to program 2 is recorded. Its 2011-13 entrants and any 2019 intern are NOT in the DB. That is a program 57 lineage gap, not a program 23 gap.
- Evidence files are in `data/raw/extraction/p23/phase2/`.
