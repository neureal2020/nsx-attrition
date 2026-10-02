# Programs interrupted by the safety-classifier outage (2026-09-28): relaunch with these notes

## Program 62 (Stony Brook)
Nothing loaded. Scratch files in data/raw/extraction/p62/ (list.py, show.py, gapaudit1.txt, neuro_all.txt, ren_sitemap.xml, live_residency_program_current-residents.html).
- 1 resident per year; PD Egnor.
- Live 2026-27 roster: Servider PGY7, Razzaq PGY6, Kleyner PGY4, Ahmed PGY3, Lian and Thompson PGY2, Talbot PGY1. No PGY5, and two PGY2s. Check this against the 2025-26 roster (stale page?).
- Hosts:
  - neuro.stonybrookmedicine.edu/Residency-Fellowship.html (2013-02..2014-09)
  - neuro.stonybrookmedicine.edu/residency-fellowship (2015-02..2025-01)
  - neuro.../education (2019-24)
  - medicine.stonybrookmedicine.edu/neurosurgery + /education-training (2015-17; captures 2016-09-25, 2017-06-15)
  - renaissance.../neurosurgery/education-training (2019-09..2026-06)
  - renaissance.../neurosurgery/residency_program (2020-08..2026-05)
  - renaissance.../residency_program/current-residents (captures 2023-09-24, 2024-03, 2024-07, 2024-08, 2024-11-03, 2025-04 x3, 2026-01-14, 2026-06-07)
- Pre-2023 pages are not opened yet. Start year unknown.

## Program 59 (SIU)
Nothing loaded. Scratch files in data/raw/extraction/p59/ (live_*.html, cdx_prefix.txt, cdx_candidates.txt, cdx_rf.py).
- Initial ACGME accreditation 2013-06-29; first resident July 2014 -> first_class_year 2014. 7-year program, 1 resident per year.
- Roster = school-wide search page www.siumed.edu/resident-fellow?field_resident_program_tid=481 (old) or ?f[0]=resident_program:481 (current), labelled "Class of <grad year>". Also older /surgery/neurosurgery/residents.html (2014-12..2017-04), and /surgery/neuro/ pages (resident-fellow, residency.html, pgy-2..7.html, neurosurgery-residency).
- Found so far:
  - 2014-15: Alex Michael PGY1
  - 2015-16: Michael 2, Breck Jones 1
  - 2016-17: Michael 3, Jones 2, Victoria Watson 1
  - 2018-19: Michael 5, Jones 4, Watson 3, Adam Lipson 2, Nathan Nordmann 1
  - 2019-20: those five + Matthew Weber 1
  - 2026-27 live: Justin Michael 7, Kayla Chin 6, Ava Hoeft 5, Joseph Bernard 4, Michael Garovich 3, Sonia Pulido 2, Chibueze Ezeudu 1
- Next: run data/raw/extraction/p59/cdx_rf.py (prefix CDX of /resident-fellow, filter for 481); parse the 2020-25 captures; Common Crawl; alumni; build/load/adjudicate; gap report. 2017-18 can be reconstructed.
