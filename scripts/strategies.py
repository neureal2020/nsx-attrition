#!/usr/bin/env python3
"""Per-program evidence-gathering strategies, in priority order.

Each strategy is a small function with the same signature so the runner can
execute them in order, log what happened, and fall through to the next when one
comes up empty. Ordering is a starting hypothesis; `strategy_log` records the
hit rate so it can be reordered on evidence.

Motivating case (SLU, program 60), which broke three assumptions at once:
  * the AANS-recorded URL 404s and was NEVER archived -- a wrong link, not a
    moved one;
  * the department is a DIVISION under /medicine/surgery/neurological-surgery/,
    so every "neurosurgery.<domain>" and "/neurosurgery/" guess missed it;
  * slu.edu/medicine is archived but slu.edu/medicine/surgery/* has ZERO
    Wayback captures, so historical roster reconstruction is impossible there
    and the program must fall through to non-Wayback strategies.
"""
import re, time, json
from urllib.parse import urlparse, urljoin
import requests

UA={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                 "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
NEURO=re.compile(r"neuro(?:logical)?[-_ ]?surg|nsgy",re.I)
ROSTER_SLUG=re.compile(r"\bresidents?\b|housestaff|house-staff|current-residents|our-residents",re.I)
ALUMNI_SLUG=re.compile(r"alumni|former-residents|past-residents|graduates?\b",re.I)
ANN_SLUG=re.compile(r"match|graduat|new-?residents?|welcome|congratulat|incoming|class-of",re.I)
SKIP_EXT=re.compile(r"\.(jpg|jpeg|png|gif|pdf|css|js|xml|shtml)$",re.I)

def get(u,t=25):
    try:
        r=requests.get(u,headers=UA,timeout=t,allow_redirects=True)
        return r if r.status_code==200 else None
    except Exception:
        return None

def registrable(h):
    p=[x for x in (h or "").lower().replace(":80","").split(".") if x]
    if len(p)>2 and p[-2] in ("ac","co","edu","gov") and len(p[-1])==2: return ".".join(p[-3:])
    return ".".join(p[-2:]) if len(p)>=2 else h

# ---------------------------------------------------------------- S1
def s1_resolve_site(ctx):
    """Confirm a working department URL. The recorded one is often wrong."""
    cands=[]
    if ctx.get("website"): cands.append(ctx["website"])
    email=(ctx.get("email") or "")
    regs=[]
    if "@" in email: regs.append(registrable(email.split("@")[-1]))
    if ctx.get("website"): regs.append(registrable(urlparse(ctx["website"]).netloc))
    seen=set(); regs=[r for r in regs if r and not (r in seen or seen.add(r))]
    for r in regs:
        cands += [f"https://neurosurgery.{r}/", f"https://{r}/neurosurgery/",
                  f"https://{r}/medicine/neurosurgery/",
                  f"https://{r}/medicine/neurological-surgery/"]
    for u in cands:
        r=get(u,t=18)
        if r and NEURO.search(r.text[:120000]):
            return {"status":"ok","url":r.url,"detail":"direct hit","n":1}
    return {"status":"empty","detail":f"{len(cands)} candidates, none resolved","n":0}

# ---------------------------------------------------------------- S2
def s2_sitemap_search(ctx):
    """Search the INSTITUTION sitemap for the department.

    This is what finds a department nested somewhere unguessable -- SLU's sits
    at /medicine/surgery/neurological-surgery/, under the surgery department.
    """
    regs=set()
    if ctx.get("website"): regs.add(registrable(urlparse(ctx["website"]).netloc))
    if "@" in (ctx.get("email") or ""): regs.add(registrable(ctx["email"].split("@")[-1]))
    found={"roster":[],"alumni":[],"announcement":[],"other":[]}
    total=0
    for reg in list(regs)[:3]:
        for base in (f"https://www.{reg}", f"https://{reg}"):
            r=get(base+"/sitemap.xml",t=45)
            if not r or "<loc" not in r.text: continue
            locs=re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", r.text)
            if "<sitemapindex" in r.text[:2000].lower():
                subs=[u for u in locs[:30]]
                locs=[]
                for su in subs:
                    sr=get(su,t=35)
                    if sr: locs += re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", sr.text)
            total+=len(locs)
            neuro=[u for u in locs if NEURO.search(u) and not SKIP_EXT.search(u)]
            for u in neuro:
                if ROSTER_SLUG.search(u): found["roster"].append(u)
                elif ALUMNI_SLUG.search(u): found["alumni"].append(u)
                elif ANN_SLUG.search(u): found["announcement"].append(u)
                else: found["other"].append(u)
            if neuro: break
        if any(found.values()): break
    n=sum(len(v) for v in found.values())
    return {"status":"ok" if n else "empty",
            "detail":f"scanned {total} sitemap urls; roster={len(found['roster'])} "
                     f"alumni={len(found['alumni'])} ann={len(found['announcement'])} "
                     f"other={len(found['other'])}",
            "n":n,"found":found}

# ---------------------------------------------------------------- S3
def s3_wayback_history(ctx):
    """Ask Wayback for the capture history of the pages S2 found.

    Returns empty for programs Wayback never crawled deeply (SLU: /medicine is
    archived, /medicine/surgery/* is not). A program-year with no capture is
    MISSING DATA and must never be scored as attrition.
    """
    import urllib.request, urllib.parse
    urls=(ctx.get("pages",{}).get("roster",[]) + ctx.get("pages",{}).get("alumni",[]))[:6]
    if not urls: return {"status":"skipped","detail":"no pages from S2","n":0}
    hist={}
    for u in urls:
        q=("http://web.archive.org/cdx/search/cdx?url="+urllib.parse.quote(u.replace("https://","").replace("http://",""))
           +"&output=json&fl=timestamp&filter=statuscode:200&collapse=timestamp:6&limit=400&from=2011")
        try:
            with urllib.request.urlopen(q,timeout=90) as fh:
                d=json.load(fh)[1:]
        except Exception:
            d=[]
        if d: hist[u]=sorted({r[0][:4] for r in d})
        time.sleep(1.5)                      # Wayback throttles aggressively
    n=sum(len(v) for v in hist.values())
    return {"status":"ok" if n else "empty",
            "detail":(f"{len(hist)}/{len(urls)} urls archived; "
                      f"years={sorted({y for v in hist.values() for y in v})}") if n
                     else f"0/{len(urls)} urls have ANY capture",
            "n":n,"history":hist}

# ---------------------------------------------------------------- S4
def s4_parse_live_roster(ctx):
    """Parse the CURRENT roster. Always available; gives one year only."""
    import sys; sys.path.insert(0,"scripts")
    from roster_parser import parse
    urls=ctx.get("pages",{}).get("roster",[])[:5]
    best=None
    for u in urls:
        r=get(u,t=25)
        if not r: continue
        names=parse(r.text,main_only=True) or parse(r.text)
        if names and (best is None or len(names)>len(best[1])): best=(r.url,names)
    if not best: return {"status":"empty","detail":"no parseable roster","n":0}
    url,names=best
    return {"status":"ok","detail":f"{url} -> {len(names)} names "
            f"({sum(1 for n in names if n['pgy'])} with PGY)",
            "n":len(names),"url":url,"names":names}

# ---------------------------------------------------------------- S5
def s5_parse_alumni(ctx):
    """Parse the graduates/alumni page -- the program-side completion list."""
    import sys; sys.path.insert(0,"scripts")
    from roster_parser import parse
    urls=ctx.get("pages",{}).get("alumni",[])[:5]
    best=None
    for u in urls:
        r=get(u,t=25)
        if not r: continue
        names=parse(r.text,main_only=True) or parse(r.text)
        if names and (best is None or len(names)>len(best[1])): best=(r.url,names)
    if not best: return {"status":"empty","detail":"no parseable alumni page","n":0}
    url,names=best
    return {"status":"ok","detail":f"{url} -> {len(names)} names","n":len(names),
            "url":url,"names":names}

# ---------------------------------------------------------------- S6
def s6_announcements(ctx):
    """Parse match/graduation posts found by S2."""
    import sys; sys.path.insert(0,"scripts")
    from roster_parser import parse_announcement
    urls=ctx.get("pages",{}).get("announcement",[])[:30]
    if not urls: return {"status":"skipped","detail":"none found","n":0}
    events=[]
    for u in urls:
        r=get(u,t=20)
        if not r: continue
        try: p=parse_announcement(r.text)
        except Exception: continue
        if not p["type"] or p["n_people"]==0: continue
        near=[q for q in p["people"]
              if q.get("dist_from_cue") is None or q["dist_from_cue"]<=700]
        if not near or len(near)>8: continue
        events.append({"url":r.url,"type":p["type"],"date":p.get("date_text"),
                       "people":near})
    return {"status":"ok" if events else "empty",
            "detail":f"{len(events)} events from {len(urls)} urls","n":len(events),
            "events":events}

STRATEGIES=[("S1_resolve_site",s1_resolve_site),
            ("S2_sitemap_search",s2_sitemap_search),
            ("S3_wayback_history",s3_wayback_history),
            ("S4_parse_live_roster",s4_parse_live_roster),
            ("S5_parse_alumni",s5_parse_alumni),
            ("S6_announcements",s6_announcements)]
