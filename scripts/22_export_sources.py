#!/usr/bin/env python3
"""Write a verifiable source list for one program (or all loaded programs).

    python3 scripts/22_export_sources.py --program-id 120
    python3 scripts/22_export_sources.py --all

Output: docs/sources/program_<id>.md -- every roster capture (with its Wayback
or live URL, date, academic year, head-count, and whether it was OBSERVED or
RECONSTRUCTED), the program-side graduation sources, and every departure /
transfer / joiner with the evidence URL and the note recorded at the time.
Generated from the database, so re-run after any change.
"""
import argparse, os, sqlite3, re, collections

ap = argparse.ArgumentParser()
ap.add_argument("--program-id", type=int)
ap.add_argument("--all", action="store_true")
a = ap.parse_args()
con = sqlite3.connect("db/neurosurgery_attrition.db")
os.makedirs("docs/sources", exist_ok=True)

def one(pid):
    name = con.execute("SELECT name FROM programs WHERE program_id=?", (pid,)).fetchone()[0]
    name = re.sub(r"\s*©.*$", "", name)
    L = [f"# Sources — {name} (program {pid})", "",
         "Every claim below links to the page it came from. Wayback links open the exact capture used.",
         "RECONSTRUCTED rows were not listed on any page for that year; the note says what they were inferred from.", ""]
    L += ["## Rosters by academic year", "",
          "| Academic year | Type | Captured | Residents | Reconstructed | Source | Note |", "|---|---|---|---|---|---|---|"]
    for ay, st, cap, url, note, n, rec in con.execute("""
        SELECT s.academic_year, s.source_type, s.captured_at, s.source_url, COALESCE(s.notes,''),
               COUNT(o.obs_id), SUM(o.role='reconstructed')
        FROM roster_snapshots s LEFT JOIN roster_observations o USING(snapshot_id)
        WHERE s.program_id=? GROUP BY s.snapshot_id ORDER BY s.academic_year, s.captured_at""", (pid,)):
        link = url if url.startswith("http") else f"`{url}`"
        kind = "reconstructed" if st == "manual" else st
        L.append(f"| {ay} | {kind} | {cap} | {n} | {rec or 0} | {link} | {note.replace('|','/')[:160]} |")
    L += ["", "## Program-side graduation lists", ""]
    for url, cnt, lo, hi in con.execute("""SELECT source_url, COUNT(*), MIN(end_year), MAX(end_year) FROM training_history
        WHERE program_id=? AND source_type='program_page' AND completed='yes' AND source_url LIKE 'http%'
        GROUP BY source_url""", (pid,)):
        L.append(f"- {url} — {cnt} graduates, {lo}–{hi}")
    L += ["", "## Departures, transfers and mid-program joiners", "",
          "| Resident | Years | Completed here | Departure type | Evidence | Source |", "|---|---|---|---|---|---|"]
    rows = con.execute("""SELECT resident_name, start_year, end_year, completed, COALESCE(departure_type,''),
        COALESCE(notes,''), COALESCE(source_url,'') FROM training_history
        WHERE program_id=? AND (completed IN ('no','unknown') OR completed IS NULL OR notes LIKE '%TRANSFER%'
              OR notes LIKE '%JOINED%' OR notes LIKE '%not a%entrant%') AND source_type!='program_page'
        ORDER BY start_year, resident_name""", (pid,)).fetchall()
    for n, s, e, c, d, note, url in rows:
        L.append(f"| {n} | {s or '?'}–{e or '?'} | {c or 'in training'} | {d} | {note.replace('|','/')} | {url or '(see note)'} |")
    L += ["", "## Graduate verification (US News / Doximity / bios)", ""]
    for n, s, e, url, note in con.execute("""SELECT resident_name, start_year, end_year, COALESCE(source_url,''), COALESCE(notes,'')
        FROM training_history WHERE program_id=? AND completed='yes' AND source_type!='program_page'
        ORDER BY start_year, resident_name""", (pid,)):
        L.append(f"- {n} ({s}–{e}): {note} {url}")
    path = f"docs/sources/program_{pid}.md"
    open(path, "w").write("\n".join(L) + "\n")
    print("wrote", path)

pids = [r[0] for r in con.execute("SELECT DISTINCT program_id FROM roster_snapshots ORDER BY 1")] if a.all else [a.program_id]
for p in pids: one(p)
