# Program 18: Dartmouth-Hitchcock / Mary Hitchcock Memorial Hospital (Lebanon, NH)

7-year program, 1 resident per year (alumni page: "admits, and typically graduates, 1 resident per year"). Roster: `data/intake/rosters_program18.json` (16 captures, 113 observations). 15 alumni graduations (2012-2026) inserted into `training_history`.

## Hosts / paths
| URL | Dates | Roster? |
|---|---|---|
| gme.dartmouth-hitchcock.org/neurosurgery/our_residents.html | 2011-08 to 2017-08 | yes; each resident shown with "(start-end)" training span; content updated only ~Aug 2012/13 and Jul 2015, Oct 2016 |
| gme.dartmouth-hitchcock.org/neurosurgery/current-residents-alumni.html | 2017-10 to 2021-06 | yes (name then "PGY n" label) + alumni list 1949-2017 |
| gme.dartmouth-hitchcock.org/neurosurgery/current-residents | 2022-01 to live | yes (PGY-n headings) |
| gme.dartmouth-hitchcock.org/neurosurgery/alumni | 2022-05 to live | graduates 2009-2026 |
| www.dartmouth-hitchcock.org/neurosurgery (clinical), dartmouth-health.org/neurosurgery, geiselmed.dartmouth.edu/neuro*, dms.dartmouth.edu/neuro* | 2010-2026 | no rosters (CDX prefix audit + sitemaps) |

## Years
- **Observed:** 2012-13 (Wayback 2013-09-01, content-dated: Desai chief, Root intern), 2015-16 (2015-10-02), 2016-17 (2016-10-12), 2017-18 (2017-10-13), 2018-19 (2019-08-18, content-dated: Root chief, Montejo PGY1), 2019-20 (2019-10-19), 2020-21 (2020-11-30), 2021-22 (2022-01-21), 2022-23 (2022-12-09), 2023-24 (2023-12-06), 2024-25 (2024-09-16), 2025-26 (2026-02-16), 2026-27 (live, advanced).
- **Reconstructed:** 2011-12, 2013-14, 2014-15.
- **Missing:** none.

## Gap details (significant)
- **2011-12:** captures 2011-08, 2012-01, 2012-05 (and Common Crawl 2012-05-23) all show the 2010-11 roster. Reconstructed 7 (Spire 7 … Hong 1) from 2010-11 and 2012-13 rosters, listed spans and the alumni list.
- **2013-14, 2014-15:** the page kept the 2012-13 roster from 2013-09 to 2015-05. Reconstructed. Every 2012-13 resident reappears in 2015-16 or graduates on schedule, so no departure is hidden among them. The only risk is an unseen 2013 or 2014 entrant who left before 2015-16. Kim (2013-2020) and Calnan (2014-2021) are the listed entrants for those years.
- **2021-22:** there is no capture from Jul to Dec 2021. The Jan 2022 capture is used.

## Consistency
Entry years are consistent for everyone. Ihezie has two entry years (2020/2021) because she is listed PGY-3 twice, in 2022-23 and 2023-24. The one-per-year complement holds, with these exceptions:
- The 2013 slot emptied after Kim left. It was filled by Makler, who transferred in at PGY4 in 2017-18 (entry-equivalent 2014) and graduated in 2021 alongside Calnan.
- The 2020 slot was taken over by Stewart at PGY5 in 2024-25 as Ihezie fell back a year.

## Departures
- **Joon-Hyung Kim:** last seen 2015-16 at PGY3. Absent from Oct 2016 on, not on the alumni list, and there is no 2020 graduate.
- **Stephanie Ihezie:** last seen 2024-25 at PGY4. She repeated PGY3 (2022-23 and 2023-24). Absent from the Feb 2026 and live rosters, and not on the alumni list.

## Joiners
- **Vyacheslav "Slava" Makler, DO:** 2017-18, PGY4 (the 2016-17 roster lacks him).
- **Caleb Stewart:** 2024-25, PGY5 (the 2023-24 roster lacks him). Medical school: University of Queensland.

## Other
- Residents entering 2011+ (including joiners): 18.
- Adjudication: 15 completed, 7 in training, 2 left (outcome unknown).
- Problems: see the JSON. The Common Crawl pass completed with no failures.

## Phase 2 (2026-09-28)

### Year status
| Year | Status | Significance | Reason |
|---|---|---|---|
| 2011-12 | reconstructed | low | Bracketed by the 2010-11 and 2012-13 rosters. Every 2010-11 resident either graduates (Radwan 2011, Spire 2012) or reappears in 2012-13. The 2011 entry slot is Hong (2011-2018). |
| 2012-13 | observed | none | Content-dated 2013-09 capture. |
| 2013-14 | reconstructed | low | The page stayed frozen (8 captures re-read). Every 2012-13 resident reappears in 2015-16 or graduates. The 2013 slot is Kim (MD 2013, "(2013-2020)"). An unseen extra entrant would exceed the one-per-year complement, and no source shows one. |
| 2014-15 | reconstructed | low | Kim's presence is confirmed by PMID 26236552 (Section of Neurosurgery, DHMC; received Dec 2014). Calnan is the 2014 entrant. |
| 2015-16 to 2024-25 | observed | none | 2018-19 is content-dated. 2021-22 comes from the Jan 2022 capture and is bracketed with no change. |
| 2025-26 | observed | low | Feb 2026 capture. No capture exists between Aug 2025 and Feb 2026 in Wayback or CC, so the date Ihezie left is unknown. |
| 2026-27 | observed (live) | none | |

### Searched
- Re-read all 35 captures of our_residents.html (2011-2017). Ran a full CDX prefix listing of gme.../neurosurgery for 2011-2017.
- Audited links in every distinct 2011-2016 capture of the program's parent pages. None links to news, match or roster material beyond our_residents.html.
- The general-surgery residents page (32 captures) lists no neurosurgery interns. The GME PDFs are only forms and training information.
- Common Crawl 2011-2016 with the fixed filter: 30 crawls × 5 prefixes (gme neuro*, dartmouth-hitchcock.org/neuro*, clinics/neuro*, geiselmed neuro*, dms neuro*), no failures. The only neurosurgery hit is the known stale 2012-05 roster. CC 2025-2026: 19 crawls, no failures.
- PubMed affiliation mining 2011-2017 (239 papers) found no unlisted resident. Missios, Valdes and others are non-residents or students.

### Outcomes recorded (training_history)
- **Joon-Hyung Kim (th 3026): switched to anesthesiology.** He left after 2015-16 (PGY3). The Sep 2016 capture still shows 2015-16 content; he is gone by Oct 2016. The Westchester Medical Center anesthesiology roster for 2020-21 lists "CA-3 Joon-Hyung Kim, Weill Cornell School of Medicine". His Dartmouth bio gives MD Weill Cornell 2013. His 2020-21 papers are affiliated with the WMC/NYMC Dept of Anesthesiology. NPI 1417214685 is anesthesiology.
- **Vyacheslav Makler (th 3027): transfer in** from Missouri-Columbia (program 94, PGY3 2016-17) at PGY4 in 2017-18. He graduated in 2021.
- **Caleb Stewart:** the transfer-in from LSU Shreveport (program 32, PGY4 2023-24) at PGY5 in 2024-25 was already recorded (th 2681/2680) by the program 32 agent. Not duplicated.
- **Stephanie Ihezie (th 3028): outcome unknown.** She is present on the Aug 2025 capture, which still shows 2024-25 content, and absent from Feb 2026 and the live page. She is not on the alumni list. Her papers still give a Dartmouth neurosurgery affiliation, including one submitted in Dec 2025. No other program's roster lists her, and her NPPES record has not been updated.

### Remaining
- 2011-12, 2013-14 and 2014-15 remain reconstructions, but all are low significance.
- Ihezie's outcome and exit date are still unknown.
- Adjudication: 15 completed, 7 in training, 1 switched specialty (Kim), 1 left with outcome unknown (Ihezie).
