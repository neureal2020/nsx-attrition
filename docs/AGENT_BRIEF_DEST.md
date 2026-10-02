# Destination hunt: residents who left their neurosurgery program

Each input person is NOT on their program's current resident page (verified), or their status is unknown. Find **where they went**. Previous queries are in `queries_already_tried`; do not repeat them.

Order of work for each person (up to 10 web searches):
1. `"<full name>" MD` (no specialty word), then `"<full name>" resident` and `"<full name>" residency`. Scan results for any specialty or program.
2. **Other programs' CURRENT resident pages**: neurosurgery programs in nearby states (transfers), and other specialties (radiology, neurology, anesthesiology, EM, PM&R, psychiatry, general surgery, orthopaedics, plastics, ophthalmology, IM, FM, pathology, radiation oncology). Search `"<full name>" <specialty> resident`.
3. **Match lists**: medical-school match lists and program "welcome our new interns" posts for the years after the person was last seen (`<last_seen year+1> match "<surname>"`).
4. **Name variants**: middle name, hyphenated or maiden surname, nicknames (e.g. "Joe" for "Joseph").
5. Research-year possibility: some programs omit research residents. If a *dated 2026* program source (news, lab page, program post) names them as a current resident, record `in_training_research_year` with that source.
6. Program **alumni/graduates page** (for final-year people): if listed as a 2025/2026 graduate, record `completed`.

Rules:
- Use only the WebSearch tool for searching. Do NOT use other search engines (DuckDuckGo, Bing, Google pages in the browser) as a workaround.
- Directory listings (Doximity/WebMD/Healthgrades/NPI/US News/LinkedIn) are stale. Use them as leads, never as proof of current status. **A destination needs a current program page, a dated announcement, or a current bio.**
- Search-result snippets of pages that now 404 do not count. Open the page (WebFetch; Chrome own tab if needed).
- No CAPTCHA/login bypass; no health.usnews.com; own Chrome tab, always pass tabId, no javascript_tool/fetch. Record only training/career facts (no personal-life, legal or health details).

Output `data/verify/phase3/dest/x_<N>_out.json`: `[{"key","name","outcome":"transferred|switched_specialty|left_medicine|completed|in_training_research_year|deceased|left_destination_unknown","destination","year_started_destination","evidence","sources":[url...],"queries_tried":[...]}]`. Write incrementally.

Final reply: one line per person (name → outcome, destination, key URL).
