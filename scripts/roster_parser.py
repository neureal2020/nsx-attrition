#!/usr/bin/env python3
"""Extract resident names (and PGY where stated) from an archived roster page.

Design notes driven by real pages sampled across 2009-2018:
  * PGY is frequently ABSENT (e.g. UCSF lists names only), so it is optional.
    Cohort year is inferred from first-appearance instead. A parser that
    required PGY would silently drop whole programs.
  * PGY appears as Roman (PGY VII), Arabic (PGY-3), or as R1..R7 / 'Chief'.
  * Names are split across sibling DOM nodes ('George Galvan' + ', M.D.'),
    so extraction works on element text, not on flattened page text.
  * Site chrome (nav/menus/breadcrumbs) dominates the text of older pages and
    must be removed structurally AND by stopword vocabulary.
"""
import re, json
from bs4 import BeautifulSoup

ROMAN={'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8}
DEG=r"(?:M\.?D\.?|D\.?O\.?|Ph\.?D\.?|M\.?B\.?B\.?S\.?|M\.?P\.?H\.?|M\.?S\.?|M\.?D\.?/Ph\.?D\.?|Sc\.?D\.?)"
DEG_RE=re.compile(rf"\b{DEG}\b",re.I)

# Site chrome vocabulary: any candidate equal to one of these is not a person.
NAV={"home","about","about us","education","research","contact","contact us","faculty","residents",
 "fellows","nurses","staff","alumni","news","events","giving","search","menu","login","intranet",
 "patient care","clinical programs","patient center","referrals","medical students","residency",
 "conferences","grand rounds","lecture series","videos","publications","links","galleries",
 "our team","people","overview","apply","application","curriculum","rotations","salary","benefits",
 "message from the chair","chairman","program director","current residents","former residents",
 "make a gift","support us","parking","maps and directions","site map","careers","privacy",
 "disclaimer","accessibility","webmaster","site credits","skip navigation","clinical trials",
 "refer a patient","patient forms","patient information","upcoming states","photo/ video galleries"}

PGY_RE=re.compile(
  r"\b(?:PGY|P\.?G\.?Y\.?)[\s\-–—]*(?:(\d{1,2})|([IVX]{1,5}))\b"
  r"|\b(?:R|PG)[\s\-]?(\d)\b"
  r"|\b(chief)\s+resident\b|\b(intern)\b", re.I)

# A personal name: 2-4 capitalised tokens, allowing initials, hyphens, apostrophes, particles.
NAME_RE=re.compile(
  r"^(?:(?:Dr|Mr|Ms|Mrs)\.?\s+)?"
  r"([A-Z][A-Za-z'’\-]{1,20}"
  r"(?:\s+(?:[A-Z]\.?|[A-Z][A-Za-z'’\-]{1,20}|van|von|de|del|della|da|di|la|le|el|bin|al|Mc|Mac|St\.?)){1,3})"
  r"\s*,?\s*$")

def pgy_from(text):
    m=PGY_RE.search(text or "")
    if not m: return None,None
    g=m.groups()
    if g[0]: return int(g[0]),m.group(0)
    if g[1] and g[1].upper() in ROMAN: return ROMAN[g[1].upper()],m.group(0)
    if g[2]: return int(g[2]),m.group(0)
    if g[3]: return None,"chief"
    if g[4]: return 1,"intern"
    return None,m.group(0)

def clean_name(s):
    s=re.sub(r"\s+"," ",(s or "")).strip(" \t\n\r,;|·–—-")
    s=re.sub(r"\(.*?\)","",s).strip()
    degrees=" ".join(sorted({d.upper().replace(".","") for d in DEG_RE.findall(s)}))
    s=DEG_RE.sub("",s)
    s=re.sub(r"[,\s]+$","",s).strip(" ,")
    return s,degrees

# Tokens that never appear in a personal name but are everywhere in site chrome
# and academic page furniture. Any candidate containing one of these is rejected.
# (Without this the parser happily returns "Penn State Word Mark", "Copy Link",
# "Our Mission", "Apply Now" and "Past Residents" as people.)
BAD_TOKENS=set("""
copy link click here more read view show hide open close next previous back top
apply now submit learn about contact email phone fax map directions visit
our your their this that these those the and for with from into
mission vision values history overview summary section page site web website
word mark logo brand toolkit portal login logout account profile search menu
news event events calendar grand rounds lecture seminar conference symposium
book books chapter chapters article articles publication publications journal
degree degrees certificate certificates diploma program programs track tracks
current former past present incoming outgoing new old recent upcoming
resident residents fellow fellows faculty staff student students alumni alumnus
intern interns trainee trainees physician physicians doctor doctors surgeon
department division section center centre institute hospital clinic school
college university medicine surgical surgery medical health healthcare system
education training residency fellowship undergraduate graduate postdoctoral
research laboratory lab clinical translational basic science sciences
administration administrative leadership chair chairman chairperson director
coordinator manager officer president dean provost professor associate assistant
anesthesiology dermatology neurology radiology pathology pediatrics psychiatry
orthopaedics orthopedics urology ophthalmology obstetrics gynecology oncology
cardiology emergency family internal general plastic thoracic vascular
january february march april may june july august september october november
december spring summer fall winter annual yearly monthly weekly daily
place placement placements position positions opportunity opportunities
award awards honor honors honour prize prizes scholarship grant grants
photo photos gallery video videos image images media press release
policy policies privacy terms accessibility disclaimer copyright sitemap
here there where when what which who whom how why all any some none
call calls schedule schedules rotation rotations workshop workshops cadaveric
attending attendings spine cranial vascular pediatric elective night float
""".split())

# Suffixes/prefixes that mark an organisation rather than a person
ORG_WORDS=re.compile(r"\b(department|university|hospital|center|centre|program|school|"
                     r"medicine|college|institute|surgery|neuro\w*|clinic|health|system|"
                     r"foundation|association|society|board|committee|group|team|office|"
                     r"campus|building|floor|suite|room|street|avenue|road|drive)\b",re.I)

ROMAN_SUFFIX=re.compile(r"^(i{1,3}|iv|v|vi{1,3}|ix|x|jr|sr)$",re.I)

def is_person(name):
    if not name or len(name)<5 or len(name)>48: return False
    # "Fields II" / "Quinn IV" are the tail of a suffixed surname, not a name
    _t=[x for x in re.split(r"[\s,]+",name) if x]
    if len(_t)==2 and ROMAN_SUFFIX.match(_t[1]): return False
    low=name.lower()
    if low in NAV: return False
    if ORG_WORDS.search(low): return False
    toks=[t for t in re.split(r"[\s,]+",low) if t]
    if len(toks)<2 or len(toks)>4: return False
    # any furniture token disqualifies the whole candidate
    if any(re.sub(r"[^a-z]","",t) in BAD_TOKENS for t in toks): return False
    # at least two tokens must be real word-like names (not single initials)
    substantive=[t for t in toks if len(re.sub(r"[^a-z'\-]","",t))>=2]
    if len(substantive)<2: return False
    if not NAME_RE.match(name): return False
    if any(c.isdigit() for c in name): return False
    # all-caps acronyms and single repeated tokens are not names
    if name.isupper(): return False
    if len(set(toks))<len(toks): return False
    return True


def extract_main(soup):
    """Return the main content element by link density.

    Site chrome (nav, menus, footers) is link-dense; article and roster bodies
    are not. Picking the largest block whose link-text ratio is under ~0.55
    isolates content on both news posts and roster pages, and works across the
    wildly different CMSs in use from 2009 to 2026.
    """
    best=None
    for el in soup.find_all(["div","section","article","main","table","ul"]):
        txt=el.get_text(" ",strip=True)
        if len(txt)<60: continue
        link=sum(len(a.get_text(" ",strip=True)) for a in el.find_all("a"))
        if link/max(len(txt),1)>0.55: continue
        if best is None or len(txt)>len(best[1]): best=(el,txt)
    return best[0] if best else soup


def parse(html, url="", main_only=False):
    soup=BeautifulSoup(html,"html.parser")
    for t in soup(["script","style","nav","header","footer","aside","form","noscript","select"]): t.decompose()
    for t in soup.find_all(attrs={"class":re.compile(r"nav|menu|breadcrumb|sidebar|footer|header|banner|search",re.I)}): t.decompose()
    for t in soup.find_all(attrs={"id":re.compile(r"nav|menu|breadcrumb|sidebar|footer|header|banner|search",re.I)}): t.decompose()

    if main_only:
        soup=extract_main(soup)

    out, seen = [], set()

    # Some rosters are laid out as running prose rather than one element per
    # person ("PGY-4 Georgios Alexopoulos, M.D. PGY-3 Jorge F. Urquiaga, M.D.
    # Medical School: ..."). Element-based extraction returns nothing there,
    # which is the WORST failure mode -- an empty roster is indistinguishable
    # from a program with no residents. A prose pass runs as a fallback below.

    # Candidate containers: elements whose own text is short (a name-sized chunk).
    for el in soup.find_all(["li","td","p","h2","h3","h4","h5","strong","b","a","div","span","figcaption"]):
        raw=el.get_text(" ",strip=True)
        if not raw or len(raw)>160: continue
        # context = this element plus a little after it, where PGY usually sits
        ctx=raw
        for sib in list(el.next_siblings)[:3]:
            t=getattr(sib,"get_text",lambda *a,**k:str(sib))(" ",strip=True)
            if t: ctx+=" | "+t[:80]
        parent=el.parent.get_text(" ",strip=True) if el.parent else ""
        if len(parent)<300: ctx+=" | "+parent

        name,deg=clean_name(re.split(r"[|•·]",raw)[0])
        if not is_person(name):
            m=re.match(rf"^\s*([A-Z][^,]{{2,40}}?)\s*,\s*{DEG}",raw)
            if m: name,deg=clean_name(m.group(0))
            if not is_person(name): continue
        if not deg:
            _,deg=clean_name(raw)
        pgy,praw=pgy_from(ctx)
        k=name.lower()
        if k in seen: continue
        seen.add(k)
        out.append({"name":name,"degrees":deg or None,"pgy":pgy,"pgy_raw":praw,
                    "context":ctx[:150]})

    if len(out) < 2:
        out = _prose_roster(soup) or out
    return out


def _prose_roster(soup):
    """Fallback: pull 'Name, M.D.' out of flat page text, with nearby PGY.

    PROSE_NAME is defined further down the module; Python resolves it at call
    time so the ordering is fine.
    """
    text=re.sub(r"\s+"," ",soup.get_text(" "))
    out,seen=[],set()
    for m in PROSE_NAME.finditer(text):
        name=re.sub(r"\s+"," ",m.group(1)).strip()
        if not is_person(name): continue
        k=name.lower()
        if k in seen: continue
        seen.add(k)
        # PGY usually sits immediately before or just after the name
        window=text[max(0,m.start()-40):m.end()+40]
        pgy,praw=pgy_from(window)
        out.append({"name":name,
                    "degrees":re.sub(r"[.\s]","",m.group(2)).upper(),
                    "pgy":pgy,"pgy_raw":praw,
                    "context":text[max(0,m.start()-60):m.end()+90][:150]})
    return out

if __name__=="__main__":
    import sys
    for f in sys.argv[1:]:
        r=parse(open(f,encoding="utf-8",errors="replace").read())
        print(f"\n===== {f}  ->  {len(r)} residents =====")
        for x in r: print(f"  {x['name']:30s} {str(x['degrees'] or ''):10s} PGY={str(x['pgy']):4s} ({x['pgy_raw']})")


# ---------------------------------------------------------------------------
# Announcement parsing (Match Day / graduation news posts)
# ---------------------------------------------------------------------------
# These are the ENTRY and EXIT sources that are independent of the roster page.
# Names appear in running prose rather than in list elements, e.g.
#   "...2022 graduating residents Nima Alan MD; Enyinna Nwachuku, MD;
#    Alp Ozpinar, MD, and Matthew Pease, MD, on their successful completion..."
# so they are matched by a name-followed-by-degree pattern, which is very high
# precision in this genre.

PROSE_NAME=re.compile(
    r"\b([A-Z][a-z'’\-]{1,18}"                     # first name
    r"(?:\s+[A-Z]\.?)?"                            # optional middle initial
    r"(?:\s+(?:van|von|de|del|da|di|la|le|el|bin|al|Mc|Mac|St\.?))?"
    r"\s+[A-Z][A-Za-z'’\-]{1,22})"                 # last name
    r"\s*,?\s*(M\.?D\.?|D\.?O\.?|Ph\.?D\.?|M\.?D\.?\s*[/,]\s*Ph\.?D\.?|M\.?B\.?B\.?S\.?)"
    r"(?![a-z])")

# Field values run until the NEXT field label or the next "Name, MD", not until
# the next capitalised word -- school names are full of capitalised words
# ("Sidney Kimmel Medical College at Thomas Jefferson University").
_FIELD_END=(r"(?=\s*(?:Medical School:|Undergraduate|Graduate School:|Residency:|"
            r"Fellowship:|Hometown:|[A-Z][a-z'’\-]+(?:\s+[A-Z]\.?)?\s+[A-Z][A-Za-z'’\-]+\s*,?\s*"
            r"(?:M\.?D\.?|D\.?O\.?|Ph\.?D\.?))|$)")
MED_SCHOOL=re.compile(r"Medical School:\s*(.{4,110}?)"+_FIELD_END)
UNDERGRAD =re.compile(r"Undergraduate(?:\s+School)?:\s*(.{4,110}?)"+_FIELD_END)

MATCH_CUES=re.compile(r"\bmatch(?:ed)?\s+(?:into|with|at|to)\b|\bmatch day\b|incoming\s+(?:resident|class|intern)|"
                      r"new\s+residents?\b|welcome\s+(?:our|the|new)|join(?:ing)?\s+(?:our|the)\s+"
                      r"(?:department|program|residency)|intern\s+class|pgy-?1\s+class",re.I)
# NB "Graduate School:" is a FIELD LABEL inside Match Day posts, so a bare
# \bgraduat cue misclassifies every match post as a graduation. Require the
# graduation sense explicitly.
GRAD_CUES =re.compile(r"graduating\s+(?:resident|chief|class)|resident\s+graduates?\b|"
                      r"\bgraduation\b|successful\s+completion|completion\s+of\s+(?:the|their|his|her)|"
                      r"commencement|finish(?:ed|ing)?\s+(?:their|his|her)\s+(?:residency|training)|"
                      r"honors?\s+\d{4}\s+graduat",re.I)

def classify_announcement(text):
    """Return 'match', 'graduation' or None for a news-post body."""
    g,m = len(GRAD_CUES.findall(text or "")), len(MATCH_CUES.findall(text or ""))
    if g==0 and m==0: return None
    return "graduation" if g>=m else "match"

def parse_announcement(html):
    """Extract {type, date_text, people[]} from a Match Day / graduation post."""
    soup=BeautifulSoup(html,"html.parser")
    for t in soup(["script","style","nav","footer","header","aside","form"]): t.decompose()
    body=extract_main(soup).get_text(" ",strip=True)
    body=re.sub(r"\s+"," ",body)
    kind=classify_announcement(body)
    # Offset of the strongest cue: names far from it are likelier to be
    # incidental mentions (faculty quoted, award winners) than cohort members.
    cue=(GRAD_CUES if kind=="graduation" else MATCH_CUES).search(body) if kind else None
    cue_at=cue.start() if cue else 0

    people,seen=[],set()
    for m in PROSE_NAME.finditer(body):
        name=re.sub(r"\s+"," ",m.group(1)).strip()
        if not is_person(name): continue
        k=name.lower()
        if k in seen: continue
        seen.add(k)
        tail=body[m.end():m.end()+260]
        ms=MED_SCHOOL.search(tail); ug=UNDERGRAD.search(tail)
        people.append({
            "name":name,
            "degrees":re.sub(r"[.\s]","",m.group(2)).upper(),
            "med_school":ms.group(1).strip(" ,;.") if ms else None,
            "undergrad":ug.group(1).strip(" ,;.") if ug else None,
            "dist_from_cue":abs(m.start()-cue_at),
            "context":body[max(0,m.start()-70):m.end()+90],
        })
    dm=re.search(r"\b((?:January|February|March|April|May|June|July|August|September|October|"
                 r"November|December)\s+\d{1,2},\s+\d{4})", body)
    return {"type":kind,"date_text":dm.group(1) if dm else None,
            "n_people":len(people),"people":people,"body":body[:4000]}
