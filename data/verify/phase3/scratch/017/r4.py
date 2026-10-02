import sys;sys.path.insert(0,'scratch/017')
from add import add
CC="Cleveland Clinic Foundation"
def mk(key,basis,yrs,detail,cur,src,ev,extra=[]):
    add(key,"confirmed",basis,[(CC,"neurosurgery",yrs[0],yrs[1])],"completed",detail,cur,True,"",("found","found","deferred"),None,[(src,"doximity",ev)]+extra,2)
mk("12:ben:whiting","Doximity Benjamin Bernard Whiting: Temple MD 2017, residency Cleveland Clinic 2017-2024; AHN bio",(2017,2024),"Doximity residency Cleveland Clinic 2017-2024 plus spine fellowship 2022-23; practising spine neurosurgeon (AHN).","spine neurosurgeon, AHN Neuroscience Institute, Pittsburgh PA","https://www.doximity.com/pub/benjamin-whiting-md","Cleveland Clinic Foundation Residency, Neurological Surgery, 2017 - 2024",
 [("https://findcare.ahn.org/Benjamin-B-Whiting","bio","search result: neurosurgeon with the AHN Neuroscience Institute specializing in complex spine surgery")])
mk("12:efs:kondylis","Doximity Efstathios Demetre Kondylis: Pitt MD 2016, residency Cleveland Clinic 2017-2023; Henry Ford bio",(2017,2023),"Doximity residency Cleveland Clinic 2017-2023; epilepsy fellowship (LinkedIn); now functional neurosurgeon at Henry Ford.","functional/epilepsy neurosurgeon, Henry Ford Health, Detroit MI","https://www.doximity.com/pub/efstathios-kondylis-md","Cleveland Clinic Foundation Residency, Neurological Surgery, 2017 - 2023",
 [("https://www.henryford.com/physician-directory/k/kondylis-efstathios","bio","search result: Efstathios Kondylis, MD | Henry Ford Health - Detroit, MI")])
mk("12:rog:murayi","Doximity Roger Bwimana Murayi: Penn MD 2016, residency Cleveland Clinic 2017-2024; LVHN bio",(2017,2024),"Doximity residency Cleveland Clinic 2017-2024; practising neurosurgeon (skull base) at Lehigh Valley.","neurosurgeon, Lehigh Valley Health Network, Allentown PA","https://www.doximity.com/pub/roger-murayi-md","Cleveland Clinic Foundation Residency, Neurological Surgery, 2017 - 2024",
 [("https://www.lvhn.org/doctors/roger-murayi","bio","search result: Roger B. Murayi, MD | Lehigh Valley Health Network")])
