"""Authors whose PubMed affiliation matches a program's neurosurgery department, by year."""
import sys, json, re, time, urllib.request, urllib.parse, collections, xml.etree.ElementTree as ET
term, y0, y1, affre = sys.argv[1], sys.argv[2], sys.argv[3], re.compile(sys.argv[4], re.I)
E = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
def get(u):
    for a in range(5):
        try: time.sleep(0.4); return urllib.request.urlopen(u, timeout=60).read()
        except Exception: time.sleep(3 * (a + 1))
q = urllib.parse.urlencode({"db": "pubmed", "term": f"{term} AND {y0}:{y1}[dp]", "retmax": 5000, "retmode": "json"})
ids = json.loads(get(E + "esearch.fcgi?" + q))["esearchresult"]["idlist"]
print("pmids", len(ids), file=sys.stderr)
A = collections.defaultdict(set); P = collections.Counter()
for i in range(0, len(ids), 200):
    x = ET.fromstring(get(E + "efetch.fcgi?" + urllib.parse.urlencode({"db": "pubmed", "id": ",".join(ids[i:i+200]), "retmode": "xml"})))
    for art in x.iter("PubmedArticle"):
        yr = (art.findtext(".//PubDate/Year") or art.findtext(".//PubDate/MedlineDate") or "")[:4]
        for au in art.iter("Author"):
            affs = [a.text or "" for a in au.iter("Affiliation")]
            if any(affre.search(a) and len(a) < 400 for a in affs):
                n = f"{au.findtext('ForeName') or ''} {au.findtext('LastName') or ''}".strip()
                A[n].add(yr); P[n]+=1
for n, ys in sorted(A.items(), key=lambda x: min(x[1])):
    if len(ys) < int(sys.argv[5] if len(sys.argv) > 5 else 1): continue
    print(f"{n:35s} {min(ys)}-{max(ys)} years={len(ys)} papers={P[n]}")
