#!/usr/bin/env python3
"""Stream the NPPES monthly bulk file into a local index of INDIVIDUAL providers.

Why bulk rather than the API: the NPPES API caps a response at 200 records and
will not page past ~1000, so it cannot enumerate a specialty. The bulk file can,
it has no rate limit, and it is a fixed monthly snapshot -- so a reviewer can
reproduce any lookup exactly.

Streamed directly out of the .zip (the CSV is 11.7 GB uncompressed and the disk
has ~32 GB free).

Columns captured, and why:
  [13][14][19] Provider Other Last/First Name + Type Code
        -> FORMER AND MAIDEN NAMES. This is the authoritative fix for the
           surname-change bias: a resident who matched as one surname and
           practices under another is linkable here rather than being scored
           as attrition.
  [36] Enumeration Date -> NPIs are issued around medical-school graduation,
           so this approximates cohort year and disambiguates common names.
  [41] Provider Sex Code -> attrition by sex is a headline comparison in this
           literature; self-reported in the public file.
  [47..103] fifteen taxonomy slots -> specialty, and therefore specialty SWITCH.
"""
import zipfile, csv, io, sqlite3, sys, time

ZIP="data/raw/nppes/NPPES_September_2026_V2.zip"
MEMBER="npidata_pfile_20050523-20260913.csv"
DB="db/nppes.db"
TAX_IDX=[47,51,55,59,63,67,71,75,79,83,87,91,95,99,103]
NEURO_PREFIX="207T"          # 207T00000X Neurological Surgery

con=sqlite3.connect(DB)
con.executescript("""
PRAGMA journal_mode=OFF; PRAGMA synchronous=OFF; PRAGMA cache_size=-200000;
DROP TABLE IF EXISTS providers;
CREATE TABLE providers(
  npi TEXT PRIMARY KEY, last TEXT, first TEXT, middle TEXT, credential TEXT,
  other_last TEXT, other_first TEXT, other_last_type TEXT,
  sex TEXT, state TEXT, enum_date TEXT, last_update TEXT, deact_date TEXT,
  tax_primary TEXT, tax_all TEXT, is_neurosurg INTEGER);
""")
cur=con.cursor()
t0=time.time(); n=0; kept=0; neuro=0; withother=0; batch=[]
z=zipfile.ZipFile(ZIP)
with z.open(MEMBER) as fh:
    rd=csv.reader(io.TextIOWrapper(fh,encoding="utf-8",errors="replace"))
    next(rd)
    for row in rd:
        n+=1
        if n%1000000==0:
            print(f"  {n:,} rows  kept={kept:,}  neuro={neuro:,}  {time.time()-t0:.0f}s",flush=True)
        try:
            if row[1]!="1": continue          # Entity Type 1 = individual
        except IndexError: continue
        taxes=[row[i].strip() for i in TAX_IDX if i<len(row) and row[i].strip()]
        isns=1 if any(t.startswith(NEURO_PREFIX) for t in taxes) else 0
        ol,of=row[13].strip(),row[14].strip()
        if ol or of: withother+=1
        if isns: neuro+=1
        kept+=1
        batch.append((row[0],row[5].strip(),row[6].strip(),row[7].strip(),row[10].strip(),
                      ol,of,row[19].strip(),row[41].strip(),row[31].strip(),
                      row[36].strip(),row[37].strip(),row[39].strip(),
                      taxes[0] if taxes else "", ",".join(taxes), isns))
        if len(batch)>=50000:
            cur.executemany("INSERT OR REPLACE INTO providers VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",batch)
            con.commit(); batch=[]
if batch:
    cur.executemany("INSERT OR REPLACE INTO providers VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",batch)
con.commit()
print(f"\nscanned {n:,} rows in {time.time()-t0:.0f}s")
print(f"  individual providers kept : {kept:,}")
print(f"  with a former/other name  : {withother:,}")
print(f"  neurological surgery (207T): {neuro:,}")
print("building indexes...",flush=True)
con.executescript("""
CREATE INDEX idx_last      ON providers(last);
CREATE INDEX idx_lastfirst ON providers(last,first);
CREATE INDEX idx_otherlast ON providers(other_last);
CREATE INDEX idx_neuro     ON providers(is_neurosurg);
CREATE INDEX idx_enum      ON providers(enum_date);
""")
con.commit()
print("done. db/nppes.db ready")
con.close()
