#!/usr/bin/env python3
"""Emit a per-resident verification worklist with ready-made lookup URLs.

    python3 scripts/19_build_worklist.py --program-id 60

US News blocks scripted fetches entirely (connection refused), so its data has
to come through a real browser. This writes a worklist to
data/intake/worklist_<program>.md with a prepared search URL per resident, and
a paste template that 20_ingest_usnews.py can read back.
"""
import argparse, sqlite3, sys, urllib.parse
sys.path.insert(0,"scripts")

ap=argparse.ArgumentParser()
ap.add_argument("--program-id",type=int,required=True)
ap.add_argument("--only-unresolved",action="store_true",
                help="skip residents whose outcome is already sourced")
a=ap.parse_args()

con=sqlite3.connect("db/neurosurgery_attrition.db"); con.execute("PRAGMA busy_timeout=60000")
prog=con.execute("SELECT name FROM programs WHERE program_id=?",(a.program_id,)).fetchone()[0]
names=[r[0] for r in con.execute("""SELECT DISTINCT name_as_listed FROM roster_observations
                                    WHERE program_id=? ORDER BY 1""",(a.program_id,))]
done={r[0] for r in con.execute("""SELECT resident_name FROM training_history
                                   WHERE program_id=? AND completed IN ('yes','no')""",(a.program_id,))}
rows=[]
for n in names:
    resolved = any(n.split()[-1].lower()==d.split()[-1].lower() for d in done)
    if a.only_unresolved and resolved: continue
    # US News' own search 500s on ?q= and otherwise fuzzy-matches within a sticky
    # location; profiles live at /doctors/<name>-<id>, so find them via site search
    q=urllib.parse.quote_plus(f'site:health.usnews.com/doctors "{n}" neurosurgeon')
    rows.append((n,resolved,
        f"https://www.google.com/search?q={q}",
        f"https://www.doximity.com/search?q={urllib.parse.quote_plus(n)}"))

out=f"data/intake/worklist_program{a.program_id}.md"
with open(out,"w") as f:
    f.write(f"# Verification worklist — {prog}\n\n")
    f.write(f"{len(rows)} residents. For each: open the US News link, find the\n")
    f.write("physician, copy the **Education & Experience** block, and paste it under\n")
    f.write("that resident's heading below. Leave the heading text exactly as-is.\n\n")
    f.write("Then run:  `python3 scripts/20_ingest_usnews.py --program-id "
            f"{a.program_id} --file {out}`\n\n---\n\n")
    for n,resolved,us,dox in rows:
        tag=" _(already sourced — recheck only if suspect)_" if resolved else ""
        f.write(f"## {n}{tag}\n")
        f.write(f"- US News: {us}\n- Doximity: {dox}\n\n```\n\n```\n\n")
print(f"wrote {out}  ({len(rows)} residents)")
con.close()
