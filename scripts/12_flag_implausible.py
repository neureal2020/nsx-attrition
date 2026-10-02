#!/usr/bin/env python3
"""Flag people in cohort events whose NPI enumeration year is inconsistent with
the event -- i.e. almost certainly faculty quoted in the announcement, not
members of the cohort.

Department chairs and senior faculty are named in these posts ("Dr. Zipfel
said...") and parse as cohort members. They are not program directors, so the
ACGME PD list does not catch them. But enumeration year does: an NPI is issued
around medical-school graduation, so

    match event in year Y      -> expect enumeration ~= Y      (+/- 2)
    graduation event in year Y -> expect enumeration ~= Y - 7  (+/- 3)

A chair enumerated in 2003 appearing in a 2021 graduation post fails by ~11
years. Flagged rather than deleted: the raw observation is preserved and the
judgement is recorded separately, per the observation/inference split.
"""
import sqlite3, sys
sys.path.insert(0,"scripts")
from nppes_lookup import lookup, _con as nppes_con
from entity_resolution import split_name

DB="db/neurosurgery_attrition.db"
RESIDENCY_YEARS=7
TOL={"match":2,"graduation":3}

con=sqlite3.connect(DB); con.execute("PRAGMA busy_timeout=60000"); cur=con.cursor()
for col,typ in [("npi","TEXT"),("npi_enum_year","INTEGER"),
                ("expected_enum_year","INTEGER"),("enum_delta","INTEGER"),
                ("plausible","TEXT")]:
    try: cur.execute(f"ALTER TABLE cohort_event_people ADD COLUMN {col} {typ}")
    except sqlite3.OperationalError: pass
con.commit()

rows=cur.execute("""SELECT p.cep_id,p.name_as_listed,e.event_type,e.event_year
                    FROM cohort_event_people p JOIN cohort_events e USING(event_id)""").fetchall()
nc=nppes_con(); updates=[]
for cep,name,etype,eyear in rows:
    f,m,l=split_name(name)
    if not f or not l:
        updates.append((None,None,None,None,"unparsed_name",cep)); continue
    cands=lookup(f,l,con=nc)
    if not cands:
        updates.append((None,None,None,None,"no_npi",cep)); continue
    if not eyear:
        best=cands[0]
        updates.append((best["npi"],best["enum_year"],None,None,"no_event_year",cep)); continue
    expected = eyear if etype=="match" else eyear-RESIDENCY_YEARS
    tol=TOL.get(etype,3)
    scored=[c for c in cands if c["enum_year"]]
    if not scored:
        updates.append((cands[0]["npi"],None,expected,None,"no_enum_date",cep)); continue

    # CRITICAL: do NOT choose the candidate closest to the expected year. That
    # is circular -- it selects the record that makes the person look plausible
    # and then tests plausibility on it, so any common name passes. (It let the
    # Minnesota chair through as a 2018 graduate.) Select on evidence that is
    # independent of the hypothesis: prefer a neurosurgery taxonomy, and only
    # rule at all when the name resolves unambiguously.
    ns=[c for c in scored if c["is_neurosurg"]]
    pool = ns if ns else scored
    if len(pool)>2:
        yrs=sorted({c["enum_year"] for c in pool})
        updates.append((None,None,expected,None,
                        f"ambiguous_npi_n{len(pool)}_{yrs[0]}-{yrs[-1]}",cep)); continue
    best=min(pool,key=lambda c:c["enum_year"])      # earliest = first NPI issued
    d=best["enum_year"]-expected
    verdict="plausible" if abs(d)<=tol else ("too_senior" if d<0 else "too_junior")
    updates.append((best["npi"],best["enum_year"],expected,d,verdict,cep))
nc.close()

cur.executemany("""UPDATE cohort_event_people
   SET npi=?, npi_enum_year=?, expected_enum_year=?, enum_delta=?, plausible=?
   WHERE cep_id=?""",updates)
con.commit()
print("=== plausibility verdicts ===")
for v,n in cur.execute("SELECT plausible,COUNT(*) FROM cohort_event_people GROUP BY 1 ORDER BY 2 DESC"):
    print(f"  {str(v):16s} {n}")
print("\n=== flagged as too senior (expected: chairs/faculty) ===")
for r in cur.execute("""SELECT p.name_as_listed,e.event_type,e.event_year,p.npi_enum_year,p.enum_delta
                        FROM cohort_event_people p JOIN cohort_events e USING(event_id)
                        WHERE p.plausible='too_senior' ORDER BY p.enum_delta LIMIT 12"""):
    print(f"  {r[0]:24s} {r[1]:10s} event={r[2]}  enumerated={r[3]}  off by {r[4]:+d}y")
print("\n=== kept as plausible ===")
for r in cur.execute("""SELECT p.name_as_listed,e.event_type,e.event_year,p.npi_enum_year
                        FROM cohort_event_people p JOIN cohort_events e USING(event_id)
                        WHERE p.plausible='plausible' LIMIT 10"""):
    print(f"  {r[0]:24s} {r[1]:10s} event={r[2]}  enumerated={r[3]}")
con.close()
