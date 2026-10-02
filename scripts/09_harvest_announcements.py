#!/usr/bin/env python3
"""Harvest Match Day and graduation announcements from program websites.

These are the ENTRY and EXIT sources that do not depend on the roster page.
A roster is rewritten when someone leaves; a dated news post is not. Verified
shape (Pitt): a March post naming the incoming matched class with their medical
schools, and a June post naming the graduating class with fellowship
destinations.

Crawl plan per program:
  homepage -> find news/blog section (link text or conventional path)
           -> collect article links whose TITLE carries a match/graduation cue
           -> fetch each article, run parse_announcement()
Live sites only; no Wayback here, so there is no rate-limit budget to manage.
"""
import sqlite3, re, sys, time, json
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
sys.path.insert(0,"scripts")
from roster_parser import parse_announcement

DB="db/neurosurgery_attrition.db"
UA={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                 "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
NEWS_PATHS=["/news","/news-events","/news-and-events","/about/news","/blog",
            "/announcements","/newsroom","/about-us/news","/news/archive"]
NEWS_LINK=re.compile(r"\bnews\b|announcement|blog|newsroom|press",re.I)
# Titles worth opening. Deliberately broad here; parse_announcement classifies.
ART_CUE=re.compile(r"match|incoming|new resident|welcome|graduat|chief resident|"
                   r"class of|congratulat|commencement|intern class",re.I)
ART_NEG=re.compile(r"grant|award for|publish|study|trial|appointed|named chair|"
                   r"promoted|lecture|symposium|webinar|obituary|memoriam",re.I)

# An article must actually be ABOUT neurosurgery. Without this the crawler
# wanders into other departments on shared GME/medical-school sites -- the
# first run pulled USC OTOLARYNGOLOGY faculty into a "match" event.
NEURO_BODY=re.compile(r"neurosurg|neurological surgery|neuro-?surgical",re.I)

# A neurosurgery match class is ~1-5 and a graduating class ~1-5. Anything much
# larger is a department roster or an all-specialty GME page, not a cohort.
MAX_COHORT=8
# Names far from the classifying cue are incidental mentions (faculty quoted,
# award winners later in the article), not cohort members.
MAX_CUE_DIST=700

def get(u,t=20):
    try:
        r=requests.get(u,headers=UA,timeout=t,allow_redirects=True)
        if r.status_code==200 and "html" in r.headers.get("content-type",""): return r
    except Exception: pass
    return None

def same_host(a,b):
    return urlparse(a).netloc.split(":")[0].lower()==urlparse(b).netloc.split(":")[0].lower()

def find_news_sections(home_r):
    out=[]
    soup_links=re.findall(r'href="([^"]+)"[^>]*>([^<]{0,80})',home_r.text)
    for href,txt in soup_links:
        if NEWS_LINK.search(txt) or NEWS_LINK.search(href):
            full=urljoin(home_r.url,href)
            if same_host(full,home_r.url): out.append(full)
    root=f"{urlparse(home_r.url).scheme}://{urlparse(home_r.url).netloc}"
    out += [root+p for p in NEWS_PATHS[:5]]
    seen=set(); res=[]
    for u in out:
        k=u.rstrip("/").lower()
        if k in seen: continue
        seen.add(k); res.append(u)
    return res[:6]

def article_links(news_r):
    out=[]
    for href,txt in re.findall(r'href="([^"]+)"[^>]*>([^<]{5,140})',news_r.text):
        t=re.sub(r"\s+"," ",txt).strip()
        if not ART_CUE.search(t) or ART_NEG.search(t): continue
        full=urljoin(news_r.url,href)
        if not same_host(full,news_r.url): continue
        out.append((full,t))
    seen=set(); res=[]
    for u,t in out:
        k=u.rstrip("/").lower()
        if k in seen: continue
        seen.add(k); res.append((u,t))
    return res[:25]

NEURO_HOST=re.compile(r"neurosurg|neurological-?surg|nsgy",re.I)

def work(row):
    pid,name,homepage=row
    r=get(homepage)
    if not r: return pid,name,[]
    # Require a neurosurgery anchor on the seed itself, else the crawl is
    # scoped to a whole medical school and picks up every department.
    if not (NEURO_HOST.search(r.url) or NEURO_BODY.search(r.text[:200000])):
        return pid,name,[]
    found=[]
    for news_url in find_news_sections(r):
        nr=get(news_url,t=18)
        if not nr: continue
        for art_url,title in article_links(nr):
            ar=get(art_url,t=18)
            if not ar: continue
            try: p=parse_announcement(ar.text)
            except Exception: continue
            if not p["type"] or p["n_people"]==0: continue
            if not NEURO_BODY.search(p["body"] or ""): continue      # wrong department
            near=[q for q in p["people"]
                  if (q.get("dist_from_cue") is None or q["dist_from_cue"]<=MAX_CUE_DIST)]
            if not near: continue
            if len(near)>MAX_COHORT:                                  # roster, not a cohort
                continue
            p=dict(p); p["people"]=near; p["n_people"]=len(near)
            found.append({"url":ar.url,"title":title,"parsed":p})
            if len(found)>=20: break
        if len(found)>=20: break
    return pid,name,found

con=sqlite3.connect(DB)
con.execute('PRAGMA busy_timeout=60000')
progs=con.execute("""SELECT program_id, name, homepage FROM (
      SELECT l.program_id, p.name, l.homepage,
             ROW_NUMBER() OVER (PARTITION BY l.program_id ORDER BY l.id) rn
      FROM live_roster_urls l JOIN programs p USING(program_id)
      WHERE l.homepage IS NOT NULL AND l.homepage<>'' ) WHERE rn=1""").fetchall()
con.close()
print(f"crawling news sections for {len(progs)} programs",flush=True)

import pickle, os
CACHE="data/processed/09_crawl_cache.pkl"
res=[]
with ThreadPoolExecutor(max_workers=10) as ex:
    futs={ex.submit(work,p):p for p in progs}
    for i,f in enumerate(as_completed(futs),1):
        try: pid,name,found=f.result()
        except Exception as e: continue
        res.append((pid,found))
        with open(CACHE,"wb") as fh: pickle.dump(res,fh)   # crash-safe
        if found:
            kinds={}
            for x in found: kinds[x["parsed"]["type"]]=kinds.get(x["parsed"]["type"],0)+1
            print(f"[{i:3d}/{len(progs)}] {name[:38]:40s} posts={len(found):2d} {kinds}",flush=True)
        elif i%15==0:
            print(f"[{i:3d}/{len(progs)}] ...",flush=True)

con=sqlite3.connect(DB)
con.execute('PRAGMA busy_timeout=60000'); cur=con.cursor()
today=time.strftime("%Y-%m-%d"); ne=0; npl=0
for pid,found in res:
    for x in found:
        p=x["parsed"]
        yr=None
        m=re.search(r"\b(20\d{2})\b", (p.get("date_text") or "")+" "+x["title"])
        if m: yr=int(m.group(1))
        cur.execute("""INSERT OR IGNORE INTO cohort_events
            (program_id,event_type,event_date,event_year,source_url,source_type,
             retrieved_at,body_text) VALUES (?,?,?,?,?,'live',?,?)""",
            (pid, p["type"], p.get("date_text"), yr, x["url"], today, p["body"][:4000]))
        if cur.rowcount==0: continue
        ne+=1; eid=cur.lastrowid
        for per in p["people"]:
            cur.execute("""INSERT INTO cohort_event_people
                (event_id,name_as_listed,degrees,med_school,undergrad,raw_context)
                VALUES (?,?,?,?,?,?)""",
                (eid,per["name"],per.get("degrees"),per.get("med_school"),
                 per.get("undergrad"),per.get("context")[:300]))
            npl+=1
con.commit()
q=lambda s:cur.execute(s).fetchone()[0]
print(f"\n=== stored {ne} announcements, {npl} named people ===")
print("by type:")
for t,n in cur.execute("SELECT event_type,COUNT(*) FROM cohort_events GROUP BY 1 ORDER BY 2 DESC"): print(f"   {t}: {n}")
print("programs with >=1 match event :",q("SELECT COUNT(DISTINCT program_id) FROM cohort_events WHERE event_type='match'"))
print("programs with >=1 grad event  :",q("SELECT COUNT(DISTINCT program_id) FROM cohort_events WHERE event_type='graduation'"))
print("event years:", [r for r in cur.execute("SELECT event_year,COUNT(*) FROM cohort_events WHERE event_year IS NOT NULL GROUP BY 1 ORDER BY 1")])
con.close()
