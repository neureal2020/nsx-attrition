# Evidence-gathering strategies, in priority order

Run per program. Each stage falls through to the next when it comes up empty.
`strategy_log` records what each attempt returned so the ordering can be
revised on evidence rather than intuition.

| # | Strategy | Script | Notes |
|---|---|---|---|
| S0 | **Web search** for the department + roster page | *(agent-driven)* | **Do this first.** Guessing URL patterns failed for SLU three times; search found it immediately. |
| S1 | Validate the recorded URL | `strategies.s1_resolve_site` | AANS URLs are often wrong, not merely stale. |
| S2 | Institution **sitemap** search | `10_sitemap_announcements.py`, `strategies.s2_sitemap_search` | Finds departments nested unguessably. Also finds announcement URLs that news-index crawling cannot reach. |
| S3 | Wayback **CDX** history of found URLs | `13_program_timeline.py` | See the asterisk gotcha below. |
| S3b | **Common Crawl** when Wayback has a gap | `17_commoncrawl_rosters.py` | An independent archive with different coverage. Supplied SLU's 2016-17 roster — the only record of a resident who left after PGY-1. **Query this before concluding data does not exist.** |
| S4 | Parse live roster | `strategies.s4_parse_live_roster` | Current year only. |
| S5 | Parse graduates/alumni page | `strategies.s5_parse_alumni` | Program-side completion list. |
| S6 | Parse match/graduation announcements | `11_parse_announcements.py` | Entry/exit evidence independent of the roster. |
| S6b | Program **X / Instagram** accounts | *(browser, logged in)* | Match Day and graduation posts. X search `from:<handle> (match OR welcome OR graduat OR chief OR intern)` reaches back to the account's start (SLU: 2019); Instagram only ~18 months. Names often sit in the image, not the text. Browse at human pace: Instagram's feed API returned 429 on the first scripted call. A match post adds the new intern to the next year's roster (`source_type='instagram'`) without moving the current-year cutoff. |
| S7 | Reconstruct entry year from PGY | `15_infer_entry_years.py` | Recovers cohorts for years with no archived roster. |
| S8 | NPPES specialty + cohort-year check | `nppes_lookup.py`, `12_flag_implausible.py` | Adjudication, and faculty rejection. |
| S9 | Archive current pages for the future | `07_save_page_now.py` | Converts future coverage from luck into a controlled panel. |

## Hard-won gotchas

**CDX: never append `*` to a `matchType=prefix` query.** It returns zero,
silently. `slu.edu/medicine/neurological-surgery*` -> 0 captures;
`slu.edu/medicine/neurological-surgery/` -> 263. This caused a false conclusion
that SLU had no archive at all.

**Wayback throttles per client, hard.** A query measured at 5s cold took 37s
with a few hundred in flight. Discover URLs on live sites (unthrottled), spend
the Wayback budget only on targeted per-URL history.

**Save Page Now requires a logged-in Internet Archive account** (401 anonymous)
and rate-limits **per account** — parallel workers all get 429. Sequential with
~8s spacing works.

**Parsers must have a prose fallback.** Some rosters are running text
("PGY-4 Georgios Alexopoulos, M.D. PGY-3 Jorge F. Urquiaga, M.D."), where
element-based extraction returns zero — indistinguishable from a program with
no residents, which is the worst possible failure mode.

**Never select a candidate record by the criterion you are about to test.**
A plausibility check that picked the NPI whose enumeration year best fit the
expectation, then tested that year, passed a department chair as a graduate.
Select on independent evidence and abstain when ambiguous.

**Validate candidate pages by CONTENT, not URL shape.** URL heuristics plateau
near 50% precision: `/residents/` is as often a portal, a research page or a
generic GME index as a roster.

**Scope announcement parsing to the specialty.** On shared medical-school
hosts, an unscoped crawl pulled otolaryngology faculty into a neurosurgery
"match" event.


## The Snyder case — why S3b and S0 exist

SLU's 2016-17 roster is absent from Wayback. It exists in Common Crawl at
`neurosurgery.slu.edu/index.php?page=residents`, and it lists **Doug Snyder,
MD, PGY-1** — a resident who left after one year and re-entered medicine in
another specialty.

He was invisible to every automated method built here:
- **Roster diff**: his only year sits in a Wayback gap.
- **NPPES switch detector**: his NPI carries only his *current* (ophthalmology)
  taxonomy, with no trace of the neurosurgery year.
- **Graduates list**: SLU's "Former Residents" page is linked but was never
  crawled by either archive.

He surfaced because a domain expert supplied the name, and was then confirmed
by an **employer bio** listing `Residency, 2017 Saint Louis University` — a
one-year stint — followed by an internship in 2019 and an ophthalmology
residency elsewhere through 2022.

Three lessons, all now encoded above:
1. The page had been **renamed** (`housestaff-2` -> `residents`), so tracking a
   single known path is insufficient; enumerate, and check a second archive.
2. Short-tenure departures are the events most likely to fall between captures,
   and they are exactly the events the study measures. Coverage gaps are not
   random with respect to the outcome.
3. The employer-bio reverse index is the only source that recorded this at all.
   It should be ranked higher than its position here suggests.
