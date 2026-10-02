# Program 45: MedStar Health Georgetown University Program (Washington, DC)

This is a 7-year program (PGY-1 to PGY-7) with 2 MedStar positions per year. NIH (program 14) residents train clinically at MedStar Georgetown and appear on its roster, marked "(NIH)", from the 2021 class. **They are excluded here**: McAbee, Roehrkasse, Der, Jessica Chen, Mizrachi and Presto. Of these, McAbee, Roehrkasse and Der carry no "(NIH)" tag on the 2026 pages, so they were excluded by name from `rosters_program14.json`.

## Hosts
| Host / path | Dates | Content |
|---|---|---|
| georgetownuniversityhospital.org/body_dept_home.cfm?id=331 | 2009 .. 2013-10 | Neurosciences/neurosurgery clinical pages. No residency page was ever archived. |
| www.medstargeorgetown.org/our-services/neurosciences/neurosurgery/... | 2013 .. live | Clinical only |
| www.medstarhealth.org/education/affiliated-hospitals-2/medstar-georgetown-university-hospital/neurosurgery-residency/{current-residents-19,recent-graduates-11}/ | 2015-08 .. 2016-11 | Roster and alumni |
| .../neurosurgery-residency-program/ | 2016-12 .. 2021-10 | Landing page only. The roster subpages were never archived (Wayback or Common Crawl). |
| www.medstarhealth.org/education/residency-programs/neurosurgery[/current-residents,/recent-graduates] | landing 2021-11; roster and alumni 2024-04 .. live | Roster and alumni |
| som.georgetown.edu/neurosurgery/ | 2019 .. 2025 | Student elective page, no roster |

## Years
- **Observed:** 2014-15, 2016-17, 2023-24, 2024-25, 2025-26 and 2026-27 (live).
- **Reconstructed, with no roster capture:** 2011-12, 2012-13, 2013-14, 2015-16, and 2017-18 through 2022-23. These use alumni-page graduation years and bracketing. Phase 2 also back-filled the 2020-2022 entrants into 2020-21 to 2022-23.

Caveats on the observed years:
- **2014-15 comes from a stale page.** It was captured from 2015-08 to 2016-05 and is content-dated by its 2015 graduates at the top.
- **The page's labels are unreliable.** In 2014-15, "NS-6..NS-1", and in 2016-17, "PGY-6..PGY-1", number the listed classes in sequence. PGYs were corrected using the alumni graduation years:
  - Felbaum and Ryan: listed as PGY-6 in 2016-17, corrected to PGY-7 (2017 graduates).
  - Jha and McGowan: listed as PGY-5 in 2016-17, corrected to PGY-6.
- **2023-24 is an April 2024 capture**, the earliest capture of the new page.

## Remaining gaps after phase 2 (all rated low)
- **2012 entry class (2012-13, 2013-14).** Still no roster before 2014-15. Everything else points to no 2012 class: there is no PGY-3 in 2014-15, no PGY-5 in 2016-17, and no 2019 graduates. PubMed also shows no unaccounted Georgetown neurosurgery author from 2012 to 2019. Only a 2012 entrant who left by June 2014 without publishing could be hidden.
- **2017-18 to 2022-23.** No roster was ever archived. Every class from 2017 to 2019 graduated intact (2 alumni each). The 2020-2022 entrants were **back-filled as reconstructed rows**: each of the 6 came straight from medical school (PubMed/med-school timelines: GU, Tufts, UF, Miami), so none is a transfer-in. Two things stay hidden: Moustafa's exit year (2017-2021), and a departure replaced 1:1 by a transfer-in.
- **2015-16.** Bracketed by the observed 2014-15 and 2016-17 rosters, which have the same members.

## Classes (entry year: residents)
- **2011:** Jha, McGowan (graduated 2018)
- **2012:** unknown
- **2013:** Conte, Mueller (graduated 2020)
- **2014:** Lynes (graduated 2021) and **Moustafa (left)**
- **2015:** Fayed, Tai (graduated 2022)
- **2016:** Zhou, Dowlati (graduated 2023)
- **2017:** Celano, Zhao (graduated 2024)
- **2018:** Patel, Pivazyan (graduated 2025)
- **2019:** Chesney, Cobourn (graduated 2026)
- **2020:** Stewart, Keating
- **2021:** Breton, Garrett
- **2022:** Grady, Bryant
- **2023:** Ronk, O'Donnell
- **2024:** Maddy, Subah
- **2025:** Wong, plus **Waldman (joined mid-year)**
- **2026:** Evans, Mahapatra

That is 30 residents entering 2011 or later. Alumni-page graduates for 2012-2026 (27 rows) were inserted into `training_history`.

## Departures before the terminal PGY
- **Raed Moustafa.** Last seen 2016-17 at PGY-3 (2014 entrant). He is not on the alumni page, and his classmate Lynes graduated 2021 alone. He left sometime between 2017 and 2021; the exact year is hidden by the gap.

## Joiners
- **Alex Waldman.** He is absent from the Jan and Feb 2026 captures, appears as PGY-1 in the June 2026 capture, and is PGY-2 in 2026-27. He was an off-cycle addition to the 2025 class.

## Problems
- **Common Crawl lookups that failed.** Retry these in phase 2:
  - `org,medstarhealth)/education/affiliated-hospitals-2/medstar-georgetown-university-hospital/neurosurgery`: CC-MAIN-2015-11, 2016-22 and 2018-09.
  - `org,medstarhealth)/education/residency-programs/neurosurgery`: CC-MAIN-2019-22 and 2024-30.
  - CC-MAIN-2012: its index is in the old format.
- **Common Crawl added no new captures.** Every hit it found has the same timestamp as a Wayback capture.
- **Reconstruction assumes 7 years of training** for every alumnus.

## Phase 2 (2026-09-28)
**Searched**
- **Common Crawl.** Retried CC-MAIN-2015-11, 2016-22, 2018-09, 2019-22 and 2024-30. All succeeded, with 0 records.
- **Wayback link audits.** Old GUH neurosurgery department pages (2010-13) have no residency links. The MedStar landing pages (2016-24) link only to GME-wide pages, and none of those names residents.
- **Georgetown SOM matchplacement tables.** The 2019 capture covers 2015-19 and the 2025 capture covers 2019-25. The counts of GU graduates matching MedStar Georgetown neurosurgery agree with the observed classes: 2021: 1 (Garrett), 2022-24: 0, 2025: 1 (Wong).
- **PubMed affiliation mining.** Georgetown AND neurosurgery, 772 PMIDs from 2011-2025, plus MedStar Washington Hospital Center neurosurgery. Every unlisted author was a student, a research fellow, an attending, or a resident elsewhere. Examples: Samir Sur (Miami resident, then GU faculty), Orgest Lajthia (MUSC), Juliana Rotter (student, then Mayo).
- **Raed Moustafa.** No PubMed or OpenAlex output. NPPES has a student-taxonomy record from 2014, never updated.

**Outcomes recorded**
- `training_history`: 1 new row, Raed Moustafa (completed=no, departure_type=unknown, end_year NULL, left 2017-2021).
- No transfers were confirmed.
- The crossmatch pair Caleb Stewart (LSU [32]) -> Jeffrey Stewart was rejected: different first names, and Jeffrey Stewart is a Georgetown SOM graduate.
- Roster: 12 reconstructed rows were added (2020-2022 entrants). Adjudication is unchanged: 27 completed, 14 in training, 1 left.
