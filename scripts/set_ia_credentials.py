#!/usr/bin/env python3
"""Write Internet Archive S3 credentials to a private local file.

The SECRET key is read from the macOS clipboard (pbpaste) so it is never typed
as a shell argument -- shell arguments land in shell history and in the process
table where other users can see them. The secret is never printed back; only a
masked confirmation is shown.

Usage:
    python3 scripts/set_ia_credentials.py --access-key <YOUR_ACCESS_KEY>
    python3 scripts/set_ia_credentials.py --clear
"""
import argparse, os, pathlib, subprocess, sys, re, stat
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ia_creds import CRED_PATH

def clipboard():
    try:
        out=subprocess.run(["pbpaste"],capture_output=True,text=True,timeout=10)
        return out.stdout.strip()
    except FileNotFoundError:
        sys.exit("pbpaste not found (this helper assumes macOS).")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--access-key")
    ap.add_argument("--secret-key", help="avoid; prefer the clipboard so it stays out of shell history")
    ap.add_argument("--clear", action="store_true")
    a=ap.parse_args()

    if a.clear:
        if CRED_PATH.exists(): CRED_PATH.unlink(); print(f"removed {CRED_PATH}")
        else: print("nothing to remove")
        return

    if not a.access_key: sys.exit("--access-key is required")
    secret = a.secret_key or clipboard()
    if not secret: sys.exit("clipboard was empty -- copy the SECRET key, then rerun")

    # IA S3 secret keys are short opaque tokens; a long multi-line paste almost
    # certainly means the wrong thing got copied.
    if "\n" in secret or len(secret) > 64:
        sys.exit(f"clipboard does not look like a secret key "
                 f"(len {len(secret)}, {secret.count(chr(10))+1} lines). Nothing written.")
    if not re.fullmatch(r"[A-Za-z0-9+/=_-]{8,64}", secret):
        sys.exit("clipboard does not look like a key (unexpected characters). Nothing written.")
    if secret == a.access_key:
        sys.exit("clipboard matches the ACCESS key -- you probably copied the wrong one.")

    CRED_PATH.parent.mkdir(parents=True, exist_ok=True)
    os.umask(0o077)
    CRED_PATH.write_text(
        "# Internet Archive S3 keys -- https://archive.org/account/s3.php\n"
        "# Written by scripts/set_ia_credentials.py. Keep private.\n"
        f"IA_ACCESS_KEY={a.access_key}\n"
        f"IA_SECRET_KEY={secret}\n")
    CRED_PATH.chmod(stat.S_IRUSR|stat.S_IWUSR)   # 0600
    mode=oct(CRED_PATH.stat().st_mode & 0o777)
    print(f"wrote {CRED_PATH}  (mode {mode})")
    print(f"  IA_ACCESS_KEY = {a.access_key}")
    print(f"  IA_SECRET_KEY = {secret[:3]}{'*'*(len(secret)-3)}  (len {len(secret)}, not echoed)")

if __name__=="__main__": main()
