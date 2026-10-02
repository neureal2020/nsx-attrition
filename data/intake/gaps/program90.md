# Program 90: University of Miami/Jackson Health System Program (Miami, FL)

7-year program. The complement was 3 per year for every observed class from 2008 to 2024, and 4 per year for the 2025 and 2026 classes. 50 residents entered in 2011 or later. The JSON twin is `program90.json`, and the parsers and captures are in `data/raw/extraction/p90/`.

## Hosts and paths
| Host / path | Dates | Content |
|---|---|---|
| jhsmiami.org/body.cfm?id=8942 (Jackson "Resident and Fellows Bios") | 2009-07 to 2010-12 | roster by PGY heading; no capture after 2010 |
| neurosurgery.med.miami.edu/about/residents-fellows | 2010-11 to 2020-02 | a link to the Jackson page only |
| neurosurgery.med.miami.edu/documents/*Training_Programs*.pdf | captured 2015-2017 | brochures with resident pages for 2010-11, 2014-15 and 2015-16 |
| neurosurgery.med.miami.edu/education/current-residents | 2015-11 to 2020-07 | roster (Name / PGY-n or Chief / Started / Graduate) |
| neurosurgery.med.miami.edu/alumni/resident-alumni | 2016-11 to 2020-02 | alumni list |
| jacksonhealth.org residency-neurologicalsurgery.asp and graduate/neurosurgery(.asp) | 2013 to 2019 | program info only |
| med.miami.edu/en/departments/neurosurgery/education/residency-program/current-residents | 2023-01 (one capture) | roster |
| med.miami.edu/departments/neurosurgery/education/residency-program/current-residents | 2024-08 to live | roster |
| med.miami.edu/departments/neurosurgery/education/alumni/meet-our-alumni | 2022-10 to live | resident alumni through 2023 |

## Years (after phase 2)
| Year | Status | Significance | Reason |
|---|---|---|---|
| 2011-12, 2012-13, 2013-14 | reconstructed | low | No roster exists anywhere. Every class from 2008 to 2013 has 3 members (the complement), seen on both sides of the gap. The NPI enumeration years of the 2011-13 entrants match their entry years, so they are original entrants and not later replacements. PubMed 2011-14 mining found no resident who was never listed. |
| 2014-15 to 2020-21 | observed | none | |
| 2021-22 | reconstructed | low | Every class seen in 2020-21 is complete in 2022-23 or on the 2022 alumni list. The 2021 interns (Elarjani, Khalafallah, Vyas) were added as PGY-1 from "Started in 07/2021" on the 2023-01 page. |
| 2022-23 | observed | none | The page omits PGY-7 Eichberg, so he was added as reconstructed. An April 18, 2023 news.med.miami.edu Spine Summit article cites "many of our 21 residents", which is the 20 listed plus Eichberg. |
| 2023-24 | reconstructed | low | Added: PGY-7s Burks, Jamshidi and Theodotou (2024 graduates, see below) and PGY-1s Govindarajan and Tigchelaar ("Started in 07/2023"). The only residual doubt is whether a third original 2023 intern left and O'Hehir filled that place. |
| 2024-25 to 2026-27 | observed | none | |

Phase 2 searches: gapaudit on all hosts, including graduate.jacksonhealth.org. CDX histories of every education page from 2021 to 2025, and the department home link audit. news.med.miami.edu Wayback prefix scan with 12 articles read. All failed Common Crawl crawls retried successfully with no roster content (2014-15, 2020-05, 2021-17, 2022-49, 2024-26, plus 2014-42 on jhsmiami). PubMed and Europe PMC mining. NPPES cohort checks. Other programs' pages (UW fellows, UPMC, AHN, Buffalo).

## Outcomes resolved in phase 2 (training_history rows added)
- **Aria Jamshidi** completed in 2024. He is listed as a University of Washington Neurological Surgery fellow ("Acting Instructor") in 2024-09 and 2025-03.
- **Christian Theodotou** completed in 2024 (inferred). The page said "Graduate in 06/2024", and NPPES lists him in neurosurgery at 265 E Rollins St, Orlando, certified 2024-07-01.
- **Joshua Burks** completed in 2024 (inferred). The page said "Graduate in 06/2024", and he is off the 2024-25 roster. NPPES shows neurosurgery with FL and CA licences, at Lake Worth, FL in 2025.
- **Katherine Berry** left before PGY-7, around mid-2024; outcome unknown. She was last on a roster as PGY-5 in 2022-23, but papers with a UM Neurological Surgery affiliation run through 2024-04, so she was probably still here in 2023-24. She is absent from 2024-25 onward and not on the alumni list. An NPPES name match (neurosurgery, Pittsburgh PA, updated 2024-06-13) is not evidence: she is not on the UPMC or AHN resident or fellow pages. Recorded as completed=no, departure_type=unknown, end_year 2024.
- **Mary Margaret O'Hehir** joined the 2023 class at PGY-2 in 07/2024, according to the page. Her Florida trainee NPI was issued 2023-04-05, in the same week as Miami's 2023 interns (2023-03-30 and 2023-04-03). She probably did a Florida PGY-1 in 2023-24; she is not on the Buffalo roster. Recorded as a joiner.

## Remaining
- There is no literal roster for 2011-14, 2021-22 or 2023-24. All three gaps are low significance.
- Whether a third 2023 intern left unseen. One unconfirmed lead: **Andres M. Corona** was a UM student with neurosurgery papers from 2021 to 2023 and got a Florida trainee NPI on 2023-03-20. Since 2025 he has had UM Department of Surgery affiliations. Nothing shows he was ever a neurosurgery resident.
- Berry's destination after she left.

## Other notes
- **Faiz Ahmad** was PGY-2 in 2010-11 but finished as a Chief Resident in the Class of 2014. The alumni page lists him under both 2014 and 2016. This is an accelerated completion, not a departure.
- **Jeremiah Johnson** was expected to graduate in 2013 and graduated in 2014, an extra year.
- **Lead: Javier Figueroa.** He is not on any Miami resident roster from 2010 to 2026. He is listed under current-fellows as a Trauma fellow at Jackson South in 2017-18, 2018-19 and 2019-20, and each page gives start and graduation dates. His 2017-2020 time at Miami/Jackson was therefore a neurotrauma fellowship, not a residency, which explains his absence from the resident alumni list.

## Alumni
The alumni page shows graduation years 2012 to 2023. I inserted 34 rows into `training_history`.

## Adjudication (after phase 2)
44 completed, 23 in training, and 1 who left without completing (Katherine Berry). These counts include the pre-2011 entrants from the 2010-11 anchor roster.

## Problems
All of the phase-1 Common Crawl failures were retried in phase 2 and succeeded, but none contained roster content. The news.med.miami.edu live search is behind a Cloudflare challenge, which I did not bypass; I used Wayback instead. OpenAlex returned 429, so I used PubMed and Europe PMC.
