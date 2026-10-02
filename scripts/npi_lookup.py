#!/usr/bin/env python3
"""NPPES NPI Registry lookup — the workhorse for adjudicating what happened to
a resident who left a roster.

Interpretation rules (and their limits):
  * taxonomy 'Neurological Surgery'  -> stayed in the specialty
  * taxonomy = another clinical specialty -> SWITCHED SPECIALTY (strong signal)
  * taxonomy 'Student in an Organized Health Care Education/Training Program'
    (390200000X) -> still a trainee at the time of enumeration; NOT graduation
  * no NPI found -> weak evidence only. Never sufficient on its own to conclude
    'left medicine': it is equally consistent with a name change (marriage),
    a name spelling variant, or a non-US move.

IMPORTANT: an NPI is issued to medical students and residents, so the mere
existence of an NPI says nothing about completing training. Only the taxonomy
and its update history are informative. Board certification (ABNS) is the
clean completion signal; this is the corroborating one.
"""
import json, time, urllib.parse, urllib.request, unicodedata, re

API="https://npiregistry.cms.hhs.gov/api/"
TRAINEE_CODE="390200000X"

def _norm(s):
    s=unicodedata.normalize("NFKD",s or "").encode("ascii","ignore").decode()
    return re.sub(r"[^a-z]","",s.lower())

def query(first=None,last=None,state=None,taxonomy=None,limit=50,enumeration_type="NPI-1"):
    p={"version":"2.1","limit":limit}
    if enumeration_type: p["enumeration_type"]=enumeration_type
    if first: p["first_name"]=first
    if last: p["last_name"]=last
    if state: p["state"]=state
    if taxonomy: p["taxonomy_description"]=taxonomy
    url=API+"?"+urllib.parse.urlencode(p)
    for a in range(3):
        try:
            with urllib.request.urlopen(url,timeout=45) as r: return json.load(r)
        except Exception:
            if a==2: return {"result_count":0,"results":[],"_error":True}
            time.sleep(2**a)
    return {"result_count":0,"results":[]}

def summarize(rec):
    b=rec.get("basic",{}) or {}
    taxes=rec.get("taxonomies",[]) or []
    primary=next((t for t in taxes if t.get("primary")), taxes[0] if taxes else {})
    return {
        "npi": rec.get("number"),
        "first": b.get("first_name"), "last": b.get("last_name"),
        "middle": b.get("middle_name"), "credential": b.get("credential"),
        "sole_prop": b.get("sole_proprietor"),
        "enumeration_date": b.get("enumeration_date"),
        "last_updated": b.get("last_updated"),
        "primary_taxonomy": primary.get("desc"),
        "primary_code": primary.get("code"),
        "all_taxonomies": sorted({t.get("desc") for t in taxes if t.get("desc")}),
        "is_trainee_taxonomy": any(t.get("code")==TRAINEE_CODE for t in taxes),
        "states": sorted({a.get("state") for a in (rec.get("addresses") or []) if a.get("state")}),
    }

def find_person(first,last,state=None):
    """Return candidate NPI records for a named person, best-effort matched."""
    out=[]
    for st in ([state] if state else [None]):
        r=query(first=first,last=last,state=st)
        for rec in r.get("results",[]) or []:
            s=summarize(rec)
            s["name_match"] = (_norm(s["first"]).startswith(_norm(first)[:4]) and
                               _norm(s["last"])==_norm(last))
            out.append(s)
    # de-dup by NPI
    seen={}; 
    for s in out: seen.setdefault(s["npi"],s)
    return list(seen.values())

def classify(cands):
    """Collapse candidate records into a specialty signal."""
    if not cands: return {"signal":"no_npi","confidence":"unverified","detail":None}
    strong=[c for c in cands if c["name_match"]] or cands
    tax=set()
    for c in strong: tax.update(c["all_taxonomies"])
    ns = any("neurological surgery" in (t or "").lower() for t in tax)
    other = {t for t in tax if t and "neurological surgery" not in t.lower()
             and "student in an organized" not in t.lower()}
    if ns:    return {"signal":"in_neurosurgery","confidence":"probable","detail":sorted(tax)}
    if other: return {"signal":"other_specialty","confidence":"probable","detail":sorted(other)}
    return {"signal":"trainee_or_unknown","confidence":"possible","detail":sorted(tax)}

if __name__=="__main__":
    # smoke test against names parsed from the real UCSF 2015 roster
    for f,l in [("Dario","Englot"),("Corinna","Zygourakis"),("Michael","Safaee"),("Doris","Wang")]:
        c=find_person(f,l); k=classify(c)
        print(f"{f} {l:14s} n={len(c):2d}  {k['signal']:20s} {str(k['detail'])[:78]}")
        time.sleep(0.4)
