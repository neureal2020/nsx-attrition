"""Scan EVERY Common Crawl index in a year range for roster-like URLs on given hosts/prefixes; save HTML."""
import sys, json, re, os, urllib.parse, urllib.request, gzip, io, time
OUT = sys.argv[1]; y0, y1 = int(sys.argv[2]), int(sys.argv[3]); prefixes = sys.argv[4:]
os.makedirs(OUT, exist_ok=True)
UA = {"User-Agent": "neurosurgery-attrition-research/1.0"}
def get(u, headers=None, timeout=120, tries=7):
    h = dict(UA); h.update(headers or {})
    for a in range(tries):
        try: return urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=timeout).read()
        except urllib.error.HTTPError as e:
            if e.code == 404: return b""
            time.sleep(min(120, 10 * 2 ** a))
        except Exception: time.sleep(min(120, 10 * 2 ** a))
    return None
coll = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "collinfo.json")))  # cached: the live endpoint times out
idxs = sorted(c["id"] for c in coll if re.search(r"CC-MAIN-(\d{4})", c["id"]) and y0 <= int(re.search(r"CC-MAIN-(\d{4})", c["id"]).group(1)) <= y1)
ROST = re.compile(r"(?i)resident|housestaff|house-staff|alumni|trainee|graduat|page=res")
hits = []; failed = []
for idx in idxs:
    for p in prefixes:
        b = get(f"https://index.commoncrawl.org/{idx}-index?url={urllib.parse.quote(p + '*', safe='')}&output=json")
        if b is None or b.lstrip()[:1] == b"<":
            print("FAILED", idx, p, flush=True); failed.append((idx, p)); continue
        print("ok", idx, p, len(b.splitlines()), "records", flush=True)
        for line in b.decode("utf-8", "replace").splitlines():
            try: r = json.loads(line)
            except Exception: continue
            if not ROST.search(r["url"]) or re.search(r"(?i)\.(jpg|png|gif|pdf|css|js)$", r["url"]) or r.get("status") != "200": continue
            raw = get("https://data.commoncrawl.org/" + r["filename"], headers={"Range": f"bytes={int(r['offset'])}-{int(r['offset'])+int(r['length'])-1}"})
            try: html = gzip.GzipFile(fileobj=io.BytesIO(raw)).read().decode("utf-8", "replace").split("\r\n\r\n", 2)[-1]
            except Exception: continue
            fn = f"{OUT}/{r['timestamp']}_{re.sub(r'[^A-Za-z0-9]+','_',r['url'])[-80:]}.html"
            open(fn, "w").write(html); hits.append((idx, r["timestamp"], r["url"], fn))
            print(idx, r["timestamp"], r["url"], flush=True)
json.dump({"hits": hits, "failed": failed}, open(f"{OUT}/hits.json", "w"), indent=1)
print("done", len(idxs), "indexes")
