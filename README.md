# U.S. Neurosurgery Residency Attrition Study

A resident-level census of U.S. ACGME neurosurgery residents (entering classes 2011–2025), built from program
websites, web archives and public biographies, with each resident's outcome traced and checked against ACGME
Data Resource Book totals. Status is as of **30 June 2025**.

> **Private data.** The database names individual residents and their outcomes. Keep this repo private and
> do not publish resident-level rows; report aggregates only.

## Quick start (any machine)

```bash
gh repo clone neureal2020/nsx-attrition
cd nsx-attrition
sqlite3 db/neurosurgery_attrition.db      # or open it in DB Browser for SQLite / Python sqlite3
```

```sql
-- attrition rate, 2014–2023 entrants (attrition ÷ entering residents)
SELECT COUNT(*) AS entrants, SUM(attrition_2025) AS attrition,
       ROUND(100.0*SUM(attrition_2025)/COUNT(*),1) AS pct
FROM outcomes
WHERE entry_year BETWEEN 2014 AND 2023 AND outcome_2025 NOT LIKE 'excluded%';
-- → 2473 | 162 | 6.6

-- one resident's record with program and roster history
SELECT r.full_name, p.name, o.entry_year, o.outcome_2025, o.last_seen_ay, o.last_seen_pgy,
       o.destination_specialty, o.confidence
FROM residents r JOIN outcomes o USING(resident_id) JOIN programs p ON p.program_id = r.match_program_id
WHERE r.last_name = 'Varela';
SELECT academic_year, pgy_numeric, name_as_listed FROM roster_observations WHERE resident_id = ? ORDER BY academic_year;
```

Python: `import sqlite3; con = sqlite3.connect("db/neurosurgery_attrition.db")` (pandas: `pd.read_sql(query, con)`).

## The database (`db/neurosurgery_attrition.db`)

One row per person per program. Schema in `db/schema.sql`.

| Table | Rows | What it holds |
|---|---|---|
| `programs` | 125 | ACGME programs: name, city/state, ACGME id, website, positions per year |
| `residents` | 3,968 | person: name, `match_year` (entry year), `match_program_id`, notes |
| `outcomes` | 3,968 | one per resident (see below) |
| `roster_observations` | 23,801 | each time a name appeared on a roster: program, academic year, PGY, `resident_id` (null = not a cohort member, mostly pre-2011 entrants) |
| `roster_snapshots` | 2,069 | the archived roster pages those observations came from |
| `training_history` | 3,406 | training lines taken from bios (program, years, completed, source) |

Key `outcomes` columns:

| Column | Meaning |
|---|---|
| `outcome_2025` | **use this for analysis.** `completed`, `in_training`, `transferred` (to another NS program), `switched_specialty`, `left_medicine`, `left_other`, `left_destination_unknown`, `deceased`, or `excluded_*` (`entered_before_2011`, `entered_after_cutoff`, `program_out_of_scope` = National Capital Consortium, `not_a_resident`) |
| `attrition_2025` | 1 = left neurosurgery without graduating by 30 Jun 2025 |
| `entry_year` | PGY-1 year (match year) |
| `last_seen_ay`, `last_seen_pgy` | last roster year/PGY at this program |
| `destination_specialty` | where residents with attrition went (radiology, anesthesiology, …, "Destination not found") |
| `confidence` | `confirmed` (program page + independent source), `probable`, `possible` (program information only), `unverified` |
| `person_key` | stable id `programid:first3:lastname` used across the JSON files |
| `status` | the same outcome in the original schema vocabulary (`graduated`, `transferred_out`, …) |

## Definitions

- **Attrition** = leaving neurosurgery without graduating from any neurosurgery residency. Transfers to another
  neurosurgery program, deaths, and leaving after graduation are **not** attrition. A resident who transferred
  and later left counts once, at the last program. Leaving for a non-physician role (e.g. PA) is attrition.
- **Attrition rate** = residents with attrition ÷ residents who entered.
- **Transfers** exclude forced moves when a program closed (Wayne State and UNM 2019–20, Puerto Rico 2020–21).
- **Program size** = mean entrants per year (1/yr, 2/yr, 3+/yr); program-level stats use programs with ≥7 entering classes in 2014–2023.

## Headline results (AANS abstract)

`writing/AANS abstract/AANS_abstract_2026-10-01-edits-v13.docx` (final; 319 words).
2014–2023 entrants at 111 programs with ≥7 classes: attrition 6.6% (160/2,432), 64% in PGY-1–2;
transfers 2.3% (56/2,473); 1/yr programs 10.7% vs 6.3% (2/yr) and 6.0% (3+/yr), p = 0.03.
ACGME check: annual resident counts within 5.4%; we found 240/262 ACGME-reported departures and an estimated 140/161 ACGME attrition.

## Repository layout

| Path | Contents |
|---|---|
| `db/` | SQLite database, schema, dated backups |
| `data/verify/phase3/merged_final.json` | source of truth for outcomes (the DB is loaded from it) |
| `data/verify/phase3/RUNLOG.md`, `RESUME.md` | full work log / where things stand |
| `data/verify/programs/` | NRMP counts per program-year, ACGME data (`acgme_attrition.json`, with PDF links and pages), roster-confidence workbook |
| `data/verify/report/` | analysis outputs (`analysis.json`, `window_analysis.json`, `acgme_validation.json`, report HTML) |
| `data/verify/lit/` | prior attrition studies: notes and extracted full texts (copyrighted; keep the repo private) |
| `data/intake/adjudication/` | per-program roster audits (all entry years) |
| `scripts/` | numbered collection pipeline (01–22) |
| `scripts/tools/` | merge, analysis and DB-load scripts |
| `docs/` | methodology, agent briefs (search rules), handoff notes |
| `writing/AANS abstract/` | abstract drafts (v1–v13) |

Not in the repo: `data/raw/` (archived pages, NPPES downloads) and `db/nppes.db` (1.5 GB). Neither is needed to use the database or rerun the analysis.

## Rebuilding

Requires Python 3.10+ with `scipy statsmodels openpyxl python-docx` (`pip install scipy statsmodels openpyxl python-docx`).

```bash
python3 scripts/tools/phase3_final_merge.py     # merged_final.json (applies overrides/additions)
python3 scripts/tools/confidence_heatmap.py     # program-year roster confidence workbook
python3 scripts/tools/attrition_analysis.py     # cohort analysis
python3 scripts/tools/national_check.py         # yearly check vs ACGME
python3 scripts/tools/acgme_validation.py       # all residents on duty vs ACGME, AY 2011-12..2024-25
python3 scripts/tools/window_analysis.py        # AY 2014-15..2023-24: rates, stages, destinations, programs
python3 scripts/tools/load_phase3_to_db.py      # reload residents/outcomes into the DB (back up first)
```

Corrections go in `scripts/tools/phase3_final_merge.py` (`OVERRIDES`, `ADDITIONS`, `ENTRY_FIX`), never by hand-editing the DB.

## Evidence rules (for anyone extending the data)

- **Counts toward `in_training`:** only the program's current resident page.
- **Leads only, never evidence:** Doximity, NPI, Healthgrades, LinkedIn and publication affiliations.
- **Allowed sources:** public pages only; no login-walled content and no CAPTCHA bypass. Record only training and career facts.
- **Full rules:** `docs/METHODOLOGY.md` and `docs/AGENT_BRIEF_*.md`.

## Updating the GitHub copy

```bash
cd "/Users/neureal/Documents/Residency Application Study"
git add -A
git commit -m "describe the change"
git push
```

On another machine, get the latest with `git pull`.
