import json,os
D="/Users/neureal/Documents/Residency Application Study/data/verify/phase3/"
inp=json.load(open(D+"batch_106_in.json"))
byk={p["key"]:p for p in inp}
F=D+"scratch/106/entries.json"
ents=json.load(open(F)) if os.path.exists(F) else {}
def add(key,**kw):
    p=byk[key]
    e={"key":key,"name":p["name"],"program_id":p["program_id"],"year_left":None,"destination_program":None,"destination_start_year":None,"abns_certified":False,"usnews_note":None}
    e.update(kw)
    e["checks"]={**e.pop("checks"),"usnews":"deferred"}
    ents[key]=e
    json.dump(ents,open(F,"w"),indent=1)
    out=[ents[p["key"]] for p in inp if p["key"] in ents]
    json.dump(out,open(D+"batch_106_out.json","w"),indent=1)
