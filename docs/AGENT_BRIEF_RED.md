# Red program-years: final recovery search

Each input program has "red" years: years where a resident could be missing from our data. Two kinds (see each year's `reason`):
- **gap**: no roster was archived and a resident who was already in the program could have left unseen (e.g. no roster before or after, or a class shrinks with no explanation).
- **entrant**: the entering class we hold is smaller than the NRMP matched count (`nrmp_matched` vs `entrants_held`), so a new intern could have started and left unseen.

`our_residents_nearby` lists everyone we already hold at that program around those years. `prior_search_notes`, `known_hosts` and `alumni_page` show what earlier searches already tried (Wayback, Common Crawl). Do not repeat those; look for **different kinds of sources**.

## What to look for (per red year)
1. Program **alumni / graduates / "former residents"** pages (live or Wayback) naming each graduating class; a class that graduated in full closes the gap for that class.
2. **Graduation / chief-resident / "welcome new residents" / Match Day** posts and news (department news, hospital news, school news, program social posts that are public).
3. **Medical-school match lists** for the year (search `"<year> match list" "neurological surgery" "<program or hospital>"`) to name each matched intern.
4. Archived **roster pages on other hosts** (sponsoring hospital site, old department URL, PDF brochures, GME resident directories), and department **annual reports / newsletters** that list residents by PGY.
5. For every name you find who is NOT in `our_residents_nearby`: find their fate by 30 June 2025 (completed there / transferred / left and where / never started).

## Output
`data/verify/programs/red_<N>_out.json` (N = your batch), written after each program:
```
[{"program_id", "program", "years": [{"year", "resolved": true|false,
   "how": "one line: what closes (or fails to close) the gap",
   "classes_confirmed": ["2014 entrants: A, B (alumni page 2021)", ...],
   "sources": [urls opened]}],
  "new_people": [{"name", "entry_year", "first_seen", "last_seen", "last_pgy",
     "outcome": "completed|transferred|switched_specialty|left_medicine|left_other|left_destination_unknown|in_training",
     "fate_detail", "sources": [urls opened]}],
  "notes": ""}]
```
Mark a year `resolved: true` only if an opened source shows that every resident in that year is accounted for (all continuing residents reappear or graduate, and the entering class count matches NRMP or is named in full).

## Rules
Only the WebSearch tool for searching; no other search engines; no CAPTCHA/login bypass; no content behind login walls; no health.usnews.com. Open pages only with WebFetch or your own Chrome tab (navigate + get_page_text); no curl or scripted fetch. Other agents share the Chrome tab group: check the URL and names on every page. Doximity/NPI/LinkedIn/publication affiliations are leads only; snippets of pages that now 404 don't count. Record only training/career facts. Budget: about 8 searches per program. Helper files only in a private scratchpad folder named red<N>agent.

Final reply: one line per program (red years → resolved / still red, and any new people with their fate).
