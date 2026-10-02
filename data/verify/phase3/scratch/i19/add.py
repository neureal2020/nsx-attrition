import json,sys,os
base="/Users/neureal/Documents/Residency Application Study/data/verify/phase3/ident/"
inp=json.load(open(base+"i_19_in.json"))
outp=base+"i_19_out.json"
cur=json.load(open(outp)) if os.path.exists(outp) else []
rec=json.load(sys.stdin)
p=next(x for x in inp if x["key"]==rec["key"])
full={"key":p["key"],"name":p["name"],"program_id":p["program_id"]}
defaults={"year_left":None,"destination_program":None,"destination_start_year":None,"agrees_with_db":True,"disagreement":"","checks":{"google":"found","doximity":"not_found","usnews":"deferred"},"abns_certified":None}
full.update(defaults); full.update(rec)
full["searches_used"]=full.get("ident_searches",0)
cur=[c for c in cur if c["key"]!=rec["key"]]+[full]
order=[x["key"] for x in inp]
cur.sort(key=lambda c: order.index(c["key"]))
json.dump(cur,open(outp,"w"),indent=1)
print(len(cur))
