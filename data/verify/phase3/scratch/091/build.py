import json
D="/Users/neureal/Documents/Residency Application Study/data/verify/phase3/"
inp={p["key"]:p for p in json.load(open(D+"batch_091_in.json"))}
out=[]
def add(key,identity,basis,res,outcome,detail,current,checks,sources,searches,abns=None,agrees=True,dis="",yl=None,dp=None,ds=None):
    p=inp[key]
    out.append({"key":key,"name":p["name"],"program_id":p["program_id"],"identity":identity,"identity_basis":basis,
    "residency_stated":res,"outcome":outcome,"outcome_detail":detail,"year_left":yl,"destination_program":dp,"destination_start_year":ds,
    "current":current,"agrees_with_db":agrees,"disagreement":dis,"checks":checks,"abns_certified":abns,"sources":sources,"searches_used":searches})
exec(open(D+"scratch/091/entries.py").read())
json.dump(out,open(D+"batch_091_out.json","w"),indent=1)
print(len(out))
