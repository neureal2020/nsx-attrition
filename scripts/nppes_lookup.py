#!/usr/bin/env python3
"""Local NPPES lookup: name -> specialty signal + approximate cohort year.

Runs against db/nppes.db (built by 08_load_nppes.py from the monthly bulk file).
No rate limits, and the snapshot date is fixed, so any result is reproducible.

TWO THINGS THIS GETS RIGHT THAT A NAIVE LOOKUP DOES NOT
-------------------------------------------------------
1. THE TRAINEE TAXONOMY IS NOT A SPECIALTY.
   390200000X = "Student in an Organized Health Care Education/Training
   Program". 254,349 individuals in the file carry ONLY that code, including
   practising neurosurgeons who never updated their record (verified: Doris
   Wang, UCSF). Treating it as "some other specialty" would generate a quarter
   of a million false specialty-switch signals. It means UNKNOWN.

2. ENUMERATION DATE RECOVERS THE COHORT YEAR.
   NPIs are issued at medical-school graduation, so enumeration clusters in
   late March-early May (Match Day season). Verified against the UCSF roster:
   Englot 2009, Zygourakis 2010, Rolston/Southwell 2011, Rutkowski/Breshears/
   Osorio 2012, Magill/Lau/Winkler 2013, Safaee 2014, Raygor 2015 -- a clean
   cohort ladder. This is an independent cohort-year signal for nearly every
   US physician, and it disambiguates common names (there are 41 "John Burke"s).
"""
import sqlite3, re, os

DB=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","db","nppes.db")
TRAINEE="390200000X"
NEURO="207T"

def _con():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c

def _surname_variants(last):
    """Compound surnames are written inconsistently across sources.

    A roster may print 'McClung-Smith' while NPPES stores 'MCCLUNG SMITH'
    (space) -- which silently loses the person. Real case: Catherine McClung
    Smith, a practising neurosurgeon, was returned as 'not_found' until this
    was handled. Generate hyphen/space/joined variants of the surname.
    """
    last=(last or "").strip()
    v={last}
    if "-" in last:
        v.add(last.replace("-"," ")); v.add(last.replace("-",""))
        v.update(p for p in last.split("-") if len(p)>2)
    if " " in last:
        v.add(last.replace(" ","-")); v.add(last.replace(" ",""))
        v.update(p for p in last.split() if len(p)>2)
    return sorted(v)


def lookup(first, last, cohort_year=None, state=None, con=None):
    """Return candidate provider rows, matching legal AND former names,
    across hyphen/space variants of compound surnames."""
    own = con is None
    con = con or _con()
    fp = (first or "")[:4]+"%"
    variants=_surname_variants(last)
    ph=",".join("?"*len(variants))
    rows = con.execute(f"""
        SELECT *, 0 AS via_other FROM providers
         WHERE last COLLATE NOCASE IN ({ph}) AND first LIKE ? COLLATE NOCASE
        UNION ALL
        SELECT *, 1 AS via_other FROM providers
         WHERE other_last COLLATE NOCASE IN ({ph}) AND other_first LIKE ? COLLATE NOCASE
    """, variants+[fp]+variants+[fp]).fetchall()
    out=[]
    for r in rows:
        d=dict(r)
        d["enum_year"]=int(r["enum_date"][-4:]) if r["enum_date"] else None
        d["cohort_delta"]=(abs(d["enum_year"]-cohort_year)
                           if (cohort_year and d["enum_year"]) else None)
        out.append(d)
    # prefer: cohort-year agreement, then neurosurgery, then active
    out.sort(key=lambda d:(d["cohort_delta"] if d["cohort_delta"] is not None else 99,
                           -d["is_neurosurg"], d["deact_date"]!=""))
    if own: con.close()
    return out

def classify(cands):
    """Collapse candidates into one specialty signal.

    Returns signal in:
      in_neurosurgery | other_specialty | trainee_only | not_found
    plus an `ambiguous` flag when the name is too common to resolve safely.
    """
    if not cands:
        return {"signal":"not_found","confidence":"unverified",
                "detail":None,"n_candidates":0,"ambiguous":False}
    ns=[c for c in cands if c["is_neurosurg"]]
    if ns:
        best=ns[0]
        return {"signal":"in_neurosurgery","confidence":"probable",
                "detail":best["tax_all"],"npi":best["npi"],
                "enum_year":best["enum_year"],"state":best["state"],
                "via_former_name":bool(best["via_other"]),
                "n_candidates":len(cands),"ambiguous":len(cands)>6}
    # no neurosurgery code anywhere -> is there a REAL other specialty?
    real=[c for c in cands
          if [t for t in (c["tax_all"] or "").split(",") if t and t!=TRAINEE]]
    if not real:
        return {"signal":"trainee_only","confidence":"unverified",
                "detail":TRAINEE,"npi":cands[0]["npi"],
                "enum_year":cands[0]["enum_year"],
                "n_candidates":len(cands),"ambiguous":len(cands)>6,
                "note":"trainee taxonomy only -- NOT evidence of a specialty switch"}
    best=real[0]
    return {"signal":"other_specialty","confidence":"probable",
            "detail":best["tax_all"],"npi":best["npi"],
            "enum_year":best["enum_year"],"state":best["state"],
            "n_candidates":len(cands),"ambiguous":len(cands)>6}

if __name__=="__main__":
    ucsf=[("John","Burke"),("Jonathan","Breshears"),("Tene","Cage"),("Andrew","Chan"),
    ("Dario","Englot"),("Seunggu","Han"),("Darryl","Lau"),("Taemin","Oh"),("Stephen","Magill"),
    ("Joseph","Osorio"),("Kunal","Raygor"),("John","Rolston"),("Martin","Rutkowski"),
    ("Caleb","Rutledge"),("Michael","Safaee"),("Derek","Southwell"),("Doris","Wang"),
    ("Ethan","Winkler"),("Corinna","Zygourakis")]
    con=_con(); tally={}
    for f,l in ucsf:
        k=classify(lookup(f,l,con=con))
        tally[k["signal"]]=tally.get(k["signal"],0)+1
        flags=[]
        if k.get("ambiguous"): flags.append(f"AMBIGUOUS n={k['n_candidates']}")
        if k.get("via_former_name"): flags.append("via-former-name")
        if k.get("note"): flags.append(k["note"])
        print(f"  {f+' '+l:22s} {k['signal']:17s} enum={k.get('enum_year')}  {' | '.join(flags)}")
    print("\n  ",tally)
