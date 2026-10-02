# Program 92: University of Minnesota Program (Minneapolis, MN)

7-year program (6-year for the 2005-2007 entrants), complement 2 per year (14 on a full roster). Roster file: `data/intake/rosters_program92.json`. Scratch: `data/raw/extraction/p92/` (phase 1) and `data/raw/extraction/p92/phase2/` (phase 2: `build2.py`, audits, CC URL listing, PubMed dumps, the 2013 call-schedule PDF).

## Hosts and paths
| URL | From | To | Note |
|---|---|---|---|
| www.neurosurgery.umn.edu/training/residency/current/home.html (also /neurosurgery/training/..., www.med.umn.edu/neurosurgery/training/residency/...) | 2007 | 2013-01 | Old AHC static site. The roster was captured only on 2010-07-01 (2009-10 content). |
| www.med.umn.edu/neurosurgery/faculty-and-staff/current-residents/index.htm | 2013 | 2014-01 | Single capture, 2014-01-10. |
| www.neurosurgery.umn.edu/faculty-residents-and-staff/current-residents | 2015-09 | 2017-09 | Drupal site; bios at /bio/neurosurgery-current-residents/<slug>; resident PDFs under /sites/neurosurgery.umn.edu/files/. |
| med.umn.edu/neurosurgery/education-training/residency/current-residents | 2019-03 | live | |
| med.umn.edu/neurosurgery/education-training/residency/alumni | 2019-03 | live | Graduates 1949-2026 with training years. |

## Years
| AY | Status | Source | Significance |
|---|---|---|---|
| 2011-12 | reconstructed | alumni list + 2009-10 page PGYs | **low**: every 2006-2011 cohort is bracketed at complement. The only unseen event is Koijan Kainth's exit (transfer to Penn State, recorded; exit between 2010 and 2012). |
| 2012-13 | reconstructed + partial | April 2013 call schedule PDF (7 residents) + alumni | **low**: no unknown names; Kristen Jones's arrival is recorded. |
| 2013-14 | observed | Wayback 2014-01 | none |
| 2014-15 | reconstructed + partial | Star Tribune 2014-10-05 (Terzic PGY7, Vasquez PGY6, Quinn and Darrow PGY2) + alumni | **low**: the 2008-2013 cohorts are bracketed. The residual doubt is whether Dixson was the second 2014 intern (with Khan) or joined in 2015 at PGY2. |
| 2015-16 .. 2026-27 | observed | Wayback / live | none. For 2019-20 the May 2020 capture is now also loaded, which adds Huang. |

## Phase 2 corrections
- **PGY / program length.** The 2009-10 page runs PGY-1..6, and the 2005-2007 entrants finished after PGY-6: Sherr and Uittenbogaard in 2010, Souslian and Colpan in 2012, Park and Qaiser in 2013. Koijan Kainth was also a PGY-6 finisher, at Penn State in 2013. Park, Qaiser, Siddiq and Koijan Kainth were all PGY-3 in 2009-10, so the 2007 class had 4 members, not "Siddiq alone". Siddiq is the exception: he was PGY-7 in 2013-14. Phase 1 had the reconstructed PGYs one year too high for Souslian and Colpan (2011-12) and for Park and Qaiser (2011-12 and 2012-13). They are now corrected, and the entry years agree. `terminal_pgy_by_entry_year` = {2005: 6, 2006: 6, 2007: 6, 2008: 7}.
- **2012-13 partial observation.** The UMMC call schedules for April 2013 were archived on the Drupal site in 2015 (`neurosurgery-resident-call-schedule.pdf`). They list Park and Siddiq on chief call, and Das, Vasquez, Gupte, Goyal and Lim on resident call.
- **2014-15 partial observation.** A department news item links a Star Tribune feature (5 Oct 2014) that names four residents by training year.

## Departures (left before the terminal PGY)
| Name | Last AY / PGY | Outcome (training_history) |
|---|---|---|
| Koijan Kainth | 2009-10 / 3 seen (probably 2011-12 / 5) | **Transferred** to Penn State (53): PGY-6 chief 2012-13, graduated 2013. th 3029 (UMN out, end 2012). The exit year cannot be observed at either program (2010-12). |
| Alana Dixson | 2015-16 / 2 | **Left, destination unknown** (th 3035, departure_type unknown). Her only later trace is a 2018 paper with a UC Davis Medical Center affiliation (PMID 29565953), role unknown. The NPI "switch" is unsupported: her NPI is surgery at BIDMC, last updated 2013. |
| Maxwell Tran | 2019-20 / 2 | **Switched specialty to radiation oncology**: the MUSC Radiation Oncology current-residents page (Wayback 2021-01-19) lists "Residency 2020-2024 ... Neurological Surgery Residency, University of Minnesota, 2018-2020", with the same Baylor MD and Michigan BS as his UMN bio. PubMed shows him at MUSC Radiation Oncology 2023-25. th 3033. |
| Youssef Hamade | 2022-23 / 6 | **Transferred** to Loma Linda (31): PGY-6 2025-26, PGY-7 2026-27. For 2023-25, his 2025 papers give a St. Elizabeth's Medical Center / Boston University neurosurgery affiliation (role unconfirmed). th 3034 (UMN out) and th 2722 (Loma Linda in). |
| Christopher Janson | 2009-10 / 5 | Before the window; not loaded. |

## Joiners (above PGY-1)
| Name | First AY / PGY | Note |
|---|---|---|
| Kristen Jones | 2012-13 / 6 | From Pitt (116; PGY-5 there in 2011-12). Graduated 2014. th 3030 (in), th 177 (Pitt out). |
| Jack Leschke | 2016-17 / 3 | After a neurology residency at MCW (bio, and PubMed MCW Neurology affiliations 2013-17). Took Dixson's slot. Graduated 2021. th 3031. |
| Shiwei Huang | 2019-20 / 2 (mid-year) | From Wayne State (125; PGY-1 there in 2018-19; that program closed around 2020). Absent 2019-11-21, present 2020-05-27. Took Tran's slot. Graduated 2025. th 3032. |
| Alana Dixson | 2014-15 or 2015-16 | General surgery PGY-1 at BIDMC 2013-14. UMN bios do not list the UMN intern year (see Khan's), so her start is unresolved. |

## Other
- Samuel Jones was PGY2 in both 2019-20 and 2020-21 and "PGY6.5" in 2024-25. He graduated in 2026.
- Name variants: Huy Donguyen, Truong "Huy" Do → Truong Do; Lauren Albert → Lauren Albert Sand; Coridon J. Quinn IV → Coridon Quinn; Kristin → Kristen Jones.
- Adjudication (phase 2): 29 COMPLETED, 14 IN TRAINING, 1 TRANSFERRED (Hamade), 1 SWITCHED SPECIALTY (Tran), 1 did not complete / unknown destination (Dixson).

## Phase 2 searches
- Wayback gap audits 2010-07..2013-08 and 2014-01..2015-10 over every neurosurgery and GME host, and link audits of the residency and department home pages. No roster was found.
- Common Crawl: a full URL listing (not just the roster filter) of CC-MAIN-2012..2015-35 for the neurosurgery, med/neurosurgery and med/gme hosts. CC-MAIN-2015-27, which failed in phase 1, was retried and completed. Only parent and faculty pages were found.
- Other sources checked: archived resident bios, department news, and the archived resident PDFs. PubMed affiliation mining for 2010-16. Per-person PubMed, Europe PMC and OpenAlex searches. The other programs' roster files (53, 116, 125, 31) and the MUSC and UC Davis pages.

## Remaining
- Koijan Kainth's exact exit year.
- Dixson's start year (2014 as PGY-1, or 2015 as PGY-2) and her destination.

## Problems
None. All queries completed.
