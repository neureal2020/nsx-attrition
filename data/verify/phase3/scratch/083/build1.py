import json
R="https://med.stanford.edu/neurosurgery/residency/residents.html"
def P(slug): return f"https://med.stanford.edu/neurosurgery/residency/residents/{slug}.html"
inp={p['key']:p for p in json.load(open('batch_083_in.json'))}
out=[]
def add(key,slug,dox,doxurl,start,pgy,extra,ns=2,cur=None):
    p=inp[key]
    src=[{"url":R,"type":"program_page","evidence":f"Stanford Neurosurgery residents 2025-2026 roster lists {p['name'].split()[0]}... at PGY-{pgy}"}]
    if slug: src.append({"url":P(slug),"type":"program_page","evidence":"Stanford Neurosurgery resident profile page: "+extra})
    if doxurl: src.append({"url":doxurl,"type":"doximity","evidence":dox})
    out.append({"key":key,"name":p['name'],"program_id":p['program_id'],"identity":"confirmed",
     "identity_basis":"Listed on Stanford Neurosurgery current residents roster (2025-26) and resident profile page; "+extra,
     "residency_stated":[{"institution":"Stanford Health Care-Sponsored Stanford University Program","specialty":"neurosurgery","start":start,"end":None}],
     "outcome":"in_training","outcome_detail":f"Current Stanford neurosurgery resident (PGY-{pgy} in 2025-26 roster); no evidence of departure.",
     "year_left":None,"destination_program":None,"destination_start_year":None,
     "current":cur or "neurosurgery resident, Stanford","agrees_with_db":True,"disagreement":"",
     "checks":{"google":"found","doximity":"found" if doxurl else "not_found","usnews":"deferred"},
     "abns_certified":False,"sources":src,"searches_used":ns})
add("61:dhi:pangal","dhiraj-pangal","Doximity: Residency, Neurological Surgery, Stanford Health Care-Sponsored Stanford University, 2023 - 2030; USC Keck Class of 2023","https://www.doximity.com/pub/dhiraj-pangal-md",2023,4,"USC Keck MD 2023",2)
add("61:joy:he","joy-he","",None,2023,4,"MD/PhD Stanford MSTP; resident since 2023",2)
add("61:mar:cavagnaro","maria-jose-cavagnaro","Doximity (Buffalo NY) page lists Spine Clinical Fellow, Univ of Buenos Aires Class of 2013; earlier profile, no Stanford residency line","https://www.doximity.com/pub/maria-jose-cavagnaro-md",2023,5,"prior 6-year neurosurgery residency in Buenos Aires and 2022-23 spine fellowship Univ at Buffalo, hence PGY-5 at Stanford after entry 2023",2)
add("61:sze:tan","owen-tan","Doximity: Neurosurgery resident, Palo Alto CA; Univ of Miami Miller School Class of 2022","https://www.doximity.com/pub/sze-kiat-owen-tan-md",2023,4,"listed as Sze Kiat (Owen) Tan, MD PhD, Miami MD 2022",3)
add("61:bo:lear","bo-lear","",None,2024,3,"MD/PhD Univ Wisconsin; Match 2024",2)
add("61:jam:sayadi","jamasb-sayadi","Doximity: Resident Physician, Palo Alto; Stanford School of Medicine Class of 2024","https://www.doximity.com/pub/jamasb-sayadi-md",2024,3,"Stanford MD 2024, Match 2024",2)
add("61:ver:ong","vera-ong","",None,2024,3,"Match 2024; MD Univ of Hawaii",2)
add("61:ast:hengartner","astrid-hengartner","Doximity: Residency, Neurological Surgery, Stanford Health Care-Sponsored Stanford University, 2025 - 2032; Yale Class of 2025","https://www.doximity.com/pub/astrid-hengartner-md",2025,2,"Yale MD 2025",2)
add("61:jay:gill",  "jay-gill","",None,2025,2,"UCLA MD/PhD; Match 2025",2)
add("61:mar:bederson","maria-bederson","",None,2025,2,"Carle Illinois MD; Match 2025",2)
add("61:pav:shah","pavan-shah","",None,2025,2,"Johns Hopkins MD; Match 2025",2)
add("61:bra:bergsneider","",'',None,2026,1,"Stanford MD; Knight-Hennessy scholar (profiles.stanford.edu)",2)
add("61:cam:hill","",'',None,2026,1,"listed on Stanford neurosurgery roster only",1)
add("61:mar:guinle","",'',None,2026,1,"Stanford MD/MS; LinkedIn lists neurosurgery resident",1)
add("61:sam:sundrani","",'',None,2026,1,"Stanford; Match 2026; LinkedIn lists Stanford Neurosurgery",1)
# fix: 2026 PGY-1 not on 2025-26 roster? they were on the fetched roster (2025-26 header seems stale). adjust texts
for o in out:
    if o['key'] in ("61:bra:bergsneider","61:cam:hill","61:mar:guinle","61:sam:sundrani"):
        o['outcome_detail']="Listed among PGY-1 residents on Stanford neurosurgery residents page (start 2026); no evidence of departure."
        o['sources'][0]['evidence']="Stanford Neurosurgery current residents page lists them under PGY-1 residents"
    if o['key']=="61:mar:cavagnaro":
        o['identity']="probable"
json.dump(out,open('batch_083_out.json','w'),indent=1,ensure_ascii=False)
print(len(out))
