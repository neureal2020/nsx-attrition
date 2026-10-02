import json,os
inp=json.load(open('batch_042_in.json'))
byk={p['key']:p for p in inp}
recs=json.load(open('scratch/042/recs.json')) if os.path.exists('scratch/042/recs.json') else {}
def add(k,**kw):
    p=byk[k]
    base={"key":k,"name":p['name'],"program_id":p['program_id'],"usnews_placeholder":None}
    base.update(kw)
    base.setdefault("checks",{})["usnews"]="deferred"
    base.setdefault("year_left",None);base.setdefault("destination_program",None);base.setdefault("destination_start_year",None)
    base.setdefault("disagreement","")
    recs[k]=base
    json.dump(recs,open('scratch/042/recs.json','w'),indent=1)
    out=[recs[q['key']] for q in inp if q['key'] in recs]
    for o in out: o.pop("usnews_placeholder",None)
    json.dump(out,open('batch_042_out.json','w'),indent=1)
