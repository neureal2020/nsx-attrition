#!/usr/bin/env python3
"""Rebuild `programs` with the ACGME list as the authoritative spine (124 US
programs, each with its 10-digit ACGME ID), joining in website URLs from the
AANS directory. AANS is a convenience directory and is incomplete/stale; ACGME
is the accreditation record. Non-US (Canada/Mexico) AANS entries are retained
separately since they are out of scope for an ACGME attrition denominator.
"""
import sqlite3, csv, re, difflib, json

DB="db/neurosurgery_attrition.db"
con=sqlite3.connect(DB)
con.execute('PRAGMA busy_timeout=60000'); cur=con.cursor()

aans=cur.execute("SELECT name,city,state,country,website FROM programs").fetchall()
acgme=list(csv.DictReader(open("data/processed/acgme_neurosurgery_programs.csv")))

STOP=re.compile(r"\b(program|the|of|at|and|medical|center|centre|hospital|health|system|"
                r"college|university|school|medicine|consortium|institute|inc)\b")
def norm(s):
    s=re.sub(r"[^a-z0-9 ]"," ",(s or "").lower())
    s=STOP.sub(" ",s)
    return " ".join(s.split())

# index AANS by state for scoped fuzzy matching
by_state={}
for n,c,st,co,w in aans:
    if co=="US": by_state.setdefault(st,[]).append((n,c,w))

matches, unmatched = {}, []
for a in acgme:
    st, cands = a["state"], by_state.get(a["state"], [])
    target=norm(a["program_name"]+" "+a["institution"])
    best, score = None, 0.0
    for n,c,w in cands:
        s=difflib.SequenceMatcher(None, target, norm(n)).ratio()
        if c and a["city"] and c.lower().strip()==a["city"].lower().strip(): s+=0.25
        tok_a, tok_b = set(norm(n).split()), set(target.split())
        if tok_a and tok_b: s += 0.30*len(tok_a&tok_b)/len(tok_a|tok_b)
        if s>score: best, score = (n,c,w), s
    if best and score>=0.55: matches[a["acgme_id"]]=(best,score)
    else: unmatched.append((a,best,score))

cur.execute("DROP TABLE IF EXISTS programs_aans_only")
cur.execute("""CREATE TABLE programs_aans_only AS
               SELECT name,city,state,country,website FROM programs WHERE country<>'US'""")
cur.execute("DELETE FROM programs")
# sqlite_sequence exists only when a table uses AUTOINCREMENT
try: cur.execute("DELETE FROM sqlite_sequence WHERE name='programs'")
except sqlite3.OperationalError: pass

for a in acgme:
    m=matches.get(a["acgme_id"])
    web = m[0][2] if m else None
    cur.execute("""INSERT INTO programs
        (name,city,state,country,acgme_id,website,active,source,notes)
        VALUES (?,?,?,?,?,?,1,'ACGME Report/1 AY2026-2027 (2026-09-23)',?)""",
        (a["program_name"], a["city"], a["state"], "US", a["acgme_id"], web,
         json.dumps({"institution":a["institution"],"director":a["program_director"],
                     "status":a["accreditation_status"],"effective":a["effective_date"],
                     "email":a["email"],"aans_match_score":round(m[1],3) if m else None})))
con.commit()

tot=cur.execute("SELECT COUNT(*) FROM programs").fetchone()[0]
web=cur.execute("SELECT COUNT(*) FROM programs WHERE website IS NOT NULL AND website<>''").fetchone()[0]
print(f"programs (US, ACGME-authoritative): {tot}")
print(f"  with an AANS website URL: {web}")
print(f"  needing a website found:  {tot-web}")
print(f"\nACGME programs with no AANS counterpart ({len(unmatched)}):")
for a,b,s in unmatched:
    print(f"   {a['acgme_id']}  {a['program_name'][:46]:48s} {a['city']}, {a['state']}   best={s:.2f}")
print("\nNon-US AANS entries parked in programs_aans_only:",
      cur.execute("SELECT COUNT(*) FROM programs_aans_only").fetchone()[0])
con.close()
