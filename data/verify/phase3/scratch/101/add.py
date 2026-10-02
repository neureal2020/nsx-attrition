import json,sys,os
out='batch_101_out.json'
cur=json.load(open(out)) if os.path.exists(out) else []
new=json.load(sys.stdin)
have={c['key'] for c in cur}
cur+= [n for n in new if n['key'] not in have]
json.dump(cur,open(out,'w'),indent=1)
print(len(cur))
