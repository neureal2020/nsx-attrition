"""Polite Wayback Machine access: CDX queries and snapshot fetches with a disk
cache and backoff when the archive throttles.

    from wayback import cdx, fetch
    caps = cdx("neurosurgery.pitt.edu/training/residency-program/current-residents",
               collapse="digest")            # one row per distinct content version
    html = fetch(caps[0]["timestamp"], caps[0]["original"])

Throttling does not look like an error: CDX answers 200 with an HTML page
instead of rows, so an empty-looking result must be retried, not trusted.
(Pitt, 2026-09: five roster URLs "had no captures" until retried slowly.)

collapse="digest" is the useful default for rosters: it returns only captures
whose CONTENT changed, which both minimises fetches and exposes stale pages --
Pitt's old static roster carried the same 2003 list in captures through 2011.
"""
import hashlib, json, os, time, urllib.parse, urllib.request

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "raw", "wayback_cache")
os.makedirs(CACHE, exist_ok=True)
_last = [0.0]

def _get(url, timeout=120):
    wait = max(0.0, 2.5 - (time.time() - _last[0]))      # >= 2.5 s between requests
    time.sleep(wait)
    _last[0] = time.time()
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()

def _cached(url):
    return os.path.join(CACHE, hashlib.md5(url.encode()).hexdigest())

def cdx(url, match="exact", collapse="digest", frm=None, to=None, tries=6):
    q = {"url": url, "output": "json", "fl": "timestamp,original,digest,length",
         "filter": "statuscode:200", "matchType": match}
    if collapse: q["collapse"] = collapse
    if frm: q["from"] = frm
    if to: q["to"] = to
    full = "http://web.archive.org/cdx/search/cdx?" + urllib.parse.urlencode(q)
    for a in range(tries):
        try:
            raw = _get(full)
            if raw.lstrip()[:1] in (b"[",):
                rows = json.loads(raw or b"[]")
                if not rows: return []
                head = rows[0]
                return [dict(zip(head, r)) for r in rows[1:]]
        except Exception:
            pass
        time.sleep(min(90, 10 * 2 ** a))                  # throttled: back off
    raise RuntimeError(f"CDX kept failing for {url}")

def fetch(ts, original, tries=5):
    """Original archived bytes (id_ = no Wayback toolbar), cached on disk."""
    url = f"https://web.archive.org/web/{ts}id_/{original}"
    f = _cached(url)
    if os.path.exists(f):
        return open(f, encoding="utf-8", errors="replace").read()
    for a in range(tries):
        try:
            raw = _get(url)
            if raw[:2] == b"\x1f\x8b":
                import gzip; raw = gzip.decompress(raw)
            s = raw.decode("utf-8", "replace")
            open(f, "w", encoding="utf-8").write(s)
            return s
        except Exception:
            time.sleep(min(90, 10 * 2 ** a))
    return None

def academic_year(ts):
    y, m = int(ts[:4]), int(ts[4:6])
    return f"{y}-{y+1}" if m >= 7 else f"{y-1}-{y}"
