"""Common Crawl lookup WITHOUT index.commoncrawl.org (down 2026-09-26).

Reads the raw CDXJ index on data.commoncrawl.org:
  1. binary-search cc-index/collections/<crawl>/indexes/cluster.idx (sorted by SURT key)
     with HTTP Range requests to find the index blocks covering a SURT prefix;
  2. fetch just those gzip blocks from cdx-NNNNN.gz and keep lines under the prefix;
  3. for roster-like URLs, fetch the WARC record and save the HTML.

    python3 cclocal.py OUTDIR YEAR0 YEAR1 SURT_PREFIX [SURT_PREFIX ...]
    e.g. SURT_PREFIX = "edu,duke,neurosurgery)/"   (www. is dropped in SURT)
"""
import sys, os, re, json, gzip, io, time, urllib.request

D = "https://data.commoncrawl.org/"
UA = {"User-Agent": "neurosurgery-attrition-research/1.0"}
ROST = re.compile(r"(?i)resident|residenc|housestaff|house-staff|alumni|trainee|graduat|page=res|meet|people|our-team|faculty-and-residents")

def rng(path, a, b):
    for t in range(6):
        try:
            req = urllib.request.Request(D + path, headers={**UA, "Range": f"bytes={a}-{b}"})
            return urllib.request.urlopen(req, timeout=120).read()
        except Exception:
            time.sleep(min(120, 5 * 2 ** t))
    raise RuntimeError(f"range failed {path} {a}-{b}")

_SIZES = {}
def size(path):
    """Total length via a 1-byte ranged GET (Content-Range); HEAD began returning 403."""
    if path not in _SIZES:
        for t in range(6):
            try:
                req = urllib.request.Request(D + path, headers={**UA, "Range": "bytes=0-0"})
                _SIZES[path] = int(urllib.request.urlopen(req, timeout=120).headers["Content-Range"].split("/")[-1]); break
            except Exception:
                time.sleep(min(120, 5 * 2 ** t))
        else:
            raise RuntimeError("size failed " + path)
    return _SIZES[path]

def line_at(path, pos, total):
    """First complete line starting at or after byte pos: (start_offset, line).
    Grows the read window when a line is longer than it (index lines can exceed 8 KB;
    the fixed 8 KB window broke the binary search, e.g. CC-MAIN-2023-23; fix from p11 phase 2)."""
    w = 8192
    while True:
        chunk = rng(path, pos, min(total - 1, pos + w - 1)).decode("utf-8", "replace")
        if pos:
            nl = chunk.find("\n")
            if nl < 0:
                if pos + w >= total: return None
                w *= 4; continue
            start, rest = pos + nl + 1, chunk[nl + 1:]
        else:
            start, rest = 0, chunk
        end = rest.find("\n")
        if end < 0 and pos + w < total:
            w *= 4; continue
        return (start, rest if end < 0 else rest[:end])

def blocks_for(crawl, prefix):
    path = f"cc-index/collections/{crawl}/indexes/cluster.idx"
    total = size(path)
    lo, hi = 0, total
    # find the last line whose key < prefix (the block that may contain the prefix start)
    best = None
    while hi - lo > 8192:
        mid = (lo + hi) // 2
        r = line_at(path, mid, total)
        if not r: hi = mid; continue
        key = r[1].split(" ", 1)[0]
        if key < prefix: lo = mid; best = r
        else: hi = mid
    # scan forward from lo collecting cluster lines until keys pass the prefix
    buf = rng(path, lo, min(total - 1, lo + 400000)).decode("utf-8", "replace").split("\n")[1 if lo else 0:]
    out, prev = [], None
    for ln in buf:
        if not ln.strip(): continue
        key = ln.split(" ", 1)[0]
        f = ln.split("\t")
        if key < prefix: prev = f; continue
        if prev is not None: out.append(prev); prev = None
        if not key.startswith(prefix):
            break
        out.append(f)
    if prev is not None and not out: out.append(prev)
    return out   # each: [key ts, cdx file, offset, length, seq]

def records(crawl, prefix):
    seen = set()
    for f in blocks_for(crawl, prefix):
        fn, off, ln = f[1], int(f[2]), int(f[3])
        if (fn, off) in seen: continue
        seen.add((fn, off))
        raw = rng(f"cc-index/collections/{crawl}/indexes/{fn}", off, off + ln - 1)
        for line in gzip.GzipFile(fileobj=io.BytesIO(raw)).read().decode("utf-8", "replace").splitlines():
            if line.startswith(prefix):
                surt, ts, js = line.split(" ", 2)
                yield json.loads(js) | {"timestamp": ts}

def warc_body(r):
    off, ln = int(r["offset"]), int(r["length"])
    raw = gzip.GzipFile(fileobj=io.BytesIO(rng(r["filename"], off, off + ln - 1))).read()
    return raw.split(b"\r\n\r\n", 2)[-1]      # bytes: HTML or PDF (Mayo 2015-16 roster was a PDF)

if __name__ == "__main__":
    out, y0, y1, prefixes = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4:]
    os.makedirs(out, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    crawls = sorted(c["id"] for c in json.load(open(os.path.join(here, "collinfo.json")))
                    if (m := re.search(r"CC-MAIN-(\d{4})", c["id"])) and y0 <= int(m.group(1)) <= y1)
    hits, failed = [], []
    for c in crawls:
        for p in prefixes:
            try:
                recs = list(records(c, p))
            except Exception as e:
                print("FAILED", c, p, e, flush=True); failed.append((c, p)); continue
            print("ok", c, p, len(recs), "records", flush=True)
            for r in recs:
                u = r.get("url", "")
                if r.get("status") != "200" or not ROST.search(u) or re.search(r"(?i)\.(jpg|jpeg|png|gif|css|js)$", u): continue
                try: body = warc_body(r)
                except Exception: print("WARCFAIL", u, flush=True); continue
                ext = ".pdf" if u.lower().endswith(".pdf") else ".html"
                fn = f"{out}/{r['timestamp']}_{re.sub(r'[^A-Za-z0-9]+', '_', u)[-80:]}{ext}"
                open(fn, "wb").write(body); hits.append((c, r["timestamp"], u, fn))
                print(c, r["timestamp"], u, flush=True)
    json.dump({"hits": hits, "failed": failed}, open(f"{out}/hits.json", "w"), indent=1)
    print("done", len(crawls), "crawls", flush=True)
