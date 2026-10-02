import json,sys,os
D="/Users/neureal/Documents/Residency Application Study/data/verify/phase3/"
inp={p["key"]:p for p in json.load(open(D+"batch_047_in.json"))}
outf=D+"batch_047_out.json"
out=json.load(open(outf)) if os.path.exists(outf) else []
def add(key,identity,basis,res,outcome,detail,current,agrees,dis,g,d,abns,sources,searches,yl=None,dest=None,dsy=None):
    p=inp[key]
    out[:]=[o for o in out if o["key"]!=key]
    out.append({"key":key,"name":p["name"],"program_id":p["program_id"],"identity":identity,"identity_basis":basis,
    "residency_stated":[{"institution":r[0],"specialty":"neurosurgery","start":r[1],"end":r[2]} for r in res],
    "outcome":outcome,"outcome_detail":detail,"year_left":yl,"destination_program":dest,"destination_start_year":dsy,
    "current":current,"agrees_with_db":agrees,"disagreement":dis,
    "checks":{"google":g,"doximity":d,"usnews":"deferred"},"abns_certified":abns,
    "sources":[{"url":s[0],"type":s[1],"evidence":s[2]} for s in sources],"searches_used":searches})
    order=list(inp)
    out.sort(key=lambda o:order.index(o["key"]))
    json.dump(out,open(outf,"w"),indent=1)
