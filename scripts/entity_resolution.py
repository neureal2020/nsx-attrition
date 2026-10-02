#!/usr/bin/env python3
"""Record linkage: resolve name strings from many sources to one human being.

This is the load-bearing component of the whole study. Every source names
people differently -- "Dario Englot", "Dario J. Englot, MD, PhD", "D. Englot",
"Englot, Dario" -- and getting it wrong in either direction corrupts the
outcome:

  * FALSE SPLIT  (one person read as two) -> the person "disappears" from the
    roster and is scored as attrition. Inflates the attrition rate.
  * FALSE MERGE  (two people read as one) -> a departure is masked by the other
    person's record. Deflates the attrition rate.

THE MARRIED-NAME PROBLEM IS A BIAS, NOT NOISE
---------------------------------------------
Surname changes at marriage are common and fall disproportionately on women. A
resident who matched as "Sarah Chen" and practices as "Sarah Okonkwo" will fail
every last-name match, vanish from follow-up, and be scored as attrition. Since
attrition by sex is a headline comparison in this literature, that single
failure mode would manufacture a finding.

So surname-change candidates are detected EXPLICITLY (same distinctive first
name + same program + compatible years + same degrees/medical school, different
surname) and routed to manual review rather than silently dropped.
"""
import re, unicodedata, json, itertools
from collections import defaultdict

# --- normalisation ----------------------------------------------------------
SUFFIX=re.compile(r"\b(jr|sr|ii|iii|iv|md|do|phd|mph|ms|mba|facs|faans|mbbs|msc|dsc)\b\.?",re.I)
PARTICLES={"van","von","de","del","della","da","di","la","le","el","bin","al","der","den","ten","ter"}

def strip_accents(s):
    return unicodedata.normalize("NFKD",s or "").encode("ascii","ignore").decode()

def norm(s):
    s=strip_accents(s).lower()
    s=SUFFIX.sub(" ",s)
    s=re.sub(r"[^a-z\s'\-]"," ",s)
    return " ".join(s.split())

def split_name(s):
    """-> (first, middle, last). Handles 'Last, First M.' and 'First M. Last'.

    The inverted form is what PubMed, board directories and many alumni tables
    use, so getting it wrong would silently de-link a whole class of sources.
    A comma is treated as inverted ONLY when the trailing part is not purely a
    degree/suffix string ("Englot, Dario" is inverted; "Englot, MD" is not).
    """
    raw=strip_accents(s or "")
    if "," in raw:
        head,_,tail=raw.partition(",")
        tail_clean=norm(tail)
        head_clean=norm(head)
        if tail_clean and head_clean:
            s=f"{tail_clean} {head_clean}"          # -> "dario englot"
        else:
            s=norm(raw)
    else:
        s=norm(raw)
    parts=s.split()
    if not parts: return ("","","")
    if len(parts)==1: return (parts[0],"","")
    # pull multi-token particle surnames back together: "van der berg"
    last_start=len(parts)-1
    while last_start>1 and parts[last_start-1] in PARTICLES: last_start-=1
    last=" ".join(parts[last_start:])
    first=parts[0]
    middle=" ".join(parts[1:last_start])
    return (first,middle,last)

# --- similarity -------------------------------------------------------------
def jaro(a,b):
    if a==b: return 1.0
    if not a or not b: return 0.0
    md=max(len(a),len(b))//2-1; md=max(md,0)
    af=[False]*len(a); bf=[False]*len(b); m=0
    for i,ca in enumerate(a):
        for j in range(max(0,i-md),min(len(b),i+md+1)):
            if not bf[j] and b[j]==ca: af[i]=bf[j]=True; m+=1; break
    if not m: return 0.0
    k=t=0
    for i,ca in enumerate(a):
        if af[i]:
            while not bf[k]: k+=1
            if ca!=b[k]: t+=1
            k+=1
    t//=2
    return (m/len(a)+m/len(b)+(m-t)/m)/3

def jaro_winkler(a,b,p=0.1):
    j=jaro(a,b); l=0
    for x,y in zip(a,b):
        if x==y and l<4: l+=1
        else: break
    return j+l*p*(1-j)

# Common English/US given-name diminutives. Deliberately conservative: a wrong
# nickname expansion creates a false merge, which is worse than a missed link.
NICK={
 "rob":"robert","bob":"robert","bobby":"robert","robbie":"robert",
 "bill":"william","will":"william","billy":"william","willie":"william",
 "dick":"richard","rick":"richard","ricky":"richard","rich":"richard",
 "jim":"james","jimmy":"james","jamie":"james",
 "mike":"michael","mickey":"michael","mitch":"mitchell",
 "dave":"david","davey":"david","steve":"steven","stevie":"steven",
 "tom":"thomas","tommy":"thomas","tony":"anthony",
 "chris":"christopher","kit":"christopher","topher":"christopher",
 "dan":"daniel","danny":"daniel","matt":"matthew","nick":"nicholas",
 "joe":"joseph","joey":"joseph","jon":"jonathan","john":"jonathan",
 "ben":"benjamin","benny":"benjamin","sam":"samuel","alex":"alexander",
 "andy":"andrew","drew":"andrew","greg":"gregory","jeff":"jeffrey",
 "ken":"kenneth","larry":"lawrence","ted":"edward","ed":"edward","eddie":"edward",
 "pete":"peter","phil":"philip","ron":"ronald","russ":"russell",
 "charlie":"charles","chuck":"charles","frank":"franklin","fred":"frederick",
 "hank":"henry","harry":"henry","jack":"john","tim":"timothy",
 "kate":"katherine","katie":"katherine","kathy":"katherine","cathy":"catherine",
 "beth":"elizabeth","liz":"elizabeth","lizzie":"elizabeth","betsy":"elizabeth",
 "sue":"susan","suzy":"susan","jen":"jennifer","jenny":"jennifer",
 "meg":"margaret","maggie":"margaret","peggy":"margaret",
 "becky":"rebecca","cindy":"cynthia","debbie":"deborah","vicky":"victoria",
 "abby":"abigail","allie":"allison","mandy":"amanda","angie":"angela",
 "trish":"patricia","patty":"patricia","sandy":"sandra","terry":"teresa",
 "val":"valerie","gabby":"gabrielle","steph":"stephanie","nat":"natalie",
}
def canon_first(f):
    f=(f or "").strip()
    return NICK.get(f,f)

def first_compatible(a,b):
    """Initials count as compatible; nicknames are canonicalised."""
    a,b=(a or "").strip(),(b or "").strip()
    if not a or not b: return 0.0
    if len(a)==1 or len(b)==1:
        return 0.85 if a[0]==b[0] else 0.0
    ca,cb=canon_first(a),canon_first(b)
    if ca==cb: return 1.0
    s=jaro_winkler(ca,cb)
    return s if s>=0.90 else 0.0

# --- blocking ---------------------------------------------------------------
def dmeta(s):
    """Tiny phonetic key: enough to survive spelling drift in blocking."""
    s=re.sub(r"[^a-z]","",(s or "").lower())
    if not s: return ""
    s=re.sub(r"[hw]","",s)
    for a,b in (("ck","k"),("ph","f"),("sch","sk"),("ce","se"),("ci","si"),
                ("cy","sy"),("c","k"),("q","k"),("x","ks"),("z","s"),
                ("ie","y"),("ee","y"),("oo","u")):
        s=s.replace(a,b)
    s=re.sub(r"(.)\1+",r"\1",s)
    v=s[0]+re.sub(r"[aeiou]","",s[1:])
    return v[:6]

def blocking_keys(rec):
    f,m,l=rec["first"],rec.get("middle",""),rec["last"]
    keys={f"L:{dmeta(l)}"}
    if f: keys.add(f"FL:{canon_first(f)[:3]}:{dmeta(l)}")
    # surname-change block: distinctive first name alone, scoped by program
    if f and len(f)>=4 and rec.get("program_id"):
        keys.add(f"NC:{canon_first(f)}:{rec['program_id']}")
    return keys

# --- pairwise scoring -------------------------------------------------------
def score_pair(a,b):
    """Return (score 0-1, reasons, surname_change_suspect)."""
    r=[]; s=0.0
    fs=first_compatible(a["first"],b["first"])
    ls=jaro_winkler(a["last"],b["last"]) if a["last"] and b["last"] else 0.0
    same_last = ls>=0.93
    if fs: r.append(f"first~{fs:.2f}")
    if a["last"] and b["last"]: r.append(f"last~{ls:.2f}")

    s += 0.34*fs + 0.34*(ls if same_last else 0.0)

    am,bm=(a.get("middle") or "").strip(),(b.get("middle") or "").strip()
    if am and bm:
        if am[0]==bm[0]: s+=0.06; r.append("middle-initial")
        else: s-=0.18; r.append("middle-CONFLICT")

    if a.get("program_id") and a.get("program_id")==b.get("program_id"):
        s+=0.14; r.append("same-program")
    if a.get("med_school") and a.get("med_school")==b.get("med_school"):
        s+=0.10; r.append("same-med-school")
    da,db=(a.get("degrees") or ""),(b.get("degrees") or "")
    if da and db:
        if set(da.split())==set(db.split()): s+=0.04; r.append("same-degrees")
    ya,yb=a.get("year"),b.get("year")
    if ya and yb:
        d=abs(ya-yb)
        if d<=8: s+=0.06*(1-d/8); r.append(f"years~{d}")
        else: s-=0.15; r.append("years-far")

    # surname change: strong first/middle/context agreement, surname differs
    nc = (not same_last and fs>=0.95 and
          (a.get("program_id") and a.get("program_id")==b.get("program_id")) and
          (ya and yb and abs(ya-yb)<=10))
    if nc:
        s=max(s,0.55); r.append("SURNAME-CHANGE-SUSPECT")
    return (max(0.0,min(1.0,s)), r, nc)

AUTO_LINK=0.88     # above: link automatically
REVIEW=0.62        # between: human adjudication queue

def make_record(name, program_id=None, year=None, degrees=None, med_school=None, source=None, obs_id=None):
    f,m,l=split_name(name)
    return {"raw":name,"first":f,"middle":m,"last":l,"program_id":program_id,
            "year":year,"degrees":degrees,"med_school":med_school,
            "source":source,"obs_id":obs_id}

def resolve(records):
    """Block, score within blocks, return (auto_links, review_queue)."""
    blocks=defaultdict(list)
    for i,rec in enumerate(records):
        for k in blocking_keys(rec): blocks[k].append(i)
    seen=set(); auto=[]; review=[]
    for k,idxs in blocks.items():
        if len(idxs)<2 or len(idxs)>400: continue
        for i,j in itertools.combinations(sorted(idxs),2):
            if (i,j) in seen: continue
            seen.add((i,j))
            sc,why,nc=score_pair(records[i],records[j])
            if sc>=AUTO_LINK and not nc: auto.append((i,j,round(sc,3),why))
            elif sc>=REVIEW: review.append((i,j,round(sc,3),why,nc))
    auto.sort(key=lambda x:-x[2]); review.sort(key=lambda x:-x[2])
    return auto,review

if __name__=="__main__":
    recs=[
      make_record("Dario Englot",            program_id=1, year=2015, degrees="MD PHD", source="ucsf-roster"),
      make_record("Dario J. Englot, MD, PhD",program_id=1, year=2016, degrees="MD PHD", source="bio"),
      make_record("D. Englot",               program_id=1, year=2014, source="news"),
      make_record("Englot, Dario",           program_id=1, year=2013, source="pubmed"),
      make_record("John Kim",                program_id=1, year=2015, source="roster-A"),
      make_record("John Kim",                program_id=7, year=2015, source="roster-B"),
      make_record("Sarah Chen",              program_id=3, year=2014, degrees="MD", med_school="Yale", source="roster"),
      make_record("Sarah Okonkwo",           program_id=3, year=2020, degrees="MD", med_school="Yale", source="faculty-bio"),
      make_record("Robert Smith",            program_id=4, year=2013, source="roster"),
      make_record("Bob Smith",               program_id=4, year=2014, source="news"),
      make_record("Michael Safaee",          program_id=1, year=2015, source="roster"),
      make_record("Michael Safaei",          program_id=1, year=2016, source="typo-variant"),
    ]
    auto,review=resolve(recs)
    print("=== AUTO-LINKED (>=0.88) ===")
    for i,j,s,w in auto: print(f"  {s}  {recs[i]['raw']:26s} <-> {recs[j]['raw']:26s}  {w}")
    print("\n=== REVIEW QUEUE (0.62-0.88) ===")
    for i,j,s,w,nc in review:
        tag="  <== SURNAME CHANGE?" if nc else ""
        print(f"  {s}  {recs[i]['raw']:26s} <-> {recs[j]['raw']:26s}  {w}{tag}")
    print("\n=== NOT LINKED (correctly kept apart) ===")
    linked={(i,j) for i,j,*_ in auto}|{(i,j) for i,j,*_ in review}
    for i,j in itertools.combinations(range(len(recs)),2):
        if (i,j) not in linked and recs[i]['last']==recs[j]['last']:
            print(f"        {recs[i]['raw']} [prog {recs[i]['program_id']}] vs {recs[j]['raw']} [prog {recs[j]['program_id']}]")
