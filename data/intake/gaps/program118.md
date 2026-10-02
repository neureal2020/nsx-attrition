# Program 118 - Virginia Commonwealth University Health System Program (Richmond, VA)

7-year program, complement 2/year. Roster JSON: `data/intake/rosters_program118.json`. Scratch: `data/raw/extraction/p118/`.

## Hosts / paths
| URL | From | To | Notes |
|---|---|---|---|
| www.neurosurgery.vcu.edu/people/residents.html | 2008 | 2017-01 | Old static site; flat alphabetical list, no PGY; footer "Updated:" date used to content-date. Omitted PGY-7s 2011-15. |
| www.neurosurgery.vcu.edu/people/graduates.html | 2008 | 2017-01 | Old graduates list |
| neurosurgery.vcu.edu/residency/current-residents/ | 2017-05 | ~2020 | CMS; seniority-ordered, no PGY. Wayback only 2017-06..08; Common Crawl 2017-05..2018-09 |
| neurosurgery.vcu.edu/residency/alumni/ | 2017 | ~2020 | |
| neurosurgery.vcu.edu/education/residency/ | 2021 (linked) / 2022-09 (first capture) | live | Roster in "Current Residents" section; PGY headings only on the live page |
| neurosurgery.vcu.edu/alumni/ | 2021 | live | Graduates through class of 2022 only |
Checked with no roster found: about/our-team (faculty/staff only), vcuhealth.org neuroscience paths, medschool.vcu.edu/education/gme.

## Years
- Observed: 2011-12 .. 2018-19 (2017-18, 2018-19 from Common Crawl), 2022-23 .. 2026-27 (live).
- Reconstructed (manual): 2019-20, 2020-21, 2021-22. These include only bracketed or alumni-confirmed residents.
- Missing: none. However, 2019-20 to 2021-22 are significant gaps: the 2019, 2020 and 2021 intern classes (Fleming/Leonard, Atkinson/Poulos, Caras/Molian) are first seen in 2022-23, so any early loss in those classes would not be visible.
- Incomplete observed years (significant): 2011-12 to 2014-15. The old page left out the PGY-7s: Powell in 2011-12, Machinis and Stanger in 2012-13, Ridder in 2013-14, Hutchins in 2014-15. All are graduates on the alumni page. They were not reconstructed because a capture exists for each of those years, and their completion is recorded in training_history.
- 2016-17: the Sep-2016 capture was stale (same as Nov 2015), so the May/Jun-2017 CMS list was used. Hajec and Rinonos disappeared somewhere between Nov 2015 and May 2017.

## PGY inference
No roster before Dec 2025 prints PGYs. PGY = AY - entry + 1, with entry taken from:
- the alumni graduation year minus 6, or
- seniority order on the 2017+ CMS pages, or
- the year of first appearance.
Merrill (entry about 2007), Hajec (2012) and Rinonos (2014) are estimates. Lisa Feldman is on the Jan-2011 (2010-11) list but graduated in 2018 with the 2011 class, so her entry was set to 2011.

## Departures (left before PGY-7)
| Name | Last AY | Last PGY | Note |
|---|---|---|---|
| Eric Merrill | 2011-12 | ~5 | not on alumni list; NPI suggests switched specialty |
| Marygrace Hajec | 2015-16 | ~4 | not on alumni list |
| Serendipity Zapanta Rinonos | 2015-16 | ~2 | not on alumni list; NPI suggests switched specialty |
| Dean Leonard | 2024-25 | 6 | classmate Fleming continued |
| Brandon Toll | 2024-25 | 2 | |
| Shawn D'Souza | 2024-25 | 1 | NPI suggests switched specialty |
(Before the study window, Jeziorski and Mahdavi were on the 2010-11 list and gone by Aug 2011.)

## Joiners (above PGY-1)
- Viktoras Palys: PGY-2 in 2011-12 (absent from the 2010-11 list).
- Steven Wakeman: PGY-2 in 2016-17 (absent from the Nov-2015 list).
- Devon Mitchell and Marissa Suchyta: PGY-2 in 2025-26 (listed "PGY-2").

## Class sizes by entry year
- 2011: 4 (Anene-Maidoh, Feldman, Kelman, Vega)
- 2012–2014: 2 each (includes Hajec and Rinonos)
- 2015: 3 (includes joiner Wakeman)
- 2016–2023: 2 each
- 2024: 4 (Mualem and D'Souza, plus joiners Mitchell and Suchyta)
- 2025: 2
- 2026: 2

## Alumni to training_history
Twenty graduation rows were inserted for 2012–2022: Powell through Opalak, Wakeman and Whitaker-Lea.

## Adjudication
- 26 completed
- 14 in training
- 1 left, switched specialty (Rinonos -> neurology, from publications)
- 5 left, outcome unknown (Merrill, Hajec, Leonard, Toll, D'Souza); phase-1 NPI "switch" calls for Merrill and D'Souza were dropped

Residents entering 2011+: 37.

## Problems
- The CC-MAIN-2018-30 cluster.idx range fetch failed. This was not needed, because Sep 2018 covers 2018-19.
- The Jul/Aug-2017 Wayback current-residents captures are stale 2016-17 content.
- The Sep-2022 capture is in a lagging state: Whitaker-Lea is still listed and the 2022 interns are absent.

## Phase 2 (2026-09-28)

### Year status and significance
| AY | Status | Significance | Reason |
|---|---|---|---|
| 2011-12 .. 2014-15 | observed (PGY-7s omitted) | none | Every omitted PGY-7 was PGY-6 the year before and is on the alumni list; only PGY-7s were left off, so no one below PGY-7 could be missed. |
| 2015-16 | observed | none | Full list including PGY-7s |
| 2016-17 | observed (May-2017 content) | low | Hajec/Rinonos left sometime between Nov 2015 and May 2017. The exact AY is unresolved. |
| 2017-18, 2018-19 | observed (CC) | none | |
| 2019-20 .. 2021-22 | reconstructed | low | No roster anywhere. Complement 2; the 2019, 2020 and 2021 classes are exactly 2 each in 2022-23. All six have NPIs enumerated Apr-Jun of their entry year (Neurological Surgery, VA), so they started here as PGY-1s. PubMed mining for 2018-23 found no unlisted resident. Only an above-complement entrant who left before 2022 could still be missed. |
| 2022-23 .. 2026-27 | observed | none | Extra 2025 captures (Jan, May, Aug) used to date the 2025 departures |

### The 2025 cluster, resolved
- **Brandon Toll** left **mid-PGY-2**: listed 2024-11-14, gone by 2025-01-18.
- **Dean Leonard** (PGY-6) and **Shawn D'Souza** (PGY-1) were listed through May 2025 (profiles captured 2025-06-16) and were gone by Aug 2025. Leonard's classmate Fleming finished (PGY-7 2025-26, gone 2026-27). D'Souza's 2026 papers list WashU Neurosurgery, but he is not on WashU's residency rosters, so this is probably a research role. Outcome unknown.
- **Mitchell and Suchyta** (PGY-2, 2025-26) took the vacated slots. Mitchell's NPI also lists Surgery (IL), so he probably did a PGY-1 surgery year in Illinois. Suchyta is an MD-PhD whose publications are affiliated with Mayo plastic surgery.

### Earlier departures and joiners
- Merrill: entry 2007, confirmed by NPI enumeration (May 2007). PGY-5 in 2011-12. He was absent in Dec 2012, when he would have been listed as a PGY-6. Destination unknown.
- Hajec: surgical internship at Morristown (VCU profile), so she may have joined at PGY-2 in 2012. Outcome unknown. She is a co-author on a 2026 ACOEM paper that prints no affiliation.
- Rinonos: switched to **neurology** (UCLA Dept of Neurology publications, 2022-23).
- Palys: surgical internship at UIC before joining at PGY-2 (VCU profile).

### training_history rows added (17)
6 departures, 4 joiners (Palys, Wakeman, Mitchell, Suchyta), and 7 roster-only graduations: O'Brien and Verma 2023, Hachmann and Patel 2024, Rajagopal and Shah 2025, Fleming 2026.

### Remaining
The 2019-22 roster gap (low significance), the exact departure AY for Hajec/Rinonos, and the destinations of Merrill, Hajec, Leonard, Toll and D'Souza. OpenAlex's IP budget was used up, so it was not used.
