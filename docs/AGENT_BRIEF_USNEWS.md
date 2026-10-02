# US News pass (dates check) — one agent at a time, slow

Input: `data/verify/phase3/usnews/u_<NNN>_in.json`. Output: `data/verify/phase3/usnews/u_<NNN>_out.json` (a JSON list, one object per input person, written incrementally).
Do not edit any other file. Do not write to the database.

For each person:
1. If `usnews_url_hint` is set, use it. Otherwise one `WebSearch`: `"<full name>" usnews doctors neurosurgery` (or the specialty in `finding_outcome` if they switched). Pick the health.usnews.com/doctors/... URL only if name + training/location plausibly match.
2. Open it in Chrome (own tab; always pass tabId; ToolSearch-load the claude-in-chrome tools first). US News shows a blank "Powered and protected by" page first: `computer` `wait` 6 s, then `get_page_text`. Check the returned text shows this URL and person's name (stale reads happen). Read "Education & Experience" (residency/fellowship lines with years), specialty, and certifications.
3. Wait at least 8 seconds between US News page loads.

Output object: `{"key","name","usnews":"found|not_found|blocked","url","education":["Residency, Neurological Surgery, 2014-2021 at X", ...],"specialty":"...","evidence":"short quote","notes":""}`.

Hard rules: read pages ONLY by `navigate` + `get_page_text` in your own tab. Do NOT use `javascript_tool`, in-page `fetch()`/XHR, or any scripted request to pull pages (that reuses the site's bot-check clearance and counts as bypassing it). Never interact with a CAPTCHA / "verify you are human" / access-denied page. If US News shows an "automated behavior"/blocked page twice in a row, STOP the batch: write `"blocked"` for the remaining people and say so in your final reply (the coordinator will pause). Record only training/career facts. Close your tab at the end.

Final reply (<100 words): counts found / not_found / blocked, and any person whose US News training contradicts `finding_outcome`.
