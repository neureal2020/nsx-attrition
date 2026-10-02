# Same-city all-specialty sweep (destination hunt, round 2)

Every input person left their neurosurgery program (they are absent from its CURRENT resident page), and a deep search (8-16 queries) found no destination. Name searches are exhausted. This pass works from **rosters**, not name searches. Precedent: Robbins was found only on UAB's current Emergency Medicine resident page.

Per person (budget ~12 web searches + as many page opens as needed):
1. List the teaching hospitals in the **old program's city/metro** (the same institution first, then other ACGME sponsors in the metro).
2. For each, open the **current** resident pages (2025-26 or 2026-27) of these specialties and check for the surname: neurology, diagnostic radiology, interventional radiology, anesthesiology, emergency medicine, PM&R, psychiatry, general surgery, orthopaedics, plastics, ENT, ophthalmology, internal medicine, family medicine, pathology, radiation oncology, neurosurgery. Use WebSearch like `site:<domain> "<surname>" resident` and open the roster page (WebFetch or own Chrome tab, get_page_text). Also check the medical school's and home-state institutions if `known` suggests ties (med school city, license state, Doximity address).
3. Then **likely destination cities** from any lead in `prior_evidence` (license state, directory address, co-author affiliation, hometown med school) and repeat step 2 there.
4. Neurosurgery programs in neighbouring states: current resident pages (transfer check).
5. Stop a person when found, or when the old city + lead cities are swept. Log every roster page you checked in `rosters_checked`.

Rules (same as docs/AGENT_BRIEF_DEST.md): only the WebSearch tool for searching; no other search engines; no CAPTCHA/login bypass; no health.usnews.com; own Chrome tab, always pass tabId, navigate + get_page_text only. Directory listings (Doximity, NPI, licenses, LinkedIn) are leads, never proof. A destination needs a current program page, a dated announcement, or a current bio that you opened. Record only training/career facts. Namesake check: match first+last name and a consistent era/med school.

Output (write after each person) to the path in your prompt: `[{"key","name","outcome":"transferred|switched_specialty|left_medicine|completed|in_training_research_year|left_destination_unknown","destination","year_started_destination","evidence","sources":[...],"rosters_checked":[...],"queries_tried":[...]}]`.
Final reply: one line per person (name → outcome, destination, key URL).
