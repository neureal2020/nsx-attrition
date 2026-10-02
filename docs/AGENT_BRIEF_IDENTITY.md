# Identity-resolution pass

> **CORRECTION (2026-09-29): `in_training` REQUIRES the program's CURRENT resident page to list the person.** Doximity, WebMD, Healthgrades, US News, NPI, LinkedIn, Cureus and license records lag by years and routinely still show people at programs they left (verified: WashU, Ohio State, UAMS, OHSU, Rush). Those sources can confirm identity or past training, never current status. If the current program page omits someone, treat them as having left (or being on a documented research year the page mentions) and look for where they went.

Every input person already has a phase-3 finding (`prior`: identity, basis, outcome, sources). Their identity is only probable, ambiguous or not found, or their outcome is unknown. Your job: **raise every identity to "confirmed" or show it is a different person, and resolve every "unknown" outcome.** Follow `docs/AGENT_BRIEF_PHASE3.md` for the hard rules, Chrome rules and output format, with these overrides:

- **US News is off**: record `"usnews": "deferred"`; never open health.usnews.com.
- Budget: up to 8 web searches per person. Use it; do not stop at 1-2 searches when unresolved.
- **Program-website sources are already on file**: `data/verify/phase3/program_sources.json` maps each `key` to the roster pages (live or Wayback) that list the person, with year and PGY. Use those as `program_site_url`; do not downgrade identity for lack of a program page if one is listed there.
- **Evidence standard (user, 2026-09-29): program website + external validation.** For EVERY person record the program-website source (roster / alumni / graduates page naming them) PLUS the external source for their outcome:
  - **completed / transferred-and-completed** → GOLD: a *current* faculty or practice bio (hospital, university, group practice) showing them practising neurosurgery (quote it). If no bio exists after searching, fall back to: Doximity/ABNS neurosurgery certification, a program graduation post, or NPI taxonomy Neurological Surgery at a practice address (say which; mark `evidence_level: "silver"`).
  - **in_training** → the program's current resident page, plus one external source (match-day announcement or school match list naming the program, program social post, or a Doximity page naming the program).
  - **switched_specialty / left_medicine** → a current bio or roster in the new specialty or role.
  - **Publication affiliations do NOT count** toward identity or outcome; mention them only as background.
  - `identity: "confirmed"` requires the program-website source AND one external source that agree on name plus program, years or medical school.
  - Add fields `program_site_url`, `external_url`, `evidence_level` ("gold" | "silver" | "program_only").
- Doximity pages that list unrelated specialties or boards are often merged namesakes. Do not let them override two consistent sources; note them in `identity_basis`.
- If the evidence shows the roster person and the found profile are **different people**, say so, set `identity: "not_found"`, and keep searching for the right one.
- **For every unknown, FIRST test "still at the program"** (user: "just search that name + neurosurgery, there should be something"). Run a plain `"<full name>" neurosurgery` search and look for the program's own people or resident page, a Doximity/WebMD/Healthgrades listing in the program city, or a recent program post. Many recorded "LEFT" people were missed by an incomplete roster capture and are still in training (spot checks: Michael Jin and Kyle McGrath on WashU people pages; Shentu at UTHealth; Mahlokozera at WashU). Only look for a destination once they are clearly gone.
- For `task: "RESOLVE OUTCOME + IDENTITY"`: determine completed / transferred (where, when) / switched_specialty (to what, when) / left_medicine / in_training / deceased. Also check other specialties' resident rosters, match announcements for the departure year, name variants (middle, hyphenated, maiden), and industry roles. If still unresolved after the full budget, keep `outcome: "unknown"` and list exactly what was tried.
- Record only training/career facts. For a death, record only `outcome: "deceased"` and the year, no circumstances.

Output: `data/verify/phase3/ident/i_<NN>_out.json`, same object format as phase 3, plus `"ident_searches": n` and `"sources_count": n` (number of independent sources supporting the identity). Write incrementally.

Final reply (<150 words): identity counts before → after, outcomes resolved (one line each), people shown to be different persons.
