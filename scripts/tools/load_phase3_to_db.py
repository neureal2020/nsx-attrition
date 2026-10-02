#!/usr/bin/env python3
"""Load verified phase-3 people (data/verify/phase3/merged_final.json) into db/neurosurgery_attrition.db.

    python3 scripts/tools/load_phase3_to_db.py

Fills `residents` and `outcomes` (replacing their contents), links roster_observations.resident_id by
program + surname + first-name prefix, and stores the 30-June-2025 cohort fields on outcomes.
Backup taken first: db/backup_pre_phase3_load_20261002.db
"""
import json, re, sqlite3, datetime, runpy, io, contextlib
DB = "db/neurosurgery_attrition.db"
merged = json.load(open("data/verify/phase3/merged_final.json"))
with contextlib.redirect_stdout(io.StringIO()):
    W = runpy.run_path("scripts/tools/window_analysis.py")
dest = W["dest"]
STATUS = {"completed": "graduated", "in_training": "in_training", "transferred": "transferred_out", "switched_specialty": "switched_specialty",
          "left_medicine": "left_medicine", "deceased": "deceased", "left_other": "attrition_unspecified",
          "left_destination_unknown": "attrition_unspecified", "unknown": "unknown", "not_a_resident": "unknown"}
CONF = {"gold": "confirmed", "silver": "probable", "program_only": "possible"}
db = sqlite3.connect(DB); c = db.cursor()
cols = {r[1] for r in c.execute("pragma table_info(outcomes)")}
for col in ("person_key TEXT", "entry_year INTEGER", "outcome_detail TEXT", "outcome_2025 TEXT", "attrition_2025 INTEGER"):
    if col.split()[0] not in cols:
        c.execute(f"alter table outcomes add column {col}")
c.execute("update roster_observations set resident_id = null")
c.execute("delete from outcomes"); c.execute("delete from residents")
def key(n):
    t = [x for x in re.sub(r"[^A-Za-z\- ]", " ", n).split() if x.upper() not in ("MD", "DO", "PHD", "MS", "MPH", "MBA", "JR", "SR", "II", "III", "DR")]
    return (t[-1].lower(), t[0][:3].lower()) if len(t) >= 2 else None
obs = {}
for oid, pid, nm in c.execute("select obs_id, program_id, name_as_listed from roster_observations").fetchall():
    k = key(nm)
    if k: obs.setdefault((pid,) + k, []).append(oid)
today = datetime.date.today().isoformat(); linked = 0
for p in merged:
    t = p["name"].split()
    c.execute("insert into residents(full_name, first_name, last_name, match_year, match_program_id, notes) values (?,?,?,?,?,?)",
              (p["name"], t[0] if t else None, t[-1] if t else None, p.get("entry_year"), p["program_id"], json.dumps(p.get("notes") or [])[:4000]))
    rid = c.lastrowid
    o = p["outcome"]
    d = dest(dict(key=p["key"], out=o, notes=p.get("notes") or [])) if o in ("switched_specialty", "left_medicine", "left_other", "left_destination_unknown", "unknown") else None
    ev = "; ".join(x for x in [p.get("gold_evidence"), p.get("gold_url")] if x) or None
    c.execute("""insert into outcomes(resident_id, status, last_seen_ay, last_seen_pgy, departure_ay, destination_specialty, confidence, evidence,
                 adjudicated_by, adjudicated_on, person_key, entry_year, outcome_detail, outcome_2025, attrition_2025) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
              (rid, STATUS.get(o, "unknown"), p.get("last_seen"), p.get("last_pgy"),
               p.get("last_seen") if o not in ("completed", "in_training") else None, d, CONF.get(p.get("evidence_level"), "unverified"), ev,
               "phase3_final_merge", today, p["key"], p.get("entry_year"), o, p.get("outcome_2025"), int(bool(p.get("attrition_2025")))))
    k = key(p["name"])
    for oid in obs.get((p["program_id"],) + k, []) if k else []:
        c.execute("update roster_observations set resident_id=? where obs_id=? and resident_id is null", (rid, oid)); linked += c.rowcount
db.commit()
print("residents", c.execute("select count(*) from residents").fetchone()[0], "outcomes", c.execute("select count(*) from outcomes").fetchone()[0],
      "observations linked", linked, "of", c.execute("select count(*) from roster_observations").fetchone()[0])
print(c.execute("select status, count(*) from outcomes group by 1 order by 2 desc").fetchall())
print(c.execute("select outcome_2025, count(*) from outcomes group by 1 order by 2 desc").fetchall())
