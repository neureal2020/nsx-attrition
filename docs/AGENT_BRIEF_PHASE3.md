# Phase 3 brief: verify each resident on US News / Doximity / Google

You are verifying ONE BATCH of residents for a neurosurgery residency attrition study (academic years 2011-12 .. 2026-27).
Working dir: `/Users/neureal/Documents/Residency Application Study`.
Your input: `data/verify/phase3/batch_<NNN>_in.json` (a list of people). Your output: `data/verify/phase3/batch_<NNN>_out.json`.
You do NOT write to the database. The coordinating session reviews your output and applies it.

## What each person needs
For every person in the batch, establish from public sources:
1. **Identity**: that the profile you found is this person. Match on at least two of: the residency program named in the input, overlapping training years, medical school (if given), a distinctive full name. Namesakes are common (the NPI registry produced >8 wrong "switched specialty" calls in phase 1-2). If you cannot confirm identity, say so; never guess.
2. **Residency**: the program(s) and years stated by the source (e.g. US News "Residency: X, 2014-2021"; Doximity "Residency: X"; a faculty bio).
3. **Outcome** at the input program: `completed` | `transferred` (to which program, which year) | `switched_specialty` (to which specialty, which year) | `left_medicine` | `in_training` | `unknown`.
   **Priority is the attrition outcome; exact dates are secondary.** Evidence that the person now practises as a neurosurgeon (faculty bio, practice page, hospital profile, US News/Doximity specialty "Neurosurgery", ABNS certification) counts as completing neurosurgery training. Still record where they trained: if the sources name a different residency program than the input's, that is a transfer. A fellowship alone (without evidence they practise neurosurgery) is not proof: a neuroradiology/pain/neurocritical-care/neurology path may be a switch.
4. **Year left** (for anyone who did not complete there): the academic year they left, and the year they started elsewhere.
5. **Current**: current specialty / position if stated (e.g. "neurosurgeon, X hospital"; "radiologist").

## >>> CURRENT STATUS (set 2026-09-28 22:15): US News is PAUSED <<<
US News started blocking ("automated behavior") under parallel load. Do NOT open health.usnews.com pages and do not run US-News searches. Record `"usnews": "deferred"` for everyone; a single slow agent will do a separate US News pass later. Run checks A (Google + bios) and B (Doximity) in full as below.

## Required checks: ALL THREE for EVERY person (no stopping early)
Every person gets all three checks, even when the first one already answers the question. Record each check's result in `checks` (see output format), including `not_found`.

**A. Google search + faculty/program profiles.** `WebSearch` for `"<full name>" neurosurgery` and `"<full name>" MD <program institution>`. Look for faculty bios, practice pages, fellowship rosters, other programs' resident pages, alumni lists, news. Open (WebFetch) any faculty/program/practice bio that names this person and states training; quote it. Also note any doximity.com/pub/... and health.usnews.com/doctors/... URLs the results show.

**B. Doximity profile, opened in Chrome.** If search A did not give the URL, run `WebSearch` `"<full name>" doximity`. Open the `doximity.com/pub/...` page in Chrome and read the "Education & Training" and "Certifications & Licensure" sections with `get_page_text`. "American Board of Neurological Surgery" under certifications is positive evidence of completion.

**C. US News profile, opened in Chrome.** If you have no URL yet, `WebSearch` `"<full name>" usnews doctors`. Open `health.usnews.com/doctors/...` in Chrome and read "Education & Experience". US News first shows a blank "Powered and protected by" page; wait ~6 seconds (computer `wait`) and read again; it normally clears by itself.

Current residents and recent graduates often have no Doximity/US News page; that is fine, but `not_found` is only allowed AFTER you ran the site-specific search for that person (`"<full name>" doximity` / `"<full name>" usnews doctors`) and it returned no matching profile. Do not skip those searches to save budget.

### Chrome rules
- Load the tools with ToolSearch: `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__tabs_close_mcp`.
- Call `tabs_context_mcp` once, then `tabs_create_mcp` to make YOUR OWN tab and use only that tab ID (other agents share the browser). ALWAYS pass your `tabId` explicitly to `navigate`, `get_page_text` and `computer`; never call `navigate` without `tabId` (that grabs another agent's tab). If your tab disappears, create a new one. Close it with `tabs_close_mcp` before your final reply.
- After each `navigate`, wait ~5 s, then check that the text returned by `get_page_text` shows the expected URL AND the person's name; `get_page_text` sometimes returns the PREVIOUS page. If it doesn't match, wait and re-read; never record data from a mismatched page.
- Human pace: one page at a time, at least 5 seconds between page loads (`computer` `wait`). Read-only: never click sign-in, "join", appointment, review, claim-profile or any form.
- If a page shows a CAPTCHA, a "verify you are human" challenge that needs interaction, an access-denied page, or a login wall, do NOT interact with it. Record the check as `blocked`, and if it happens on 2 consecutive pages of the same site, stop using that site for the rest of the batch and say so in your final reply. **Never stop the batch because of a blocked site**: keep verifying every person with Google search + faculty/practice bios (and the other site if it still works). Doximity/US News are mainly for dates.
- Never type anything into a website. Navigate only to URLs from search results or `doximity.com/pub/...` / `health.usnews.com/doctors/...` profile URLs.

Budget: up to 4 web searches per person (tier 1: up to 6). No limit on reading the profile pages found.

## Hard rules
- **Never bypass a CAPTCHA, bot check, login wall or paywall.** No alternate search engines through other routes.
- **Never send the user's email address, name or any other personal identifier to an outside service** (no `mailto=`, `email=`, or contact fields in User-Agents).
- Record only training/career facts. Do not record personal-life details (name-change reasons, family, health, legal matters) even if a source mentions them; if a name change matters for identity, write only "listed under a different surname at <program>".
- Every claim needs a `source_url`. A search snippet counts only if you quote the snippet text in `evidence`.
- Do not edit any file except your own `batch_<NNN>_out.json` (and scratch files under `data/verify/phase3/scratch/<NNN>/`).

## Output format (`batch_<NNN>_out.json`)
A JSON list, one object per input person, in input order:
```json
{"key": "<copied from input>", "name": "<as input>", "program_id": 0,
 "identity": "confirmed|probable|not_found|ambiguous",
 "identity_basis": "US News lists residency at <program> 2013-2020 and MD <school>",
 "residency_stated": [{"institution": "...", "specialty": "neurosurgery", "start": 2013, "end": 2020}],
 "outcome": "completed|transferred|switched_specialty|left_medicine|in_training|unknown",
 "outcome_detail": "e.g. transferred to <program> as PGY-3 in 2016; or switched to diagnostic radiology (<program>, 2017-2021)",
 "year_left": 2016, "destination_program": "...", "destination_start_year": 2016,
 "current": "e.g. neurosurgeon, <hospital>, <city>",
 "agrees_with_db": true, "disagreement": "what differs from the input's recorded outcome, if anything",
 "checks": {"google": "found|not_found", "doximity": "found|not_found|blocked", "usnews": "found|not_found|blocked|deferred"},
 "abns_certified": true,
 "sources": [{"url": "...", "type": "usnews|doximity|bio|program_page|news|pubmed|search_snippet", "evidence": "short quote"}],
 "searches_used": 2}
```

## Final reply (under 150 words)
Counts by outcome and identity; counts of doximity/usnews found / not_found / blocked; total web searches; every case where your finding DISAGREES with the input's recorded outcome (one line each); problems (blocked pages, searches that errored).
