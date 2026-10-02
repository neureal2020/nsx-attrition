import json,sys,os
out='data/verify/programs/x_recon_4_out.json'
rows=json.load(open(out)) if os.path.exists(out) else []
new=json.load(sys.stdin)
rows=[r for r in rows if r['program_id']!=new['program_id']]+[new]
json.dump(rows,open(out,'w'),indent=1,ensure_ascii=False); print(len(rows))
