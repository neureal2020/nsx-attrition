import json,sys
inp={p['key']:p for p in json.load(open('batch_131_in.json'))}
out=[]
def add(key,ident,basis,res,outcome,detail,cur,agrees,dis,g,dx,abns,src,n,extra=None):
    p=inp[key]
    d={"key":key,"name":p['name'],"program_id":p['program_id'],"identity":ident,"identity_basis":basis,
    "residency_stated":res,"outcome":outcome,"outcome_detail":detail,"year_left":None,"destination_program":None,"destination_start_year":None,
    "current":cur,"agrees_with_db":agrees,"disagreement":dis,"checks":{"google":g,"doximity":dx,"usnews":"deferred"},
    "abns_certified":abns,"sources":[{"url":u,"type":t,"evidence":e} for u,t,e in src],"searches_used":n}
    if extra: d.update(extra)
    out.append(d)
USC="University of Southern California/Los Angeles General Medical Center"
def usc(s,e): return [{"institution":USC,"specialty":"neurosurgery","start":s,"end":e}]
