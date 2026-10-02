import sys;sys.path.insert(0,'scratch/017')
from add import add
CC="Cleveland Clinic Foundation"
add("12:wil:kemp","confirmed","Doximity William J Kemp III: Indiana Univ SOM 2014, Cleveland Clinic residency 2014-2021, ABNS; bio: internship general surgery William Beaumont, matches DB note",
 [(CC,"neurosurgery",2014,2021)],"completed","Doximity residency Cleveland Clinic 2014-2021 with ABNS certification; neurosurgeon (spine), Neurosurgical Associates, Reston VA, after spine fellowship at Univ of Wisconsin.",
 "spine neurosurgeon, Neurosurgical Associates of Virginia, Reston VA",True,"",("found","found","deferred"),True,
 [("https://www.doximity.com/pub/william-kemp-md-6eb58065","doximity","Cleveland Clinic Residency, 2014 - 2021; American Board of Neurological Surgery"),
  ("https://www.neurosurgicalva.com/william-kemp-md/","bio","search summary: neurological surgery residency at Cleveland Clinic Foundation, internship general surgery William Beaumont Hospital, MD Indiana University")],2)
add("12:amr:morsi","confirmed","Doximity Amr Morsi (Weston FL neurosurgery): residency Cleveland Clinic 2015-2022; Cleveland Clinic provider page; co-author with CC residents Kondylis, Sharma",
 [(CC,"neurosurgery",2015,2022)],"completed","Doximity: residency neurological surgery Cleveland Clinic 2015-2022; epilepsy/functional fellowship Mount Sinai (search snippet); staff neurosurgeon at Cleveland Clinic Florida (Weston) / Rutgers RWJ.",
 "functional/epilepsy neurosurgeon, Cleveland Clinic Florida (Weston) / RWJBarnabas-Rutgers",True,"",("found","found","deferred"),None,
 [("https://www.doximity.com/pub/amr-morsi-md-96f529d3","doximity","Cleveland Clinic Foundation Residency, Neurological Surgery, 2015 - 2022"),
  ("https://providers.clevelandclinic.org/provider/amr-morsi/5833751","bio","search result: Dr. Amr Morsi, MD - Weston, FL - Functional Neurosurgery, Epilepsy Surgery")],2)
add("12:eri:schmidt","confirmed","Doximity Eric Scott Schmidt: MD Univ of Kentucky 2015, residency Cleveland Clinic 2015-2022, ABNS; co-author with CC residents (Soni, Davison, Sundar, Kondylis)",
 [(CC,"neurosurgery",2015,2022)],"completed","Doximity residency neurological surgery Cleveland Clinic 2015-2022, fellowships spine 2019-20 and epilepsy 2020-21 within residency; board-certified neurosurgeon (Lexington KY, now Englewood CO).",
 "neurosurgeon, Englewood CO (previously Lexington KY)",True,"",("found","found","deferred"),True,
 [("https://www.doximity.com/pub/eric-schmidt-md-392ce543","doximity","Cleveland Clinic Foundation Residency, Neurological Surgery, 2015 - 2022; American Board of Neurological Surgery")],2)
add("12:pra:soni","confirmed","Cleveland Clinic provider page/LinkedIn: skull base neurosurgeon at Cleveland Clinic; MD Jefferson 2015; co-author with CC residents",
 [(CC,"neurosurgery",2015,2022)],"completed","Practising skull base neurosurgeon at Cleveland Clinic (staff); implies completion of neurosurgery residency there (2015 entry). Exact end year not seen in a source.",
 "skull base neurosurgeon, Cleveland Clinic",True,"",("found","not_found","deferred"),None,
 [("https://providers.clevelandclinic.org/provider/pranay-soni/4270468","bio","search result: Dr. Pranay Soni, MD - Cleveland, OH - Skull Base Surgery"),
  ("https://www.linkedin.com/in/pranay-soni-4436321b6/","search_snippet","Pranay Soni - Skull Base Neurosurgeon at Cleveland Clinic")],2)
# patch earlier
import json
o=json.load(open('batch_017_out.json'))
for r in o:
    if r['key'] in('12:bal:otvos','12:mat:grabowski','12:vik:chakravarthy'): r['searches_used']=2
    if r['key'] in('12:mat:grabowski','12:vik:chakravarthy'): r['checks']['usnews']='deferred'
json.dump(o,open('batch_017_out.json','w'),indent=1)
