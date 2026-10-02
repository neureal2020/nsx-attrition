import sys;sys.path.insert(0,'scratch/017')
from add import add
CC="Cleveland Clinic Foundation"
add("12:ada:khalil","confirmed","Doximity: MD Univ of Colorado 2014; residency neurological surgery Cleveland Clinic; publication with Cleveland Clinic/UT Health San Antonio IR affiliation; same name as input",
 [(CC,"neurosurgery",2014,2021)],"switched_specialty","Doximity summary text says residency in neurological surgery at Cleveland Clinic 2014-2016, then switched to interventional radiology (fellowship Brigham and Women's); Education field lists 2014-2021 (template default). Now board-certified (ABR) diagnostic+interventional radiology.",
 "interventional radiologist, Grass Valley CA (Doximity)",True,"",("found","found","blocked"),False,
 [("https://www.doximity.com/pub/adam-khalil-md","doximity","followed by a residency in neurological surgery at the Cleveland Clinic Foundation from 2014 to 2016. He then switched fields to interventional radiology"),
  ("https://www.doximity.com/pub/adam-khalil-md","doximity","American Board of Radiology - Interventional Radiology and Diagnostic Radiology"),
  ("https://health.usnews.com/doctors/adam-khalil-1375615","usnews","blocked (automated-behavior page)")],3,yl=2016,dp="Interventional/diagnostic radiology (fellowship Brigham and Women's)",ds=None)
add("12:bal:otvos","confirmed","Doximity: MD Case Western 2014, residency neurological surgery Cleveland Clinic 2014-2021; MU faculty bio",
 [(CC,"neurosurgery",2014,2021)],"completed","Doximity Education lists Cleveland Clinic neurological surgery residency 2014-2021; practising neurosurgeon and residency program director at Univ of Missouri.",
 "neurosurgeon, Univ of Missouri Health Care, Columbia MO",True,"",("found","found","blocked"),None,
 [("https://www.doximity.com/pub/balint-otvos-md","doximity","Cleveland Clinic Foundation Residency, Neurological Surgery, 2014 - 2021"),
  ("https://www.muhealth.org/doctors/balint-otvos-md","bio","search snippet: Neurosurgery Residency Program Director, Associate Professor of Neurological Surgery")],3)
add("12:mat:grabowski","confirmed","Doximity (Cleveland, neurosurgery): Cleveland Clinic Lerner College of Medicine 2014, residency Cleveland Clinic 2014-2021, ABNS; Cleveland Clinic provider page",
 [(CC,"neurosurgery",2014,2021)],"completed","Doximity residency neurological surgery Cleveland Clinic 2014-2021; ABNS certified; staff neurosurgeon (neuro-oncology) at Cleveland Clinic.",
 "neurosurgeon (brain tumor), Cleveland Clinic",True,"",("found","found","blocked"),True,
 [("https://www.doximity.com/pub/matthew-grabowski-md-9e2849cc","doximity","Cleveland Clinic Foundation Residency, Neurological Surgery, 2014 - 2021; American Board of Neurological Surgery"),
  ("https://providers.clevelandclinic.org/provider/matthew-grabowski/4270467","bio","search result: Brain Tumor Neurosurgery, Cleveland Clinic")],3)
add("12:vik:chakravarthy","confirmed","Doximity: MD UMKC 2014; residency Loma Linda 2014-2017 then Cleveland Clinic 2017-2021; ABNS",
 [("Loma Linda University Health Education Consortium","neurosurgery",2014,2017),(CC,"neurosurgery",2017,2021)],"completed","Transferred IN from Loma Linda (2014-2017) to Cleveland Clinic PGY-4 in 2017; completed 2021; fellowships CC spine 2020-21, MSK neurosurgical oncology 2021-22. Completed at Cleveland Clinic (entry_year 2014 in DB reflects class year).",
 "neurosurgeon, Garden Grove CA (Doximity); previously Ohio State asst professor per search",True,"DB entry year 2014 is class year; actual start at CC 2017 (already noted in phase2)",("found","found","blocked"),True,
 [("https://www.doximity.com/pub/vikram-chakravarthy-md","doximity","Cleveland Clinic Foundation Residency 2017 - 2021; Loma Linda ... 2014 - 2017; American Board of Neurological Surgery")],3)
