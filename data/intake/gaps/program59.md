# Program 59: Southern Illinois University School of Medicine (Springfield, IL)

- Length 7 years, complement 1 per year. New program: ACGME initial accreditation 2013-06-29, first resident July 2014 (`first_class_year` 2014). 2011-12 to 2013-14 are pre-program years, not gaps.
- **Observed:** every academic year from 2014-15 to 2026-27 (13 years). **Reconstructed:** none. **Missing:** none.
- Residents entering 2011 or later: 13 (entry classes 2014-2026, one each).

## Hosts / pages
| Page | Dates |
|---|---|
| siumed.edu/surgery/neurosurgery/residents.html (old site) | 2014-12 to 2017-04 |
| siumed.edu/surgery/neuro, the division home page with a "Neurosurgery Residents and Fellows" block | 2017-07 to 2019 |
| siumed.edu/surgery/neuro/resident-fellow | 2018-07 to 2019-12 |
| siumed.edu/resident-fellow?field_resident_program_tid=481 (school-wide search, "Class of") | 2018-07 to 2021-03 |
| siumed.edu/resident-fellow?f[0]=resident_program:481 (faceted search) | 2022-01 to live |
| /surgery/neuro/neurosurgery-resident-research (live, "2025-26 Resident Scholarly Activity") | live |

## Captures used
| AY | Capture | Residents |
|---|---|---|
| 2014-15 | residents.html 2014-12-04 | 1 |
| 2015-16 | residents.html 2015-10-03 | 2 |
| 2016-17 | residents.html 2016-10-31 | 3 |
| 2017-18 | /surgery/neuro 2017-12-07 | 4 |
| 2018-19 | /surgery/neuro 2018-11-19 | 5 |
| 2019-20 | tid=481 search 2019-10-16 | 6 |
| 2020-21 | tid=481 search 2021-03-05 | 7 |
| 2021-22 | facet 431+481, 2022-01-17 (one page, all 25 shown) | 6 |
| 2022-23 | facet 481, 2023-02-02 | 6 |
| 2023-24 | facet 481, 2024-07-10 (content is still 2023-24) | 7 |
| 2024-25 | facet 481, 2025-04-18 | 7 |
| 2025-26 | live resident-research page (source_type other), all 7 listed | 7 |
| 2026-27 | live facet 481 | 7 |

The PGYs come from each resident's "Class of" year, because the pages list names without PGY labels; the Apr-2017 capture and the research-awards page agree with this.

## Significant gaps
None. Every year from 2014-15 to 2026-27 is observed and complete (phase 2 checked this).
- Per-year significance: every year is `none`, except 2025-26, which is `low` (the list comes from the scholarly-activity page, not a roster, but it names all 7 classes).
- **2021-22 (6 listed, no PGY6) and 2022-23 (6 listed, no PGY7):** both are Watson's vacated Class-of-2023 slot, not parser misses. I re-read the raw HTML: there are no "Chiefs" headings, no PGY labels, no pagination, and each card's program label is Neurosurgery. The name counts are 6, 6, 7 and 7 for 2021-22 to 2024-25.
- Terminal PGY is 7 for every entry cohort, 2014-2026.

## Departures
- **Victoria Watson** (Class of 2023, entered 2016). She was last listed as PGY-5 in Mar 2021 (her SIU profile was last captured Feb 2021) and is absent from Jan 2022 on. **She switched to internal medicine.** The Marshall University JCESOM Internal Medicine "Our Residents" page lists "Victoria Watson, MD. Hometown: Pinch, WV. Medical School: Marshall University Joan C. Edwards SOM. Future Goals: Neurocritical care Fellowship":
  - under **PGY-1** in the Sep-2023 capture ([wayback](https://web.archive.org/web/20230928212739/https://www.jcesom.marshall.edu/residents-fellows/programs/internal-medicine/our-residents/));
  - under **PGY-2** in the Dec-2024 capture;
  - not in the Mar-2022 or Sep-2022 captures.
- The identity is confirmed because her SIU profile gives the same med school (Marshall). PubMed tracks Victoria L Watson through Marshall neurosurgery (2017), then SIU neurosurgery (2019-2022), then Marshall Internal Medicine (2024, PMID 39886699). NPPES was not used.
- She left SIU between Mar 2021 and Jan 2022, most likely in June 2021. Her 2021-23 interval is unaccounted for.

## Joiners
None.

## Adjudication
7 in training, 5 completed (Alex Michael 2021, Breck Jones 2022, Adam Lipson 2024, Nathan Nordmann 2025, Matthew Weber 2026), 1 switched specialty (Watson).

## training_history (phase 2)
6 rows (th_id 3404-3409):
- 5 completions: `completed='yes'`, `source_type='program_page'`, note "PGY-terminal roster".
- Watson: `completed='no'`, `departure_type='switched_specialty'`, `end_year` 2021, source is the Marshall IM page.

## Problems
- The program has no alumni or graduates page. Completions come from PGY7 roster presence (phase 2 added training_history rows).
- The Common Crawl pass was started and then stopped, because all years were already covered.
- `scripts/wayback.py` fetch returned None in this session. Captures were fetched with curl through `data/raw/extraction/p59/wbget.sh` instead.
