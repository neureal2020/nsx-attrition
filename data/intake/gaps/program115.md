# Program 115: University of Wisconsin Hospitals and Clinics Program (Madison, WI)

7-year program. Usual complement is 2 per year, with 3 in the classes of 2010, 2014, 2018, 2024 and 2026. Roster file: `data/intake/rosters_program115.json` (16 captures, 230 observations). Scratch work is in `data/raw/extraction/p115/`: `build.py` builds the roster file, and `dumps/` holds the text of every capture.

## Hosts
| host / path | from | to |
|---|---|---|
| http://www.neurosurg.wisc.edu/current_residents.asp (+ former_residents.asp). Old ASP site; names and PGY appear only in the rollover menus of a photo image map | 2001 | roster last captured 2011-12-25; site 302s to the new host from 2013-05 |
| http://www.neurosurgery.wisc.edu/people/residents/alpha (Drupal) | 2013-05 | 2018-10 |
| http://www.neurosurgery.wisc.edu/people/residents/year, /picture, /former (Drupal) | 2015-09 | 2019-10 |
| https://www.neurosurgery.wisc.edu/people/ (WordPress; Residents and Fellows section with PGY-n headings) and /staff-type/resident/ | 2019-10 | live |
| https://www.neurosurgery.wisc.edu/alumni/alumni-list/ (graduates by year) | 2019-11 | live |
| uwhealth.org/neurosurgery/ (clinical pages only, no roster) | 2008 | 2013 |

## Years
- **Observed (15):** 2011-12, 2012-13, and 2014-15 through 2026-27. The 2011-12, 2012-13 and 2014-15 captures carry no PGY labels, so PGY comes from each person's entry year. 2011-12 was parsed from the page's JS menus. The 2012-13 and 2014-15 captures are alphabetical lists, so their PGYs are inferred.
- **Reconstructed (1): 2013-14.** No roster capture exists:
  - Wayback has no capture of any people/residents page between 2013-05-14 and 2014-10-19. A domain-wide CDX search found only the home, research, specialties and education pages.
  - Common Crawl 2013-20 through 2014-52 has only faculty/dempsey.

  13 people were reconstructed:
  - 11 are bracketed by the 2012-13 and 2014-15 rosters.
  - Lake and Nickele are confirmed by the alumni list (graduated 2014).
  - Haldeman is confirmed by the alumni list (graduated 2020, entry 2013).
- **Missing:** none.
- **Stale pages:** the Drupal "by year" view lagged about a year behind. Its Aug 2016 to Jan 2017 captures show 2015-16, and its Aug 2017 capture shows 2016-17. For 2016-17 and 2017-18 the June captures, which are content-dated, were used instead. The WordPress capture from 2025-07-23 still showed 2024-25.

**Significant gap:** 2013-14. The class of 2013 has only one person, Haldeman. A second 2013 intern who left during 2013-14 would not be visible.

## Departures (left before PGY-7)
- **Sung Ha:** class of 2010. Last seen 2015-16 as PGY-6, and on the alpha list until 2016-07-08. Not on the alumni list, while classmates Baggott and Sandoval-Garcia graduated in 2017. **Switched to anesthesiology/pain (phase 2):** Sung P. Ha, Department of Anesthesiology, UW SMPH, 2020 (PMID 32022852). It is the same person: his UW profile gives an Indiana MD, and Sung P. Ha published from Indiana University SOM in 2007-2010 (PMID 21084750). training_history row 3169.
- **Zhikui "Zeke" Wei:** class of 2016. Last seen 2017-18 as PGY-2, and on the alpha list until 2018-06-12. Not on the alumni list; classmate Page graduated alone in 2023. **Switched to neurology (phase 2):** Department of Neurology, Vanderbilt, 2020-22 (PMID 32055253, 35892989), then Neurology / Jefferson Sleep Disorders Center, 2024-26 (PMID 38656805). His UW profile gives a Johns Hopkins MD, which matches his Hopkins neurosurgery papers from 2015-16. training_history row 3170.

## Joiners (above PGY-1)
None in 2011-27.

Before the window: Jane Ng was PGY-3 in 2011-12 (class of 2009). Ng is absent from the Aug 2009 roster, whose PGY-1s were Ryan Holdsworth and Brenton Meier; both were gone by 2011-12. Ng probably joined above PGY-1 in 2010-11. Ng is not counted as a joiner because 2010-11 is unobserved. Phase 2 findings: Ng was a lateral entrant, with a UCL MD and neurosurgery work at Queen Square, London in 2005 (PMID 16276564). The June 2010 capture of the old ASP page still carries Aug-2009 content, so she joined either in 2010-11 as PGY-2 or in July 2011 as PGY-3. This is unresolved, with low significance. Holdsworth later appears in UW Radiology (PMID 23544414).

## Alumni
29 graduations from 2012 to 2026 were inserted into `training_history`, taken from the live alumni list. Every graduation year matches entry year + 7.

## Adjudication
47 residents in total:
- 29 completed
- 16 in training
- 2 left and switched specialty (Ha: anesthesiology; Wei: neurology)

35 residents entered in 2011 or later.

## Notes
- **Fellows listed inside PGY groups:** Dawkins, Parmar, Corriveau, Burkett, Bowman and Meisner appear there with fellow titles. These are in-folded fellowships of residents seen since PGY-1, so they are kept. People listed only as fellows are excluded.
- **Chief-only listings:** Haldeman (2019-20) and Bodden and Dawkins (2020-21) appear only under Chief, and are counted as PGY-7. Bowman appears only as Chief in 2023-24 and is counted as PGY-6 from entry year.
- **Certificate:** the TLS certificate of www.neurosurgery.wisc.edu fails verification, so live fetches needed `curl -k`.

## Phase 2 (2026-09-28)
**Result:** 2013-14 is still reconstructed and still **significant**. A second 2013 intern who left during 2013-14 cannot be ruled out. Only Haldeman is in the 2013 class, and the 2014 class took 3, which means a slot was free. The program took 3 again in 2010 and 2018, each after an attrition, so the free slot could be a departure or an unfilled match position.

Every other year is observed, with significance none.

**Searched:**
- Wayback full-host CDX for 2013-06 to 2014-10 (226 URLs). Fetched every page that is not an asset: home, rss, education, education/description, people, and the news nodes. None of them is a roster or match/welcome news.
- The Drupal "former" list (2015-09). It holds graduates only.
- Resident profiles for Haldeman, Ha, Wei, Ng and Tarula (Tarula is a fellow).
- Common Crawl, full-domain prefixes for both hosts, across all 10 crawls in 2013-14. The only hits were faculty/dempsey, and no crawl failed.
- PubMed affiliation mining for 2013-16, which found no unknown UW resident.
- The SMPH Match Day news for 2013 and 2014.
- crossmatch.json, which has no entries for program 115.

**Outcomes recorded:** 2 switched_specialty rows (Ha, Wei). Adjudication now shows 29 completed, 16 in training and 2 who switched specialty.

**terminal_pgy_by_entry_year:** 7 for every cohort.

Scratch files are in `data/raw/extraction/p115/phase2/`.
