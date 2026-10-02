import json
J="https://www.jefferson.edu/academics/colleges-schools-institutes/skmc/departments/neurosurgery/education/residency/residents.html"
inp=json.load(open('../../batch_080_in.json'))
def e(i,doxy_url,dstat,train,school,extra_src=None,idb=None,cur=None,ss=4):
    p=inp[i]
    src=[{"url":J,"type":"program_page","evidence":f"{p['name']}, MD - {school}; listed on current Jefferson neurosurgery residents page"}]
    if doxy_url: src.append({"url":doxy_url,"type":"doximity","evidence":train})
    if extra_src: src+=extra_src
    return {"key":p['key'],"name":p['name'],"program_id":p['program_id'],"identity":"confirmed",
     "identity_basis":idb or f"Jefferson residents page and Doximity both list neurosurgery residency at Sidney Kimmel/TJUH; MD {school}",
     "residency_stated":[{"institution":"Sidney Kimmel Medical College at Thomas Jefferson University/TJUH","specialty":"neurosurgery","start":int(train.split(' - ')[0][-4:]) if False else p['entry_year'],"end":p['entry_year']+7}],
     "outcome":"in_training","outcome_detail":"Current neurosurgery resident at Jefferson per program page"+(" and Doximity ("+train+")" if doxy_url else ""),
     "year_left":None,"destination_program":None,"destination_start_year":None,
     "current":cur or "neurosurgery resident, Thomas Jefferson University Hospital, Philadelphia",
     "agrees_with_db":True,"disagreement":"",
     "checks":{"google":"found","doximity":dstat,"usnews":"deferred"},"abns_certified":False,"sources":src,"searches_used":ss}
out=[]
out.append(e(0,"https://www.doximity.com/pub/keenan-piper-md","found","Residency, Neurological Surgery, 2023 - 2030; SKMC Class of 2023","Sidney Kimmel Medical College"))
out.append(e(1,"https://www.doximity.com/pub/logan-massman-md","found","Residency, Neurological Surgery, 2023 - 2030","Medical College of Wisconsin"))
out.append(e(2,"https://www.doximity.com/pub/anish-sathe-md","found","Residency, Neurological Surgery, 2024 - 2031; SKMC Class of 2024","Sidney Kimmel Medical College"))
out.append(e(3,"https://www.doximity.com/pub/chitra-kumar-md","found","Residency, Neurological Surgery, 2024 - 2031; Univ of Cincinnati Class of 2024","University of Cincinnati"))
out.append(e(4,"https://www.doximity.com/pub/marissa-tucci-md","found","Residency, Neurological Surgery, 2024 - 2031; Tulane Class of 2024","Tulane University"))
o=e(5,None,"not_found","","Sidney Kimmel Medical College at Thomas Jefferson University",extra_src=[{"url":"https://www.linkedin.com/in/india-shelley-m-d-095b3a126/","type":"search_snippet","evidence":"India Shelley, M.D. - Neurosurgery Resident at Thomas ..."}])
o["outcome_detail"]="Current PGY-1 neurosurgery resident at Jefferson per program page; no Doximity profile found by name search"
out.append(o)
out.append(e(6,"https://www.doximity.com/cv/jean-filo","found","Residency, Neurological Surgery, 2025 - 2032; Harvard Class of 2025","Harvard Medical School"))
out.append(e(7,"https://www.doximity.com/pub/jenna-langbein-md","found","Residency, Neurological Surgery, 2025 - 2032; VCU Class of 2024","Virginia Commonwealth University School of Medicine"))
out.append(e(8,"https://www.doximity.com/pub/sai-sriram-md","found","Residency, Neurological Surgery, 2025 - 2032; Univ of Florida Class of 2025","University of Florida"))
json.dump(out,open('../../batch_080_out.json','w'),indent=1)
json.dump(out,open('out1.json','w'))
print(len(out))
