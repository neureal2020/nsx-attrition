"""Retry FAILED index/prefix pairs from a ccscan log, slowly, until they succeed (max 6 rounds)."""
import sys, re, time, subprocess
log, out = sys.argv[1], sys.argv[2]
pairs = sorted(set(re.findall(r"^FAILED (\S+) (\S+)$", open(log).read(), re.M)))
for rnd in range(6):
    left = []
    for idx, p in pairs:
        y = re.search(r"CC-MAIN-(\d{4})", idx).group(1)
        r = subprocess.run(["python3", "ccscan_one.py", out, idx, p], capture_output=True, text=True)
        print(r.stdout.strip(), flush=True)
        if "FAILED" in r.stdout: left.append((idx, p))
    pairs = left
    if not pairs: break
    time.sleep(600)
print("retry done; still failing:", pairs, flush=True)
