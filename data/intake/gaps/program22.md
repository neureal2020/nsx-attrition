# Program 22: George Washington University (Washington, DC), Phase 1 gap report

This is a 7-year program. Intern classes alternate between 1 and 2 (complement about 2 per year at most). The program was first accredited in 1966.

## Hosts / paths
| URL | From | To |
|---|---|---|
| http://www.gwneurosurgery.com/residents.shtml (department's own site; the domain later became spam) | 2007-06 | 2013-09 |
| http://smhs.gwu.edu/neurosurgery/residents | 2014-10 | 2020-04 |
| https://smhs.gwu.edu/neurosurgery/residency-program-0 ("Our Residents") | 2020-07 | 2022-01 |
| https://neurosurgery.smhs.gwu.edu/our-residents (live; the graduates list is on the same page) | 2022-10 | live |

I also checked these hosts and found no roster: www.gwumc.edu/smhs/neurosurgery (intranet only), gwdocs.com/neurosurgery (MFA clinical pages) and the live sitemap.

## Year-by-year
| AY | Source | Status |
|---|---|---|
| 2011-12 | Common Crawl CC-MAIN-2012, 2012-02-05, gwneurosurgery.com | Observed, 8 (no Wayback capture 2008-07..2013-08) |
| 2012-13 | Wayback 2013-08-13 | Observed, 8. The August capture still shows 2012-13 content (Wind PGY7, Knudson PGY1) |
| 2013-14 | Wayback 2013-09-28 | Observed, 9 |
| 2014-15 | Wayback 2014-10-28 smhs | Observed, 9. Babington is shown as PGY6 but is a 2015 graduate (true PGY7) |
| 2015-16 | manual | Reconstructed, significance **none** (phase 2). The page was stale 2015-07..2016-05 and Common Crawl has nothing, but all 9 residents are bracketed; Reagan added as PGY1 (MUSC roster names GW as his intern year). The 2015 class (Reagan, Hogan) fills the complement of 2 |
| 2016-17 | Wayback 2016-11-17 | Observed, 8 |
| 2017-18 | manual | Reconstructed, significance **low** (phase 2). Every capture 2017-06..2018-08 repeats the 2016-17 list. 8 names: 2017 interns Elliott and Sack added (PGY2 2018-19, graduated 2024), so the 2017 class fills the complement of 2. Open point: only whether Reagan (PGY3) was still there; his exit itself is documented |
| 2018-19 .. 2019-20 | Wayback smhs 2018-12-26, 2019-11-18 | Observed, 8 / 9 |
| 2020-21 .. 2021-22 | Wayback residency-program-0 2020-11-12, 2021-10-22 | Observed, 8 / 9 |
| 2022-23 .. 2025-26 | Wayback our-residents 2022-10-18, 2023-09-23, 2025-01-18, 2025-12-08 | Observed, 9 / 11 / 10 / 11 |
| 2026-27 | live 2026-09-27 | Observed, 9. The page has advanced (Ashby is the new PGY1). A commented-out block for Fleisher and Patrick (2026 graduates) is excluded |

## Departures (left before PGY-7), phase 2 evidence
- **Peter DeRosa** (2011 class): last seen 2013-14 PGY3, absent Oct 2014. **Switched to pathology** (publication affiliations: GW Neurological Surgery 2014, PMID 25083377; GW Pathology 2020, PMID 32939388; then U Maryland Pathology).
- **Moshe Chinn** (2013 class): last seen 2014-15 PGY2, removed from the page May-Jul 2015. **Switched to anesthesiology** (GW Anesthesiology & Critical Care Medicine, PMID 33963083 2021, 39380859 2024).
- **Justin Reagan** (2015 class): last seen 2016-17 PGY2 (stale page to Aug 2018), absent Dec 2018. **Switched to diagnostic radiology**: the MUSC radiology current-residents page (Wayback 2019-10-19) lists him as a first-year resident in 2019-20 with "Clinical Year: George Washington University"; MUSC Radiology affiliation 2021 (PMID 33783916). Exit date within Jul 2017 to Dec 2018 unknown; recorded end_year 2018.
- **Crystal Adams** (2016 class): last seen 2019-20 PGY4, not on the alumni list. **Switched to anesthesiology** (GW Neurological Surgery 2018, PMID 29614361; GW Anesthesiology & Critical Care Medicine 2025-26, PMID 41509883, 42171957).
- **Kristina Terrani** (2025 class): PGY1 2025-26 (still listed Apr 2026), absent from the live page Sep 2026. Last paper (received Feb 2026) gives GW Neurosurgery; she is on no other roster in this study (U Arizona Tucson checked); NPPES unchanged since 2025-06. **Outcome unknown.**

All five are recorded in `training_history` (4 switched_specialty, 1 unknown).

## Joiners
None.

## Alumni
The graduates list (2012 Sweet .. 2026 Fleisher/Patrick) is consistent with the rosters. I inserted 16 `training_history` rows. The alumni page spells "Ross-Elliott Jordon"; the roster and NPPES give Ross-Jordon Elliott. There were no graduates in 2014 or 2023, which matches the losses of the 2007 entrant (Weingarten, gone before 2012, before the study window) and of Adams.

## Class sizes by entry year (24 residents entering 2011+)
2011: 2 (DeRosa left) · 2012: 1 · 2013: 2 (Chinn left) · 2014: 1 · 2015: 2 (Reagan left) · 2016: 1 (Adams left) · 2017: 2 · 2018: 1 · 2019: 2 · 2020: 1 · 2021: 2 · 2022: 1 · 2023: 2 · 2024: 1 · 2025: 2 (Terrani left) · 2026: 1

Each resident's entry year is consistent across all observations, apart from Babington's 2014-15 label.

## Problems
- Terrani's outcome is unknown. Reagan's exact exit date is unknown.
- CC-MAIN-2017-04 was retried in phase 2 and worked (no roster URL in it).

## Phase 2 (2026-09-28)
Searched: gapaudit 2015-18 over the department, legacy gwneurosurgery.com, gwdocs, GME, SMHS news and gwhospital hosts; every smhs.gwu.edu/neurosurgery URL 2014-21; the residency-program page links; all 43 Common Crawl crawls 2015-18 (no failures); PubMed affiliation mining 2014-20 (no unknown resident); author searches (PubMed, Europe PMC, OpenAlex) for the five departures; MUSC radiology roster; NPPES; live page.
Found: specialty switches for DeRosa, Chinn, Reagan and Adams backed by real evidence. The 2015 and 2017 intake classes are each complete at the complement of 2 (Reagan + Hogan; Elliott + Sack), and the program alternates 2/1, so no early leaver can be hidden in those years.
Remaining: Terrani's outcome; Reagan's exit date (2017-18 or mid-2018). No gap is significant.
