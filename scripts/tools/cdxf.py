import sys, json, urllib.parse, time
sys.path.insert(0, "/Users/neureal/Documents/Residency Application Study/scripts")
from wayback import _get
def cdxf(url, regex, match="prefix", frm=None, to=None, limit=5000):
    q = [("url", url), ("matchType", match), ("output", "json"), ("fl", "timestamp,original"),
         ("filter", "statuscode:200"), ("filter", "original:" + regex), ("collapse", "urlkey"), ("limit", str(limit))]
    if frm: q.append(("from", frm))
    if to: q.append(("to", to))
    u = "http://web.archive.org/cdx/search/cdx?" + urllib.parse.urlencode(q)
    for a in range(6):
        try:
            raw = _get(u, timeout=300)
            if raw.lstrip()[:1] == b"[":
                rows = json.loads(raw or b"[]"); return rows[1:] if rows else []
        except Exception as e: pass
        time.sleep(min(90, 10 * 2 ** a))
    return None
if __name__ == "__main__":
    for host in sys.argv[2:]:
        r = cdxf(host, sys.argv[1], match="domain" if host.count(".")==1 else "prefix")
        print("==", host, None if r is None else len(r))
        for ts, o in (r or []): print("  ", ts[:8], o)
