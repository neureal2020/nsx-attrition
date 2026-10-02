# Program 74: University of California (Irvine) Program (Orange, CA)

7-year program; ACGME accreditation and first residents July 2008. Took about 1 resident a year through the 2018 entry class and 2 a year from 2019 (only 1 in 2020 and in 2022). Roster file: `data/intake/rosters_program74.json` (16 captures, 149 rows). JSON twin: `program74.json`.

## Hosts
| Host/path | From | To | Content |
|---|---|---|---|
| neurosurgery.uci.edu/residency.shtml, /residrein.shtml | 2008-07 | 2010-08 | old static site (before the study window) |
| neurosurgery.uci.edu/residency.asp | 2011-01 | 2024-04 | resident list without PGY labels 2011-13; roster section with PGY labels 2019-12 to 2024-04 |
| neurosurgery.uci.edu/resident-bios.asp | 2014-10 | 2019-07 | "residents for YYYY-YYYY" with PGY labels |
| neurosurgery.uci.edu/resident-alumni.asp | 2016-07 | 2019-07 | alumni by class |
| neurosurgery.uci.edu/news_Residency_Program_Year4.asp | 2012-01 | 2020-07 | caption of the June-2011 photo of the 2010-11 residents |
| medschool.uci.edu/.../neurological-surgery/education-training/residency-program/residents-alumni | 2024-10 | live | residents grouped by "Class of", plus alumni; every old neurosurgery.uci.edu URL now 301-redirects to medschool.uci.edu |

## Years
- **Observed:** every year from 2011-12 to 2026-27 except 2012-13.
- **Reconstructed:** 2012-13 (phase 2: **low**, was significant). The Wayback capture of 2012-11-07 and the Common Crawl capture CC-MAIN-2013-20 (2013-05-19) both carry the unchanged 2011-12 list, with no 2012 intern. Rows reconstructed:
  - 7 residents listed in both 2011-12 and 2013-14.
  - Reeves (on the 2011-12 list; alumni Class of 2013).
  - Paff as PGY-1 (PGY-2 in 2013-14; alumni Class of 2019).
- **2011-12:** the list has no PGY labels, so each PGY is taken from the 2013-14 roster (which has labels) minus 2, and from the alumni class years.
- **Content dating** (the capture date or page heading does not match the roster shown):
  - The 2013-14 roster is a resident-bios capture from 2014-10 headed "2013-2014". Common Crawl on 2013-12-10 has the same 8 names.
  - The 2020-21 roster comes from a 2021-05 capture whose heading still says "2019-2020".
  - The 2022-23 roster comes from a 2023-07 capture headed "2022-2023".
- **2026-27:** the live page has moved on from 2025-26, so it is loaded.
- **Common Crawl** 2012-2013 (3 crawls) is done, with no failures.

## Departures
- **Isidora Beach**: PGY-1 in 2023-24. Gone from 2024-25 onward and not on the alumni list. This is pre-terminal attrition. Phase 2 found no destination (see below).
- **Marlon Mathews**: PGY-7 in 2014-15, then gone. He never appears on any alumni list (the 2016, 2019 and live lists have no Class of 2015). Phase 2 could not confirm completion (see below).

## Joiners (transfers in)
- **George Hanna**: PGY-5 in 2017-18, from Loma Linda (PGY-4 there in 2016-17). Not on the 2016-17 roster. Class of 2020.
- **Nathan Oh, DO**: PGY-4 in 2017-18, from Loma Linda (PGY-3 there in 2016-17). Not on the 2016-17 roster. Class of 2021.
- Hanna and Oh were part of the 2017 Loma Linda exodus (all six non-graduating LL residents left in summer 2017).
- **Jordan Davies**: PGY-2 in 2019-20, from the University of New Mexico (his UCI bio says he did his first year of residency at UNM and transferred to UCI). Added between the 2019-12 and 2020-05 versions and not on the 2018-19 roster. Class of 2025.

These three joined before 2011 and are outside the window: Reeves (transfer from UTMB), Owen (joined in 2008 above PGY-1), and Mathews (former postdoc).

## Consistency
Each person has a single entry year, with one exception. Daniela Alexandru is listed PGY-6, 7, 7 (2013-14 to 2015-16). She entered in 2008 (with Mathews) and graduated in 2016 after 8 years, so she had an extended final year. This is not an entry-year conflict. 25 residents entered in 2011 or later.

**Joseph Lockwood** (Tulane, program 66) was at UCI in 2023-24 as a skull-base **fellow**, not a resident. He is on no UCI resident roster.

## Alumni
The alumni list is on the live medschool page (Classes of 2013 to 2026). I inserted 18 graduation rows into `training_history` (source_type program_page).

## Adjudication (after phase 2)
18 completed, 11 in training, 1 left with outcome unknown (Mathews), and 1 left without completing (Beach).

## Phase 2 (2026-09-28)
- **2012-13 (reconstructed, now low).** No 2012-13 roster exists.
  - Searched: a Wayback CDX list of every URL on neurosurgery.uci.edu from 2012-06 to 2014-09; the news, gallery, about and index pages; the three Common Crawl crawls from phase 1; and PubMed affiliation mining for 2011-15 (56 PMIDs, no unknown resident).
  - Why low: every 2011-12 resident is back in 2013-14 or graduated (Reeves, 2013), so no known resident could have left unseen. The only possible miss is an extra 2012 entrant or transfer who left before October 2013, and the complement was 1 a year.
- **2011-12 PGYs (low).** The inferred PGYs are confirmed by a June 2011 news page, which calls Gill PGY-2.
- **Mathews.**
  - Still listed as PGY-7 on the August 2015 page (headed 2014-2015), and gone by September 2015.
  - The 2016 alumni list names the Classes of 2013, 2014 and 2016 but has **no Class of 2015**. His last paper with a UCI affiliation is from 2016, and no later neurosurgery papers appear.
  - NPPES (enumerated 2008-07) now lists him as Family Medicine/Sports Medicine in Palm Springs. This suggests he did not practise neurosurgery, but I did not use it as evidence.
  - Recorded as `completed='unknown'`. Completion is **not confirmed**, and non-completion is probable.
- **Beach.** Recorded as `completed='no'`, `departure_type='unknown'`. No destination was found on other study programs' rosters, in NPPES (only a 2023 student NPI) or in PubMed.
- **training_history rows added (5):**
  - Transfers in: Hanna (2017-2020), Oh (2017-2021), Davies (2019-2025, from UNM).
  - Departures: Beach (2023-2024) and Mathews (2008-2015, unknown).
- **For program 97:** Davies (UNM PGY-1 2018-19) is missing from the UNM file's reconstructed 2018-19 roster.
