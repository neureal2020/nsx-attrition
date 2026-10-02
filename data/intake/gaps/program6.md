# Program 6: Baylor Scott & White Medical Center (Temple), Temple TX

7-year program. First class entered in 2014. Complement was 1 per year for the 2014-2023 entry classes and 2 per year from 2024.

## Hosts
| URL | From | To |
|---|---|---|
| healthcare-professionals.sw.org/graduate-medical-education/residencies/neurosurgery/{neurosurgery,residents} | 2015-09 | 2018-03, then 301 to bswhealth.med |
| www.bswhealth.med/education/Pages/gme/temple/neurosurgery-residency.aspx | 2018 (first capture 2019-07) | 2025-04, then 301. The roster was loaded by JS from phyndapi.bswapi.com/v2/Gme/GetGmePhysicians and was never archived. |
| www.bswhealth.com/medical-professionals/education/graduate-medical-education/temple/neurosurgery-residency/faculty-and-residents | 2025-04 | live (roster and Alumni section) |

## Years
- **Not applicable (2011-12 to 2013-14):** neurosurgery does not appear in the S&W GME index in captures from 2012 through 2014-09. Robinson (UNM 2014, NPI 2014-04) was the first resident.
- **Observed:** 2015-16 (2016-06 capture), 2016-17 (2016-09), 2017-18 (2017-08), 2024-25 (2025-04), 2025-26 (2025-10).
- **Reconstructed (manual):**
  - 2014-15: Robinson only.
  - 2018-19 to 2023-24: only the alumni-confirmed residents (Robinson, Dayawansa, Lyon, Liang, Soto, Reed).
- **Missing / significant gaps:**
  - **2018-19 to 2023-24:** no roster text exists in any archived version (19 bswhealth.med versions checked). There are no GetGme API captures for this program, no matching photo captures, and the department page and the scholarly-work PDF name no neurosurgery residents. Common Crawl (75 crawls, 2018-2025) returned 29 captures of the bswhealth.med page, all JS shells with no names. The 2018 version loaded its roster from providerapi.bswapi.com/v1/Gme, which has no Wayback captures, and CC has 0 GetGme API records. 6 index-range lookups failed. Details are in `data/raw/extraction/p6/cc/hits.json`. Keith, Nguyen, Daly, Gearhart and Gonzalez are first seen in 2024-25 at PGY6, 5, 4, 3 and 2. I did not reconstruct them because they are neither bracketed nor graduated.
  - **2026-27:** the live page (2026-09-27) is identical to the 2025-10 capture: Keith is still PGY-7, Birney and Khan are PGY-1, and the alumni list stops at 2025. Because it is stale, it was not loaded as 2026-27.

## Alumni (live page)
| Year | Graduates |
|---|---|
| 2021 | Robinson |
| 2022 | Dayawansa |
| 2023 | Liang, Lyon |
| 2024 | Soto |
| 2025 | Reed |

All six were inserted into `training_history`.

## Entry classes
| Entry year | Residents |
|---|---|
| 2014 | Robinson |
| 2015 | Dayawansa |
| 2016 | Lyon, plus Liang (joined at PGY2 in 2017) |
| 2017 | Soto |
| 2018 | Reed |
| 2019 | Keith |
| 2020 | Nguyen |
| 2021 | Daly |
| 2022 | Gearhart |
| 2023 | Gonzalez |
| 2024 | Bindal, Ciavarra |
| 2025 | Birney, Khan |

15 residents in total.

## Departures and joiners
- **Departures:** none visible. Every resident who entered before 2019 graduated on time according to the alumni list.
- **Joiner:** Buqing Liang joined in 2017-18 at PGY2. He is not on the 2016-17 roster and has a 2014 Fudan MD. This was either a transfer in or credit for a PGY1 done elsewhere.

## Adjudication
6 COMPLETED and 9 IN TRAINING.

## Problems
- The 2016-06 page lists Robinson under "PGY1" (his PGY was left null).
- Any resident who entered and left between 2018 and 2024 would not be visible.
- Continuity for the 2019-2023 entrants before 2024-25 rests only on entry-year arithmetic. Keith's NPI (2019-03) supports her 2019 start.


## Phase 2 (2026-09-28)

### Year status
| Year | Status | Significance | Reason |
|---|---|---|---|
| 2011-12 to 2013-14 | not_applicable | none | Program not running yet (first class 2014) |
| 2014-15 | reconstructed | low | Robinson was the only resident |
| 2015-16 to 2017-18 | observed | none | sw.org rosters (the Jan 2018 capture is identical to 2017-08) |
| 2018-19 | reconstructed | low | All 6 residents are alumni-confirmed. Reed fills the single 2018 slot. |
| 2019-20 to 2022-23 | reconstructed | low | Alumni-confirmed residents plus the 2019-2023 entrants, each shown at Temple from their entry year by NPI and PubMed (details below) |
| 2023-24 | **observed** (group photo, source_type other) | low | See below |
| 2024-25, 2025-26 | observed | none | |
| 2026-27 | missing | **significant** | The live page, fetched again 2026-09-28, is still the 2025-26 roster |

### What phase 2 found
- **2023-24 group photo.** `bswhealth.med/education/PublishingImages/temple/neurosurgery-residency/group.jpg` (captured 2024-03-30) shows 7 residents in coats with their names embroidered. Legible labels: Anthony Nguyen, Sam Daly, Laura Reed, Samuel Gearhart. Partly legible: Gonzalez, Keith. One figure has no readable label (Soto). Only 2023-24 fits this group. It is loaded as 2023-24, with PGYs inferred from entry year.
- **Continuity for the 2019-2023 entrants.** Each is at Temple from their entry year:

| Resident | NPPES | PubMed at Temple neurosurgery |
|---|---|---|
| Keith | enumerated 2019-03 | from 2019 (PMID 31861595) |
| Nguyen | enumerated 2020-03, at the neurosurgery mail stop MS-01-610A | from 2020 (PMID 33425519) |
| Daly | — | from 2021 (PMIDs 34729264, 34786547) |
| Gearhart | enumerated 2022-04, Temple | from 2023 (PMID 36874307) |
| Gonzalez | enumerated 2023-04, Temple | from 2023 (PMID 37509641) |

  All five are reconstructed into 2019-20 to 2022-23.
- **No other residents found.** PubMed returned 329 PMIDs for 2014-2026. The only other Temple-neurosurgery authors are faculty or research staff, or medical students. Sulhan was a TAMU student, then a Houston Methodist resident. Ajala, Bhenderu, Hernandez and Danka were students.
- **Keith graduated in 2026.** NPPES (updated 2026-08) shows Neurological Surgery in Waco TX. A training_history row was added.
- **Liang joined at PGY2.** His PGY1 was general surgery at Harlem Hospital (Columbia, PubMed 2016), followed by a Weill Cornell research affiliation. He is not a transfer from another neurosurgery program. A training_history row was added (start 2017).
- **Crossmatch rejected.** Huy Tram Nguyen (UChicago) and Anthony Nguyen (Temple) are different people.
- **API hosts, dead end.** Wayback CDX for providerapi.bswapi.com returned 23 URLs, none of them /Gme. phyndapi.bswapi.com returned 1281 URLs, with 31 GetGmePhysicians captures, all for other programs. Neither host has a neurosurgery roster.

### Remaining
- **2026-27:** the 2026 intern class and any departures after 2025-26 cannot be seen. Nguyen, Gearhart and Gonzalez appear on Temple papers indexed July to September 2026. Asad Danka (NPI 2026-03, Temple) might be a 2026 intern; this is unconfirmed.
- **Common Crawl:** see `cc_status` in the JSON.

### Common Crawl (phase 2)
- **Phase-1 failures retried, all succeeded.** Five crawls of phyndapi GetGmePhysicians Neurosurgery (2018-26, 2019-30, 2022-33, 2024-26, 2025-43) had 0 records. CC-MAIN-2020-50 had one capture of the bswhealth.med page (2020-11-28), a JS shell with no names.
- **providerapi v1/gme:** 0 records in 2018-05 and 2018-09.
- **Not finished:** providerapi v1/gme for the later 2018-2019 crawls and phyndapi v1/gme for 2019-2024. data.commoncrawl.org kept returning intermittent 403s, and the scan was killed. The pairs are listed in `cc_status.unfinished` in the JSON. They are expected to add nothing, because Wayback shows no /Gme URLs on either host.
