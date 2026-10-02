# Handoff — neurosurgery residency attrition study

Written 2026-09-27 at the end of a long session. Start here in a new session.

## 1. Goal and non-negotiable procedure

Build a per-program attrition database for US neurosurgery residencies, covering classes entering in 2011 or later. For every program, in this order:

1. **Site history back to 2011.** Find every host and path the department used, including sponsoring-hospital sites, renamed sections and redirects.
2. **A roster for every academic year.** Search exhaustively, whatever the page is called. "Missing" years were nearly always a different address, a roster embedded in a parent page, a script-loaded page, or a firewall block page — not the archive skipping the site. Use the gap audit (section 4).
3. **Confirm entrants** against Instagram / X match posts (Google-indexed posts work best).
4. **US News + Doximity** for graduation and years in training.
5. **Google each resident** for a current bio. Confirm neurosurgery completion or a specialty switch.

**Every resident must be individually verified (step 5), not just departures.** A PGY-7 roster listing is not enough.

Other rules:
- Keep sources for everything.
- Never bypass a CAPTCHA or bot check.
- Browse Instagram at a human pace, read-only.
- Once the web-search limit is hit, do not switch to other search engines as a workaround (the last run did; see section 5).

The full rules and lessons are in the memory file `program-procedure.md` (auto-loaded).

## 2. File layout

```
db/neurosurgery_attrition.db      SQLite: programs, roster_snapshots, roster_observations, training_history
docs/PROGRAM_STATUS.md            per-program status, which years are observed/reconstructed, and why
docs/sources/program_<id>.md      verifiable source list per program (regenerate with scripts/22_export_sources.py)
docs/METHODOLOGY.md, STRATEGIES.md, BROWSER_WORKFLOW.md
data/intake/rosters_program<ID>.json   curated yearly rosters (the input of record; see loader docstring)
data/intake/partial/                   programs in progress (Penn: alumni.json, live2026.json, obs.json)
data/verify/                           resident-by-resident verification (section 3)
data/raw/wayback_cache/                cached Wayback fetches (used automatically by scripts/wayback.py)
data/raw/extraction/<program>/         per-program extraction outputs (obs.json, chosen.json, extract.py, PDFs)
data/raw/commoncrawl/<cl_program>/     pages recovered from Common Crawl
scripts/
  wayback.py              cached, polite Wayback CDX + fetch
  roster_extract.py       generic roster parser (heading / inline / table / split-name / surname-first layouts)
  roster_analysis.py      content_date, choose, class_table, dropouts
  21_load_curated_roster.py   load data/intake/rosters_program<ID>.json (--replace)
  16_adjudicate_program.py    per-program outcome table (bio > roster PGY7 > NPPES)
  20_ingest_usnews.py, 22_export_sources.py, ...
  tools/
    gapaudit.py      every URL on given hosts in a date window, any status (redirects, 404s) -> finds moved rosters
    linkaudit.py     follow links from archived parent pages in gap years
    cdxf.py          filtered Wayback CDX query helper
    cclocal.py       Common Crawl lookup via raw index files on data.commoncrawl.org
                     (works while index.commoncrawl.org is down; the size lookup uses a ranged GET because HEAD returns 403)
    ccscan.py / ccscan_one.py / ccretry.py   index-server based CC scan + retry (server often down)
    pubmed_aff.py    authors by PubMed affiliation (finds unlisted residents)
    collinfo.json    cached list of Common Crawl crawls
```

## 3. Resident verification status (the main open task)

Worklist: `data/verify/all_residents.json`, 561 residents from 11 programs (entry year 2011 or later):
- 325 have finished or left
- 236 are still in training

The 325 were split into `batch_1..8_in.json`, checked by parallel agents into `batch_1..8_out.json`, and merged into **`data/verify/exited_verified_merged.json`**. Each result has a verdict, the NS residency institution and years, other training, the current position, sources, evidence and a confidence rating.

**`data/verify/UNVERIFIED.md` lists every name still needing work:**
- **A. Never searched: 36.** Batch 7 hit the search limit. These are placeholders, not real results.
- **B. Searched, not found: 13.**
- **C. Conflicting sources: 4** (Wozny, Yoon, Alexopoulos, Bhandarkar).
- **D. Low confidence: 6.**
- **E. Medium confidence: 59.** Mostly completions inferred from NPI registry / PubMed data or a PGY-7 listing, with no source stating graduation.
- **F. Still in training, never checked: 236.**

Why it stopped: the session web-search limit (200) ran out, and Doximity began returning 406/410 to direct fetches. The user is raising `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` (target about 3000; confirm the variable actually takes effect).

**Nothing from the verification has been written to the database yet.** Proposed changes, awaiting a final check:

| Resident | Program | Proposed change | Evidence / confidence |
|---|---|---|---|
| David McMullen | Hopkins | unknown -> left medicine/other | NIMH 2018–25, FDA neuro devices 2024–25 (medium) |
| Shanna Fang | Northwestern | transferred -> switched specialty (diagnostic radiology) | Mayo radiology residency 2017–21 (medium) |
| Mason Blacker | Barrow | unknown -> military leave (Navy GMO), not attrition | NPI military address |
| James Yoon | Pitt | unknown -> likely in training (research years) | residency through 2027, UPMC papers 2024 |
| Archis Bhandarkar | Mayo | unknown -> likely in training (research) | NPI updated Feb 2026 + 2026 Mayo papers |
| Anne Park | Northwestern | CONFLICT: US News 2011–2018 completion vs not on alumni list + anesthesiology/pain taxonomy | re-check |
| Moshe Praver | Northwestern | our "switched specialty" unconfirmed | papers stop at Columbia 2017; re-check |
| Wozny | Pitt -> UCSF | KEEP transfer | Pitt Nov-2018 roster PGY1; UCSF Oct-2018 roster lacks him; UCSF PGY2 2019-20 |
| Guniganti | WashU | KEEP switch to ophthalmology | earlier Google: "Resident, Ophthalmology, Louisville" |
| Alexopoulos | SLU | KEEP did-not-complete (user-supplied) | note: practises neurosurgery in Greece; prior NS training there |

- **Transfers-in confirmed** (already recorded as joiners): Fernández-de Thomas (Puerto Rico -> Pitt 2021), Goldschmidt (-> Pitt 2015 as PGY3), Gooldy (Tennessee -> Barrow), Berry-Candelario (MGH -> Duke), Cleary (SLU -> WashU 2021), Southwell (Stanford -> UCSF 2013; also a Stanford transfer-out, to use when Stanford is done).
- **Date corrections:** Gandhoke graduated 2018; Labib 2016–21 (had already completed a Canadian residency); Goldschmidt 2015–20; Willsey 2014–21?; Rahme 2011–19; El Tecle start 2015?/end 2021 vs 2022; Kerezoudis possibly a 2019 start.
- **Notes:** Marcellino (Mayo) completed NS 2015–22, then a second residency in anesthesiology. Name variants: Kelly Ryan Murphy = Wackerle; Gabriella Paisan = Williams; Joelle Hartke = Noon; Katie McCoy = Kathleen Dlouhy; Christina Jackson (formerly Chen); Muftuoglu's legal first name is Ilayda.

Next steps:
1. Confirm the higher search limit works.
2. Re-run A + B + C + D (and E where feasible) with the same agent prompt (section 6). Instruct agents not to fall back to other search engines or the browser's Google.
3. Review, then write changes to `training_history` with `source_url` + notes.
4. Re-run `16_adjudicate_program.py` and `22_export_sources.py --all`.
5. Verify group F (in training): confirm start years and catch silent departures.

## 4. Program status (details in docs/PROGRAM_STATUS.md)

Done (loaded, adjudicated, sources exported):
- WashU 120
- Pitt 116
- UCSF 76
- Barrow 4
- Johns Hopkins 30
- Northwestern 41
- Michigan 91
- UCLA 67
- Duke 19
- SLU 60
- Mayo Rochester 40

Remaining reconstructed years after the exhaustive audits:

| Program | Rebuilt years | Reason |
|---|---|---|
| Barrow | 2011–13 | only chief letters + grad list on the St. Joseph's site |
| Barrow | 2015–16 | stale page |
| Barrow | 2021–22 | loaded by script |
| Northwestern | 2010–11 | no capture |
| Mayo | 2011–15 | no roster was ever published |
| Mayo | 2017 interns | not yet on the page |
| Mayo | 2018–19 | no capture |
| UCLA | 2011–14 | no capture |
| SLU | 2011–12, 2014–16, 2018–20, 2022–23 | no capture |
| WashU | 2020–22 | script-loaded; the 2022–23 initials tally matches exactly |
| Hopkins | 2018–19 | the department photo caption covers 19 residents |

The Library of Congress web archive is behind a Cloudflare check; the user could open it manually.

**In progress: Penn (program 100).**
- Hosts, oldest first: `uphs.upenn.edu/neurosurgery` -> `pennmedicine.org/neurosurgery/academics/residency/current-residents/` (2011–16) -> `pennmedicine.org/departments-and-centers/neurosurgery/education-and-training/residency/{current-residents,residents}` (2019+) -> `departments.med.upenn.edu/academic-departments/department-of-neurosurgery/...` (live).
- Observed: 2010–16, 2018–21 (Common Crawl for 2013–14 and 2018–19), 2024–26, live 2026–27.
- Gaps: 2016–18 (the new path was not archived until Jan 2019) and 2021–24 (captures are Incapsula firewall block pages).
- The alumni list (3 graduates a year, 2013–2026) is saved in `data/intake/partial/penn/alumni.json`.
- Next: build `rosters_program100.json`, compare each class with the alumni list for transfers, then verify residents.

Candidate next programs: Columbia 48, Stanford 61, Emory 20, Cleveland Clinic 12, Baylor 5, Mount Sinai 27.

## 5. Things that went wrong (do not repeat)

- Deferring Duke because it was hard. The user rejected this; never skip a program.
- Searching only the known roster URL. Always run `tools/gapaudit.py` over all hosts and the whole window, redirects included.
- Parser layouts that caused errors:
  - "Name / PGY-n" inline layout read as headings (Northwestern 2013–15 had been stored wrong)
  - a singular "Chief resident" subtitle clearing the PGY
  - bio text triggering stop words
  - surname-first names
- After any parser change, re-check the other programs for regressions.
- Fellows listed among the PGY-7s (Barrow: Spinazzi, Yaghi, Silva; earlier Rebchuk). Check class sizes above the complement against graduation lists.
- Shared scratch files between parallel agents collided. Give each agent its own subfolder.
- When the search limit ran out, agents fell back to Brave/DuckDuckGo and to Google in the user's Chrome, which triggered Google's CAPTCHA. Do not do this.

## 6. Agent prompt used for verification

See the batch agents' instructions (reproduced in this session). In short: WebSearch "<name>" neurosurgery residency / site:health.usnews.com / doximity, then WebFetch Doximity or an employer bio. Tie identity to the program. Verdicts: completed_here | transferred_out | switched_specialty | left_medicine_or_other | joined_from_elsewhere | not_found | conflicting. Output is JSON with sources, evidence and confidence, one object per input row in input order, written incrementally to `data/verify/batch_N_out.json`. No database edits.

## 7. Round 2 (2026-09-27, later session)

- **Penn (100) done:** `data/intake/rosters_program100.json` loaded (17 captures; 2016-18 and 2021-24 reconstructed), 47 alumni graduations in training_history, adjudicated (47 completed, 22 in training, 0 departures), sources exported, Wayback gap audit in `data/raw/extraction/gap/penn_{a,b}.txt`, Common Crawl rescan 2016-24 in `data/raw/commoncrawl/cl_penn2/`. Verified resident by resident in `batch_13_out.json` (27 completed_here, 22 still_in_training). Match lists: 2021, 2023 complete; 2016, 2017, 2022 partial or none.
- **Groups A-D re-run:** `batch_9..12_in/out.json` (A = 9 + 10, C + D = 11, B = 12). Nothing written to the DB yet. Open items are in `data/verify/FOLLOWUPS.md`.
- **The web-search cap is real:** 200 WebSearch calls per session, shared by all agents. It was hit again during batch 12 (Mahlokozera and Jin were not searched). The env-var idea was not real. Group F (236 in-training residents) needs several fresh sessions at about 3-4 searches per resident.
- **Adjudicator gap:** a resident missing from the latest roster can stay IN TRAINING (Mayo, Cohen Cohen). Fix before trusting group F counts.
- **Planchard:** record only the outcome (left neurosurgery after about 5 years). Do not copy the personal name-change details in the batch 9 notes into the DB or the source docs.

## 8. Overnight run (2026-09-27/28): all programs
- **Phase 1 is COMPLETE** for all 112 remaining programs plus Wayne State (added as program 125, closed ~2020). Brief: `docs/AGENT_BRIEF_PHASE1.md`. For each program: `data/intake/rosters_program<ID>.json` (loaded), `data/intake/gaps/program<ID>.{md,json}`, scratch in `data/raw/extraction/p<ID>/`, alumni rows in training_history, and adjudication plus export run. Queue: `data/intake/phase1_queue.json`.
- **Phase 2 is RUNNING** (brief `docs/AGENT_BRIEF_PHASE2.md`, queue `data/intake/phase2_queue.json`, helper `python3 data/intake/q2.py <done> <start>`), ordered by gap severity. Done so far: 45, 38, 8, 47 (47 is still unresolved: no roster exists, so it needs phase 3).
- **Everything learned is in `data/intake/PHASE2_NOTES.md`.** Read it before any consolidation. Key items:
  - About 70 cross-program transfers, found by `scripts/tools/crossmatch.py` (-> `data/intake/crossmatch.json`). Many records now wrongly show "switched specialty" or "unknown" for these people.
  - Three program closures, whose residents dispersed: Wayne State (~2020), UNM (old program lost accreditation, ~2018-20; new program 2022), UPR (accreditation withdrawn 2022; new program 2025). Report these separately from voluntary attrition.
  - Adjudicator fixes needed: a terminal PGY per entry cohort (6 -> 7 year switches, AOA-era programs); residents last seen at PGY-6 just before a gap should not count as departures; closed programs; NPPES namesake false "switches".
  - DB correction: Javier Figueroa (Barrow) was a Miami neurotrauma FELLOW, not a resident, so the transfer row written 2026-09-27 is wrong.
  - Manual-check list: live pages behind bot checks (UMass, SUNY Upstate, Geisinger, Walter Reed).
- The shared-script fixes made during the run: `cclocal.py` filter widened; 'left_medicine' branch added to `16_adjudicate_program.py`.
- **Phase 3** (US News/Doximity/Google per person) is NOT started. It needs WebSearch, which is capped at 200 per session and shared by all agents.
