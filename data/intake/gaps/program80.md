# Program 80: University of Colorado (Aurora, CO)

- 7-year program with 2 positions a year (3 in the 2023, 2024 and 2026 classes; the 2021 class was 2, per the Spring 2021 newsletter). The residency-program page says "two appointments each year".
- Roster file: `data/intake/rosters_program80.json`. Scratch files: `data/raw/extraction/p80/` (parser `p80parse3.py`, builder `build.py`).

## Hosts
| URL | From | To | Note |
|---|---|---|---|
| www.ucdenver.edu/.../Neurosurgery/education/ResidencyProgram/Pages/CurrentResidents.aspx | 2011-11 | 2019-10 | SharePoint. The 2011-13 layout is "Name / PGY roman". The 2014-15+ layout has "Chiefs / PGY - n" headings before the names. The 2013-14 version only linked an unarchived PDF. The page was frozen at 2018-19 content from Aug 2018 to Oct 2019. |
| www.ucdenver.edu/.../Neurosurgery/education/Pages/Alumni.aspx | 2013-07 | 2019-10 | graduation-year table |
| medschool.cuanschutz.edu/neurosurgery/education-and-training/alumni | 2019-12 | 2020-07 | |
| medschool.cuanschutz.edu/neurosurgery/education-and-training/residency-program/meet-our-current-residents | 2020-10 | live | Its year heading lags one year behind the content. |
| medschool.cuanschutz.edu/neurosurgery/education-and-training/our-alumni | 2020-10 | live | Lists graduates only up to the class of 2022. |

## Years (after phase 2)
| AY | Status | Significance | Reason |
|---|---|---|---|
| 2011-12, 2012-13, 2014-15 .. 2018-19, 2020-21, 2022-23 .. 2026-27 | observed | none | full roster captures (2012-13 via Common Crawl; 2022-23 plus a Mar 2023 mid-year capture; 2026-27 live) |
| 2013-14 | reconstructed | low | Roster PDF never archived (all CC crawls incl. retried 2014-41 read). Every 2012-13 resident below PGY7 is on the 2014-15 roster or the alumni list except Boylan, a confirmed transfer to Wayne State. 2013 intern class = Folzenlogen + Kunigelis = complement. Only Boylan's exit date is open. |
| 2019-20 | reconstructed | low | No roster capture (ucdenver frozen, then 302 by Dec 2019). 14 reconstructed, including 2019 interns L. Freeman and Razmara (PGY II 2020-21). McKay was still at UNM, so his absence is correct. Headcount closes. |
| 2021-22 | reconstructed | low | Page stale through Dec 2021. 14 reconstructed, including 2021 interns Alvarez and Harris, who are named as the only "New Interns" in the Spring 2021 department newsletter. Headcount closes. |

Phase-2 evidence for the reconstructed years:
- **Spring 2021 department newsletter** (`medschool.cuanschutz.edu/docs/librariesprovider62/newsletters/internal-final-headlines_newsletter_spring21-.pdf`). It lists "New Interns" Reinier Alvarez (FIU) and William Harris (U Hawaii), names Whelan and Hosein as the graduating chiefs, and names McKay Resident of the Quarter (Apr 2021). The 2021 class was 2, not 3: Helal was a separate 2022-23 PGY2 joiner.
- **Retried Common Crawl crawls.** CC-MAIN-2014-41, 2019-09 and 2019-51 all read OK. None had a roster. In 2019-51 the ucdenver CurrentResidents page 302-redirects.
- **Gap audits.** These covered the ucdenver Neurosurgery, SOM education, surgery and GME hosts, cuanschutz neurosurgery and GME, and news.cuanschutz.edu. I also listed the ucdenver Documents/ folders and the cuanschutz docs library. No other roster turned up. The ucdenver per-resident pages (2015-2019) are only bios.
- **PubMed affiliation mining** ("neurosurgery AND Colorado") for 2013-15, 2019-20 and 2021-23 found no unknown residents.

## Departures (left before the terminal PGY), recorded in training_history
| Name | Last AY | Last PGY | Outcome |
|---|---|---|---|
| Arianne Boylan | 2012-13 | 4 | **Transferred** to Wayne State/DMC (program 125): Year 5 in 2014-15, alumni 2017. She left CU between 2013-06 and 2014-06. |
| Avra Laarakker | 2017-18 | 1 | **Switched specialty** to plastic surgery at UNM. PubMed shows Division of Plastic, Reconstructive and Burn Surgery, UNM, 2019-2024. |
| Andrew Donovan | 2022-23 | 3 | Unknown. He left mid-year (on the Aug 2022 roster, gone by Mar 2023). |
| Michael Kortz | 2023-24 | 2 | Unknown. Absent from Sep 2024 on; his last CU PubMed affiliation is 2024-10. |

## Joiners (transfer in), recorded in training_history
| Name | First AY | First PGY | Origin |
|---|---|---|---|
| Pal Randhawa | 2015-16 | 4 | University of Oklahoma (program 99; PGY5 there in 2013-14). Graduated 2019. |
| William McKay | 2020-21 | 4 | University of New Mexico (program 97). This was a forced transfer: ACGME withdrew UNM's accreditation effective 2020-06-30. Graduated 2024 (PGY-terminal roster). |
| Ahmed Helal | 2022-23 | 2 | Joined mid-year. His prior training was in Alexandria (Egypt) plus Mayo Clinic research/fellowship; I found no US residency. He probably filled Donovan's vacancy. PGY VI in 2026-27. |

Also added PGY-terminal graduation rows, because the alumni page stops at the class of 2022: Sethi and Ung (2023), Chatain (2024), Hoffman and Wittenberg (2025), L. Freeman and Razmara (2026).

## Other notes
- Alexander Yang was PGY3 in both 2014-15 and 2015-16. He entered in 2012 and graduated in 2020.
- Canonical names:
  - "Leslier" Robinson is recorded as Leslie Robinson.
  - "Dusty"/"Marlin"/"M. Dustin" Richardson is recorded as Dustin Richardson.
  - Sam Waller is recorded as Samuel Waller.
  - Hoffmann is recorded as Hoffman.
  - Grégoire is recorded as Gregoire.
  - The listing "Michael | Kortz, DO" is recorded as Michael Kortz.
- I inserted 22 alumni graduation rows (2012-2022) into `training_history`.
- Residents entering 2011 or later (by PGY-derived entry year): 38.
- Adjudication after phase 2: 30 COMPLETED, 16 IN TRAINING, 1 transferred (Boylan), 1 switched specialty (Laarakker), 2 did not complete with outcome unknown (Donovan, Kortz).

## Problems
- None blocking. The previously failed Common Crawl crawls (2014-41, 2019-09, 2019-51) all read successfully in phase 2.
- The 2013-14 roster PDF cannot be recovered.
- Remaining low-significance points:
  - Boylan's exact exit date.
  - Where Donovan and Kortz went.
