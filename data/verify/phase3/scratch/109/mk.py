import json,sys,os
D="/Users/neureal/Documents/Residency Application Study/data/verify/phase3/"
inp=json.load(open(D+"batch_109_in.json"))
out_p=D+"batch_109_out.json"
out=json.load(open(out_p)) if os.path.exists(out_p) else []
def add(key, identity, basis, resid, outcome, detail, current, dox, abns, sources, searches=2, google="found", year_left=None, agrees=True, dis=""):
    p=next(x for x in inp if x['key']==key)
    out[:]=[o for o in out if o['key']!=key]
    out.append({"key":key,"name":p['name'],"program_id":p['program_id'],"identity":identity,"identity_basis":basis,
     "residency_stated":resid,"outcome":outcome,"outcome_detail":detail,"year_left":year_left,"destination_program":None,"destination_start_year":None,
     "current":current,"agrees_with_db":agrees,"disagreement":dis,
     "checks":{"google":google,"doximity":dox,"usnews":"deferred"},"abns_certified":abns,
     "sources":[{"url":u,"type":t,"evidence":e} for u,t,e in sources],"searches_used":searches})
    order={x['key']:i for i,x in enumerate(inp)}
    out.sort(key=lambda o:order[o['key']])
    json.dump(out,open(out_p,"w"),indent=1)
    print(len(out))
IA="University of Iowa Hospitals and Clinics"
AL="https://neurosurgery.medicine.uiowa.edu/education/neurological-surgery-residency/our-people/alumni-residents"
