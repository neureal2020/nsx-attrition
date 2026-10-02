# Deep pass: residents whose outcome is still "unknown"

Each input person already had a phase-3 check (see `phase3_finding`: what was found, sources). Your job is to resolve WHERE THEY WENT or confirm they completed. Rules, output format and Chrome rules are the same as `docs/AGENT_BRIEF_PHASE3.md` (read it), EXCEPT:
- **US News is off**: record `"usnews": "deferred"`; do not open health.usnews.com.
- Budget: up to 8 web searches per person.
- Search ideas beyond name + neurosurgery: `"<name>" resident` + other specialties (radiology, neurology, anesthesiology, emergency medicine, psychiatry, PM&R, general surgery, ortho, radiation oncology, pathology, family/internal medicine); `"<name>" match` / "matched" with the departure year; the name with the destination-program resident roster pages; `"<name>" MD` + the city; `"<name>" MD PhD` + industry/biotech/consulting; name variants (middle name, hyphenated or maiden surname); PubMed author affiliations after the departure year (use as supporting evidence only).
- Doximity in Chrome for every plausible profile found (verify URL + name on the page).
- Output: `data/verify/phase3/deep/d_<NN>_out.json`, same object format as phase 3, plus `"deep_searches": n`.
- Never guess: if still unresolved, `outcome: "unknown"` with a one-line note of what was tried. Record only training/career facts (no personal-life details).
