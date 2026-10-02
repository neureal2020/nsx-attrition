# External-validation ("gold standard") pass

> **CORRECTION (2026-09-29): `in_training` REQUIRES the program's CURRENT resident page to list the person.** Doximity, WebMD, Healthgrades, US News, NPI, LinkedIn, Cureus and license records lag by years and routinely still show people at programs they left (verified: WashU, Ohio State, UAMS, OHSU, Rush). Those sources can confirm identity or past training, never current status. If the current program page omits someone, treat them as having left (or being on a documented research year the page mentions) and look for where they went.

The user's evidence standard (2026-09-29): **program website + external validation** for every resident. The program-website part is already attached to each input person (`program_site`: roster or archived roster URLs that list them). Your job is the **external** part.

## Tasks (see each person's `task`)
- **CURRENT_BIO** (completed, transferred, switched or left): find a **current** faculty, hospital, university or group-practice bio page for the person and quote the line showing their current role.
  - completed / transferred: a bio showing them **practising neurosurgery** (or in a neurosurgery fellowship) is the gold standard. Record where they trained if the bio says so. If the bio names a different residency program than `program`, that is a transfer: say so.
  - switched_specialty / left_medicine: a bio showing the new specialty or role.
  - If there is no bio after 3-4 searches, fall back to: Doximity page opened in Chrome showing Neurosurgery plus ABNS/AOA board certification, a program graduation or alumni post, or an NPI registry entry (npiregistry.cms.hhs.gov) with taxonomy Neurological Surgery at a practice address. Mark `evidence_level: "silver"`.
- **EXTERNAL_TRAINING** (in_training): one source outside the roster page confirming them in this program: medical school match list or match-day news naming the program, the program's/school's social-media match or welcome post (via Google), a Doximity page naming the program, or a program news item. Mark `evidence_level: "gold"` if it names the program, else `"silver"`.
- If what you find contradicts `outcome` (e.g. a "completed" person practises dermatology), record the new outcome and explain it in `disagreement`.

## Rules
- **"gold" requires that you OPENED the bio page** (WebFetch or Chrome) and quote text from the page itself, with its URL in `external_url`. A search-result snippet or AI search summary alone is at most "silver" and must be marked `external_type` + `"(snippet)"`. Add `"page_opened": true|false`.
- Same hard rules and Chrome rules as `docs/AGENT_BRIEF_PHASE3.md`: own tab, always pass tabId, pages only via navigate + get_page_text (no javascript_tool or scripted fetch), check URL + name on each page (stale reads happen), never bypass CAPTCHAs or logins, close your tab at the end.
- **US News is off.** Do not open health.usnews.com.
- **Publication affiliations do not count.**
- Identity: the bio must match on name AND at least one of residency program, medical school, or years/era. Namesakes are common. If unsure, mark `evidence_level: "program_only"` and explain.
- Budget: up to 4 web searches per person. WebFetch is fine for bio pages; use Chrome for Doximity.
- Record only training and career facts.

## Output
`data/verify/phase3/gold/g_<NNN>_out.json`: a JSON list in input order, one object per person:
`{"key","name","program_id","outcome","evidence_level":"gold|silver|program_only","external_url","external_type":"faculty_bio|practice_bio|fellowship_roster|match_list|program_post|doximity|abns|npi","evidence":"short quote","current":"role, institution, city","disagreement":"","searches_used":n}`
Write incrementally (every 5 people).

Final reply (<120 words): counts by evidence_level, and every disagreement (one line each).
