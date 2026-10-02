# Program 93: University of Mississippi Medical Center (Jackson, MS): roster gaps (phase 2)

Program length 7. The handbooks (2009-10, 2011-12) and the 2017-19 residency overview say the **PGY7 year is either transitional training at UMMC, with the resident credentialed as "Instructor in Neurosurgery", or a subspecialty fellowship**. PGY7s therefore show up on the faculty page as Instructors, or not at all. That is why the 2017-18 and 2018-19 residents pages have no PGY VII heading. Complement is about 2 per year: intern classes alternated 2 and 1 until 2020 and have been 2 every year since 2021. There is no alumni page.

## Hosts
| Host / path | From | To |
|---|---|---|
| neurosurgery.umc.edu/residents.html (static; faculty_staff.html lists PGY7 Instructors) | 2001-12 | 2012-08 (roster frozen Aug 2010) |
| www.umc.edu/Education/Schools/Medicine/Clinical_Science/Neurosurgery/Academics(Neurosurgery)/Current_Residents.aspx + Faculty_and_Staff.aspx (Ektron) | 2013 | 2016-07 (Common Crawl only) |
| www.umc.edu/som/Departments and Offices/SOM Departments/Neurosurgery/Educational Programs/Residency-Program/Current-Neurosurgery-Residents.html | 2017-08 (CC) | 2026-05 |
| .../Residency-Program/Neurosurgery/Current-Neurosurgery-Residents.html | live | 2026-09-27 |

## Year status
| AY | Status | Significance | Reason |
|---|---|---|---|
| 2011-12 | reconstructed (+ partial observed) | low | PGY7 Instructors Gaspard and Marks observed on the faculty page. PGY2-6 bracketed, now including Rey-Dios and Orozco-Castillo (supported by UMMC-affiliated papers). Interns Perez and Tawfik first appear as PGY3 (NPIs issued July 2011). |
| 2012-13 | reconstructed | low | Everyone at PGY2-7 is bracketed. Rey-Dios was PGY7 and is an Assistant Professor by Mar 2014. The only intern, Hidalgo (NPI July 2012), is first seen as PGY2. The 2/1 intake pattern leaves no slot unexplained. |
| 2013-14 | observed | none | Ektron roster, plus the faculty page listing Orozco-Castillo as PGY7 Instructor (Mar-Apr 2014). |
| 2014-15, 2015-16 | observed | none | Complete. |
| 2016-17 | reconstructed | low | PGY2-5 are bracketed. PGY7s Burnsed and Luqman are on a UMMC paper received Dec 2016. Perez and Tawfik later complete. The only remaining risk is an unseen second intern in 2016, which was a 1-intern year. |
| 2017-18 | observed | none | PGY VII is left off by design. Perez and Tawfik are recorded as completing in 2018. |
| 2018-19 | observed | none | PGY VII is left off by design. Hidalgo's UMMC faculty bio gives residency 2018 and a pediatric neurosurgery fellowship in 2019. |
| 2019-20 to 2026-27 | observed | none | Smalley's 2020-22 omission is only a page omission: he is now UMMC faculty. A. Smith's removal in May 2022 was his graduation (faculty bio: residency 2022). |

## Phase 2 changes
- Roster file: added a 2011-12 "other" capture (faculty page: Gaspard and Marks as PGY7 Instructors) and a 2013-14 "other" capture (CC faculty page: Orozco-Castillo as PGY7 Instructor). Reconstructed Rey-Dios (2011-12 PGY6, 2012-13 PGY7) and Orozco-Castillo (2011-12 PGY5, 2012-13 PGY6). This brings the total to 36 residents in the program from 2011-12 on.
- `training_history`, 8 rows:
  - Wetsel: transferred, end 2022. He did research at Boston Medical Center in 2024-25, then joined UA Phoenix (program 71) as PGY4 in 2025-26.
  - A. Clark: completed='no', departure_type='unknown', end 2025.
  - Completions from employer bios: Hidalgo 2019 (UMMC faculty bio), Luqman 2017 (Wayne State faculty page, Jan 2018), A. Smith 2022 (UMMC faculty bio).
  - Completions inferred from affiliations: Burnsed 2017, Perez 2018 (Stanford pediatric neurosurgery), Tawfik 2018 (Swedish Neuroscience Institute, the PGY7 fellowship option).
- Adjudication: 22 completed, 12 in training, 1 transferred (Wetsel), 1 did not complete (A. Clark).

## Remaining
- No residents roster exists anywhere for 2011-12, 2012-13 or 2016-17. All three are low significance.
- The completion years for Burnsed, Perez and Tawfik are inferred; no stated graduation was found for them.
- Alec C. Clark's destination is unknown.
- Johnson appears as Instructor in Aug-Sep 2014, after his PGY VII listing in 2013-14. This is probably a short post-graduation appointment.

## Problems
All six phase-1 failed Common Crawl fetches were retried and succeeded. They added nothing new: the 2018-47 SOM roster matches the 2018-19 roster. The two Resident_Manual.pdf CC records are truncated and cannot be read. OpenAlex returned 429 and was not used.
