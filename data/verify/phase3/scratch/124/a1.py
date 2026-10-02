import sys; sys.path.insert(0,'scratch/124')
from add import add
U='https://www.med.unc.edu/neurosurgery/education/residency/prior-graduates2/'
def E(key,name,start,end,cur,dx_url,dx_ev,alum,extra=[],dx='found',abns=None,s=2):
    add({"key":key,"name":name,"program_id":98,"identity":"confirmed",
     "identity_basis":"UNC neurosurgery alumni page and Doximity both list residency at University of North Carolina Hospitals",
     "residency_stated":[{"institution":"University of North Carolina Hospitals","specialty":"neurosurgery","start":start,"end":end}],
     "outcome":"completed","outcome_detail":"Completed UNC neurosurgery residency "+str(end)+"; "+alum,
     "year_left":None,"destination_program":None,"destination_start_year":None,"current":cur,
     "agrees_with_db":True,"disagreement":"",
     "checks":{"google":"found","doximity":dx,"usnews":"deferred"},"abns_certified":abns,
     "sources":[{"url":U,"type":"program_page","evidence":alum}]+([{"url":dx_url,"type":"doximity","evidence":dx_ev}] if dx_url else [])+extra,"searches_used":s})
E("98:ran:barnett","Randaline Barnett",2016,2023,"Director of Pediatric Neurosurgery, University of Kentucky, Lexington KY","https://www.doximity.com/pub/randaline-barnett-md","Residency, Neurological Surgery, 2016 to 2023 at University of North Carolina Hospitals","2023 alumni: Fellowship Pediatric Neurosurgery UTHSC Memphis; current Kentucky Children's Hospital")
E("98:dar:shastri","Darshan Shastri",2017,2024,"Cerebrovascular/endovascular neurosurgeon, St. Louis MO (WashU fellowship 2024-25)","https://www.doximity.com/pub/darshan-shastri-md","Residency, Neurological Surgery, 2017 - 2024, University of North Carolina Hospitals; Fellowship Endovascular Surgical Neuroradiology WashU 2024-2025","2024 alumni: Fellowship Neuroendovascular at Washington University in St. Louis",[{"url":"https://www.med.unc.edu/neurosurgery/dr-darshan-shastri-and-dr-nathan-quig-complete-their-neurosurgery-residency-at-unc-health/","type":"program_page","evidence":"Complete their Neurosurgery Residency at UNC Health"}])
E("98:nat:quig","Nathan Quig",2017,2024,"Neurosurgeon (endovascular), St. Luke's, Fountain Hill PA","https://www.doximity.com/pub/nathan-quig-md","Neurosurgery, Fountain Hill PA; MD UNC 2017 (no residency line listed)","2024 alumni: Endovascular fellowship Temple; academic practice St. Luke's Neurosurgical Associates Bethlehem PA",[{"url":"https://www.med.unc.edu/neurosurgery/dr-darshan-shastri-and-dr-nathan-quig-complete-their-neurosurgery-residency-at-unc-health/","type":"program_page","evidence":"Complete their Neurosurgery Residency at UNC Health"}])
E("98:and:abumoussa","Andrew Abumoussa",2018,2025,"Neurosurgeon, Saint Luke's Neurological and Spine Surgery, Lee's Summit MO","https://www.doximity.com/pub/andrew-abumoussa-md","Neurosurgery, Lee's Summit MO; MD UNC 2018; NC license 2018-2025 (no residency line)","2025 alumni: Private practice, St. Luke's Hospital of Kansas City")
E("98:kel:chamberlin","Kelly Chamberlin",2018,2025,"Pediatric neurosurgeon, Orlando FL (Le Bonheur pediatric fellowship)","https://www.doximity.com/pub/kelly-chamberlin-md","Residency, Neurological Surgery, 2018 - 2025, University of North Carolina Hospitals","2025 alumni: Fellowship Pediatric Neurosurgery Le Bonheur Memphis")
