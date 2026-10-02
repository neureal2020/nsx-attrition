# Collecting US News data with the Claude Chrome extension

US News refuses scripted requests outright (connection refused, not 403), and
WebFetch times out on it. A real logged-in browser is the only way in, which is
what the extension provides.

## One-time setup

1. **Restart Claude Code.** `/chrome` alone did not enable browser tools in this
   session; a restart triggers the one-time prompt to turn them on.
2. Accept the prompt.
3. In the extension, grant permission for `health.usnews.com` (and
   `doximity.com` if you want it driven too).
4. Verify: ask Claude "are browser tools available?" — it will say so directly.

## Once enabled — automated loop

Ask for: **"run the US News lookups for program 60"**. Tested on SLU 2026-09-25.

1. **Find the profile by web search**, not US News' own search. Its `?q=` URL
   returns 500, and the name box fuzzy-matches inside a sticky saved location
   ("Eichholz" -> 668 unrelated doctors). Profiles live at
   `/doctors/<first-last>-<id>`; `site:health.usnews.com/doctors "<name>"` finds them.
2. **Read the Education & Experience block** from a US News tab (in-page `fetch`
   of each profile works; keep it in the background — >45s of work times out).
3. Dry-run through `20_ingest_usnews.py`, then commit.

Coverage on SLU: 15 of 23 people had a profile; 12 had a residency line. Current
residents and recent leavers mostly have none (or only "Medical School").

Pacing is deliberate (a few seconds between profiles) — this is an ordinary
browsing rate, not a crawl.

## Meanwhile — manual intake, works today

1. `python3 scripts/19_build_worklist.py --program-id 60`
   writes `data/intake/worklist_program60.md`: one heading per resident with a
   prepared US News and Doximity search link and an empty fenced block.
2. Open each link, copy the **Education & Training** section, paste it inside
   that resident's ``` fence. Paste raw — no cleanup needed.
3. `python3 scripts/20_ingest_usnews.py --program-id 60 --file data/intake/worklist_program60.md --dry-run`
   to preview, then drop `--dry-run` to commit.

## The format trap this handles for you

The two sites publish different things and they must not be conflated:

| Source | Example | Meaning |
|---|---|---|
| US News (older layout) | `St Louis University…, 2014, Neurosurgery` | a **single year = the year training ENDED** |
| US News (current) | institution line, then `Residency, Neurological Surgery, 2018-2024` | a **range**; institution is on the line ABOVE |
| Doximity | `Residency, Neurological Surgery, 2009 - 2015` | a **range** |

Reading a bare year as a start date is what produced three phantom same-year
entrants earlier in this project. The ingester stores a single year as
`end_year` and leaves `start_year` NULL rather than guessing.

## Completion rule applied

- **>= 7 years** at the program -> `yes` (graduated)
- **6 years, started before 2014** -> stored `unknown`, noted probable (a pre-2014 programme could legitimately be six: McClung-Smith, Sampath 2009-2015)
- **6 years, started 2014 or later** -> `no` (Alexopoulos 2018-2024)
- an **internship at the program** counts toward the span (Pierson)
- **materially shorter** -> `no`; the **end year dates the attrition event**
- **single year only** -> `unknown`; records the end year, asserts nothing about entry
