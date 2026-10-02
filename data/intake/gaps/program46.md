# Program 46: Montefiore Medical Center / Albert Einstein College of Medicine (Bronx, NY)

## Phase 2 (2026-09-28) summary
7-year program; entrants alternated 2/1 per year until 2015, then 2 per year from 2016 (except 2018 and 2020 with 1). Every entrant PGY-terminal = 7.

| AY | Status | Significance | Reason |
|---|---|---|---|
| 2011-12 | observed (content-dated) | low | einstein list captured 2013; consistent with alumni grads and 2014-15 |
| 2012-13 | reconstructed (11) | low | 2011-12 continuers + Haranhalli/Kobets (bios: internship+residency at Montefiore). 2012 class full at 2. Only risk: a second 2013 entrant who left before Nov 2014 |
| 2013-14 | reconstructed (11) | low | as above + Gelfand (2013, bio) |
| 2014-15 | observed | none | |
| 2015-16 | reconstructed (10) | **significant** | Sandler (PGY-7 expected) unresolved; everyone else accounted for |
| 2016-17 | reconstructed (11) | low | = complement; finishers and entrants dated by PubMed/bios |
| 2017-18 | reconstructed (11) | low | = complement; Hamad/Holland (Rutgers NJMS 2017) added |
| 2018-19, 2019-20 | observed (CC) | none | |
| 2020-21 | observed | none | |
| 2021-22 | observed + 2 reconstructed interns | low | Benton (MD 2021) and Kirnaz (Montefiore internship) from virtual-tour bios |
| 2022-23 | reconstructed (12) | low | DLGR and Scoco 2023 graduation confirmed by employer bios |
| 2023-24 | observed | none | |
| 2024-25 | reconstructed (11) | low | Inocencio PGY-7 (City of Hope 2026), Kang/Mitrasinovic PGY-1 (PubMed 2024); only Javed's exit timing unknown |
| 2025-26 | observed | none | |
| 2026-27 | missing | **significant** | live page (re-fetched 2026-09-28) unchanged from 2025-26 |

### Outcomes recorded in training_history (18 rows)
- Graduations with independent evidence (7): Biswas 2016 (PubMed: attending at Carle 2020, Westchester since 2022), Jada 2017 (Weill Cornell spine 2017-18), Nasser 2017 (Cincinnati 2018-), Nakhla 2018 (Brown 2018-19), De La Garza Ramos 2023 (Montefiore bio), Scoco 2023 (Stony Brook profile: residency Montefiore 2023), Inocencio 2025 (City of Hope 2026).
- PGY-terminal roster graduations (9): Baxi 2015, Kobets and Haranhalli 2019, Gelfand 2020, Echt 2021, Ammar and Cezayirli 2022, Holland and Hamad 2024.
- **Kainaat Javed**: completed=no, switched_specialty, end_year 2025. She was last listed at PGY-2 in 2023-24. The last manuscript with her Montefiore neurosurgery affiliation was received in Jan 2025, and a Jun 2026 paper lists her at the Department of Medicine, New York University (PMID 42316552). She left between Jul 2024 and Jul 2025.
- **Adam Sandler**: completed=unknown. His last Montefiore affiliation is on a manuscript received Nov 2016, with no later neurosurgery output. NPPES shows primary Preventive/Occupational Medicine, but NPPES alone is not evidence.

### Adjudication after phase 2
34 residents (25 entered 2011+): 20 COMPLETED, 12 IN TRAINING, 1 SWITCHED SPECIALTY (Javed), 1 LEFT unknown (Sandler). No joiners and no transfers (crossmatch.json has no entries for program 46).

### Searches (phase 2)
- PubMed affiliation mining: 1957 PMIDs for Montefiore/Einstein neurosurgery, 2010-26, plus per-person author histories. No unlisted residents turned up. Two names were checked and excluded:
  - Adesh Tandon: 2013 Montefiore affiliation, but he is on no roster (his later affiliations are UVA and NYMC, and he is on neither roster), so he was treated as a research fellow.
  - Niketh Bhashyam: Spine Research Group affiliation 2016-17 only, not a resident.
- Wayback, full prefix of both virtual-tour hosts, including page-data.json from Feb 2024, Dec 2024, Aug 2025 and Jan 2026. The Dec 2024 JSON still carries the 2023-24 list.
- Einstein department aspx pages (2013-2018). The current-residents page (id=33796) in Sep/Oct 2015 is frozen on the 2014-15 list.
- Common Crawl, re-run with the new filter over 2012-18 and 2021-26. The montefiore.org residents page is frozen on the 2020-21 list in every copy from 2021 to Dec 2023, and the Einstein pages are frozen as well.
- Bios: Montefiore provider bios, the Stony Brook provider profile, and the virtual-tour bios.
- Einstein match results carry no names. The montefiore.org pages have no alumni list.
- NPPES, used as support only.

### Problems (phase 2)
Phase 2 Common Crawl reruns (new filter) were killed after ~45 min in retry backoff. Unfinished: ccB (2012-18 montefiore residency / einstein dept prefixes) crawls CC-MAIN-2016-36 (montefiore neurological-surgery-residency part) through CC-MAIN-2018-51, which phase 1 had already covered for the einstein current-residents URL (identical frozen copies); ccA (virtual-tour hosts + montefiore residency 2021-26) crawls CC-MAIN-2025-51 (montefioreeinstein part) through CC-MAIN-2026-39. Range failures: CC-MAIN-2021-21 virtualtour prefix; CC-MAIN-2023-06, 2024-22, 2024-46 montefiore neurological-surgery-residency; CC-MAIN-2015-14 montefiore professional-training prefix. Also: WMC (wmchealth.org) and doctors.stonybrookmedicine.edu return 403 live (Stony Brook read via Wayback); einsteinmed.edu live Access Denied (not bypassed).

---
# Phase 1 report (kept for reference; superseded above where they differ)

7-year program, 1-2 residents per year (the live page says "one to two"). Website of record: montefiore.org/neurosurgery-professional-training-programs-residency, which now redirects to montefioreeinstein.org/patient-care/services/neurosurgery/education (that page has no roster).

## Hosts and paths
| Host / path | Dates | Content |
|---|---|---|
| montefiore.org/prof/departments/neurosurgery/ (residency/, bios/) | 2007-02 to 2012-05 | No current roster. The bios/ page from Dec 2011 has an old pre-2010 resident list. Returns 301 from May 2012. |
| einstein.yu.edu/departments/neurological-surgery/current-residents/ | 2013-05 (CC) to 2018-10 | Showed the **2011-12** list until Sep 2014, then the 2014-15 list, frozen until 2018 |
| einstein.yu.edu/departments/neurological-surgery/alumni/ | 2012-09 to 2018-10 | Graduates 2007-2014 |
| montefiore.org/neurosurgery-professional-training-programs-residency-residents | 2014-11 to 2019-01 | Frozen on the 2014-15 list until Aug 2018. Rebuilt Dec 2018 with the 2018-19 list, which exists **only in Common Crawl**. |
| montefiore.org/neurological-surgery-residency-residents (body id=6571) | 2018-12 to 2024-05 | 2018-19 list in Feb-May 2019 and 2019-20 list in Feb-Jun 2020 (both CC). From Aug 2020 it is frozen: the headings show 2020-21 and the inline labels show 2019-20. |
| virtualtour.montefiore.org/neurological-surgery-residency | 2021-01 to 2025-04 | The roster from 2020-21 onward. Returns 301 from Aug 2025. |
| virtualtour.montefioreeinstein.org/neurological-surgery-residency | 2025-08 to live | 2025-26 list, unchanged on the live page |
| montefiore.org neurological-surgery-residency/-education/-team; montefioreeinstein.org education/team; einsteinmed.org/.edu dept pages | 2019 to live | No roster. The live einsteinmed.edu returns Access Denied. |

## Years
| AY | Status | Source |
|---|---|---|
| 2011-12 | observed, **content-dated** | einstein current-residents page (Wayback 2013-08-29). The content matches 2011-12 (Nakhla PGY-1 here and PGY-4 in Nov 2014; Daniels, Altschul and Kinon graduate 2012, 2013 and 2014). |
| 2012-13 | reconstructed (9) | Bracketed or confirmed by the alumni page. Haranhalli and Kobets (2012 entrants) are not included. |
| 2013-14 | reconstructed (8) | Same basis. Gelfand (2013 entrant) is not included. |
| 2014-15 | observed | montefiore.org, Wayback 2014-11-02 |
| 2015-16 to 2017-18 | reconstructed (5 each) | Both sites stayed frozen on the 2014-15 list, confirmed in Wayback and in every Common Crawl copy. Only Haranhalli, Kobets, Gelfand, Echt and Cezayirli are reconstructed (Cezayirli's PGY is unknown). |
| 2018-19 | observed (CC) | CC-MAIN-2018-51, 2018-12-16, 11 names |
| 2019-20 | observed (CC) | CC-MAIN-2020-10, 2020-02-27, 11 names |
| 2020-21 | observed | virtual tour, 2021-01-16 |
| 2021-22 | observed, **incomplete** | virtual tour, 2021-09-21. It lists no PGY-1, so the 2021 interns Benton and Kirnaz are missing. |
| 2022-23 | reconstructed (6) | The virtual tour showed the 2021-22 list in every capture through Mar 2023 |
| 2023-24 | observed | virtual tour, 2023-12-11 |
| 2024-25 | reconstructed (8) | The virtual tour kept the 2023-24 list through Apr 2025 |
| 2025-26 | observed | virtual tour on the montefioreeinstein.org host, 2025-11-05 |
| 2026-27 | **missing** | The live page (2026-09-27) is identical to 2025-26: the PGYs have not advanced and there are no new interns |

All 2012-13 to 2025-26 unobserved years are significant gaps. A second entrant in any of the single-entrant classes (2011, 2013, 2015, 2018, 2020) who left inside a gap would not show up.

## Alumni (inserted into training_history)
Lawrence Daniels 2012, David Altschul 2013, Merritt Kinon 2014, Michael Weicker 2014. The page was not updated after 2014.

## Departures (left the roster before the terminal PGY)
- **Kainaat Javed**: last seen 2023-24 at PGY-2 (2022 entrant). She is absent in 2025-26, while her classmate Nia continues. This is the strongest attrition candidate; 2024-25 was not observed.
- Gap artefacts are likely for the rest. Their final years fall inside unobserved windows:
  - Biswas and Sandler: last seen 2014-15 at PGY-6.
  - Jada and Nasser: last seen 2014-15 at PGY-5.
  - Nakhla: last seen 2014-15 at PGY-4.
  - De La Garza Ramos and Scoco: last seen 2021-22 at PGY-6. De La Garza Ramos is now faculty.
  - Inocencio: last seen 2023-24 at PGY-6.
- Not departures, but worth noting:
  - Michael Weicker was listed at PGY-4 in 2011-12, yet the alumni page gives class of 2014. He may have been promoted early.
  - Phillip Cezayirli was PGY-1 in 2014-15 and PGY-4 in 2018-19, so he spent an extra year somewhere. He finished PGY-7 in 2021-22.

## Joiners
None confirmed. Everyone first seen above PGY-1 appears right after an unobserved year:
- Haranhalli, Kobets and Gelfand (2014-15)
- Ammar, Scoco, De La Garza Ramos, Hamad and Holland (2018-19)
- Benton, Kirnaz, Nia and Javed (2023-24)
- Kang and Mitrasinovic (2025-26)

## Adjudication (16_adjudicate)
34 residents; 25 entered in 2011 or later. 13 COMPLETED, 12 IN TRAINING, 9 LEFT with outcome unknown (Javed plus the 8 gap artefacts listed above).

## Problems
- Common Crawl fetches that failed, for phase 2 to retry:
  - CC-MAIN-2012 montefiore residency prefix (size)
  - CC-MAIN-2014-23 and CC-MAIN-2015-11 org,montefiore)/neurological-surgery-residency
  - CC-MAIN-2017-09 einstein current-residents
  - CC-MAIN-2018-09 montefiore residency prefix
  - CC-MAIN-2024-51 virtualtour page-data
  - CC-MAIN-2025-51 montefioreeinstein virtualtour
- The 2018-19 and 2019-20 rosters exist only in Common Crawl (loaded as `other`).
- Baxi, Haranhalli, Gelfand and De La Garza Ramos are now faculty. A phase-2 bio check can use this to close the gap-artefact departures.
