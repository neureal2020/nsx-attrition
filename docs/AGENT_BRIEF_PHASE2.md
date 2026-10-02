# Phase 2 brief: close one program's roster gaps

You are closing the gaps for ONE program whose phase-1 roster already exists.
Working dir: `/Users/neureal/Documents/Residency Application Study`.
Read first: `data/intake/gaps/program<ID>.md` and `.json` (the phase-1 result), `data/intake/rosters_program<ID>.json`, the lines about this program in `data/intake/PHASE2_NOTES.md` (grep for the program id and for its residents' surnames), and `docs/AGENT_BRIEF_PHASE1.md` (the rules still apply).

## Goal
Make every remaining gap "not significant": for each reconstructed, missing or incomplete year, either find a real roster, or show from independent evidence that no resident could have entered or left unseen.

## Hard rules (unchanged from phase 1)
- **No WebSearch.** No other search engines, and no browser. Allowed: the program's own sites, Wayback via `scripts/wayback.py`, Common Crawl via `scripts/tools/cclocal.py`, NPPES, PubMed/Europe PMC/OpenAlex APIs, and pages on other programs' sites.
- Never send the user's email address, name or any other personal identifier to an outside service (e.g. OpenAlex/Crossref `mailto=`, NCBI `email=`, or User-Agent contact fields). Leave those parameters out entirely; if an API rate-limits you, back off and wait.
- Never kill processes by name pattern (`pkill -f ...`, `killall`): other agents run the same scripts on this machine. Kill only PIDs you started yourself (record them with `$!`).
- Never bypass CAPTCHAs or bot checks. Stay polite with Wayback and Common Crawl (several agents share one IP): back off on 403/429.
- **Write only these paths:** `data/raw/extraction/p<ID>/phase2/`, `data/intake/rosters_program<ID>.json`, and `data/intake/gaps/program<ID>.md` / `.json`. You may also insert rows into `training_history` for this program. Do not edit shared scripts, docs or other programs' files.
- Reload after any roster change: `21_load_curated_roster.py --replace`, then `16_adjudicate_program.py`, then `22_export_sources.py`.

## Before anything else
List `data/raw/extraction/p<ID>/` (including any `cc*/` subfolders). Phase-1 agents sometimes downloaded Common Crawl or Wayback captures they never parsed. Parse every roster-like file dated inside a gap year first (Temple's 2013-14 roster was found this way). Also re-read the raw text of every OBSERVED year marked incomplete (e.g. missing a PGY group): the phase-1 parser sometimes missed entries written inline as "Name, M.D. PGY-1" (Henry Ford Providence 2023-24 interns).

## Checklist for every gap year
1. **Full host audit:** `python3 scripts/tools/gapaudit.py p<ID> <FROM> <TO> <host> <host> ...` over every host in the gap file, and over the parent department / GME / surgery-department hosts. Pass hosts as separate arguments. Look for moved rosters, PDFs, handbooks, brochures, "meet our residents", news and match-day pages, redirects, and per-resident profile pages.
2. **Link audit:** fetch the archived parent pages (department home, education, GME index) captured inside the gap and follow every link (`scripts/tools/linkaudit.py` pattern).
3. **Common Crawl across ALL crawls** in the gap window, with the fixed filter (`cclocal.py` now matches `residenc|meet|people|our-team|faculty-and-residents`). Retry every crawl listed as failed in the gap file. Rerun programs whose phase-1 pass used the old filter (programs 1-18) over their gap years.
4. **Per-resident pages:** archived bio or profile URLs for residents on either side of the gap often print their PGY or class year.
5. **Program news:** match-day, graduation, awards and "welcome" posts on the program's own site (archived) name interns and graduates.
6. **PubMed / OpenAlex affiliation mining** for the gap years: `scripts/tools/pubmed_aff.py`, with an affiliation query such as "<Dept> of Neurosurgery, <University>" AND the year. It surfaces residents never listed. Keep only people confirmed as residents (paper footnotes, later rosters, or bios).
7. **Cross-program evidence:** `data/intake/crossmatch.json` lists probable transfers in and out of this program. Confirm each against both programs' rosters and record it (step 9).

Background scans: do not end your turn just to wait for them. Wait inside one Bash call (e.g. `timeout 1200 tail --pid=<pid> -f /dev/null`). If a scan is still running after about 20 minutes, kill that PID and list the unfinished crawls under `problems`.

## After the searches
8. Update the rosters file: replace reconstructed rows with observed ones where found. Add newly found residents. Keep `reconstructed: true` only where still needed.
9. **Record outcomes in `training_history`** (one row per event, with `source_url`):
   - Transfer out: `completed='no'`, `departure_type='transferred'`, `end_year` = the year they left. Put the destination program in `notes`.
   - Transfer in: add a row at the destination with `start_year` and the PGY they joined at (in `notes`).
   - Graduation seen only on a roster (no alumni row): `completed='yes'`, `end_year`, `source_type='program_page'`, note "PGY-terminal roster".
   - Use your judgement on a specialty switch only when a program page or a publication affiliation shows it. NPPES name matches alone are NOT evidence: the adjudicator's NPI "switch" calls were wrong many times in phase 1.
10. **Program length by cohort:** if the program changed length (6 -> 7 years) or was AOA before ACGME, record it in the gap JSON as `"terminal_pgy_by_entry_year": {"<year>": 6, ...}`, so PGY-6 finishers are not counted as departures.
11. Rewrite the gap files. For every year, record status `observed | reconstructed | missing | not_applicable`, and a `significance` field (`none | low | significant`) with a one-line reason. Add `"phase2": {"searched": [...], "found": [...], "remaining": [...]}`.

## Final reply (short, under 200 words)
Which gaps were closed and how, what remains significant and why, outcomes recorded (counts), and problems.
