# ACGME Data Resource Book: Neurological Surgery attrition

Data: `acgme_attrition.json`. There is one row per academic year (AY), keyed to **the AY in which the residents left**, not to the year of the book.

## Lag: each book reports the previous year's departures
Each Data Resource Book reports residents who left during the **previous** AY. For example, the 2011-2012 book says: "Counts reflect residents completing a program between 9/1/2010 and 8/31/2011". The 2024-2025 book covers residents who "graduated or left their programs between September 1, 2023 and August 31, 2024". So the book for year N+1 gives the attrition for AY N.

## Tables used
| Books | Table | Columns |
|---|---|---|
| 2011-12 to 2014-15 | "Number of Residents Not Graduating from a Program, by Specialty and Subspecialty" | # not graduating, % in specialty not graduating, Deceased, Dismissed, Transferred, Unsuccessfully Completed Program, Withdrew |
| 2016-17 to 2024-25 | Table D.13 "Number of Residents Leaving Prior to Completion of a Program by Specialty and Subspecialty and Status, YYYY AY" | Number of Residents Not Graduating, Transferred, Withdrew, Dismissed, Unsuccessfully Completed Program, Deceased |
| 2016-17 to 2024-25 | Table D.14 "Number of Transferring Residents by Specialty and Resident Year" | Transfers by program resident year 1-7 (**transfers only**, not total attrition) |
| 2024-25 only | Table D.15 "Number of Transferring Residents by Specialty and New Specialty" | Transfer Specialty Same/Different, Transfer Subspecialty Same/Different |

- The old-format books print `.` for zero cells. The components always sum to the printed total, so these are recorded as 0.
- In D.14, the resident-year column for each value was assigned from the word x-coordinates in the PDF, because blank cells shift the plain-text layout.
- `residents_on_duty` is the number of active NS residents in the AY the attrition describes. It comes from the books' multi-year trend tables (the page is cited in each row's `notes`).
- The old books also print a "% not graduating" (`pct_not_graduating_printed`). Its denominator appears to be the book-year resident count (for example, 32 of 1,212 is 2.6%), not the departure year.

## Definitions of the reasons
None of the books read here defines Transferred, Withdrew, Dismissed, Unsuccessfully Completed Program or Deceased. The "Definitions" / "Explanation of Terms" sections do not cover these statuses. The books only say that these statuses mean the resident "left or completed the program" within the 9/1–8/31 window, and they group them as leaving "prior to successful completion". Transfers count a move to any other program, including one in the same specialty. D.15 (2024-25 book only) splits transfers into same vs different specialty. ACGME's online Glossary of Terms is cited by the books for fuller definitions, but it was not read here.

## Neurological surgery results
| AY left | On duty | Not graduating | Transferred | Withdrew | Dismissed | Unsucc. | Deceased | Transfers by PGY |
|---|---|---|---|---|---|---|---|---|
| 2010-11* | 1,133 | 35 | 14 | 11 | 8 | 2 | 0 | – |
| 2011-12 | 1,179 | 32 | 11 | 15 | 5 | 1 | 0 | – |
| 2012-13 | 1,212 | 26 | 8 | 15 | 3 | 0 | 0 | – |
| 2013-14 | 1,265 | 25 | 9 | 14 | 2 | 0 | 0 | – |
| 2014-15 | 1,295 | **missing** | | | | | | |
| 2015-16 | 1,325 | 31 | 15 | 11 | 4 | 0 | 1 | yes |
| 2016-17 | 1,375 | 34 | 21 | 12 | 1 | 0 | 0 | yes |
| 2017-18 | 1,408 | 29 | 11 | 14 | 3 | 0 | 1 | yes |
| 2018-19 | 1,462 | 37 | 13 | 14 | 10 | 0 | 0 | yes |
| 2019-20 | 1,515 | 16 | 5 | 7 | 4 | 0 | 0 | yes |
| 2020-21 | 1,561 | 25 | 13 | 10 | 2 | 0 | 0 | yes |
| 2021-22 | 1,579 | 21 | 8 | 10 | 3 | 0 | 0 | yes |
| 2022-23 | 1,593 | **missing** | | | | | | |
| 2023-24 | 1,607 | 30 | 6 (3 same / 3 different specialty) | 18 | 6 | 0 | 0 | yes |
| 2024-25 | 1,611 | **not yet published** | | | | | | |

\*2010-11 is outside the requested range. It comes from the 2011-12 book.

## Missing years
- **2014-15** is in the 2015-2016 book (`2015-2016_acgme_databook_document_locked.pdf`).
- **2022-23** is in the 2023-2024 book (`dataresourcebook2023-2024.pdf`).
  - Both files are over the 10 MB WebFetch limit.
  - In Chrome, the PDF viewer showed only thumbnails, never rendered the main pages, and `get_page_text` returned no text.
  - No later book repeats single-year attrition, so these years are still unfilled.
  - Next step: open these pages by hand. The table should be D.13 at about pdf p.106 in the 2015-16 book.
- **2024-25** would appear in the 2025-2026 book. That book is not listed on the ACGME Data Resource Book page as of 2026-09-30.
