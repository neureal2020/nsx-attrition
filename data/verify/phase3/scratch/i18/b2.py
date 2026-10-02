import json
U="https://md.rcm.upr.edu/neurosurgery/current-residents/"
R_="https://www.urmc.rochester.edu/education/graduate-medical-education/prospective-residents/neurosurgery/our-residents"
def rec(key,name,pid,site,inst,start,pgy,ms,ident,basis,ext,exttype,extev,lvl,n,sc,dox="not_found",more=[],cur=None):
    return {"key":key,"name":name,"program_id":pid,"program_site_url":site,"identity":ident,"identity_basis":basis,
    "residency_stated":[{"institution":inst,"specialty":"neurosurgery","start":start,"end":None}],
    "outcome":"in_training","outcome_detail":f"Listed on the program's current resident page as {pgy} (medical school: {ms})",
    "year_left":None,"destination_program":None,"destination_start_year":None,
    "current":cur or f"{pgy} neurosurgery resident, {inst}","agrees_with_db":True,"disagreement":"",
    "external_url":ext,"evidence_level":lvl,"checks":{"google":"found","doximity":dox,"usnews":"deferred"},"abns_certified":None,
    "sources":[{"url":site,"type":"program_page","evidence":f"Current residents: {name}, {pgy}, {ms}"}]+([{"url":ext,"type":exttype,"evidence":extev}] if ext else [])+more,
    "ident_searches":n,"sources_count":sc,"searches_used":n}
R=[
rec("101:adr:vazquez-medina","Adriana S. Vazquez-Medina",101,U,"University of Puerto Rico School of Medicine",2025,"PGY-2","UPR-RCM Medical School","confirmed",
 "Current UPR page: Adriana S. Vazquez-Medina, PGY-2, UPR-RCM MD; El Nuevo Dia: first resident of the reopened UPR neurosurgery program (2025); Metro PR 2026-07: Fundacion para el Futuro de la Salud funds her stipend through completion in 2032. Name + program + year agree (resolves ambiguous-name flag)",
 "https://www.elnuevodia.com/noticias/locales/notas/primera-residente-del-nuevo-programa-de-neurocirugia-de-la-upr-tengo-una-responsabilidad-con-el-resto-de-la-gente-que-viene-detras/","news","Primera residente del nuevo programa de Neurocirugia de la UPR (headline); search summary: Adriana Vazquez Medina first resident to enter the reopened program in 2025, currently second year","gold",1,3,
 more=[{"url":"https://www.metro.pr/noticias/2026/07/16/alianza-apuesta-por-formar-mas-neurocirujanos/","type":"news","evidence":"Alliance funds stipend of the program's resident until she completes residency in 2032 (search summary)"}]),
rec("101:est:rivera","Esteban R. Rivera Rivera",101,U,"University of Puerto Rico School of Medicine",2026,"PGY-1","UPR-RCM Medical School","confirmed",
 "Current UPR page: Esteban R. Rivera Rivera, PGY-1, UPR-RCM MD; El Nuevo Dia / Metro PR (Match Day 2026): Esteban Rivera Rivera selected as second resident of UPR neurosurgery since reaccreditation",
 "https://www.elnuevodia.com/noticias/locales/notas/seleccionado-el-segundo-residente-en-neurocirugia-de-la-upr-ese-era-el-camino-que-tenia-que-seguir/","news","Seleccionado el segundo residente en Neurocirugia de la UPR (headline); search summary: Esteban Rivera Rivera announced as new neurosurgery resident on Match Day 2026","gold",0,3,
 more=[{"url":"https://www.metro.pr/noticias/2026/03/22/neurocirugia-en-ciencias-medicas-suma-su-segundo-residente-tras-su-reapertura","type":"news","evidence":"Neurocirugia en Ciencias Medicas suma su segundo residente tras su reapertura (headline)"}]),
rec("102:huy:dang","Huy Dang",102,R_,"University of Rochester Medical Center",2025,"PGY-2","Baylor College of Medicine","confirmed",
 "Current URMC page: Huy Dang, MD, PGY-2, Baylor College of Medicine; URMC/UR Neurosurgery welcome post (search summary): incoming PGY-1, Baylor research year in neuromodulation, Dartmouth undergrad; BCM Functional & Cognitive Neurophysiology Lab lists Huy Dang, 2022, Medical Student; Doximity Baylor Class of 2025 profile agrees. Other Huy Dang profiles are namesakes",
 "https://www.bcm.edu/research/faculty-labs/functional-and-cognitive-neurophysiology-laboratory/lab-members","program_page","Huy Dang | 2022 | Medical Student (BCM lab alumni)","silver",1,3,dox="found",
 more=[{"url":"https://www.doximity.com/pub/huy-dang-md-0ecd7516","type":"doximity","evidence":"Huy Dang MD, Houston TX; Baylor College of Medicine Class of 2025"}]),
rec("102:ibr:jalal","Ibrahim Jalal",102,R_,"University of Rochester Medical Center",2026,"PGY-1","University of Rochester","confirmed",
 "Current URMC page: M. Ibrahim Jalal, MD, PGY-1, University of Rochester; Spine Summit 2024 presenter bio Muhammad I. Jalal: University of Rochester medical student researcher in neurosurgery (spine, neuromodulation), UPenn BA 2022; Stone Lab (URMC neurosurgery) member page. Name variant M. Ibrahim = Muhammad Ibrahim; name + med school agree",
 "https://spinesummit24.eventscribe.net/ajaxcalls/PresenterInfo.asp?efp=WkZYS0JXVU8xNzQ1Mg&PresenterID=1760223&rnd=0.954212","search_snippet","Muhammad I. Jalal, BA: third-year medical student interested in device development, surgical simulation, and neurosurgical education research... medical student researcher at the University of Rochester Medical Center","silver",1,3,
 more=[{"url":"https://www.urmc.rochester.edu/labs/stone-lab/lab-members","type":"program_page","evidence":"Stone Lab member Ibrahim Jalal, University of Rochester medical student"}]),
rec("102:mar:green","Martin Green",102,R_,"University of Rochester Medical Center",2026,"PGY-1","Brody School of Medicine at East Carolina University","probable",
 "Current URMC page: Martin Green, MD, PGY-1, Brody/ECU. Only corroboration: ECU Match Day 2026 news says the Brody class includes a neurosurgery match for the first time since 2017 (person not named). Searches '\"Martin Green\" Brody neurosurgery Rochester', '\"Martin Green\" medical student ECU neurosurgery research', '\"Martin Green\" doximity neurosurgery' found no named external profile. Common name; in_training rests on the current program page itself",
 "https://news.ecu.edu/2026/03/20/match-day-2026/","news","This is the first time since 2017 that the class has included an applicant and match in neurosurgery. (no name given)","program_only",3,1),
]
json.dump(R,open("b2.json","w"))
