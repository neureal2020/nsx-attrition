# Program 9: Carolinas Medical Center Program (Charlotte, NC)

- 7-year program, 1 resident per year. Faculty are Carolina Neurosurgery & Spine Associates (CNSA). Sponsor: Carolinas HealthCare System, now Atrium Health.
- **New program: the first class entered in July 2014** (Tyler Atkins was the only resident, PGY1, in 2014-15; a CNSA newsletter from April 2014 announced the "new Charlotte residency"). The years 2011-12 to 2013-14 are before the program started. They are not gaps.

## Hosts
| Host/path | Dates | Notes |
|---|---|---|
| www.carolinashealthcare.org/neurological-surgery-residents | 2015-01 to 2017-07 (Wayback) | Roster. The program page `neurological-surgery-residency-programs-medical-education` goes back to 2014-03 |
| www.carolinashealthcare.org/education/graduate-medical-education/physician-residencies/neurological-surgery/residents | 2017-08 to 2018-06 | Sitecore era. Wayback has **no** capture; Common Crawl has it |
| atriumhealth.org/education/graduate-medical-education/physician-residencies/neurological-surgery/residents | 2018-09 (CC) / 2019-08 (Wayback) to live | Current roster. The DB website (carolinashealthcare.org) now 301s here |
| www.carolinasneurosurgicalresidency.org | 2015-08 to 2022-04 | CNSA Weebly site with faculty and schedules only; links to the CHS roster |
| cnsa.com/about-us/residency-program, cnsa.com/newsletter/archive/2014-april/residency.html | 2014 to 2019 | Pointers and the launch announcement. No roster |

## Observed years (one capture each)
| AY | Source | Roster |
|---|---|---|
| 2014-15 | WB 20150127 | Atkins 1 |
| 2015-16 | WB 20151130 | Atkins 2, Parish 1 |
| 2016-17 | WB 20161202 | Atkins 3, Parish 2, Rossi 1 |
| 2017-18 | CC-MAIN-2018-09 (2018-02-19) | Atkins 4, Parish 3, Rossi 2, Peters 1 |
| 2018-19 | CC-MAIN-2018-39 (2018-09-23) | Atkins 5, Parish 4, Rossi 3, Peters 2, Mulvaney 1 |
| 2019-20 | WB 20191209 | Atkins 6 ... Monk 1 |
| 2020-21 | WB 20210119 | Atkins 7 ... DeCarlo 1 |
| 2021-22 | WB 20211026 | Parish 7 ... VanHorn 1 |
| 2022-23 | WB 20221002 | Rossi 7 ... Zeitouni 1 |
| 2023-24 | WB 20231205 | Peters 7, Mulvaney 6, Monk 5, DeCarlo 4, VanHorn 3, Zeitouni 2, Miller 1 |
| 2024-25 | WB 20241208 | Monk 6, DeCarlo 5, VanHorn 4, Zeitouni 3, Miller 2, Allen 1 (**no Mulvaney, no PGY-7**) |
| 2025-26 | WB 20251214 | Monk 7, DeCarlo 6, VanHorn 5, Zeitouni 4, Miller 3, Allen 2, Drossopoulos 1 |

Reconstructed: none.

**Missing: 2026-27.** The live page (fetched 2026-09-27) is identical to the 2025-26 roster, which is also what the Wayback captures from 2026-03 and 2026-06 show. It has not been updated, so I did not load it as 2026-27. Two things remain unobserved: the 2026 intern, and whether Monk finished in June 2026.

Content-dating notes: the Wayback captures from 2019-08 and 2019-10 still showed the 2018-19 list, and the 2024-09 capture still showed the 2023-24 list. I did not use either of those as the roster for the year in which it was captured.

## Consistency
- Every resident has one entry year across all observations: Atkins 2014, Parish 2015, Rossi 2016, Peters 2017, Mulvaney 2018, Monk 2019, DeCarlo 2020, VanHorn 2021, Zeitouni 2022, Miller 2023, Allen 2024, Drossopoulos 2025. Each class has 1 person, which matches the complement.
- **Departure: Graham Mulvaney** (entered 2018). He was last seen in 2023-24 as PGY-6 and was absent from 2024-25 onward, when the program listed no PGY-7. By 2024-11 the main page had replaced his testimonial with Peters'. He may have left or transferred one year before the terminal year; the outcome is unknown.
- Joiners above PGY-1: none.
- Completions: Atkins (PGY-7 in 2020-21) and Parish (PGY-7 in 2021-22) are inferred from the roster. Rossi (2023) and Peters (2024) are "Graduate" testimonials on the program main page. The program has no alumni page. I inserted Rossi and Peters into training_history as th_id 758 and 759.
- Adjudication (16): 7 in training, 4 completed, 1 left with outcome unknown (Mulvaney).

## Problems
- The live roster is stale, so 2026-27 is missing (see above).
- The DB `programs.website` is the old carolinashealthcare.org URL, which now redirects to atriumhealth.org.
- Wayback has nothing between 2017-07 and 2019-07. Common Crawl filled that gap. Three CC index range fetches failed (2017-34, 2017-51, 2018-30); these were outside the captures I needed.

## Phase 2 (2026-09-28)
- **Mulvaney: transfer out, confirmed.** He left Carolinas after 2023-24 (PGY-6) and joined the University of Oklahoma (program 99) at PGY-6 in 2024-25. He graduated from OU in 2026. Evidence: both programs' rosters, plus PubMed affiliations (CMC through 2024 in PMID 39278539; OU in 2025-26 in PMIDs 40965516 and 40804577). training_history th 3133 records the transfer out (end_year 2024). th 2989 is the OU row.
- **Graduates 2021-2026:**
  - 2021 Atkins: PGY-terminal roster. He was PGY-7 in 2020-21 and was gone from the page by 2021-09 (th 3130).
  - 2022 Parish: CNSA employer bio (live, and Wayback 2022-08-20). It lists the CMC residency, chief resident 2021-22, and "first graduate ... to join CNSA" in July 2022 (th 3131).
  - 2023 Rossi (th 758) and 2024 Peters (th 759): main-page testimonials.
  - 2025: no graduate, because Mulvaney transferred.
  - 2026 Monk: PGY-7 on the 2025-26 roster, recorded as a PGY-terminal graduation (th 3132). Not confirmed independently.
- **Still missing: 2026-27.** The live page was still stale on 2026-09-28. Significance is **low**: the only unknowns are the 2026 intern and confirmation of Monk's graduation.
- Every other year from 2014-15 to 2025-26 is observed. Each has a complete roster with 1 resident per class, so significance is none.
- Adjudication: 6 in training, 5 completed, 1 transferred.
