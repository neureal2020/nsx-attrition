# Neurosurgery Residency Attrition Database — Methodology

**Status:** in development. Started 2026-09-23.
**Scope:** US ACGME-accredited neurological surgery residency programs, match years 2012–2026.

---

## 1. Study design problem

Attrition is measured as: *matched into a program, did not complete that program.*
That requires three things, and they need **three independent sources**:

| Need | Source | Why this source |
|---|---|---|
| Who **started** | Match Day / "new residents" announcements | Dated news posts; not rewritten later |
| Who was **present**, year by year | Archived roster pages (Wayback) | Only source with annual granularity |
| Who **finished** | Alumni pages, graduation announcements, ABNS | Published by program/board at completion |

### 1.1 Why the roster page cannot establish who started

**A program rewrites its roster page when a resident leaves.** So the current
roster only shows survivors. Even using archived rosters, Wayback samples a
site roughly once or twice a year — a resident who matched in July and was
removed by the following spring may appear in **no snapshot at all**.

That missingness is **not random**. It is biased toward short-tenure
departures, which are precisely the events this study measures. Relying on
rosters alone would systematically *undercount* attrition, and the bias would
run in the direction of the conclusion.

Hence `cohort_events` (entry/exit announcements) is a first-class table,
independent of `roster_observations`.

Worked example (Univ. of Pittsburgh, both retrieved from Wayback):
- **Entry**, dated 2020-03-20: *"medical students who matched into the
  University of Pittsburgh Department of Neurological Surgery residency
  program"* — 4 named, each with medical school.
- **Exit**, dated 2022-06-19: *"2022 graduating residents … on their successful
  completion of the … seven-year neurological surgery residency program"* —
  4 named, each with fellowship destination.

### 1.2 Cohort maturity

Neurosurgery residency is 7 years; attrition is ~10–17% cumulative and
concentrated in PGY 1–3. Therefore:

- **2012–2019 match years** — mature cohorts; these carry the findings.
- **2020–2026** — prospective registry only. No attrition conclusions.

A 2025–2026-only database would have a denominator with essentially no events.

---

## 2. Program list (complete)

**Authoritative source:** ACGME ADS *public* report "List of Programs by
Specialty" (`apps.acgme.org/ads/Public/Reports/Report/1`, specialty code 160),
which returns a PDF carrying the 10-digit ACGME program ID, program director,
address, accreditation status and effective date.

- **124 US programs**, AY 2026–2027.
- The ADS *Advanced Program Search* is reCAPTCHA-protected and was deliberately
  **not** used; the public report is a cleaner source and needs no login.
- The AANS residency directory (158 entries: 120 US, 15 CA, 23 MX) is a
  convenience directory only — it was missing 4 US programs and carries some
  stale/generic URLs. It is joined in for website URLs; non-US rows are parked
  in `programs_aans_only` (out of scope for an ACGME denominator).

Also public and needed for historical work, since the set of programs changes
over a 14-year window: Report/7 (withdrawn programs) and Report/8 (newly
accredited).

---

## 3. Handling URL and domain changes

Wayback indexes by **URL, not institution**, so a program that moved hosts
between 2012 and 2026 is invisible from its current URL alone.

1. **Multi-seed** — ACGME program-director email domain, AANS host, and
   `neurosurgery.<domain>` patterns.
2. **Subdomain moves** (`neurosurgery.x.edu` → `x.edu/neurosurgery`) — caught by
   enumerating the department subdomain plus path-prefix queries on the apex.
3. **Cross-domain rebrands** (`thebarrow.org` → `barrowneuro.org`; Lifespan →
   Brown University Health) — **cannot be guessed.** These surface as holes in
   the per-program/per-year coverage matrix and are seeded by hand.

**Rule: a program-year with no snapshot is recorded as MISSING DATA, never as
attrition.** Otherwise every domain migration manufactures a phantom cohort of
residents who "vanished". This is why `roster_observations` (what a source
literally said, with a date) is stored separately from `outcomes` (what we
inferred).

---

## 4. Pipeline performance notes

- The Wayback CDX API **throttles hard** under sustained load: a query measured
  at 5s cold took 37s once a few hundred were in flight. Broad enumeration
  (2,207 queries) projected to ~6 hours and was abandoned.
- **Inverted approach:** discover roster URLs on the **live** sites (124
  programs in ~45s, unthrottled), then spend a small Wayback budget on targeted
  per-URL history queries.
- Candidate URLs are validated **by content, not by URL shape**. URL heuristics
  plateaued near 50% precision (`/residents/` is as often a resident *portal*,
  *research* page or generic GME index as a roster). The reliable test is to
  fetch the page and check whether a parser extracts names.

---

## 5. Roster parsing

Built against real pages sampled 2009–2018:
- **PGY is frequently absent** (e.g. UCSF lists names only) → PGY is optional
  and cohort is inferred from first appearance. Requiring PGY would silently
  drop whole programs.
- PGY appears as Roman (`PGY VII`), Arabic (`PGY-3`), or `R1..R7` / `Chief`.
- Names split across sibling DOM nodes (`George Galvan` + `, M.D.`) → parse
  element text, not flattened page text.
- Site chrome is removed structurally *and* by a link-density heuristic
  (nav is link-dense; content is not).

### 5.1 Announcement parsing

Match Day and graduation posts state names in running prose, not in list
elements, so they are matched on a name-followed-by-degree pattern
(`Matthew Pease, MD`), which is very high precision in this genre.

Two traps found in real posts:
- **`Graduate School:` is a field label inside Match Day posts**, so a bare
  `\bgraduat` cue misclassifies every match announcement as a graduation.
  Graduation cues must be explicit (`graduating resident`, `successful
  completion`, `resident graduates`).
- A post names people beyond the cohort (faculty, award winners). Recording
  each name's **character distance from the classifying cue** separates them
  cleanly: in the Pitt 2022 post the four graduates sit at distance 205–262 and
  the five incidental mentions at 1108+.

---

## 6. Outcome adjudication

| Signal | Source | Strength |
|---|---|---|
| Board certification | ABNS | Strongest completion evidence |
| Named in graduation announcement | Program news | Strong |
| On alumni / "former residents" page | Program site | Strong |
| NPI taxonomy = Neurological Surgery | NPPES API | Corroborating |
| NPI taxonomy = another specialty | NPPES API | Strong switch signal |
| No NPI found | NPPES API | **Weak** — see below |

**NPI caveats.** An NPI is issued to medical *students* and residents, so its
existence says nothing about completing training; only taxonomy is informative,
and trainees often carry taxonomy `390200000X` ("Student in an Organized Health
Care Education/Training Program") long after finishing. Absence of an NPI is
equally consistent with a name change on marriage, a spelling variant, or
leaving the US — it is never on its own sufficient to conclude "left medicine."

### 6.1 Reverse index: practicing neurosurgeons' bios

The strongest completion evidence available at scale is the **employer-published
bio of a practicing neurosurgeon**, which routinely states where and *when* they
trained. Verified example (Vanderbilt, retrieved 2026-09-23):

> "Residency and Fellowship: 2010-2016 - Resident, Department of Neurological
> Surgery, University of California, San Francisco"

That subject was independently parsed out of the archived **UCSF 2015 roster**,
closing the chain: roster presence -> employer bio -> completion, with years.

This is powerful because the source is a *third party* (the hiring institution),
not the training program, so it is not rewritten when a resident leaves. Building
this as a reverse index — scrape department/hospital faculty bios across the
field, extract `(person, residency program, years)` — yields an independent
completion register covering anyone who stayed in US practice.

Its blind spot is the mirror image of the roster's: it only sees people who are
*currently practicing and findable*. Someone who finished and left clinical
practice looks the same as someone who never finished. So it corroborates
completion; it cannot establish attrition on its own.

### 6.1b NPPES bulk file — the second independent source

The monthly CMS bulk file (1.08 GB zip, 11.7 GB CSV, streamed from the archive
rather than extracted) yields a local index: **7,471,371 individual providers,
9,186 carrying neurological surgery taxonomy (207T), 485,378 with a recorded
former/other name.** The API cannot substitute — it caps responses at 200 and
will not page past ~1000, so it cannot enumerate a specialty.

Three capabilities, each verified against the archived UCSF 2015 roster:

**Specialty switch detection.** Current taxonomy for a matched name.
18 of the 19 parsed UCSF residents were located; 17 confirmed in neurosurgery.

**Former and maiden names** (main file cols 13-19, with a type code:
342,361 type-1 "former name", 58,418 type-2 "professional name"). This is the
authoritative fix for the surname-change bias in section 9 — a resident who
matched under one surname and practises under another is linkable here instead
of being scored as attrition.

**Enumeration date recovers the cohort year.** NPIs are issued at medical-school
graduation, so enumeration clusters in late March-early May (Match Day season).
Against the UCSF roster this reproduced a clean cohort ladder — Englot 2009,
Zygourakis 2010, Rolston/Southwell 2011, Rutkowski/Breshears/Osorio 2012,
Magill/Lau/Winkler 2013, Safaee 2014, Raygor 2015. It is an independent
cohort-year signal for nearly every US physician and is essential for
disambiguating common names (the file holds 41 "John Burke"s).

**Trap, found the hard way.** Taxonomy `390200000X` = "Student in an Organized
Health Care Education/Training Program". **254,349 individuals carry ONLY that
code**, including practising neurosurgeons who never updated their record
(verified: Doris Wang, UCSF). Classifying it as "some other specialty" would
manufacture a quarter of a million false specialty-switch signals. It means
UNKNOWN and is reported as `trainee_only`.

### 6.2 Board certification — no public source

**ABNS has no public diplomate lookup.** `abns.org/content/diplomates` is about
the Primary Exam, not a directory, and there is no search endpoint. ABMS
*Certification Matters* (`certificationmatters.org`) returns HTTP 403 to
scripted requests. The Lynch et al. (2015) study used the printed *ABNS
Directory of Diplomates*.

Consequence: board certification — the single cleanest completion signal —
**cannot be automated from public endpoints.** Options: a browser session
against Certification Matters, per-state medical board licensure lookups, or
"board certified" statements harvested from the bios in 6.1.

### 6.3 Medical school Match Day lists — partial

Match lists published by the *sending* medical school are attractive as an entry
source (third-party, dated March, never scrubbed by the program). Coverage is
uneven: some schools publish named lists, but many publish **counts only**
(e.g. UToledo 2019 reports "Neurological Surgery: 2" with no names). Usable as a
supplementary entry source, not a complete one.

---

## 7. Sources deliberately NOT used as primary

- **Instagram** — ToS-hostile, non-reproducible, biased toward programs with
  active accounts, absent before ~2015, and invites collecting personal/health
  detail that does not belong in a research dataset. Retained only as
  last-resort *manual verification* of a specific ambiguous case.
- **ACGME ADS Advanced Program Search** — reCAPTCHA-protected. The public
  Reports endpoint supplies the same data.

---

## 8. Ethics / governance

The dataset contains **named real individuals** and a career outcome that can
be sensitive. Before any analysis leaves this machine:

- Seek IRB review. Published precedent (e.g. Lynch et al., *J Neurosurg* 2015)
  treats this as exempt human-subjects research on public data, but that is the
  IRB's call, not ours.
- Restrict to **publicly available** sources.
- **Do not record or infer a reason for departure.** Record only that a
  departure occurred and, where independently documented, the destination.
- Report aggregate rates; do not publish individual-level attrition.


---

## 10. Worked example: SLU (program 60), the first vertical slice

Chosen as a single-program proof. It broke several assumptions at once and is
therefore a good template for what the other 123 will require.

**Four hostnames in fourteen years.** `neurosurgery.slu.edu` (2012-2017, a
Department), then `slu.edu/medicine/neurological-surgery/` (2017-2026), with
`refresh.slu.edu` serving the live roster and the current site nesting the unit
at `/medicine/surgery/neurological-surgery/` as a Division. The AANS-recorded
URL 404s and was never archived at all.

**Archive coverage is the binding constraint, not parsing.**
- 2012-2014: roster archived at `index.php?page=housestaff-2` (names, no PGY)
- 2015-2019: **no roster page archived under any hostname.** The pages existed;
  Wayback did not crawl them. Checked and excluded: `?page=neurosurgery-residency`
  (program description), the 2019 `residency.php` (call schedules), all 47
  `?page=` values, and all 27 archived news articles (none are match or
  graduation posts).
- 2020-2026: roster archived with PGY labels, 14 snapshots.

**Result:** 4 completions, 7 in training, 2 departure candidates, and 9 people
from 2012-2014 correctly left unclassified because the trail dies in the gap.

Of the two departure candidates, one (Cleary, PGY-5, now neurosurgery-taxonomy
in Virginia) reads as a transfer; the other (Alexopoulos, last seen PGY-6, now
neurosurgery-taxonomy in Missouri) is a **confirmed non-completion**: a
program-side report says he trained 2018-2024, never reached PGY-7, and did not
graduate. His Doximity profile lists the same 2018-2024 span, which reads like a
normal residency but is one year short of the 7 years required after 2014.
Neither roster absence nor NPPES taxonomy settles a case like this; the
program-side report does.

### 10.1 Left-censoring

Entry years for 2014-2019 are recoverable from PGY observed in 2020
(`entry = academic_year_start - (PGY - 1)`), which reaches back to 2014 without
any archived roster for those years. But this only sees people who **survived
to a captured year**. Anyone who entered 2015-2019 and left before the 2020
capture appears nowhere.

Those cohorts are therefore **left-censored and must be reported as such, never
as a rate.** Only cohorts whose whole span is covered by snapshots give an
honest denominator — for SLU, 2020 onward.

### 10.2 Two independent cohort-year signals disagree for IMGs

Reconstructed entry year (from PGY) and NPI enumeration year agree for US
graduates (Khan 2015/2015, Prim 2015/2015, Cleary 2017/2017, Quadri 2019/2019)
but diverge for international graduates (Alexopoulos 2018/2016, Kandel
2018/2016, Urquiaga 2019/2017). NPIs are issued at US medical-school
graduation; an IMG's enumeration tracks US entry, not residency start, and
dedicated research years shift the PGY-derived estimate later. Neither signal
is authoritative alone, and the disagreement is itself informative.
