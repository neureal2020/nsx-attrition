import sys; sys.path.insert(0,'scratch/089')
from add import add
U="https://www.uclahealth.org/departments/neurosurgery/education/residency-training/current-residents"
def r(k,n,school,pgy,entry,ns,extra=[]):
    add(k,n,67,"confirmed",f"UCLA current-residents page lists {n}, MD, {school}, {pgy}; program match",[{"institution":"UCLA David Geffen School of Medicine/UCLA Medical Center","specialty":"neurosurgery","start":entry,"end":None}],"in_training",f"Listed as current UCLA neurosurgery resident ({pgy}) in 2026-27","neurosurgery resident, UCLA",True,"","found","not_found",False,[{"url":U,"type":"program_page","evidence":f"{n}, MD - {pgy} - {school}"}]+extra,ns)
r("67:shr:budhiraja","Shreya Budhiraja","Northwestern","NS2",2025,2,[{"url":"https://www.uclahealth.org/sites/default/files/documents/54/pictorial-roster-25-26.pdf?f=3707abed","type":"search_snippet","evidence":"UCLA Surgery house staff 2025-26 lists her as Neuro clinical resident, per search summary"}])
r("67:vai:shah","Vaibhavi Shah","Stanford","NS2",2025,2)
r("67:jor:sifuentes","Jorge Salcedo Sifuentes","UCLA","NS1",2026,2,[{"url":"https://x.com/JorgeUCLA/status/1974228263510622351","type":"search_snippet","evidence":"MS4 at DGSOMUCLA applying for Neurosurgery Match2026"}])
r("67:nik:das","Nikita Das","Case Western","NS1",2026,2)
r("67:zac:bernstein","Zachary Bernstein","Emory","NS1",2026,2,[{"url":"https://www.linkedin.com/in/zachary-bernstein-md-ms-7b957311a/","type":"search_snippet","evidence":"Zachary Bernstein, MD MS - UCLA Department of Neurosurgery"}])
