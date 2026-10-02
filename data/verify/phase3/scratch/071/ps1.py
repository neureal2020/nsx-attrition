import sys
sys.path.insert(0,".")
from add import add
PS="Penn State Milton S Hershey Medical Center"
def comp(key,basis,res,detail,current,dox,srcs,searches=2,abns=None,ident="confirmed"):
    add(key,identity=ident,identity_basis=basis,residency_stated=res,outcome="completed",outcome_detail=detail,
        year_left=None,destination_program=None,destination_start_year=None,current=current,agrees_with_db=True,disagreement="",
        checks={"google":"found","doximity":dox,"usnews":"deferred"},abns_certified=abns,sources=srcs,searches_used=searches)
comp("53:emi:sieg","Doximity and UofL bio: MD Penn State College of Medicine 2011, neurosurgery residency Penn State Hershey; distinctive name Emily Payne Sieg",
 [{"institution":PS,"specialty":"neurosurgery","start":2011,"end":2018}],"Completed neurosurgery residency at Penn State Hershey 2011-2018; now practising neurosurgeon.",
 "neurosurgeon, Associate Professor, Director of Neurotrauma and Vice Chair, UofL Health, Louisville KY","found",
 [{"url":"https://www.doximity.com/pub/emily-sieg-md","type":"doximity","evidence":"Residency, Neurological Surgery, Penn State Milton S Hershey Medical Center 2011 - 2018; American Board of Neurological Surgery"},
  {"url":"https://louisville.edu/medicine/departments/neurosurgery/emily-p-sieg","type":"search_snippet","evidence":"completed her residency in neurological surgery at Penn State Milton S. Hershey Medical Center"}],abns=True)
comp("53:eph:church","Doximity/Penn State Health bio: neurological surgery residency at Penn State Health, chief resident 2017-18; distinctive name",
 [{"institution":PS,"specialty":"neurosurgery","start":2011,"end":2018}],"Completed neurosurgery residency at Penn State Hershey (chief 2017-18); returned as faculty.",
 "cerebrovascular/endovascular neurosurgeon, Associate Professor, Penn State Health, Hershey PA","found",
 [{"url":"https://www.doximity.com/pub/ephraim-church-md","type":"doximity","evidence":"Residency, Neurological Surgery, Penn State Milton S Hershey Medical Center 2011 - 2018; chief resident at Penn State 2017-18; ABNS"}],abns=True)
comp("53:pra:rohatgi","BMC bio says neurosurgery residency at Penn State University, practising since 2011 start; distinctive name Pratik Rohatgi",
 [{"institution":PS,"specialty":"neurosurgery","start":2011,"end":None}],"Completed neurosurgery residency at Penn State (per BMC bio) with enfolded functional fellowship, then UCLA functional fellowship; practising neurosurgeon.",
 "functional neurosurgeon, Assistant Professor, Boston Medical Center / BU","not_found",
 [{"url":"https://www.bmc.org/about-us/directory/doctor/pratik-rohatgi-md","type":"bio","evidence":"completed neurosurgery residency at Penn State University as well as an enfolded fellowship in functional neurosurgery, followed by post-graduate fellowship training in functional neurosurgery at UCLA"}],abns=True,ident="confirmed")
comp("53:bri:anderson","Doximity: Penn State Hershey neurosurgery residency 2012-2019, OHSU MD 2012; bio (Summit/Quincy) says Penn State Hershey residency; common name but program+years match",
 [{"institution":PS,"specialty":"neurosurgery","start":2012,"end":2019}],"Completed neurosurgery residency at Penn State Hershey 2012-2019; practising neurosurgeon.",
 "neurosurgeon, Lehi UT (previously Quincy Medical Group, IL)","found",
 [{"url":"https://www.doximity.com/pub/brian-anderson-md-1a4e2aed","type":"doximity","evidence":"Residency, Neurological Surgery, Penn State Milton S Hershey Medical Center 2012 - 2019; OHSU School of Medicine Class of 2012; ABNS"},
  {"url":"https://www.summitbrainandspine.com/brian-anderson-bio-new","type":"search_snippet","evidence":"completed his neurosurgical residency at Pennsylvania State University in Hershey, Pennsylvania"}],searches=2,abns=True)
