# Reconcile our departure counts with ACGME (targeted)

Our yearly departure counts are a little below the ACGME's (most in 2017-19 and 2023-24). Each input row is a specific lead.

**Step 0 (free, do first): check our own files** before any web search. grep the person/program in
data/verify/phase3/merged_final.json, data/verify/phase3/gold/*_out.json, data/verify/phase3/ident/*_out.json,
data/verify/phase3/dest/**/*_out.json, data/verify/programs/*_out.json. If the answer is already there, record it with
"source":"local:<file>" and do not search.

**kind = intern_shortfall**: NRMP says more interns matched than we hold. Name every matchee for that year (school match lists, program news / match posts) and, for anyone missing from `our_residents_nearby`, find what happened (left in intern year and where to; transferred; deferred; never started).

**kind = transfer_in_unknown_origin**: the person first appears at this program above PGY-1. Find their earlier residency (current bio "Training/Education", Doximity training lines as a lead, program welcome posts). We only care whether they came from another **US ACGME neurosurgery program** (then the origin program had a departure we are missing). Foreign residency, research fellowship, preliminary surgery year, or a different US specialty = not an ACGME neurosurgery departure.

Output (write after each row) to the path in your prompt:
`[{"kind","program_id","program","match_year"|"name","finding":"one line","people":[{"name","origin_program"|null,"origin_is_us_acgme_ns":true|false|null,"left_origin_ay":"YYYY-YYYY"|null,"pgy_when_left":n|null,"outcome":"transferred|switched_specialty|left_medicine|left_other|left_destination_unknown|never_started|deferred|in_our_data","destination","sources":[...]}]}]`

Rules: only the WebSearch tool for searching (no other engines); no CAPTCHA/login bypass, no content behind logins; no health.usnews.com; open pages with WebFetch or your own Chrome tab (navigate + get_page_text), no curl. Doximity/NPI/LinkedIn = leads only. Check URL and name on every page (shared Chrome tab group). **Budget: at most 4 searches per row; skip searching when Step 0 answers it.** Helper files only in your private scratchpad folder. Record only training/career facts. Final reply: one line per row.
