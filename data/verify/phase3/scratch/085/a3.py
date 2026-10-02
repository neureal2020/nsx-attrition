import sys; sys.path.insert(0,'scratch/085')
from add import add
TU="Tufts Medical Center"
def r(key,basis,start,end,url,ev,src2,tag,cur="resident, Tufts Medical Center",searches=1):
    add(key,"confirmed",basis,[(TU,start,end)],"in_training","Current Tufts neurosurgery resident (Doximity end year %d)"%end,cur,True,None,"found","found",
    [(url,"doximity",ev),(src2[0],"search_snippet",src2[1])],searches=searches)
r("65:alp:dincer","Doximity: Tufts residency 2020-2027, VCU MD 2020; Tufts history-of-neurosurgery paper co-author",2020,2027,"https://www.doximity.com/pub/alper-dincer-md","Tufts Medical Center Residency, Neurological Surgery, 2020 - 2027",("https://www.linkedin.com/in/alper-dincer-35b93a25/","Alper Dincer - Tufts Medical Center"),1)
r("65:jac:kosarchuk","Doximity: Tufts residency 2020-2027, EVMS MD 2020; LinkedIn Neurosurgery Resident",2020,2027,"https://www.doximity.com/pub/jacob-kosarchuk-md","Tufts Medical Center Residency, Neurological Surgery, 2020 - 2027",("https://www.linkedin.com/in/jacob-kosarchuk-md-0884972a/","Jacob Kosarchuk, MD - Neurosurgery Resident"),1)
r("65:har:snyder","Doximity: Tufts residency 2021-2028, UVA MD 2021; LinkedIn Neurosurgery Resident at Tufts",2021,2028,"https://www.doximity.com/pub/harrison-snyder-md","Tufts Medical Center Residency, Neurological Surgery, 2021 - 2028",("https://www.linkedin.com/in/harrison-snyder-md-b86855a1/","Harrison Snyder, MD - Neurosurgery Resident at Tufts"),1)
r("65:joh:herendeen","Doximity: Tufts residency 2021-2028, Rutgers NJMS 2021; Tufts Neurosurgery X post calls him one of our residents",2021,2028,"https://www.doximity.com/pub/john-herendeen-md","Tufts Medical Center Residency, Neurological Surgery, 2021 - 2028",("https://x.com/TuftsNeurosurg/status/1945220310384435302","John Herendeen one of our amazing residents"),1)
r("65:ant:yu","Common name. Doximity: Tufts residency 2022-2029, Tufts MD 2022; Tufts Medicine page and co-authorship with Tufts residents Snyder/Dincer",2022,2029,"https://www.doximity.com/pub/anthony-yu-md-8dfe26e2","Tufts Medical Center Residency, Neurological Surgery, 2022 - 2029",("https://www.tuftsmedicine.org/anthony-yu-md","Anthony Yu, MD | Tufts Medicine"),1)
