import json,glob,sys,re
files=['data/verify/phase3/merged_final.json']+glob.glob('data/verify/phase3/gold/*_out.json')+glob.glob('data/verify/phase3/ident/*_out.json')+glob.glob('data/verify/phase3/dest/**/*_out.json',recursive=True)+glob.glob('data/verify/programs/*_out.json')
pat=re.compile(sys.argv[1],re.I)
def walk(o,path,f):
    s=json.dumps(o)
    if not pat.search(s): return
    if len(s)<2500 or not isinstance(o,(dict,list)):
        print(f,path,s);print();return
    items=o.items() if isinstance(o,dict) else enumerate(o)
    for k,v in items: walk(v,f'{path}/{k}',f)
for f in files:
    try: d=json.load(open(f))
    except Exception: continue
    walk(d,'',f)
