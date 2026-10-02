# Program 98: University of North Carolina Hospitals Program (Chapel Hill, NC)

**Length by entry cohort:** 7 years for entrants 2005-2008, 6 years for entrants 2009-2012 (the RRC restructure of January 2010), and 7 years from the 2013 entrants on. There were no graduates in 2019. Recorded in the JSON as `terminal_pgy_by_entry_year`.
**Complement:** 1 per year for entrants 2004-2009, and 2 per year from 2010.

## Hosts
| URL | From | To |
|---|---|---|
| med.unc.edu/neurosurgery/education/composite11 (Plone "Current Residents") | 2011 | 2013-05. Only in Common Crawl: CC-MAIN-2012 (2012-05-26) and CC-MAIN-2013-20 (2013-05-23). Wayback has only a 301. |
| med.unc.edu/surgery/education/files/ (Dept of Surgery housestaff PDFs listing Neurosurgery by year) | 2010-11 | 2011-12 |
| med.unc.edu/neurosurgery/education/current-residents (Plone) + prior-graduates2 | 2013-07 | 2018-01 |
| med.unc.edu/neurosurgery/education/residency/2872-2/ (WordPress) + residency/prior-graduates2/ | 2018 | live 2026-09-27 |
| med.unc.edu/neurosurgery/news (match 2011, 2012, 2016, 2018, 2019, 2024; Geryk elective 2012) | 2011 | 2024 |

## Year status (all significance none unless noted)
- **2011-12: OBSERVED (phase 2).** From composite11 (CC 2012-05-26). The content is 2011-12: the interns are Aucoin and Olasunkanmi. The Surgery housestaff PDFs for 2010-11 (05/18/11) and 2011-12 (09/22/11) agree name for name.
- **2012-13: OBSERVED (phase 2).** From composite11, titled "Current Residents 2012-2013" (CC 2013-05-23). It lists everyone from 2011-12 except the graduate Perry, plus the 2012 interns Omofoye and Yap.
- **2013-14 to 2026-27:** observed and complete, as in phase 1.
  - 2016-17 is significance **low**: the only capture is from February 2017, but the neighbouring years match.
  - 2018-19 comes from Common Crawl CC-MAIN-2019-26.
- No reconstructed or missing years remain.

## Corrections in phase 2
- **Bruce Geryk** (2008 entrant) was missing from phase 1.
  - He was PGY3 in 2010-11, PGY4 in 2011-12 and PGY5 in 2012-13. A program news item dated 2012-07-19 describes an "elective rotation during his PGY-5 year".
  - He is absent from the 2013-14 roster and from the alumni list.
- The pre-2009 entrants did 7 years. Two consequences:
  - Orning in 2013-14 is PGY7, not PGY6.
  - 2011-12 Perry and 2012-13 Steenland are PGY7 ("Chief Resident").
- Parsing trap on composite11: the PGY heading comes BEFORE the names.

## Departures
- **Bruce Geryk:** last seen 2012-13 at PGY5. Outcome unknown (`departure_type` unknown). NPPES shows a neurology NPI, which is not used as evidence.
- **Oluwaseun Omofoye:** last seen 2016-17 at PGY5, then transferred.
  - 2017-18: affiliated with the Department of Neurosurgery at Boston Medical Center (PMID 29294115, received Jun 2017, accepted Nov 2017). His role is not stated, and that program is not in the DB.
  - Then UC Davis (program 77) at PGY6 in 2018-19, graduating in 2020.
- **Sam (Satvir) Saggi:** last seen 2025-26 at PGY1. Transferred to UVA (program 113) at PGY2 in 2026-27. His UVA bio lists "Neurosurgery Resident Intern, UNC Medical Center - 2025".

## Joiners
- **Momodou Gobi Bah:** PGY2 in 2026-27, after a preliminary general surgery year at Penn State Health. He fills Saggi's slot and is not a neurosurgery transfer.

## training_history (phase 2: 6 rows)
- Geryk (98): left, outcome unknown.
- Omofoye: out-row at 98 (transferred) and in-row at 77 (PGY6 2018).
- Saggi: out-row at 98 (transferred) and in-row at 113 (PGY2 2026).
- Bah (98): joined at PGY2 in 2026.
- The 23 alumni graduation rows from phase 1 are kept.

## Adjudication
40 persons: 23 COMPLETED, 14 IN TRAINING, 1 LEFT (did not complete: Geryk), 2 TRANSFERRED (Omofoye, Saggi). 33 of them entered in 2011 or later.

## Problems
- SurgRes.xls (2011) is password-protected, so it was not opened.
- Common Crawl CC-MAIN-2018-22 failed in phase 1. Not critical: AY 2017-18 is already observed.
