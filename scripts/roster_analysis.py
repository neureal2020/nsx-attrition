"""Shared analysis for extracted roster captures (one program).

    from roster_analysis import content_date, choose, class_table, dropouts

Input `R`: list of {"ts","ay","url","rows":[[name,pgy,ctx],...]} from any
extractor. Steps, as applied to Barrow/Hopkins/Northwestern:
  content_date(R) -> {ts: offset}; a capture whose PGYs are uniformly one year
                     behind (+1) / ahead (-1) of each person's modal entry year
                     is stale / pre-updated and is relabelled by content.
  choose(R, shift) -> {content_ay: capture}; prefer Aug-Jan captures (July is
                     often last year, spring adds matched interns), then the
                     largest list.
  class_table(pick) -> {entry_year: [(name, first_ay, last_ay, last_pgy, n_entry_estimates)]}
  dropouts(pick, terminal=7) -> people last seen below terminal PGY, before
                     the latest year -- candidates for Google/US News checks.
"""
import collections

def _entries(R):
    imp = collections.defaultdict(list)
    for r in R:
        y = int(r["ay"][:4])
        for n, p, *_ in r["rows"]:
            if p: imp[n].append(y - p + 1)
    return {n: collections.Counter(v).most_common(1)[0][0] for n, v in imp.items()}

def content_date(R):
    mode = _entries(R); shift = {}
    for r in R:
        y = int(r["ay"][:4])
        c = collections.Counter((y - p + 1) - mode[n] for n, p, *_ in r["rows"] if p)
        if c:
            off, k = c.most_common(1)[0]
            if off and k >= 0.6 * sum(c.values()): shift[r["ts"]] = off
    return shift

def cay(r, shift):
    y = int(r["ay"][:4]) - shift.get(r["ts"], 0); return f"{y}-{y+1}"

def choose(R, shift):
    by = {}
    for r in R:
        if r["rows"]: by.setdefault(cay(r, shift), []).append(r)
    pick = {}
    for ay, L in by.items():
        fall = [r for r in L if r["ts"][4:6] in ("08", "09", "10", "11", "12", "01")] or L
        big = max(len(r["rows"]) for r in fall)
        cand = [r for r in fall if len(r["rows"]) >= big - 1]
        pick[ay] = cand[len(cand) // 2]
    return pick

def people(pick):
    P = {}
    for ay, r in sorted(pick.items()):
        for n, p, *_ in r["rows"]:
            if p: P.setdefault(n, {})[ay] = p
    return P

def class_table(pick):
    P = people(pick); cls = {}
    for n, d in P.items():
        ents = collections.Counter(int(a[:4]) - p + 1 for a, p in d.items())
        e = ents.most_common(1)[0][0]; last = max(d)
        cls.setdefault(e, []).append((n, min(d), last, d[last], len(ents)))
    return cls

def dropouts(pick, terminal=7):
    P = people(pick); latest = max(pick)
    out = []
    for n, d in P.items():
        last = max(d)
        if last < latest and d[last] < terminal:
            nxt = [a for a in pick if a > last]
            out.append((n, last, d[last], min(nxt) if nxt else None))
    return sorted(out, key=lambda x: x[1])
