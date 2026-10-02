"""For a program's gap years: fetch every distinct capture of seed pages (home,
residency/education pages) in the window, collect every link whose URL or anchor
text looks like a roster, then list each target's captures inside the window."""
import sys, re, json, urllib.parse
sys.path.insert(0, "/Users/neureal/Documents/Residency Application Study/scripts")
from wayback import cdx, fetch
ROST = re.compile(r"(?i)resident|house.?staff|trainee|people|our.?team|current|meet|class|intern")
def audit(seeds, frm, to):
    targets = {}
    for sd in seeds:
        try: caps = cdx(sd, collapse="digest", frm=frm, to=to)
        except Exception: caps = []
        for c in caps[:12]:
            s = fetch(c["timestamp"], c["original"]) or ""
            for m in re.finditer(r'(?is)<a[^>]+href="([^"#]+)"[^>]*>(.*?)</a>', s):
                href, txt = m.group(1), re.sub(r"<[^>]+>", " ", m.group(2)).strip()
                if re.search(r"(?i)\.(jpg|png|pdf|gif|css|js)$|mailto:|javascript:|facebook|twitter|linkedin|youtube", href): continue
                if not (ROST.search(href) or ROST.search(txt)): continue
                if re.search(r"(?i)patient|faculty|fellow|nurse|clinical.?trial|news|event|job|career", href + " " + txt): continue
                u = urllib.parse.urljoin(c["original"], href)
                u = re.sub(r"^https?://web\.archive\.org/web/\d+(id_)?/", "", u)
                targets.setdefault(u, set()).add(txt[:40])
    out = []
    for u, t in sorted(targets.items()):
        base = re.sub(r"^https?://", "", u).replace(":80/", "/")
        try: caps = cdx(base, collapse="digest", frm=frm, to=to)
        except Exception: caps = None
        out.append((u, sorted(t)[:2], None if caps is None else [c["timestamp"][:8] for c in caps]))
    return out
if __name__ == "__main__":
    cfg = json.loads(sys.argv[1])
    for u, t, caps in audit(cfg["seeds"], cfg["frm"], cfg["to"]):
        if caps: print(caps[:12], u, t)
    print("done")
