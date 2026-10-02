import json
exec(open("scratch/121/part1.py").read().split("out=[]")[0])
out=json.load(open("batch_121_out.json"))
UN="https://www.unmc.edu/neurosurgery/education/residency/alumni.html"
nf={"google":"found","doximity":"found","usnews":"deferred"}
def neb(i,key,name,yr,end,basis,cur,dox,abns,extra,n=2,doxfound=True,dis=""):
    ch=dict(nf); 
    if not doxfound: ch["doximity"]="not_found"
    srcs=[]
    if dox: srcs.append({"url":dox[0],"type":"doximity","evidence":dox[1]})
    srcs.append({"url":UN,"type":"program_page","evidence":extra})
    return P(i,key,name,96,"confirmed",basis,[{"institution":"University of Nebraska Medical Center","specialty":"neurosurgery","start":yr,"end":end}],"completed","Completed UNMC neurosurgery residency; practising neurosurgeon",cur,True,dis,ch,abns,srcs,n)
D="https://www.doximity.com/pub/"
out.append(neb(20,"96:jor:lacy","Jordan Lacy",2012,2019,"Doximity: MD Nebraska 2012, Residency Neurological Surgery UNMC 2012-2019, ABNS; UNMC alumni 2018 graduate; MD West One bio","neurosurgeon, MD West ONE, Omaha NE",(D+"jordan-lacy-md","University of Nebraska Medical Center College of Medicine Residency, Neurological Surgery, 2012 - 2019; American Board of Neurological Surgery"),True,"Jordan P. Lacy, MD - 2018 Graduate",dis="Doximity graduation year 2019 vs UNMC alumni page 2018"))
out.append(neb(21,"96:lin:fornoff","Linden Fornoff",2012,2019,"Doximity: MD Nebraska 2012, Residency Neurological Surgery UNMC 2012-2019, ABNS; pediatric fellowship Stanford; UNMC alumni 2018 graduate","pediatric neurosurgeon, Boys Town National Research Hospital, Omaha NE",(D+"linden-fornoff-md","University of Nebraska Medical Center College of Medicine Residency, Neurological Surgery, 2012 - 2019; American Board of Neurological Surgery"),True,"Linden E. Fornoff, MD - 2018 Graduate",dis="Doximity graduation year 2019 vs UNMC alumni page 2018"))
out.append(neb(22,"96:kyl:schmidt","Kyle Schmidt",2013,2020,"Doximity: MD Nebraska 2013, Residency UNMC 2013-2020, ABNS; Monument Health bio confirms UNMC residency 2020; co-authored with UNMC residents Tenny/McMordie","neurosurgeon, Monument Health, Rapid City SD",(D+"kyle-schmidt-md","University of Nebraska Medical Center College of Medicine Residency, Neurological Surgery, 2013 - 2020; American Board of Neurological Surgery"),True,"Kyle P. Schmidt, MD - 2020 Graduate"))
out.append(neb(23,"96:ste:tenny","Steven Tenny",2013,2020,"Doximity: MD Univ of Kansas 2013, Residency UNMC 2013-2020, ABNS; UNMC alumni 2020 graduate","neurosurgeon, Salina Regional Health Center, Salina KS",(D+"steven-tenny-md","University of Nebraska Medical Center College of Medicine Residency, Neurological Surgery, 2013 - 2020; American Board of Neurological Surgery"),True,"Steven O. Tenny, MD - 2020 Graduate"))
out.append(neb(24,"96:jos:mcmordie","Joseph McMordie",2014,2021,"CHRISTUS bio (search snippet): neurosurgery residency at University of Nebraska in Omaha, spine fellowship Northwestern; Texas Tech MD; UNMC alumni 2021 graduate","neurosurgeon, CHRISTUS Trinity Clinic, Texarkana TX",None,None,"Joseph H. McMordie, MD - 2021 Graduate",doxfound=False,dis=""))
o=out[24]; o["sources"].insert(0,{"url":"https://www.christushealth.org/find-a-doctor/joseph-mcmordie-59851","type":"search_snippet","evidence":"Neurosurgery residency at University of Nebraska in Omaha and fellowship in complex and reconstructive spine surgery at Northwestern University"})
json.dump(out,open("batch_121_out.json","w"),indent=1)
from collections import Counter
print(len(out),Counter(x["outcome"] for x in out),Counter(x["identity"] for x in out))
for k in ("doximity","usnews","google"):print(k,Counter(x["checks"][k] for x in out))
print(sum(x["searches_used"] for x in out))
print([x["name"] for x in out if not x["agrees_with_db"]])
