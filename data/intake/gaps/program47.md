# Program 47: National Capital Consortium Program (Bethesda, MD)

> **Phase 2 update (2026-09-28):** the Phase 1 text below is kept as it was. The rosters file now holds 15 partial `other` snapshots with 3 confirmed residents, and training_history has 1 graduation row. See the Phase 2 section at the end.

This is the military neurosurgery residency, sponsored by the NCC at Walter Reed National Military Medical Center (WRNMMC) and USU. The Army program (WRAMC, founded 1954) and the Navy program (NNMC Bethesda, founded 1975) merged into the NCC in 1998. The program moved to WRNMMC Bethesda in 2011. It is a 7-year program; the pages call the levels R1-R7. None of the pages give a complement per year.

**Result: 0 observed years, 0 reconstructed years, 16 missing years (2011-12 through 2026-27).** The program has never published a resident roster or a graduates list on any of its own web hosts. `data/intake/rosters_program47.json` is `[]`. It was loaded with `--replace`, so the DB holds 0 observations. No rows were added to `training_history`.

## Hosts / paths (all checked in every Wayback content version)
| URL | Dates | Roster? |
|---|---|---|
| www.wramc.amedd.army.mil/Patients/healthcare/surgery/neuro/Pages/ (default, directory, residency.aspx, 2003 brochure PDF) | 2009-01 only | no (phone directory and service info) |
| www.bethesda.med.navy.mil/patient/health_care/neuro_musculoskeletal_services/neurosurgery/ | 2004-2006 | no |
| www.usuhs.edu/surgery/, usuhs.mil/surgery/ (USU Dept of Surgery, old site) | 2005-2015 | no neurosurgery residency content |
| www.wrnmmc.capmed.mil/Health Services/Surgery/Surgery/Neurosurgery/SitePages/Home.aspx | 2012-06 to 2019-08 | no (in 2012 an empty IFRAME web part; later only a program blurb). The Shared Documents and Announcements lists are empty. |
| www.wrnmmc.capmed.mil/ResearchEducation/GME/SitePages/Neurological Surgery/Residency.aspx | 2015-03 to 2019-03 | no. Lists only the PD (Rosner, then Neal), the APD (Neal, then Dirks) and coordinator Rachel Martin. |
| www.wrnmmc.capmed.mil GME Welcome Class page (2013) and walterreed.tricare.mil Welcome-Class (2021) | 2013, 2021 | no names |
| www.usuhs.edu/sur/neurosurgery | 2017-04 to 2021-04 | no (service description) |
| walterreed.tricare.mil/About-Us/Graduate-Medical-Education/...NCC-Neurosurgery-Residency-Program, /Neurosurgery-Residency-Program, /Overview..., /History-of-the-Neurosurgery-Training-Program | 2021-01 to 2023-12 | no. The history page is narrative only and names the PDs. |
| walterreed.tricare.mil/Academics/Graduate-Medical-Education/.../NCC-Neurosurgery-Residency-Program (+ History...Program42) | 2024-01 to 2024-06, 301 afterwards | no |
| walterreed.tricare.mil/Health-Services/Hospital-Care-Surgery/Neurosurgery (+ 2026 staff sub-pages) | 2021-01 to 2026-06 | no. Lists 5 staff surgeons in 2026: Cirivello, Puffer, Graves, Miller, Meister. |
| wrnmmc.capitalregion.health.mil, walterreed.health.mil | none | no Wayback captures; DNS does not resolve |

How the hosts were found:
- `gapaudit.py` covered 2009-2026 on all of the hosts above.
- Domain-wide CDX searches filtered on `neuro.?surg` covered wrnmmc.capmed.mil, walterreed.tricare.mil, wramc, bethesda.med.navy.mil and usuhs.edu/.mil.
- The usuhs.edu sitemap has no neurosurgery or GME pages.
- The live site (walterreed.tricare.mil) returns **HTTP 403** to both curl and WebFetch, including sitemap.xml. It was not bypassed.

## Years
- **Observed:** none.
- **Reconstructed:** none. No person was ever observed, so there is nothing to bracket, and there is no alumni list.
- **Missing:** 2011-12 through 2026-27, all of them significant gaps.
  - 2011-12 to 2014-15: the WRNMMC department page has no names, and the GME program page appears only from 2015. Common Crawl 2012 to 2014-49 has only the department Home.aspx.
  - 2015-16 to 2019-20: the GME page and the department page carry no roster in any version.
  - 2020-21 to 2025-26: none of the walterreed.tricare.mil GME, history or clinical pages lists residents.
  - 2026-27: the live site returns 403. The latest archive (2026-06) shows only staff.

## Consistency / attrition
Nothing can be assessed from program pages. There are no departures or joiners, and residents_2011plus = 0.

## Problems / for phase 2
- **Common Crawl was only partly run.** The prefixes were the walterreed.tricare.mil GME, Academics and neurosurg paths plus the wrnmmc GME Neurological and department Neurosurgery paths. The run finished only CC-MAIN-2012 through CC-MAIN-2014-49, and one lookup failed: CC-MAIN-2014-10 walterreed neurosurg (range error). I killed the run after about 20 minutes because it was very slow, so CC-MAIN-2015-06 through 2026 were not checked. The same URLs in Wayback carry no roster, so retrying is low-yield.
- This roster has to be built from non-program sources: military and USU news releases, NPPES, PubMed affiliations ("Walter Reed National Military Medical Center, Department of Neurosurgery"), and social media or match announcements. Graduate counts must also come from outside sources.

---

# Phase 2 (2026-09-28): rebuilt from non-program sources

**Result:** the program never published a roster, so all 16 years stay **missing / significant**. Three residents are now confirmed by a source that says they were residents. They are loaded as partial `source_type: "other"` snapshots in 15 years (19 rows). The PGY in each row is **inferred** from the start year the source gives, in a 7-year program. No year has a full class list, and the class size is unknown.

## Confirmed residents (loaded)
| Name | Stated by | Rows loaded | Outcome |
|---|---|---|---|
| Corey Mossop | ORCID 0009-0002-9585-2558: "Residency, WRNMMC Neurological Surgery 2009-2016" (then Chief of Neurosurgery, Tripler 2016-19; ABNS 2020) | 2011-12..2015-16, PGY3-7 | **Graduated 2016**. training_history th_id 2526, completed=yes, source_type=cv |
| Jason H. Boulter | ORCID 0000-0001-6397-8530: "Resident, WRNMMC Neurosurgery 2017-" (MD Emory 2017). WR neurosurgery affiliation on papers 2018-2026 | 2017-18..2023-24, PGY1-7 | End year is not stated. The adjudicator's "COMPLETED" rests only on the inferred PGY-7, so no training_history row was added |
| Callum D. Dewar | ORCID 0009-0001-1313-9816: "Resident, WRNMMC Neurosurgery 2020-". NPPES 1225665953 (trainee taxonomy, 8901 Rockville Pike, NPI 2020-03). Papers 2020-2026 | 2020-21..2026-27, PGY1-7 | In training |

**Confirmed trainee, not loaded:** Melissa R. Meister. NPPES 1174900815 (NPI 2015-05) lists both Neurological Surgery and "Student in an Organized Health Care Education/Training Program" at 8901 Rockville Pike. She is now staff (Maj.). No source gives her training years, and her ORCID calls her "Neurosurgeon" from 2018, which conflicts with the NPI date. Her entry year therefore can't be set.

## Probable but unconfirmed (NOT loaded; need a stating source in phase 3)
The evidence for these is WR Dept of Neurosurgery affiliations in consecutive years, a junior rank, NPPES trainee taxonomy, or a later posting as a neurosurgeon at another military hospital (MTF). None of these sources says they were NCC residents.
- Michael J. Cirivello: listed as "Lt." in a 2012 contributors list; WR 2011-2026; now PD.
- Frederick L. Stephens: WR 2008-12; later Madigan.
- Meryl A. Severson: WR 2009-16.
- Jay J. Choi: 2011 "National Capital Neurosurgery Consortium"; later Tripler.
- George N. Rymarczuk: WR 2015-20; later Landstuhl.
- Daniel J. Coughlin: WR 2016-19; later Madigan.
- Nicholas S. Szuflita: WR 2016-24; later JBLM.
- Joseph Spinelli: WR 2016-19.
- John J. Delaney: WR 2018-20; NPPES trainee + neurosurgery at Portsmouth.
- Brian P. Curry: WR 2018-26; NPI 2014.
- Abraham Sabersky: WR 2018-19.
- Samuel A. Woodle: WR 2023-26.
- Hana Yokoi: MD 2021; WR 2022-25.
- John V. Dang: NPPES trainee at WRNMMC, NPI 2018.
- Elias Geist: NPPES trainee at WRNMMC, NPI 2024; WR neurosurgery 2026.
- William Coburn.

## Excluded (WR neurosurgery authors who were not NCC residents)
- **Trained elsewhere, then WR staff:** Miller (Mayo), Puffer (Mayo), Hooten (UF), Dengler (UTSA, program 108), Graves (Temple resident per PMC7067615), Ikeda (Ohio State), Tomlin, Dirks, Bell, Neal, Armonda, Rosner, Schuette, Faillace, Gilhooly, Mulligan, P. Cooper.
- **USU students who became residents elsewhere:** Larkin (Baylor), R. M. Meyer (UW).
- **Georgetown residents or collaborators:** Felbaum, Mai, McCullough, A. Carroll, Dowlati, D. Dang.
- **Other specialties:** A. R. Kumar (plastic surgery), Larochelle (ophthalmology), S. Wallace (occupational medicine), Tigno (research scientist).

## What was searched
All sources are listed in `data/raw/extraction/p47/phase2/evidence.json`.
- **PubMed:** 765 PMIDs.
- **OpenAlex:** 764 works and author affiliation histories.
- **PMC full text:** 1068 articles. No affiliation or footnote labels anyone a WR neurosurgery resident. Other WR programs (OMFS, psychiatry, anesthesia) do label their residents.
- **Europe PMC:** full-text searches.
- **ORCID:** all 873 records with Walter Reed, NCC or NNMC affiliations were scanned.
- **NPPES.**
- **DVIDS:** site search, plus all 61 issues of the WRNMMC newspaper "The Journal" (2017-18).
- **news.usuhs.edu.**
- **walterreed.tricare.mil (Wayback):** NCC graduation stories 2023-2025 name no neurosurgery graduates. The 2026 staff bios are Q&A and give no training institution.
- **Other military hospital (MTF) neurosurgery pages.**
- **Navy GMESB PDFs:** these are selection goals only, with no names.
- **Common Crawl:** 2015-2026 retry.

## What could not be established
- **Class sizes, entrants and graduates:** could not be established for any year. The program complement is not published, and no graduates list, match list or GME selection list with names was found on an allowed source.
- **Attrition:** can't be assessed. No departures or joiners can be identified.
- **Program length:** 7 years (R1-R7), recorded as `terminal_pgy_by_entry_year` = 7 for every cohort.

## Common Crawl retry
Phase-2 Common Crawl retry (walterreed.tricare.mil about-us/academics GME + hospital-care-surgery/neurosurg, wrnmmc GME neurological prefixes): CC-MAIN-2015-06..CC-MAIN-2016-50 checked, 0 records (none of these prefixes were in those crawls); failed lookups CC-MAIN-2015-06 (walterreed about-us GME, wrnmmc GME), CC-MAIN-2015-40 (walterreed about-us GME), CC-MAIN-2016-30 (walterreed academics GME); run killed after ~35 min, CC-MAIN-2017-04..2026 not reached. Low yield: Wayback has every version of these pages and none carries a roster.
