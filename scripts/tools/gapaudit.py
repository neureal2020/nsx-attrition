"""Exhaustive gap-year audit: every URL captured on a program's hosts inside a
gap window, ANY status (200/301/302/404), filtered to roster-ish words.

    python3 gapaudit.py LABEL FROM TO HOST [HOST ...]
Prints: status, first capture in window, url.  3xx rows show where pages moved.
Lesson (Penn/Duke/Barrow 2026-09-27): "missing" years were almost always a
different host/path, a redirect, a roster embedded in a parent page, or a
firewall block page -- not the archive skipping the site.
"""
import sys, json, re, time, urllib.parse
sys.path.insert(0, "/Users/neureal/Documents/Residency Application Study/scripts")
from wayback import _get

KEY = re.compile(r"(?i)resid|house.?staff|trainee|people|meet|our.?team|class.?of|alumni|graduat|intern|headshot|profile|education|training|gme")
SKIP = re.compile(r"(?i)\.(css|js|woff2?|ttf|svg|ico)(\?|$)|/wp-(includes|content/plugins)/|clinical-briefings|/calendar|trumba")

def q(host, frm, to):
    p = [("url", host), ("matchType", "prefix"), ("output", "json"), ("fl", "timestamp,original,statuscode"),
         ("collapse", "urlkey"), ("from", frm), ("to", to), ("limit", "100000")]
    u = "http://web.archive.org/cdx/search/cdx?" + urllib.parse.urlencode(p)
    for a in range(7):
        try:
            raw = _get(u, timeout=600)
            if raw.lstrip()[:1] == b"[":
                rows = json.loads(raw or b"[]"); return rows[1:] if rows else []
        except Exception:
            pass
        time.sleep(min(120, 10 * 2 ** a))
    return None

if __name__ == "__main__":
    label, frm, to, hosts = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
    print(f"###### {label} {frm}-{to}", flush=True)
    for h in hosts:
        r = q(h, frm, to)
        if r is None: print("== FAILED", h, flush=True); continue
        hits = [(st, ts[:8], o) for ts, o, st in r if KEY.search(o) and not SKIP.search(o)]
        print(f"== {h}: {len(r)} urls captured in window, {len(hits)} roster-ish", flush=True)
        for st, ts, o in sorted(hits, key=lambda x: x[2].lower()):
            print(f"   {st} {ts} {o}", flush=True)
