# Find unseen neurosurgery residents via X/Twitter (and public Instagram) announcements

Our departure counts are a little below the ACGME's. The likely cause: residents who started and left between archived rosters, so we never saw them. Programs announce people on X/Twitter: Match Day ("welcome our new interns"), new-resident intros, chief/graduation posts, award posts, group photos with names.

For each input row:
1. Find the program's X/Twitter handle (search `"<program/department> neurosurgery" twitter` or `site:x.com <program> neurosurgery`).
2. Search for announcements in the target years: `site:x.com OR site:twitter.com <handle or program> "match" <year>`, `... "welcome" interns <year>`, `... residents <year>`, and the same with `site:instagram.com`. Also try `"<program> neurosurgery" "matched" <year>` for medical-school posts naming who matched there.
3. List every resident name you see for the target years. Compare it with `residents_we_hold` (match by surname). **Anyone NOT on that list is the point of this search.** For each one, find their fate by 30 June 2025: completed there, transferred (to where), left NS (to what), or still training. Check our files first: grep the name in data/verify/phase3/merged_final.json (they may be at another program).

Evidence: an X/Instagram post or snippet showing the name and program is acceptable as evidence that the person was matched/on the roster. Open posts in your own Chrome tab only if they display without logging in; never log in, never bypass a login wall. If only a search snippet shows the post, record the snippet text and URL and mark `"snippet_only": true`. Fate needs a real source (bio, program page, news); Doximity/NPI/LinkedIn are leads only.

Output, written after each row, to the path in your prompt:
`[{"program_id","program","target_years":[...],"handle":"@..."|null,"names_found":[{"name","year","context":"match/welcome/grad...","source","snippet_only":bool}],
  "missing_from_our_data":[{"name","entry_year","first_seen","last_seen","last_pgy","outcome":"completed|transferred|switched_specialty|left_medicine|left_other|left_destination_unknown|in_training|never_started","destination","fate_sources":[...]}],"note":""}]`

Rules: only the WebSearch tool for searching (no other search engines, no nitter or X search pages); no CAPTCHA/login bypass; no content behind logins; no health.usnews.com; no curl. Other agents share the Chrome tab group: check URL and names on every page; close your tabs at the end. **Budget: about 4 searches per row (more only when you have found a missing name and need their fate).** Helper files only in a private folder under data/verify/programs/<your agent folder>. Record only training/career facts. Final reply: one line per row (names missing from our data + fate, or "none found").
