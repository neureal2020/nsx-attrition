#!/usr/bin/env python3
"""Load Internet Archive S3 credentials.

Stored OUTSIDE the project directory (~/.config/nsx-attrition/ia.env, mode 0600)
so they cannot be committed by accident if this folder ever becomes a git repo.
Environment variables win if set, so CI or a one-off shell can override.
"""
import os, pathlib

CRED_PATH = pathlib.Path.home()/".config"/"nsx-attrition"/"ia.env"

def load():
    ak, sk = os.environ.get("IA_ACCESS_KEY"), os.environ.get("IA_SECRET_KEY")
    if ak and sk: return ak, sk
    if CRED_PATH.exists():
        vals={}
        for line in CRED_PATH.read_text().splitlines():
            line=line.strip()
            if not line or line.startswith("#") or "=" not in line: continue
            k,_,v=line.partition("=")
            vals[k.strip()]=v.strip().strip('"').strip("'")
        return vals.get("IA_ACCESS_KEY"), vals.get("IA_SECRET_KEY")
    return None, None

def require():
    ak, sk = load()
    if not (ak and sk):
        raise SystemExit(
            f"No Internet Archive credentials found.\n"
            f"  Run: python3 scripts/set_ia_credentials.py --access-key <KEY>\n"
            f"  (reads the SECRET key from your clipboard)\n"
            f"  Or set IA_ACCESS_KEY / IA_SECRET_KEY in the environment.")
    return ak, sk

if __name__=="__main__":
    ak, sk = load()
    def mask(v): return "(not set)" if not v else f"{v[:4]}{'*'*max(0,len(v)-4)} (len {len(v)})"
    print(f"  credentials file: {CRED_PATH}  exists={CRED_PATH.exists()}")
    print(f"  IA_ACCESS_KEY : {mask(ak)}")
    print(f"  IA_SECRET_KEY : {mask(sk)}")
