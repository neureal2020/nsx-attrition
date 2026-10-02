"""Generic roster-page parser, built from the layouts met on SLU, WashU, Pitt,
UCSF, Barrow and Hopkins. Returns [(name, pgy_or_None, context)].

    from roster_extract import lines, parse
    rows = parse(lines(html))

Layouts handled (auto-detected):
  * HEADING  -- a PGY heading precedes a block of names:
               "PGY-7 Chiefs", "PGY 3", "Postgraduate Year 4 (Class of 2027)",
               "Chief Residents", "Interns"/"First Year"/"Fourth Year Residents"
  * INLINE   -- each name followed within a few lines by its own "PGY-n"
               (Barrow 2014: "Name, MD | Neurosurgery Resident | PGY-6").
               Detected when PGY lines sit right after a '...Resident' line;
               treating these as headings shifts everyone by one year.
  * FLAT     -- names only (UCSF old site); pgy None.
Stops at 'Incoming'/'Matched'/'New Residents' sections (next year's interns)
and at fellows/faculty/alumni sections. Skips lines that look like faculty
or news ('Professor', 'Chair', 'named', 'Fellow').

'Chief Residents' as a bare heading returns pgy None: at Pitt it meant PGY6
(and PGY6+7 before 2021), elsewhere PGY7 -- the person's other years decide.
"""
import re, html as _html

CRED = r"(?:MD|M\.D\.|DO|D\.O\.|MBBS|MBChB|MBBCh)"
NAME = re.compile(r"^(?:Dr\.\s+)?([A-Z][\w.'\-]*(?:\s+[\w.'\-()]+){1,5}?),?\s+" + CRED + r"(?=[\s,.;|)]|$)")
# bare personal name (no credential), used only under PGY headings on pages that print none
BARE = re.compile(r"^([A-Z][a-zA-Z'\-]+(?:\s+(?:\([A-Za-z]+\)|[A-Z]\.|[A-Z][a-zA-Z'\-]+|de|van|von|del|da)){1,4})$")
NOTNAME = re.compile(r"(?i)biograph|publication|in this section|section|contact|site map|legal|disclaimer|privacy|patient|clinic\b|international|maryland|medical|news|concierge|johns hopkins|policy|careers|giving|directions|class of|quick links|about|frequently|how to|view|follow|residen|interns?$|chief|assistant|year|program|education|research|awards?|profiles?|school|university|college|hospital|department")
ORD = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "sixth": 6, "seventh": 7}
STOP = re.compile(r"(?i)^(incoming|matched|new residents|our new|fellows?|current fellows|faculty|alumni|past residents|former residents|graduates|recent graduates)\b")
NOISE = re.compile(r"(?i)newsweek|\bnamed\b|professor|\bchair\b|fellow\b|director")

def lines(s):
    # NOT <header>: some CMSs (Michigan 2013-18) put each person's name in a per-card <header>
    b = re.sub(r"(?s)<(script|style|nav|footer|noscript).*?</\1>", " ", s)
    b = re.sub(r"(?i)<br\s*/?>|</(p|div|li|h\d|tr|td|a|span|strong|b|em)>", "\n", b)
    b = _html.unescape(re.sub(r"<[^>]+>", "\n", b))
    return [re.sub(r"\s+", " ", l).strip() for l in b.split("\n") if l.strip()]

def heading_pgy(l):
    """PGY number for a heading line, 'chief' for a bare chief heading, else False."""
    if len(l) > 60: return False
    m = re.match(r"(?i)^(?:PGY|post[- ]?graduate year|postgraduate year|program year ns|ns)[\s-]*(\d)\b", l)
    if m: return int(m.group(1))
    m = re.match(r"(?i)^(first|second|third|fourth|fifth|sixth|seventh)[- ]year\b", l)
    if m: return ORD[m.group(1).lower()]
    if re.match(r"(?i)^interns?$|^pgy-?1 interns?$", l): return 1
    # plural only: SLU prints a singular 'Chief resident' subtitle inside a PGY-7 card
    if re.match(r"(?i)^chief residents$", l): return "chief"
    return False

def _inline(L):
    """Count PGY lines that describe the person just above them. Barrow 2014:
    'Name, MD | Neurosurgery Resident | PGY-6'; Duke 2022+: 'Name, MD | PGY-7,
    Sub-Internship Resident Coordinator'. A name directly above a PGY line
    also happens once per group in HEADING layouts, so name-above only counts
    when it holds for most names on the page."""
    pgy = re.compile(r"^PGY[\s-]*\d\b")
    # label line only ('Neurosurgery Resident'); Mayo bios ending in '...our residents.' sit above headings
    res = sum(1 for k, l in enumerate(L) if k and pgy.match(l) and len(L[k - 1]) < 60 and re.search(r"(?i)resident", L[k - 1]))
    nm = sum(1 for k, l in enumerate(L) if k and pgy.match(l) and NAME.match(L[k - 1]))
    names = sum(1 for l in L if NAME.match(l))
    return max(res, nm if names and nm >= 0.6 * names else 0)

def _join_split_names(L):
    """UCLA-style cards split names over lines: 'Srinivas' + 'Chivukula, MD' or
    'Mark Attiah,' + 'MD, MS, MPH'. Re-join them before parsing. The second
    line must be a lone surname: a school line ('Keck USC') followed by a whole
    'First Surname, MD' must not be prepended."""
    out, i = [], 0
    cred = re.compile(r"^" + CRED + r"(?=[\s,.;|)]|$)")
    first = re.compile(r"^[A-Z][a-zA-Z.'\-]*(?:\s+(?:\([A-Za-z]+\)|[A-Z][a-zA-Z.'\-]*)){0,2}$")   # 'H. Westley', 'Jasmine A.T.'
    surname = r"^[A-Z][\w'\-]+(?:\s+(?:II|III|IV|Jr\.?))?,?\s+" + CRED + r"(?=[\s,.;|)]|$)"         # 'Bell IV, MD' 
    while i < len(L):
        l = L[i]; nxt = L[i + 1] if i + 1 < len(L) else ""
        if l.endswith(",") and cred.match(nxt):
            out.append(l + " " + nxt); i += 2; continue
        if first.match(l) and not heading_pgy(l) and not NOTNAME.search(l) and re.match(surname, nxt) and not NAME.match(l + " x, MD") is None:
            out.append(l + " " + nxt); i += 2; continue
        out.append(l); i += 1
    return out

LASTFIRST = re.compile(r"^([A-Z][\w'\-]+), ([A-Z][\w'\-]+(?: [A-Z][\w.'\-]*)?), (" + CRED + r"(?=[\s,.;|)]|$).*)$")

def parse(L):
    # Penn 2019 prints one class surname-first: 'Ackah, Sabrina-Heman, MD, PhD' -> 'Sabrina-Heman Ackah, MD, PhD'
    L = [LASTFIRST.sub(r"\2 \1, \3", l) for l in L]
    for _ in range(3):                      # names can be split over 3 lines ('Rudi' / 'Scharnweber,' / 'MD, PhD')
        J = _join_split_names(L)
        if J == L: break
        L = J
    heads = sum(1 for l in L if heading_pgy(l) not in (False,))
    if _inline(L) >= 3 or heads < 2:
        return _parse_inline(L)
    return _parse_heading(L)

def _parse_heading(L):
    rows = _parse_heading_mode(L, bare=False)
    return rows if rows else _parse_heading_mode(L, bare=True)

def _parse_heading_mode(L, bare):
    out, seen, cur, started = [], set(), False, False
    for l in L:
        h = heading_pgy(l)
        if h is not False:
            cur = None if h == "chief" else h; started = True; continue
        # section headings are short and capitalised; Mayo bios wrap mid-sentence ('fellow in gynecologic oncology')
        if started and STOP.match(l) and l[:1].isupper() and len(l) < 50 and out: break
        if not started or NOISE.search(l): continue
        m = NAME.match(l) if not bare else (BARE.match(l) if not NOTNAME.search(l) else None)
        if m:
            n = m.group(1).strip()
            if n not in seen:
                out.append((n, cur, "heading" + ("-bare" if bare else ""))); seen.add(n)
    return out

def _parse_inline(L):
    out, seen = [], set()
    for k, l in enumerate(L):
        if NOISE.search(l): continue
        m = NAME.match(l)
        if not m: continue
        n = m.group(1).strip()
        pgy = None
        for x in L[k + 1:k + 5]:
            p = re.search(r"PGY[\s-]*(\d)", x)
            if p: pgy = int(p.group(1)); break
            if NAME.match(x): break
        if n not in seen:
            out.append((n, pgy, "inline" if pgy else "flat")); seen.add(n)
    return out
