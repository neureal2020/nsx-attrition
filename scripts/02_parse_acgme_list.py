#!/usr/bin/env python3
"""Parse the ACGME 'List of Programs by Specialty' PDF (Report/1, specialty 160)
into a structured CSV. This is the AUTHORITATIVE program roster: it carries the
10-digit ACGME program ID, program director, accreditation status and effective date.

Column boundaries were read off the PDF's word x-positions (page width 792):
  name 38-170 | address 171-335 | director 336-397 | status 398-458 | date 459+
"""
import pdfplumber, re, csv, collections, sys

PDF = "data/raw/acgme_report1_neurosurg_2026-09-23.pdf"
OUT = "data/processed/acgme_neurosurgery_programs.csv"
BOUNDS = [(38,171,"name"), (171,336,"address"), (336,398,"director"),
          (398,459,"status"), (459,900,"effective")]
ID_RE = re.compile(r"^\[(\d{10})\]")

def col_for(x0):
    for lo,hi,nm in BOUNDS:
        if lo <= x0 < hi: return nm
    return None

records, cur, country = [], None, "US"
with pdfplumber.open(PDF) as pdf:
    for pg in pdf.pages:
        lines = collections.defaultdict(lambda: collections.defaultdict(list))
        for w in pg.extract_words():
            c = col_for(w["x0"])
            if c: lines[round(w["top"])][c].append((w["x0"], w["text"]))
        for top in sorted(lines):
            cols = {c: " ".join(t for _, t in sorted(v)) for c, v in lines[top].items()}
            nm = cols.get("name", "")
            # Country section headers appear alone in the name column
            if nm in ("United States", "Canada", "Puerto Rico") and len(cols) == 1:
                country = nm; continue
            if nm.startswith("Program Number") or nm.startswith("List of accredited") \
               or nm.startswith("Academic Year") or nm.startswith("Neurological Surgery Programs"):
                continue
            m = ID_RE.match(nm)
            if m:                                   # start of a new program record
                if cur: records.append(cur)
                cur = {"acgme_id": m.group(1), "country": country,
                       "name": ID_RE.sub("", nm).strip(),
                       "address": [], "director": [], "status": [], "effective": ""}
            if not cur: continue
            if not m and nm: cur["name"] += " " + nm
            for f in ("address", "director", "status"):
                if cols.get(f): cur[f].append(cols[f])
            if cols.get("effective") and not cur["effective"]:
                cur["effective"] = cols["effective"]
        if cur: records.append(cur); cur = None

EMAIL = re.compile(r"[\w.+-]+@[\w.-]+\.\w+")
# ZIP may appear as 5, 5-4, or 9 run-together digits (e.g. Stony Brook "117948122")
CSZ   = re.compile(r"^(.*),\s*([A-Z]{2})\s+(\d{5})(?:-?\d{4})?$")
rows = []
for r in records:
    addr = [a for a in r["address"] if not a.startswith("Ph:")]
    email = next((EMAIL.search(a).group(0) for a in r["address"] if EMAIL.search(a)), "")
    addr = [a for a in addr if not EMAIL.search(a)]
    city = state = zipc = ""
    for a in reversed(addr):
        m = CSZ.match(a.strip())
        if m: city, state, zipc = m.group(1).strip(), m.group(2), m.group(3); break
    phone = next((a.replace("Ph:","").strip() for a in r["address"] if a.startswith("Ph:")), "")
    rows.append({
        "acgme_id": r["acgme_id"],
        "program_name": re.sub(r"\s+", " ", r["name"]).strip(),
        "institution": addr[0] if addr else "",
        "city": city, "state": state, "zip": zipc, "country": r["country"],
        "phone": phone, "email": email,
        "program_director": re.sub(r"\s+", " ", " ".join(r["director"])).strip(),
        "accreditation_status": re.sub(r"\s+", " ", " ".join(r["status"])).strip(),
        "effective_date": r["effective"],
    })

with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

print(f"parsed {len(rows)} programs -> {OUT}")
for c, n in collections.Counter(x["country"] for x in rows).most_common(): print(f"  {c}: {n}")
print("\naccreditation status:")
for s, n in collections.Counter(x["accreditation_status"] for x in rows).most_common(): print(f"  {n:4d}  {s}")
print("\nsanity — first 3:")
for x in rows[:3]: print("  ", x["acgme_id"], "|", x["program_name"][:52], "|", x["city"], x["state"], "|", x["program_director"][:28])
bad = [x for x in rows if not x["state"]]
print(f"\nrows missing city/state: {len(bad)}")
for x in bad[:5]: print("   ", x["acgme_id"], x["program_name"][:50])
