import json,sys,os
F='batch_124_out.json'
def add(e):
    d=json.load(open(F)) if os.path.exists(F) else []
    d=[x for x in d if x['key']!=e['key']]; d.append(e); json.dump(d,open(F,'w'),indent=1)
