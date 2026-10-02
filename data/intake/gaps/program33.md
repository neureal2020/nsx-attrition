# Program 33 - LSU School of Medicine (New Orleans) Neurosurgery - gap report

7-year program; the program says it "accepts one and two residents in alternating years" (site text 2016-2023). Entrants 2011+: **25**. Phase 1 built 2026-09-27; phase 2 updated 2026-09-28.

## Hosts
- http://www.medschool.lsuhsc.edu/neurosurgery/residency_residents.aspx (2007-12 -> 2020-07 (roster content; Common Crawl fills 2017-18); by 2022-08 a meta-refresh stub to residents.lsuhsc.edu; 404/301 from 2024-07)
- http://www.medschool.lsuhsc.edu/Neurosurgery/residents.asp (2004 -> 2007, before the study window)
- https://www.medschool.lsuhsc.edu/neurosurgery/ (department site: alumni.aspx, faculty.aspx, docs/ newsletters and resident manuals) (2004 -> live)
- https://residents.lsuhsc.edu/no/neurosurgery/residents.aspx (2024-04 first capture in any archive; the site root has existed since 2020-10 -> live)

## Year status (phase 2)
| Year | Status | Significance | Reason |
|---|---|---|---|
| 2011-12 .. 2015-16 | observed | none | full roster |
| 2016-17 | reconstructed + partial | low | no roster anywhere. The 2015-16 roster, the Aug 2016 newsletter (which names the whole 2016 intern class: Podet and Webb) and the 2017-18 roster give the same class membership on both sides. |
| 2017-18 | **observed (new)** | none | Common Crawl CC-MAIN-2017-43, 2017-10-19, "2017- 2018 Residents" (9 names) |
| 2018-19, 2019-20 | observed | none | full roster (in-year CC captures from 2018-10 and 2019-02 confirm the July 2019 Wayback capture) |
| 2020-21 | reconstructed | low | every 2019-20 resident is accounted for; the 2020 class (Crabill and Shoap, MD 2020) fills an even-year class of 2 |
| 2021-22 | reconstructed | low | same bracketing; the 2021 class (Lawhon, MD 2021) fills an odd-year class of 1 |
| 2022-23 | reconstructed | low | same bracketing; the 2022 class (Glasser and Hayden, MD 2022) fills an even-year class of 2 |
| 2023-24 .. 2026-27 | observed | none | full roster |

No year is still significant. For 2016-17 and 2020-23, an unseen resident could only be one who transferred in and out within one year, or an extra entrant beyond the stated 1/2 alternation. PubMed and OpenAlex affiliation mining (2016-2025) found no unlisted resident.

## Evidence for the 2020-23 reconstruction
- **Lasseigne** (PGY-7 2020-21): Thibodaux Regional, 19 Aug 2021: "completed her Residency and Internship in Neurosurgery at LSUHSC New Orleans". PubMed shows an LSU neurosurgery affiliation in Jun 2021.
- **Morrow and Shields** (PGY-6 2020-21, PGY-7 2021-22): LSU Dept of Neurosurgery affiliation Sep 2021 (PMID 34557290). Afterwards Morrow is in neurosurgery at Colorado (2024) and Desert Regional (2025), and Shields in Emory neurosurgery (Jun 2023). Graduation in 2022 is **inferred**: no program page confirms it.
- **Podet** (PGY-7 2022-23): the LSU neurosurgery faculty page lists "Residency: Neurological Surgery, LSUHSC New Orleans", and he is on the residents-site faculty list by Dec 2023.
- **Robichaux, Girolamo, Wilson, Guillen Arguello**: on the 2019-20 and 2023-24 rosters at matching PGYs.
- **Crabill, Shoap, Lawhon, Glasser, Hayden**: PGY on the 2023-24 roster plus MD year gives the entry year.

## Alumni page
https://www.medschool.lsuhsc.edu/neurosurgery/alumni.aspx lists graduates for 2014 (Trahan), 2015 (Sure, Volk), 2016 (Conger), 2017 (Eggart), 2018 (Gesheva Baxter), 2019 (DiGiorgio) and 2020 (Crutcher). Every capture from 2021 to 2025 stops at 2020.

## Departures
- **Walid Radwan**: last seen 2014-15 as PGY-2. He transferred to West Virginia University (program 121) as PGY-3 in 2015-16; PubMed shows a WVU neurosurgery affiliation from Oct 2016.
- **Leo Webb**: PGY-1 in 2016-17 (newsletter) and PGY-2 in 2017-18 (Common Crawl roster). He then **switched to anesthesiology**: the LSU New Orleans anesthesiology residents page (Oct 2019) lists him in the Class of 2021. He is absent from that page's class lists in the Nov 2017 and Jul 2018 captures, so he joined in July 2018.
- John Gachiani: entered 2005, before the study window; not loaded.

## Joiners
None.

## training_history rows added (phase 2)
- Radwan: transferred, end_year 2015
- Webb: switched_specialty, end_year 2018
- Completions:
  - Lasseigne 2021 (employer_bio)
  - Morrow 2022 and Shields 2022 (source_type other, inferred)
  - Podet 2023 (program_page, faculty)
- PGY-terminal roster rows: Robichaux 2024, Girolamo 2025, Wilson 2025, Guillen Arguello 2026, Badr 2012, Owen 2012

## Adjudication
- 18 completed
- 11 in training
- 1 transferred (Radwan)
- 1 switched specialty (Webb)

## Common Crawl
- Phase 1 covered CC-MAIN-2016-18 to 2016-40.
- Phase 2 covered 2016-07 and 2016-44 through 2023-50 on both SURT prefixes. Roster hits:
  - 2017-18: 2017-10-19, 2017-12, 2018-02
  - 2018-19: 2018-10, 2019-02, 2019-04
  - 2019-20: 2019-10; the 2020-07 capture is stale
  - 2022-08: redirect stub only
- residents.aspx on residents.lsuhsc.edu was never crawled before 2024.
- Crawls that failed on range errors: CC-MAIN-2017-30, 2019-39 and 2022-33 (residents prefix), and 2018-13, 2019-30 and 2020-24 (medschool prefix). All were retried successfully except CC-MAIN-2018-13 on the medschool prefix, which does not matter because 2017-18 and 2018-19 are both observed.

## Problems
- Morrow and Shields' graduation year (2022) comes from publication affiliations, not a program page.
- The Radwan transfer-in row at WVU (program 121) was not written, because that row is outside this program.
- The programs.name field contains ACGME footer text.

Scratch: data/raw/extraction/p33/ (phase 1) and data/raw/extraction/p33/phase2/ (ccrun.py, cc/, gapaudit.out, pm_authors.txt, oa_out.txt, pubmed_2020_2025.txt, Newsletter_2017.pdf/.txt, scan_*.txt).
