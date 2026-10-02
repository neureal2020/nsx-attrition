# Program universe, AY 2011-12 to 2024-25 (with 2026 Match for context)

Built 2026-09-29. Files in this folder:
- `national_totals.json`: ACGME Data Resource Book numbers per academic year: programs, residents on duty, residents by PGY 1-7.
- `program_years.json`: 1,746 rows of NRMP positions offered and filled by program code, match years 2011-2026, mapped to `our_program_id`.
- `program_events.json`: 90 events. Documented events have news or program-page URLs. Rows whose detail starts with "DERIVED" were inferred from NRMP first/last appearance, gaps or quota step changes.

## Sources
| Source | Coverage | Status |
|---|---|---|
| ACGME Data Resource Book, one per AY (acgme.org/about/publications-and-resources/graduate-medical-education-data-resource-book/) | 2011-12 to 2024-25 | Read 12 of 14 books directly. The 2015-16 and 2023-24 books are over 10 MB and could not be fetched. Their program and resident totals come from the 5-year trend tables in the 2016-17 and 2024-25 books. Their PGY breakdown is missing. |
| NRMP *Results and Data 2011* (program listing) | Match 2011 | Read: 98 programs, 195 offered, 192 filled. This matches the 2012 R&D trend table. |
| NRMP *Program Results* 2012-2016, 2016-2020, 2021-2025, 2022-2026 | Matches 2012-2026 | Read. The overlapping years (2016 and 2022-2025) agree exactly. Totals match the R&D specialty tables (for example 2012: 196/194). |
| ACGME ADS public reports: Report/7 (withdrawn) and Report/8 (new) | n/a | **Not obtained.** The reports are POST-generated PDFs, and the Chrome PDF viewer did not render them for text extraction. The one thumbnail that could be read (withdrawn programs, AY 2020-21) showed 0 programs. |
| News and program pages | Closures, reaccreditations | See `program_events.json`. |

**Correction to the brief:** neurosurgery joined the NRMP Main Match in **2009**, not 2012. The 2012 NRMP R&D says "Neurological Surgery joined The Match in 2009". The 2011 entering cohort is therefore covered by NRMP data, and no SF Match data is needed.

## Programs and positions per year
| Match yr / AY | ACGME programs | ACGME residents on duty | ACGME PGY-1 on duty | NRMP programs | NRMP offered | NRMP filled | Our roster entrants (entry_year est.) |
|---|---|---|---|---|---|---|---|
| 2011 / 2011-12 | 101 | 1179 | 199 | 98 | 195 | 192 | 223 |
| 2012 / 2012-13 | 102 | 1212 | 202 | 98 | 196 | 194 | 218 |
| 2013 / 2013-14 | 105 | 1265 | 207 | 99 | 204 | 203 | 228 |
| 2014 / 2014-15 | 105 | 1295 | 206 | 102 | 206 | 206 | 248 |
| 2015 / 2015-16 | 108 | 1325 | n/a | 102 | 210 | 208 | 240 |
| 2016 / 2016-17 | 110 | 1375 | 220 | 105 | 216 | 214 | 243 |
| 2017 / 2017-18 | 112 | 1408 | 220 | 107 | 218 | 218 | 243 |
| 2018 / 2018-19 | 115 | 1462 | 230 | 110 | 225 | 225 | 250 |
| 2019 / 2019-20 | 118 | 1515 | 231 | 112 | 232 | 231 | 246 |
| 2020 / 2020-21 | 116 | 1561 | 233 | 112 | 232 | 232 | 248 |
| 2021 / 2021-22 | 118 | 1579 | 236 | 115 | 234 | 234 | 244 |
| 2022 / 2022-23 | 117 | 1593 | 242 | 115 | 240 | 240 | 259 |
| 2023 / 2023-24 | 118 | 1607 | n/a | 115 | 243 | 240 | 253 |
| 2024 / 2024-25 | 119 | 1611 | 244 | 115 | 241 | 241 | 265 |
| 2025 / 2025-26 |  |  | n/a | 118 | 266 | 263 | 279 |
| 2026 / 2026-27 |  |  | n/a | 121 | 280 | 280 |  |
- ACGME PGY-1 on duty runs 0-8 above NRMP filled each year. The gap is expected: it covers the National Capital Consortium (military match), off-match or outside-Match hires, and PGY-1s repeating a year.
- **Our roster has more entrants than NRMP filled in every year** (+5% to +20%; 3,687 vs 3,341 over 2011-2025). The largest per-program excesses are Riverside (+26), Cooper (+19), Henry Ford Providence (+18), UTHSC San Antonio (+17), Carilion (+10) and UF (+10). Likely causes:
  - former-AOA or pre-NRMP residents (Riverside, Providence and Cooper existed before their first NRMP match)
  - transfers-in
  - `entry_year` being an estimate
  - possible non-categorical or research-track people on rosters

  These should be reviewed. The overall surplus does not suggest missing residents.
- There are 47 program-years (54 residents) where our roster is **below** NRMP filled. In 18 of them the roster has 0 entrants (list below). Some are probably off-by-one `entry_year` estimates. Others may be real roster holes.

## Programs in sources but missing from our list
- **Philadelphia College of Osteopathic Medicine (PCOM) neurosurgery** (NRMP 2158160C0). Former AOA program, ACGME-accredited under the single accreditation system. It matched 1/1 in 2020, 2021 and 2022, and is absent from NRMP 2023-26, from the current PCOM program list and from the 2026-27 ACGME list. Its closure date was not found. **About 3 NRMP entrants (2020-22) plus earlier AOA-era residents are outside our universe.**
- No other NRMP neurosurgery code in 2011-2026 is unmapped. Wayne State/DMC (NRMP 1295160C0, 2011-2019) is already in our list as id 125.
- The ACGME count for 2011-12 is 101 programs. NRMP 2011 lists 98; the difference is NCC plus UC Davis and Mayo Jacksonville, which were not in the 2011 Match. This is consistent with our list, so no other missing program is indicated for the early years.

## Programs in our list with no evidence of existing in some years
First NRMP match year, used as a proxy for opening. ACGME accreditation may be earlier.
- 2012: UC Davis, Mayo Jacksonville (these recruited outside the 2011 Match)
- 2013: NIH, UI Peoria
- 2014: Carolinas, Geisinger, SIU, Louisville (Louisville had no NRMP positions in 2012-13)
- 2016: Baylor S&W Temple
- 2017: BIDMC, Inova
- 2018: Carilion, Corewell GR/MSU, Corewell/Beaumont (founded 2018 per its program page), Henry Ford Providence
- 2019: UMass
- 2020: Mayo Phoenix, Riverside, Stony Brook, UConn
- 2022: UT Austin Dell
- 2023: Cooper
- 2025: Arizona COM-Phoenix, Ascension St Vincent
- **2026 (outside cohort):** Cleveland Clinic Florida, MaineHealth, UMKC
- **Never in NRMP:** National Capital Consortium (military match; no by-program source) and Hackensack Meridian (no evidence of any residents yet)
- **Gaps and closures:**
  - UNM lost accreditation on 30 Jun 2020 and a new program was accredited on 1 Apr 2022, so there were no NRMP positions in 2020-22.
  - UPR's accreditation was withdrawn on 30 Jun 2022. The **current ACGME ID 1604200001 is a new program**, which matched 1 in 2026. No UPR entrants are possible for 2022-2025.
  - Wayne State/DMC closed on 30 Jun 2020, with its last match in 2019.
  - The MGB/BWH NRMP code had 0 positions in 2026 while MGH offered 6, which points to combined recruitment.
  - Single-year skips (no NRMP positions): Cedars 2015, UC Davis 2015, NIH 2014, Arizona-Tucson 2013, SLU 2014/2020/2023, Missouri-Columbia 2018/2020, UTMB 2020, Houston Methodist 2024.

## Years with no by-program source
- None among match years 2011-2026 for NRMP participants.
- Gaps:
  - NCC in all years
  - residents who entered outside the Match
  - approved complement (ACGME total positions per program), which is not public in these sources; NRMP quota is the proxy
  - ACGME PGY breakdown for AY 2015-16 and 2023-24

## Roster below NRMP filled (program-years)
- Albany Med Health System Program (1) 2016: roster 1 vs NRMP filled 2
- Barrow Neurological Institute at St Joseph's Hospital and Medical Center Program (4) 2012: roster 3 vs NRMP filled 4
- Emory University School of Medicine Program (20) 2013: roster 2 vs NRMP filled 3
- Geisinger Health System Program (21) 2014: roster 0 vs NRMP filled 1
- Houston Methodist Hospital (Medical Center) Program (26) 2017: roster 2 vs NRMP filled 3
- Houston Methodist Hospital (Medical Center) Program (26) 2023: roster 2 vs NRMP filled 3
- Inova Fairfax Hospital Campus Program (29) 2023: roster 0 vs NRMP filled 1
- Inova Fairfax Hospital Campus Program (29) 2025: roster 0 vs NRMP filled 2
- Johns Hopkins University Program (30) 2014: roster 2 vs NRMP filled 3
- Johns Hopkins University Program (30) 2018: roster 3 vs NRMP filled 4
- Johns Hopkins University Program (30) 2023: roster 3 vs NRMP filled 4
- Loma Linda University Health Education Consortium Program (31) 2021: roster 0 vs NRMP filled 1
- Loyola University Medical Center Program (34) 2016: roster 1 vs NRMP filled 2
- Mayo Clinic College of Medicine and Science (Jacksonville) Program (38) 2018: roster 0 vs NRMP filled 1
- Mayo Clinic College of Medicine and Science (Phoenix) Program (39) 2020: roster 1 vs NRMP filled 2
- Mayo Clinic College of Medicine and Science (Rochester) Program (40) 2025: roster 3 vs NRMP filled 4
- McGaw Medical Center of Northwestern University Program (41) 2014: roster 3 vs NRMP filled 4
- Medical College of Georgia Program (42) 2011: roster 0 vs NRMP filled 1
- Medical College of Wisconsin Affiliated Hospitals Program (43) 2013: roster 1 vs NRMP filled 2
- MedStar Health Georgetown University Program (45) 2012: roster 0 vs NRMP filled 2
- NYU Grossman School of Medicine Program (50) 2012: roster 1 vs NRMP filled 2
- Riverside University Health System Program (55) 2024: roster 0 vs NRMP filled 1
- Riverside University Health System Program (55) 2025: roster 0 vs NRMP filled 1
- SUNY Upstate Medical University Program (63) 2011: roster 1 vs NRMP filled 2
- SUNY Upstate Medical University Program (63) 2025: roster 0 vs NRMP filled 2
- Tulane University/Ochsner Clinic Foundation Program (66) 2025: roster 1 vs NRMP filled 2
- UMass Chan Medical School Program (68) 2025: roster 0 vs NRMP filled 1
- University at Buffalo Program (69) 2017: roster 2 vs NRMP filled 3
- University of Arizona College of Medicine- Tucson Program (72) 2015: roster 1 vs NRMP filled 2
- University of Arkansas for Medical Sciences (UAMS) College of Medicine Program (73) 2015: roster 1 vs NRMP filled 2
- University of California (San Francisco) Program (76) 2012: roster 0 vs NRMP filled 3
- University of California Davis Health Program (77) 2021: roster 2 vs NRMP filled 3
- University of Chicago Program (78) 2018: roster 1 vs NRMP filled 2
- University of Minnesota Program (92) 2017: roster 1 vs NRMP filled 2
- University of New Mexico School of Medicine Program (97) 2017: roster 1 vs NRMP filled 2
- University of New Mexico School of Medicine Program (97) 2018: roster 0 vs NRMP filled 1
- University of New Mexico School of Medicine Program (97) 2019: roster 0 vs NRMP filled 1
- University of New Mexico School of Medicine Program (97) 2023: roster 0 vs NRMP filled 1
- University of Oklahoma Health Sciences Center Program (99) 2016: roster 1 vs NRMP filled 2
- University of Puerto Rico School of Medicine Program (101) 2011: roster 0 vs NRMP filled 1
- University of Puerto Rico School of Medicine Program (101) 2016: roster 1 vs NRMP filled 2
- University of Puerto Rico School of Medicine Program (101) 2019: roster 1 vs NRMP filled 2
- University of Puerto Rico School of Medicine Program (101) 2021: roster 0 vs NRMP filled 2
- University of Utah Health Program (111) 2023: roster 2 vs NRMP filled 3
- University of Wisconsin Hospitals and Clinics Program (115) 2013: roster 1 vs NRMP filled 2
- West Virginia University Program (121) 2025: roster 1 vs NRMP filled 2
- Westchester Medical Center Program (122) 2024: roster 0 vs NRMP filled 2