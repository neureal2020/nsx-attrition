#!/usr/bin/env python3
"""Load the AANS neurosurgical residency directory into programs table."""
import sqlite3, re, sys, csv
from bs4 import BeautifulSoup

SRC = "data/raw/aans_directory_2026-09-23.html"
DB  = "db/neurosurgery_attrition.db"

US_STATES = set("""AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO
MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY DC PR""".split())
CA_PROV = set("AB BC MB NB NL NS ON PE QC SK".split())

def country_for(state):
    s = (state or "").strip()
    if s.upper() in US_STATES: return "US"
    if s.upper() in CA_PROV or s in ("Ontario","Quebec","Alberta","British Columbia","Manitoba","Nova Scotia","Saskatchewan","Newfoundland"): return "CA"
    return "MX" if s else "??"

soup = BeautifulSoup(open(SRC, encoding="utf-8", errors="replace").read(), "html.parser")

# The page also contains cookie-consent tables; the directory is the one whose
# header names the program column. Select it explicitly rather than by position.
directory = None
for t in soup.find_all("table"):
    first = t.find("tr")
    hdr = " ".join(c.get_text(" ", strip=True) for c in first.find_all(["td","th"])) if first else ""
    if "Residency Program" in hdr and "City" in hdr:
        directory = t; break
if directory is None:
    sys.exit("ERROR: could not locate the directory table in " + SRC)

seen, rows = set(), []
for tr in directory.find_all("tr"):
    cells = [td.get_text(" ", strip=True) for td in tr.find_all(["td","th"])]
    if len(cells) < 3: continue
    name, city, state = cells[0], cells[1], cells[2]
    if not name or name.lower().startswith("neurosurgical residency"): continue
    a = tr.find("a", href=True)
    url = a["href"].strip() if a else None
    key = (name.lower(), city.lower())
    if key in seen: continue
    seen.add(key)
    rows.append((name, city, state, country_for(state), url))

con = sqlite3.connect(DB)
con.execute('PRAGMA busy_timeout=60000'); cur = con.cursor()
cur.executemany(
    "INSERT INTO programs (name, city, state, country, website, source) VALUES (?,?,?,?,?,'AANS directory 2026-09-23')",
    rows)
con.commit()
print(f"inserted {len(rows)} programs")
for c, n in cur.execute("SELECT country, COUNT(*) FROM programs GROUP BY country ORDER BY 2 DESC"):
    print(f"  {c}: {n}")
print("with website:", cur.execute("SELECT COUNT(*) FROM programs WHERE website IS NOT NULL AND website<>''").fetchone()[0])
con.close()
