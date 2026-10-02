import json,os
IN=json.load(open('batch_156_in.json'))
P='batch_156_out.json'
def load(): return json.load(open(P)) if os.path.exists(P) else []
def add(idx, **k):
    out=load(); p=IN[idx]
    e={"key":p['key'],"name":p['name'],"program_id":p['program_id'],"identity":"confirmed","identity_basis":"","residency_stated":[],"outcome":"completed","outcome_detail":"","year_left":None,"destination_program":None,"destination_start_year":None,"current":"","agrees_with_db":True,"disagreement":"","checks":{"google":"found","doximity":"not_found","usnews":"deferred"},"abns_certified":None,"sources":[],"searches_used":2}
    e.update(k); out=[o for o in out if o['key']!=e['key']]; out.append(e)
    order={q['key']:i for i,q in enumerate(IN)}; out.sort(key=lambda o:order[o['key']])
    json.dump(out,open(P,'w'),indent=1)
