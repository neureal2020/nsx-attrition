# Program 101: University of Puerto Rico School of Medicine Program (San Juan, PR). Phase 2

**Summary.** The UPR neurosurgery section never published a resident roster between 2010 and June 2026. The ACGME withdrew the old program's accreditation effective **2022-06-30**, with 14 citations (UPR GME "Status de Acreditación 2021" PDF: `data/raw/extraction/p101/gme_799_acred2021.pdf`). A new program received Initial Accreditation effective **2025-07-01**, with 1 position per year.

Phase 2 rebuilt the old program's residents for 2011-12 to 2021-22 without any program-side roster. The sources were:
- PubMed and Europe PMC affiliations and footnotes;
- NPPES enumeration dates;
- other programs' pages: transfer destinations' rosters and bios, and fellowship alumni lists.

Every one of those years is `reconstructed` (source_type `manual`, rows flagged `reconstructed: true`, evidence in `context`).

- Program length: 7 (PGY-1 to PGY-7) for every cohort entering 2009 or later (`terminal_pgy_by_entry_year`). The section's own pre-2010 roster used NS-1 to NS-5 labels, which were stale from about 2006-07.
- Years: observed 2026-27. Reconstructed 2011-12 to 2021-22, and 2025-26. `not_applicable` 2022-23 to 2024-25 (no accredited program). Missing: none.
- 17 residents in 2011 or later: 15 from the old program and 2 from the new one.

## Old-program residents (reconstructed)
| resident | UPR years (inferred) | outcome | key evidence | confidence |
|---|---|---|---|---|
| Rodolfo E. Alcedo-Guardia | ?2009-2016 | completed 2016 | Brigham fellows list: fellowship 2016-18, residency UPR | high (entry assumed) |
| Samuel Estronza-Ojeda | 2010-2017 | completed ~2017 | NPI 08/2010 PR; UPR co-author 2011-19; now PD | low (probable resident) |
| Juan C. Vicenty-Padilla | 2012-2019 | completed 2019 | Brigham fellows list: fellowship 2019-21, residency UPR | high |
| José A. Fernández-Abinader | 2012-2019 | completed ~2019 | PubMed footnotes "Neurosurgery Resident PGY 5" (2017) and "PGY 6" (2019) | medium ±1 |
| Joel E. Pellot Cestero | 2013-2020 | completed ~2020 | NPI 06/2013 PR; UPR affiliation 2020-22; CWRU 2023; now faculty | low (2015-2022 possible) |
| Christian I. Ríos-Vicil | 2014-2021 | completed 2021 | LVHN profile: "Residency 2021 Neurosurgery, Puerto Rico Medical Center" | high |
| Miguel A. Mayol Del Valle | 2014-2021 | completed 2021 | Emory neuro-oncology fellowship alumni "2022" (year = fellowship end) | medium ±1 |
| Gabriel Flores-Milán | 2015-2020 | **transferred 2020** to USF (PGY-5 2020-21) | PubMed UPR 2017, 2020; USF roster | strong |
| César M. Carballo Cuello | 2015-2021 | **transferred 2021** to USF (PGY-5) | USF bio: "Previous Residency: University of Puerto Rico, Neurosurgery" | high |
| Andrés E. Monserrate Marrero | 2016-2021 | **transferred 2021** to Arizona Tucson (PGY-5) | PubMed UPR 2020-21 (upr.edu email) | strong |
| Ricardo J. Fernández-de Thomas | 2017-2021 | **transferred 2021** to UPMC/Pitt (PGY-4) | Doximity UPR 2017-2021 | high |
| Alejandro J. Matos Cruz | 2017-2021 | **transferred 2021** to Allegheny (PGY-5) | papers list UPR Neurosurgery and AGH | strong |
| José I. Sandoval Consuegra | 2018-2021 | **transferred 2021** to Allegheny (PGY-4) | NPI 06/2018 PR; PubMed UPR 2021, 2023 | strong |
| José G. Sánchez Jiménez | 2019-2021 | **transferred 2021** to MCW (PGY-3) | PubMed UPR 2019-2022 | strong |
| Santos E. Santos Fontánez | 2020-2021 | **transferred 2021** to Brown (PGY-2) | Brown profile: "Residency: University of Puerto Rico" | high |

Entry years come from NPI enumeration dates. That rule reproduces the fellowship-dated graduation of Vicenty, Ríos-Vicil and Mayol, and Fernández-de Thomas's Doximity dates. Where the NPI contradicts the destination level (Matos Cruz: NPI 2014 PA; Sánchez Jiménez: NPI 2017 WI), the entry year assumes he transferred at the same level. Most transferees restarted one level lower at the destination.

**Closure outcome.** Everyone known to be in training when the program lost accreditation had gone by July 2021, a year before the withdrawal date:
- 7 transferred in June/July 2021. Treat these as closure-driven transfers, separate from voluntary attrition.
- Flores-Milán had already left for USF in 2020.
- The last known graduates (Ríos-Vicil, Mayol) finished in June 2021.

No old-program resident is known in 2021-22.

`training_history`: 15 rows for program 101 (8 `transferred`, 7 `completed='yes'`), each with a `source_url`. The destination programs' transfer-in rows were not written, because this agent may write only program 101 rows. Those programs' own files already record the joiners (USF 103, AGH 2, MCW 43, Brown 54, Arizona 72, Pitt 116).

## Year by year
| year | status | significance | reason |
|---|---|---|---|
| 2011-12 | reconstructed | significant | Only Alcedo and Estronza are known. The 2006-08 and 2011 classes are unidentified. Lincoln Jiménez (PGY-3 in a 2008 footnote) may still have been there. |
| 2012-13 | reconstructed | significant | 4 known. The 2007, 2008 and 2011 classes are unidentified. |
| 2013-14 | reconstructed | significant | 5 known. The 2008 and 2011 classes are unidentified. |
| 2014-15 | reconstructed | significant | 7 known. The 2011 class is unidentified. |
| 2015-16 | reconstructed | significant | 9 known. The 2011 class is unidentified. |
| 2016-17 | reconstructed | significant | 9 known. The 2011 class is unidentified. |
| 2017-18 | reconstructed | low | Every class from 2012 to 2017 is represented. Entry years are ±1. |
| 2018-19 | reconstructed | low | Every class from 2012 to 2018 is represented. |
| 2019-20 | reconstructed | low | Every class from 2013 to 2019 is represented. |
| 2020-21 | reconstructed | low | 2 graduates plus 7 closure transfers, each confirmed on the destination roster. |
| 2021-22 | reconstructed (empty) | low | No resident known. All in-training residents left by July 2021. Risks: Pellot may have finished in 2022; a 2021 intern is unlikely. |
| 2022-23 to 2024-25 | not_applicable | none | No accredited program. |
| 2025-26 | reconstructed | low | First class of the new program. Vázquez-Medina must have been the PGY-1. |
| 2026-27 | observed | none | Live page: Rivera Rivera (PGY-1), Vázquez-Medina (PGY-2). |

## Candidates not loaded
- **Lincoln M. Jiménez**: "PGY-3" in a Dec 2008 footnote. He probably finished in 2011 or 2012.
- **Hermes G. García**: NPI 2009 FL. A 2016 paper lists Jefferson and UPR Neurological Surgery. His role is unresolved.
- **Eva Pamias-Portalatín**: UPR affiliation in 2014 and 2019, with research at Hopkins and Mayo in between. Her role is unresolved.
- **Saavedra-Pozo, Báez, Cardona, Feliciano, Almodóvar**: on the stale ~2006-07 roster; presumed graduated before 2011-12.
- **Not ACGME residents or not residents**:
  - International trainees and fellows: Corona-Ruiz, Effio, Rondón-Granados.
  - Students and researchers: Amaral Nieves (UPR MD, then Brown PGY-1), Mignucci-Jiménez, Ruiz Rodríguez, Rosado-Philippi, Rodríguez-Beato, K. Ortiz, Carro-Figueroa, Pagán-Rodríguez, Aixa de Jesús Espinosa, and others.

## Phase 2 searches
- PubMed affiliation mining 2009-2024: 317 PMIDs, 295 author-affiliation hits. Resident, PGY and residente footnote search. Per-person affiliation histories for 45 names, with received dates.
- Europe PMC affiliation mining 2010-2023: 258 records. It was down (503) earlier and rerun. It added only Corona-Ruiz.
- OpenAlex author affiliations for 18 candidates.
- NPPES: all 46 PR neurosurgery NPIs, plus every candidate nationally.
- Other programs' pages (Wayback):
  - USF, AGH, MCW, Brown and Arizona rosters and bios;
  - Brigham cerebrovascular fellows list;
  - Emory neurosurgical-oncology fellowship;
  - LVHN profile;
  - Case Western fellows page (no Pellot).
- UPR hosts:
  - live WP REST pages (program-faculty, history, research);
  - archived faculty pages (Vigo, Carro);
  - GME directory (2007-2026, program director only);
  - md.rcm.upr.edu blog;
  - `/surgery/neurosurgery/images/facres/`: faculty photos only;
  - all 6 distinct versions of the 2006-2009 `sectionres.php`: one stale list, unchanged.
- Common Crawl (cclocal): 2015-2018 rescanned (81 crawl/prefix pairs, no roster hits). The earlier failures (2015-11, 2016-30, 2017-39 /neurosurgery, 2018-47) now succeeded. New failures: 2015-06, 2015-22, 2016-44 and 2017-39 (/surgery/neurosurgery). The 2020-2022 scan (66 pairs ok) found no rosters. The only GME hit is again the 2022-12 landing page of "Resident Housestaff 2021", without the file. Failed: 2020-05, 2020-24, 2021-10 (gme), 2021-21 and 2021-49.

## Problems
- There is no primary roster, so every old-program year depends on inference. Entry years are ±1.
- `16_adjudicate` shows Matos Cruz as "TRANSFERRED (University of Louisville)". That comes from an ambiguous-name match outside this program's data. The actual destination is Allegheny.
