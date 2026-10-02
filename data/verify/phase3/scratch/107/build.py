import json,os,sys
IN=json.load(open('batch_107_in.json'))
byk={p['key']:p for p in IN}
OUT='batch_107_out.json'
recs=json.load(open(OUT)) if os.path.exists(OUT) else []
have={r['key'] for r in recs}
UIC="University of Illinois College of Medicine at Chicago"
def add(key,identity,basis,resid,outcome,detail,current,agrees,dis,g,d,src,ns,abns=None,yl=None,dest=None,dsy=None):
    if key in have: return
    p=byk[key]
    recs.append({"key":key,"name":p['name'],"program_id":p['program_id'],"identity":identity,"identity_basis":basis,
    "residency_stated":resid,"outcome":outcome,"outcome_detail":detail,"year_left":yl,"destination_program":dest,"destination_start_year":dsy,
    "current":current,"agrees_with_db":agrees,"disagreement":dis,"checks":{"google":g,"doximity":d,"usnews":"deferred"},
    "abns_certified":abns,"sources":[{"url":u,"type":t,"evidence":e} for u,t,e in src],"searches_used":ns})
    have.add(key)
def save():
    json.dump(recs,open(OUT,'w'),indent=1)
