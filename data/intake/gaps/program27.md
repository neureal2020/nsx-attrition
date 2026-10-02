# Program 27: Icahn School of Medicine at Mount Sinai Program (New York NY)

- 7 years, 2 per year (the program moved from 6 to 7 years around 2012-14). The site was checked from 2008. `programs.website` (www.mssm.edu/neurosurgery/residency/) now redirects to icahn.mssm.edu. Curl gets an Akamai 403 on the live site, but WebFetch works.

## Hosts
| Host/path | From | To |
|---|---|---|
| www.mssm.edu/neurosurgery/residency/residents.shtml | 2008-03 | 2008-11 (before the study window) |
| www.mssm.edu/departments-and-institutes/neurosurgery/programs-and-services/neurosurgery-residency/residents | 2010-05 | 2012-06 (301 in 2013) |
| icahn.mssm.edu/departments-and-institutes/neurosurgery/programs-and-services/neurosurgery-residency/residents (+/alumni) | 2013-05 (CC) / 2014-10 (WB) | 2016-02 (301) |
| icahn.mssm.edu/education/residencies-fellowships/list/msh-neurosurgery (roster on the main page) | 2016-03 | 2020-11 |
| icahn.mssm.edu/about/departments/neurosurgery/alumni | 2016-08 | 2020-02 |
| icahn.mssm.edu/education/residencies-fellowships/list/msh-neurosurgery/residents (+/alumni) | 2021-10 | live |
| mountsinai.org/patient-care/service-areas/neurosurgery | 2013 | 2015 (no roster) |

## Years
| AY | Status | Significance | Source / reason |
|---|---|---|---|
| 2010-11 | observed (context) | none | WB 2011-12-19, headed "Residents 2010-2011". De Los Reyes' "PGY-4" is a stale label: he was PGY-2 in May 2008 and PGY-4 in May 2010, so he is corrected to PGY-5. |
| 2011-12 | **reconstructed** | low | No roster was ever archived. Phase 2 retried CC-MAIN-2012 and it succeeded (13 dept URLs, Feb/May 2012, no residents page). The gap audit and PubMed 2011-13 found nothing new. All 14 residents are bracketed. The only open point is Jannapureddy's exit date. |
| 2012-13 | observed | none | CC-MAIN-2013-20, headed "Residents 2012-2013". |
| 2013-14 | observed | none | CC-MAIN-2013-48, headed "Residents 2013-2014". |
| 2014-15 | **reconstructed** | low | The page stayed on the 2013-14 list until Aug 2015. Every class is complete at 2 on both sides. The re-read CC files, the gap audit and PubMed 2014-16 found no unlisted resident. |
| 2015-16 .. 2023-24 | observed | none | Wayback (see phase 1). |
| 2024-25 | observed | none | Captures from 14 Jan and 12 Feb 2025 bracket Nichols' mid-year exit. |
| 2025-26 | observed | low | Only one capture (Feb 2026), and none from Mar 2025 to Jan 2026, so Chi Le's exit month is unknown. |
| 2026-27 | observed | none | Live page (WebFetch 2026-09-28). It has advanced from 2025-26. |

## Program length (6 -> 7)
`terminal_pgy_by_entry_year`: entrants up to 2006 = 6 years; 2007 onward = 7 years. Individual overrides: Binello (2006 entrant) took 7 years and graduated 2013; Gologorsky (2007 entrant) finished at PGY-6 in 2013. Biro, George and De Los Reyes (2006 entrants) graduated 2012. The phase-1 "mismatches" came from one stale PGY label and these individual track differences.

## Departures (before terminal PGY): 3, all with outcome unknown
- **Madhu Jannapureddy**: 2008 entrant, last listed 2010-11 at PGY-3. Absent from 2012-13 on and not on the alumni page, so she left between Jul 2011 and May 2013 (end_year 2012 is an estimate). No later PubMed or NPPES trace.
- **Noah Nichols**: 2021 entrant, PGY-4. Listed 14 Jan 2025 and gone by 12 Feb 2025. The NPPES "switch" is **not** evidence (his NPI is the 2021 student record). Papers submitted up to Oct 2025 still list Mount Sinai Neurosurgery, so a leave is possible.
- **Chi Le**: 2022 entrant, PGY-3 2024-25. Absent from Feb 2026 on. Papers submitted Aug 2025 still list Mount Sinai Neurosurgery, so a research leave is possible.

## Joiners
- **Hekmat Zarzour**: transferred in from SLU (program 60), where he is on the Feb 2013 housestaff list and was chief in 2011-12. He joined in 2013-14 with a "PGY-4" label, was PGY-7 in 2015-16 and graduated in 2016. The labels reflect credited SLU training, not a single entry year.
- **Santiago Gomez Paz**: joined at PGY-2 in 2026-27. He was a neurosurgery research fellow at Utah in 2024-25 (PubMed; not on Utah's roster), and probably did a 2025-26 prelim year at Mount Sinai (a Feb 2026 paper lists that affiliation). This is not a transfer from another residency.

## training_history rows added in phase 2 (9)
- 3 departures (completed=no, departure_type=unknown): Jannapureddy, Nichols, Le.
- 1 transfer in: Zarzour (2013-2016).
- 1 joiner: Gomez Paz (2026).
- 2 alumni graduations for 2026: Schupper, Bhimani.
- 1 alumni graduation for 2011: Haridas. It clears the LEFT artefact.
- De Los Reyes' roster PGY was corrected (roster file reloaded).

## Adjudication (after phase 2)
32 completed, 14 in training, 3 LEFT (did not complete; outcome unknown). There is no specialty switch.

## Phase 2
- Searched: the cc/ folder re-read; Wayback captures 2008-2012; CC-MAIN-2012 (retried, OK); CC-MAIN-2014-23 (retried, 0 records); gap audits for 2011-12 and 2014-15; PubMed affiliation mining 2011-16; PubMed, Europe PMC, OpenAlex and NPPES for each departure and joiner; every 2024-26 capture of the residents page; the live residents and alumni pages; the SLU roster.
- Remaining: Jannapureddy's exit date and destination; whether Nichols and Le left or are on leave.

## Problems
- data.commoncrawl.org returned 403 briefly, then the retry succeeded. No crawls remain failed.
- The live site still blocks curl, so WebFetch was used.
