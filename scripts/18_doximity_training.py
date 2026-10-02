#!/usr/bin/env python3
"""Harvest structured training history from Doximity public profiles.

    python3 scripts/18_doximity_training.py --program-id 60

Doximity publishes exactly the field this study needs, as a YEAR RANGE:

    Residency, Neurological Surgery, 2009 - 2016   Saint Louis University
    Fellowship, Pediatric Neurosurgery, 2016 - 2017

Source comparison (measured 2026-09-24):
    Doximity      HTTP 200, training data present   <- usable
    US News       connection refused to scripts     <- hard-blocked
    Vitals        HTTP 403
    Healthgrades  HTTP 200 but training JS-rendered
    Employer bios HTTP 200, usable but one-off per institution

COMPLETION RULE (per program-side guidance): a residency of >=7 years at the
program means graduated; before ~2014 a 6-year range can also mean graduation,
so 6 years is reported as 'probable' rather than 'yes'. A range much shorter
than that is a departure -- and the END year of a short range is the year they
left, which is what dates the attrition event.

Caveats kept deliberately visible:
  * A person may have TWO residency rows (Zarzour: 2012-13 then 2013-16) --
    that pattern IS the transfer, so all rows are kept, never collapsed.
  * Doximity profiles are self-maintained and can be wrong. The user flagged
    'Vin Mathur 2013-2020' as implausible, and our rosters show Mathur in
    2012 -- so a Doximity row that contradicts a dated roster loses.
"""
import argparse, re, sqlite3, sys, time, urllib.parse
import requests
sys.path.insert(0,"scripts")
from entity_resolution import split_name

UA={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                 "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"}
# Doximity lists the INSTITUTION FIRST, then the entry beneath it:
#     SSM Health/Saint Louis University School of Medicine
#         Residency, Neurological Surgery, 2009 - 2015
#     Mayo Clinic College of Medicine and Science
#         Internship, Transitional Year, 2007 - 2008
# Reading the text AFTER the year range therefore attaches the NEXT
# institution to the current row -- it put Mayo Clinic on McClung-Smith's SLU
# residency and Ohio State on Musgrave's. Parse the structured list instead,
# and fall back to a regex that looks BACKWARDS for the institution.
ENTRY=re.compile(r"^(Residency|Fellowship|Internship|Medical School)\s*,\s*"
                 r"(.*?),?\s*(\d{4})\s*[-\u2013]\s*(\d{4})\s*$")
ROW=re.compile(r"(.{4,80}?)\s+"
               r"(Residency|Fellowship|Internship|Medical School)\s*,\s*"
               r"([^,]{0,60}?)\s*,\s*(\d{4})\s*[-\u2013]\s*(\d{4})")

def slugs(name):
    f,m,l=split_name(name)
    f=re.sub(r"[^a-z]","",f); l=re.sub(r"[^a-z\-]","",l).replace(" ","-")
    base=f"{f}-{l}"
    return [f"https://www.doximity.com/pub/{base}-md",
            f"https://www.doximity.com/pub/{base}-md-phd",
            f"https://www.doximity.com/pub/{base}-do"]

def fetch_profile(name, delay=2.0, verify_terms=None, roster_years=None):
    """Fetch a profile and VERIFY it is the right person before trusting it.

    Slug guessing reaches the wrong physician often enough to matter:
    'Matthew Pierson' resolved to a Duke resident (2009-2014) while
    'Matt Pierson' resolved to the correct SLU one (2013-2019). A profile is
    accepted only if it mentions the program OR its residency years overlap
    the years we actually observed this person on the program's roster.
    """
    for u in slugs(name):
        try:
            r=requests.get(u,headers=UA,timeout=30,allow_redirects=True)
        except Exception:
            continue
        time.sleep(delay)
        if r.status_code!=200 or "Residency" not in r.text: continue
        from bs4 import BeautifulSoup
        soup=BeautifulSoup(r.text,"html.parser")
        rows=[]
        # Preferred: the structured training list, institution per <li>
        # NB: class_=lambda silently matches nothing here; the attrs+regex form works.
        for ul in soup.find_all("ul",attrs={"class":re.compile("training",re.I)}):
            for li in ul.find_all("li"):
                parts=[re.sub(r"\s+"," ",x).strip()
                       for x in li.stripped_strings]
                inst=parts[0] if parts else ""
                for line in parts[1:]:
                    m=ENTRY.match(line)
                    if m:
                        rows.append({"kind":m.group(1),"specialty":m.group(2).strip(" ,"),
                                     "start":int(m.group(3)),"end":int(m.group(4)),
                                     "institution":inst})
        if not rows:
            for t in soup(["script","style"]): t.decompose()
            txt=re.sub(r"\s+"," ",soup.get_text(" "))
            rows=[{"kind":m.group(2),"specialty":m.group(3).strip(),
                   "start":int(m.group(4)),"end":int(m.group(5)),
                   "institution":re.sub(r"\s+"," ",m.group(1)).strip(" ,;")}
                  for m in ROW.finditer(txt)]
        if not rows: continue
        ok_inst = verify_terms and any(
            any(t.lower() in x["institution"].lower() for t in verify_terms) for x in rows)
        ok_years = False
        if roster_years:
            lo,hi=min(roster_years),max(roster_years)
            ok_years = any(x["kind"]=="Residency" and x["start"]<=hi and x["end"]>=lo for x in rows)
        if verify_terms or roster_years:
            if not (ok_inst or ok_years):
                return r.url, []          # found a profile, but not this person
        return r.url, rows
    return None, []

import datetime
THIS_YEAR=datetime.date.today().year

def completion(rows, program_terms, terminal=7):
    """Judge completion from residency rows matching this program.

    Doximity lists a resident's EXPECTED completion year, so a current trainee
    shows a future end date (Musgrave: 2021-2028). Treating that as a finished
    7-year span marks someone still in training as graduated, so any end year
    beyond the current one resolves to 'in_training', never 'yes'.
    """
    res=[r for r in rows if r["kind"]=="Residency"
         and any(t.lower() in r["institution"].lower() for t in program_terms)]
    if not res: return None,None,"no matching residency row"
    span_start=min(r["start"] for r in res); span_end=max(r["end"] for r in res)
    if span_end>THIS_YEAR:
        return span_start,span_end,"in_training"      # expected, not achieved
    yrs=span_end-span_start
    if yrs>=terminal: return span_start,span_end,"yes"
    if yrs>=6:        return span_start,span_end,"probable"
    return span_start,span_end,"no"

ap=argparse.ArgumentParser()
ap.add_argument("--program-id",type=int,required=True)
ap.add_argument("--terms",nargs="*",default=["Saint Louis","St Louis","SSM"])
ap.add_argument("--delay",type=float,default=2.0)
a=ap.parse_args()

con=sqlite3.connect("db/neurosurgery_attrition.db"); con.execute("PRAGMA busy_timeout=60000")
names=[r[0] for r in con.execute("""SELECT DISTINCT name_as_listed FROM roster_observations
                                    WHERE program_id=? ORDER BY 1""",(a.program_id,))]
print(f"{len(names)} distinct roster names for program {a.program_id}\n")
print(f"{'name':24s} {'span':11s} {'compl':9s} rows")
print("-"*100)
ry={}
for nm,ay in con.execute("""SELECT name_as_listed,academic_year FROM roster_observations
                            WHERE program_id=?""",(a.program_id,)):
    ry.setdefault(nm,set()).add(int(ay[:4]))

for n in names:
    url,rows=fetch_profile(n,a.delay,verify_terms=a.terms,roster_years=ry.get(n))
    if not rows:
        print(f"{n[:24]:24s} {'-':11s} {'unverified' if url else 'no profile':9s}")
        continue
    s_,e_,verdict=completion(rows,a.terms)
    span=f"{s_}-{e_}" if s_ else "-"
    detail="; ".join(f"{r['kind'][:4]} {r['start']}-{r['end']} {r['institution'][:26]}" for r in rows[:3])
    print(f"{n[:24]:24s} {span:11s} {str(verdict):9s} {detail[:58]}")
con.close()
