#!/usr/bin/env python3
"""Ingest pasted US News / Doximity training blocks into training_history.

    python3 scripts/20_ingest_usnews.py --program-id 60 --file data/intake/worklist_program60.md
    python3 scripts/20_ingest_usnews.py --program-id 60 --file <f> --dry-run

Reads the worklist written by 19_build_worklist.py: '## <Name>' headings, each
followed by a fenced block holding whatever was copied from the site.

Handles BOTH published formats, which mean different things:
  US News   'St Louis University Health Sciences Center, 2014, Neurosurgery'
            -> a SINGLE year, which is the year training ENDED
  Doximity  'Residency, Neurological Surgery, 2009 - 2015'
            -> a RANGE

Conflating them is a real hazard: a bare year read as a start date produced
three phantom same-year entrants earlier in this project. A single year is
therefore stored as end_year with start_year left NULL.

Completion rule (program-side guidance): >=7 years at the program = graduated;
6 years = probable (stored as 'unknown' with a note) only if training STARTED
before 2014 (pre-2014 programs could be six); for 2014+ entrants a 6-year span
is a departure, as is anything shorter, and its end year dates the event.
An internship at the program counts toward the span.
"""
import argparse, re, sqlite3, sys, time

# "Chief Residency" is still residency; without the prefix, "Chief" is read as the institution
RANGE=re.compile(r"(?:Chief\s+)?(Residency|Fellowship|Internship)\s*,\s*([^,]{0,60}?)\s*,\s*"
                 r"(\d{4})\s*[-–]\s*(\d{4})",re.I)
SINGLE=re.compile(r"^(.{4,90}?),\s*(\d{4})\s*,\s*(.{3,60})$")
SECTION=re.compile(r"^(Residency|Residencies|Internship|Internships|Fellowship|Fellowships|"
                   r"Medical School|Education)\s*$",re.I)

def parse_block(text):
    out=[]; section=None; prev=None
    for raw in text.splitlines():
        line=raw.strip()
        if not line: continue
        m=SECTION.match(line)
        if m: section=m.group(1).rstrip("s").title(); continue
        m=RANGE.search(line)
        if m:
            out.append({"kind":m.group(1).title(),"specialty":m.group(2).strip(),
                        "start":int(m.group(3)),"end":int(m.group(4)),
                        # US News profiles put the institution on the line ABOVE;
                        # left empty it would pass any program's filter
                        "institution":line[:m.start()].strip(" ,-") or prev,
                        "fmt":"range"})
            continue
        m=SINGLE.match(line)
        if m and section:
            out.append({"kind":section,"specialty":m.group(3).strip(),
                        "start":None,"end":int(m.group(2)),
                        "institution":m.group(1).strip(),"fmt":"single-year=END"})
            continue
        if section and re.match(r"^[A-Z].{5,90}$",line) and not out:
            pass
        prev=line
    return out

def verdict(rows, terms, terminal=7):
    # an internship AT the program is PGY-1 (Pierson: SLU intern 2012-13, then
    # "Residency 2013-2019" -- six years only if the intern year is dropped)
    res=[r for r in rows if r["kind"].lower().startswith(("resid","intern"))
         and (not r["institution"] or any(t.lower() in r["institution"].lower() for t in terms))]
    if not res: return None,None,"unknown","no residency row matching the program"
    spans=[r for r in res if r["start"] and r["end"]]
    if spans:
        s=min(r["start"] for r in spans); e=max(r["end"] for r in spans); yrs=e-s
        if yrs>=terminal: return s,e,"yes",f"{yrs}y span"
        # six years only passes for someone who STARTED before 2014; entrants
        # from 2014 on face a seven-year program, so a 6y span is a departure
        # (Alexopoulos, 2018-2024: left before PGY-7). Keyed on start, not end:
        # McClung-Smith and Sampath did 2009-2015 in six and graduated.
        # stored as 'unknown': training_history.completed only allows yes/no/unknown
        if yrs>=6 and s<2014: return s,e,"unknown",f"{yrs}y span, probable (6y can be a pre-2014-entry graduation)"
        return s,e,"no",f"only {yrs}y — departure; end year dates the event"
    e=max(r["end"] for r in res)
    return None,e,"unknown",f"single year {e} = END of training; start not stated"

ap=argparse.ArgumentParser()
ap.add_argument("--program-id",type=int,required=True)
ap.add_argument("--file",required=True)
ap.add_argument("--terms",nargs="*",default=["Saint Louis","St Louis","SSM","SLU"])
ap.add_argument("--dry-run",action="store_true")
a=ap.parse_args()

txt=open(a.file,encoding="utf-8").read()
chunks=re.split(r"^##\s+",txt,flags=re.M)[1:]
con=sqlite3.connect("db/neurosurgery_attrition.db"); con.execute("PRAGMA busy_timeout=60000")
today=time.strftime("%Y-%m-%d"); n_ing=0
for ch in chunks:
    name=ch.splitlines()[0].strip()
    name=re.sub(r"\s*_\(.*?\)_\s*$","",name).strip()
    blocks=re.findall(r"```(.*?)```",ch,flags=re.S)
    body="\n".join(blocks).strip()
    if not body: continue
    rows=parse_block(body)
    if not rows:
        print(f"  {name:26s} pasted text present but nothing parsed — check format"); continue
    s_,e_,v,why=verdict(rows,a.terms)
    print(f"  {name:26s} {str(s_ or '?'):5s}-{str(e_ or '?'):5s} {v:9s} {why}")
    if a.dry_run: continue
    con.execute("""INSERT INTO training_history
      (resident_name,program_id,institution,role,start_year,end_year,completed,
       source_type,retrieved_on,notes)
      VALUES (?,?,?,?,?,?,?,'other',?,?)""",
      (name,a.program_id,"; ".join(sorted({r['institution'] or '' for r in rows}))[:120],
       "residency",s_,e_,v,today,
       f"pasted from US News/Doximity worklist; {why}; formats={sorted({r['fmt'] for r in rows})}"))
    n_ing+=1
if not a.dry_run: con.commit()
print(f"\n{'would ingest' if a.dry_run else 'ingested'} {n_ing} records")
con.close()
