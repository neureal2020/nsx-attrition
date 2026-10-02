# Program 70 - University of Alabama Hospital (Birmingham) Program (UAB Neurosurgery)

7-year program, complement 3/yr (4 in the 2013 class, 2 in the 2016 class).
The alumni page lists graduates by year, 2004-2025.

## Hosts
| Host / path | Dates | Note |
|---|---|---|
| main.uab.edu/Sites/neurosurgery/ (education/40944 = Current Residents, 40950 = Alumni) | 2009-07 to 2013-05 | Division of Neurosurgery. Roster not updated after 2011-12 |
| uabneurosurgery.com (current-uab-residents/, alumni/) | 2013-05 to 2016 | Department WordPress site |
| www.uab.edu/medicine/neurosurgery/education/current-residents | 2014-10 to 2017-11 | Joomla. Stale 2016-17 list until Nov 2017 |
| www.uab.edu/medicine/neurosurgery/education/residency/current-residents | 2018-02 (CC) to live | Wayback captures start only in 2019-11 |
| .../education/alumni, then .../residency/graduates, then .../residency/alumni | 2014 to live | Alumni by graduation year |

I checked uabmedicine.org: it has no roster pages.

## Years
- **Observed (15):** 2011-12 (stale Sept-2012 capture, content-dated), 2013-14 through 2016-17 (Wayback), 2017-18 and 2018-19 (Common Crawl 2018-02-19 and 2018-10-22), 2019-20 through 2025-26 (Wayback), 2026-27 (live, advanced).
- **Reconstructed:** 2012-13. No updated roster exists anywhere. The Wayback captures of 2012-09 and the Common Crawl copy of 2013-05 both repeat the 2011-12 list. I added 16 people:
  - 13 bracketed by the 2011-12 and 2013-14 rosters.
  - 3 who graduated in 2013 by the alumni page: Fusco, Whisenhunt and Mortazavi.
  - 3 who entered in 2012: Amburgy, McClugage and Dupepe. They are PGY-2 in 2013-14 and on the alumni list.
- **Missing:** none.

## Gap significance (phase 2)
- **2012-13: reconstructed, significance LOW.** No roster was ever published. Phase 2 re-checked every Sept-2012 education subpage, ran a Wayback host audit for 2012-05 to 2013-10 (main.uab.edu neurosurgery/surgery/gme and uabneurosurgery.com), and mined PubMed 2012-14 for UAB neurosurgery affiliations. Nothing new turned up. Every 2011-12 resident not graduating in 2012-13 reappears in 2013-14. The 2012 class of 3 (the full complement) was seen at PGY-2 and all of them graduated. The only case that could be invisible is a fourth 2012 intern who left within the year.
- **2016 class of 2: resolved, significance NONE.** A Common Crawl copy of the roster dated 2016-07-24 (CC-MAIN-2016-30, three weeks into the year) already shows the new 2016-17 list with exactly 2 PGY-1s, Salehani and Tabibian. The copies from June 2016 and 2016-07-01 still show 2015-16. The 2016-17 total is 21, which equals the 7x3 complement, because the 2013 class had 4. The third 2016 slot was used by that class, so it was not an unseen early leaver.

## Departures (left before the terminal PGY)
- **Logan Powell:** PGY-1 in 2025-26 and absent in 2026-27; the PGY-2 class has only Butler and Patrick. He left after PGY-1 and his destination is unknown. The adjudicator's NPI "switched specialty" call is not evidence. I recorded a training_history row with completed='no' and departure_type='unknown'.

## Joiners above PGY-1
None. Amburgy, McClugage and Dupepe were first seen at PGY-2 in 2013-14, but that follows the 2012-13 gap, so they are not transfers in.

## Consistency notes
- **E.B. Kuhn and Elizabeth Alford are the same person** (married name). I canonicalised her to "Elizabeth Alford".
- **John Amburgy** is listed at PGY-7 on four rosters, 2018-19 through 2021-22. The alumni page gives his graduation as 2021. He is still listed on the Dec-2021 roster, so this was probably an off-cycle finish in late 2021 after extra time. He is counted as completed.
- **Pre-2013 PGY labels are irregular:**
  - Gordon: PGY-3 in 2010-11, PGY-4 in 2011-12, chief in 2013-14, graduated 2014. I set her 2013-14 PGY to 6.
  - 2011-12 chiefs: I set Fleming to PGY-7 and Naftel to PGY-6, from the May-2011 page.
- **Resident count:** 48 residents entered in 2011 or later.

## Adjudication
- 39 COMPLETED
- 20 IN TRAINING
- 1 LEFT, did not complete (Powell; destination unknown)

I inserted 36 alumni graduation rows (2012-2025) into training_history.
