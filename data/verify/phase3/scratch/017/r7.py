import sys;sys.path.insert(0,'scratch/017')
from add import add
CC="Cleveland Clinic Foundation"
add("12:dan:lilly","confirmed","Doximity Daniel Lilly: Rush MD 2020, residency Cleveland Clinic 2020-2027 (resident physician, Cleveland Clinic main campus); LinkedIn/AANS bios",
 [(CC,"neurosurgery",2020,2027)],"in_training","Current neurosurgery resident at Cleveland Clinic (Doximity: 'Resident Physician - Neurological Surgery', 2020-2027).",
 "neurosurgery resident (PGY-5/6), Cleveland Clinic",True,"",("found","found","deferred"),None,
 [("https://www.doximity.com/pub/daniel-lilly-md","doximity","Cleveland Clinic Foundation Residency, Neurological Surgery, 2020 - 2027"),
  ("https://www.linkedin.com/in/dan-lilly-aa4a53b3/","search_snippet","Dan Lilly - Resident physician, neurosurgery")],2)
add("12:rob:winkelman","confirmed","Doximity Robert Winkelman (Cleveland neurosurgery): CWRU MD Class of 2020; search snippets (Cleveland Clinic magazine, Doximity/WebMD) state residency Cleveland Clinic 2020-2027; Cleveland Clinic Catalyst grant article",
 [(CC,"neurosurgery",2020,2027)],"in_training","Neurosurgery resident at Cleveland Clinic per Cleveland Clinic magazine and directory snippets (residency 2020-2027). Fetched Doximity page lists only CWRU MD 2020 (no residency entry) but specialty Neurosurgery, Cleveland; co-authors are CC residents.",
 "neurosurgery resident, Cleveland Clinic",True,"",("found","found","deferred"),None,
 [("https://www.doximity.com/pub/robert-winkelman-md","doximity","Neurosurgery - Cleveland, OH; Case Western Reserve University School of Medicine Class of 2020"),
  ("https://magazine.clevelandclinic.org/2025-summer-catalyst-grants","news","search result: Training in 3D (Winkelman 3D-printed spine/cranial simulators, Cleveland Clinic Catalyst Grant)"),
  ("https://doctor.webmd.com/doctor/robert-winkelman-8bf9ac09-96cf-40ea-8daf-ee77bb9d10a9-overview","search_snippet","search summary: residency in Neurological Surgery at Cleveland Clinic Foundation from 2020-2027")],2)
add("12:she:sheikh","confirmed","Doximity Shehryar Sheikh: CWRU MD 2020, residency Cleveland Clinic 2020-2027; AANS 2024 bio 'PGY-4 neurosurgical resident at Cleveland Clinic ... PhD at Lerner Research Institute'",
 [(CC,"neurosurgery",2020,2027)],"in_training","Current neurosurgery resident at Cleveland Clinic (2020-2027), in dedicated PhD research years.",
 "neurosurgery resident, Cleveland Clinic (PhD, Lerner Research Institute/CWRU)",True,"",("found","found","deferred"),None,
 [("https://www.doximity.com/pub/shehryar-sheikh-md","doximity","Cleveland Clinic Foundation Residency, Neurological Surgery, 2020 - 2027"),
  ("https://aans2024.eventscribe.net/ajaxcalls/presenterInfo.asp?PresenterId=1785288","bio","search snippet: PGY-4 neurosurgical resident at Cleveland Clinic ... completing a PhD at the Cleveland Clinic Lerner Research Institute")],2)
add("12:gre:glauser","confirmed","Cleveland Clinic residency directory/Healthgrades: Temple MD 2021, neurosurgery resident at Cleveland Clinic; X post from Cleveland Clinic Neurosurgery naming PGY-3 Greg Glauser; co-author with CC residents",
 [(CC,"neurosurgery",2021,None)],"in_training","Current Cleveland Clinic neurosurgery resident (PGY-3 in Sept 2023 per Cleveland Clinic Neurosurgery X post; consistent with 2021 entry). No Doximity profile found.",
 "neurosurgery resident, Cleveland Clinic",True,"",("found","not_found","deferred"),None,
 [("https://x.com/CleClinicNS/status/1705647070009241723","search_snippet","Our talented #residents PGY-3 Greg Glauser and PGY-5 Josie Volovetz ... showcased their recent #research projects at the Ohio State Neurosurgical Society"),
  ("https://www.healthgrades.com/physician/dr-gregory-glauser-xsnlkp2295","search_snippet","Dr. Gregory Glauser, MD - Neurosurgeon in Cleveland, OH; Temple 2021")],2)
