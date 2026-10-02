# Program 117: Vanderbilt University Medical Center (Nashville, TN)

7-year program with 3 residents per year (2 per year for classes that entered up to 2010). The program has no alumni page. Scratch files and parsers are in `data/raw/extraction/p117/` (`parse117b.py`, `build117.py`); phase-2 work in `phase2/`.

## Hosts
| URL | From | To |
|---|---|---|
| http://www.mc.vanderbilt.edu/root/vumc.php?site=neurosurgery&doc=16652 (old sitebuilder) | 2013-01 (first roster capture) | 2016-10, then 301 to ww2 |
| https://ww2.mc.vanderbilt.edu/neurosurgery/16652 | 2017-01 | 2019-11 |
| https://www.vumc.org/neurosurgery/<node> (roster node 16652 never captured) | 2019-12 | 2021 |
| https://www.vumc.org/neurosurgerydept/current-residents (stale 2020-21 list) | 2021-09 | 2021-09 |
| https://www.vumc.org/neurosurgerydept/person/current-residents | 2021-10 | live |
| mc.vanderbilt.edu/documents/neurosurgery/files/ (org charts; the 10/14/2016 chart says "19 Residents") | 2012 | 2017 |

The ww2 host was found through a Common Crawl 301 from the old sitemap. A Wayback prefix query on `www.mc.vanderbilt.edu` alone misses it.

## Years
- **Observed (15):** 2012-13 through 2026-27. For 2013-14, 2016-17 and 2017-18 the source is Common Crawl. The 2020-21 roster is a stale page captured in Sep 2021. The 2018-19 roster was found in phase 2 (see below).
- **Missing (1):** 2011-12. No roster capture exists before 2013-01-06, in either Wayback or Common Crawl.

### 2018-19 (closed in phase 2)
The roster node was never captured in 2018-19, but every resident bio page on the ww2 host printed the full "Current Residents" side menu. The Wayback capture of Ahilan Sivaganesan's bio (`ww2.mc.vanderbilt.edu/neurosurgery/43771`, 2019-05-13) lists all 20 residents:
- It includes the PGY7s Dewan, Morone and Zuckerman.
- It includes the 2018 interns Ali, Dambrino and Kamal.
- It does not include Cooper or He, who graduated in 2018.

The menu is alphabetical with no PGY labels, so each PGY is inferred from entry year. Mistry and Voce are left blank because each had an extended year.

CC-MAIN-2019-04 answers again. It holds a single ww2 neurosurgery record, which is not a roster.

### Significance
| Year | Status | Significance | Reason |
|---|---|---|---|
| 2011-12 | missing | low | Every entry class from 2006 to 2012 is at complement on the Jan 2013 list. Only a 2011 intern above complement who left before Jan 2013 could be missed. |
| 2018-19 | observed | none | Every class is full: 3 interns and 3 PGY7s. |
| All other years | observed | none | |

Phase 2 re-audited 2011-12 and found nothing:
- The old sitebuilder's "Residency" and "Resident Applicants" docs have no capture before 2013.
- Nothing turned up on the mc documents, sbworddocs or GME paths.
- PubMed mining for 2010-13 found no unexplained resident.

## Outcomes (phase 2, recorded in training_history, 39 rows)
| Name | Outcome | Evidence |
|---|---|---|
| Jason Agran | Left in Aug 2014 at the start of PGY5: `left_medicine` (industry, a judgement call) | Medtronic Restorative Therapies research affiliation: PMID 29065235 (2017) and 29633438 (2019) |
| Coby Ray | Left after PGY1 2015-16: `switched_specialty`, to ophthalmology | Texas Tech ophthalmology, PMID 41246121 (2025); oculoplastics, PMID 42455407 (2026) |
| Scott Parker | **Completed in 2017** after 6 years; not a departure | His VUMC faculty bio says "Intern 2011-2012, Resident 2012-2017". He is listed as Assistant Professor on the faculty page by Apr 2018. |
| Claudio Cavallo | Left after 2021-22: `transferred`, to neurosurgery in Switzerland (outside the US) | EOC Lugano 2022-24 (PMID 36258118, 38021011, 38258004); Zurich 2025 (PMID 41158872). His exact role there is not confirmed. |
| Dewan, Morone, Zuckerman | Completed in 2019 | On the 2018-19 list |
| Breanne Reisen | Transferred in as PGY2 in 2023-24 | Origin unknown. MD from Central Michigan; her 2022 affiliation is Children's Hospital of Michigan pediatric neurosurgery. She is on no other roster in the study. |
| Akshay Bhamidipati | Transferred in from UNM (program 97) as PGY2, mid 2025-26 | Absent from the Oct 2025 capture, present on the Jan 2026 one |

Another 33 graduates are recorded as `completed='yes'` with the note "PGY-terminal roster": all PGY7 finishers from 2013 to 2026, including the Ghiassi twins as separate rows. Every cohort's terminal PGY is 7.

**Adjudication after phase 2:**
| Outcome | Count |
|---|---|
| Completed | 33 |
| In training | 24 |
| Left medicine | 1 |
| Switched specialty | 1 |
| Transferred | 1 |

## Consistency
Class sizes by entry year:
- 2006-2010: 2 per year.
- 2011-2021: 3 per year.
- 2022: 4, including Reisen.
- 2023: 3.
- 2024: 4, including Bhamidipati.
- 2025: 4 interns.
- 2026: 3.

Some residents did not follow the standard timeline:
- **Brandon Davis:** PGY6 in both 2014-15 and 2015-16; graduated 2017.
- **Akshitkumar Mistry:** entered 2013; PGY6 in 2019-20 and PGY7 in 2020-21.
- **David Voce:** entered 2014; research gap year in 2021-22; PGY7 in 2022-23.
- **Kwadwo Sarpong:** PGY4 in both 2025-26 and 2026-27.
- **Michael Longo:** entered 2020; chief as PGY6 in 2025-26, then "PGY 7/Neuro Endovascular Fellow" in 2026-27.

From 2022-23 onward some chiefs are PGY6.

**Residents entering 2011 or later:** 51.

**Adjudication (phase 1, superseded; see Outcomes):** 29 completed, 24 in training, 5 left with outcome unknown, 2 switched specialty (by NPI).

## Problems
- The adjudicator merges the twins Mahan and Mayshan Ghiassi, who entered before 2011. Separate training_history rows were inserted for them.
- The 2018-19 PGYs are inferred, because the side menu carries no PGY labels.
- All the Common Crawl scans that failed in phase 1 ran successfully in phase 2. The one exception is CC-2015-32 to 2015-48 on the old host, which was not needed because 2015-16 is already observed. Scratch files are in `data/raw/extraction/p117/phase2/`.
- There is no alumni page.
