import json,sys,os
P="/Users/neureal/Documents/Residency Application Study/data/verify/phase3/"
def add(key,**kw):
    inp={p['key']:p for p in json.load(open(P+'batch_100_in.json'))}[key]
    out=json.load(open(P+'batch_100_out.json')) if os.path.exists(P+'batch_100_out.json') else []
    out=[o for o in out if o['key']!=key]
    e={"key":key,"name":inp['name'],"program_id":inp['program_id'],"year_left":None,"destination_program":None,"destination_start_year":None,"abns_certified":False}
    e.update(kw); out.append(e)
    order=[p['key'] for p in json.load(open(P+'batch_100_in.json'))]
    out.sort(key=lambda o:order.index(o['key']))
    json.dump(out,open(P+'batch_100_out.json','w'),indent=1)
