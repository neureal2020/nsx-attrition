import json,os,sys
IN='batch_085_in.json'; OUT='batch_085_out.json'
inp={p['key']:p for p in json.load(open(IN))}
def load():
    return json.load(open(OUT)) if os.path.exists(OUT) else []
def add(key,identity,basis,res,outcome,detail,current,agrees,dis,g,d,srcs,abns=None,searches=2,yl=None,dest=None,dsy=None):
    p=inp[key]; L=[x for x in load() if x['key']!=key]
    L.append({"key":key,"name":p['name'],"program_id":p['program_id'],"identity":identity,"identity_basis":basis,
    "residency_stated":[{"institution":r[0],"specialty":"neurosurgery","start":r[1],"end":r[2]} for r in res],
    "outcome":outcome,"outcome_detail":detail,"year_left":yl,"destination_program":dest,"destination_start_year":dsy,
    "current":current,"agrees_with_db":agrees,"disagreement":dis,
    "checks":{"google":g,"doximity":d,"usnews":"deferred"},"abns_certified":abns,
    "sources":[{"url":u,"type":t,"evidence":e} for u,t,e in srcs],"searches_used":searches})
    order=[q['key'] for q in json.load(open(IN))]
    L.sort(key=lambda x:order.index(x['key']))
    json.dump(L,open(OUT,'w'),indent=1)
