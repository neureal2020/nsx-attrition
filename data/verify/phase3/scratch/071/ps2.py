import sys
sys.path.insert(0,".")
from add import add
from ps1 import comp, PS
add("53:end:ziu",identity="confirmed",identity_basis="Doximity lists MD University of Arkansas for Medical Sciences 2013 with residencies at both Penn State Hershey and University of Missouri-Columbia; distinctive name",
 residency_stated=[{"institution":PS,"specialty":"neurosurgery","start":2013,"end":2017},{"institution":"University of Missouri-Columbia","specialty":"neurosurgery","start":2014,"end":2021}],
 outcome="transferred",outcome_detail="Doximity lists neurosurgery residency at Penn State Hershey 2013-2017 and University of Missouri-Columbia 2014-2021 (overlapping dates, likely a profile quirk; Missouri MO license 2017-2022). Practises as neurosurgeon (Mayo Clinic Jacksonville / Ascension). Two programs named, so transfer to Missouri is consistent with DB; exact leave year not stated by source.",
 year_left=None,destination_program="University of Missouri-Columbia",destination_start_year=None,current="neurosurgeon, Jacksonville FL (Mayo Clinic / Ascension St. Vincent's)",
 agrees_with_db=True,disagreement="Doximity dates are 2013-2017 (Penn State) and 2014-2021 (Missouri); DB has left Penn State after 2015-16 and Missouri PGY-4 in 2017-18. Dates not resolved by source.",
 checks={"google":"found","doximity":"found","usnews":"deferred"},abns_certified=True,
 sources=[{"url":"https://www.doximity.com/pub/endrit-ziu-md","type":"doximity","evidence":"Residency, Neurological Surgery, University of Missouri-Columbia 2014 - 2021; Penn State Milton S Hershey Medical Center 2013 - 2017; ABNS"}],searches_used=2)
comp("53:rus:payne","Doximity: MD Texas Tech 2012, Penn State Hershey neurosurgery residency 2012-2019; ResearchGate lists PGY5 at Penn State Hershey; distinctive name/program match",
 [{"institution":PS,"specialty":"neurosurgery","start":2012,"end":2019}],"Completed neurosurgery residency at Penn State Hershey 2012-2019 (peripheral nerve fellowship 2016-17 and Perth fellowship 2017-18 enfolded); practising neurosurgeon.",
 "neurosurgeon, Neurosurgery Site Director, Texoma Medical Center, Denison TX","found",
 [{"url":"https://www.doximity.com/pub/russell-payne-md","type":"doximity","evidence":"Residency, Neurological Surgery, Penn State Milton S Hershey Medical Center 2012 - 2019; ABNS"}],abns=True)
comp("53:jus:davanzo","Doximity: Penn State Hershey neurosurgery residency 2013-2020, Jefferson MD 2013; AHN bio",
 [{"institution":PS,"specialty":"neurosurgery","start":2013,"end":2020}],"Completed neurosurgery residency at Penn State Hershey 2013-2020; practising neurosurgeon.",
 "neurosurgeon, Allegheny Health Network, Monroeville PA","found",
 [{"url":"https://www.doximity.com/pub/justin-davanzo-md","type":"doximity","evidence":"Residency, Neurological Surgery, Penn State Milton S Hershey Medical Center 2013 - 2020; ABNS"}],abns=True)
comp("53:rya:jafrani","Doximity: residency Houston Methodist 2014-2017 then Penn State Hershey 2017-2021 (matches DB transfer-in); distinctive name",
 [{"institution":"Houston Methodist Hospital","specialty":"neurosurgery","start":2014,"end":2017},{"institution":PS,"specialty":"neurosurgery","start":2017,"end":2021}],
 "Transferred in from Houston Methodist in 2017 and completed neurosurgery residency at Penn State Hershey (2017-2021); then pediatric neurosurgery fellowship WashU. Completed at the input program.",
 "pediatric neurosurgeon, Orlando Health Arnold Palmer Hospital for Children, Orlando FL","found",
 [{"url":"https://www.doximity.com/pub/ryan-jafrani-md","type":"doximity","evidence":"Residency, Penn State Milton S Hershey Medical Center 2017 - 2021; Houston Methodist Hospital 2014 - 2017"},
  {"url":"https://www.arnoldpalmerhospital.com/physician-finder/ryan-jafrani-md","type":"bio","evidence":"completed a residency in neurosurgery at Penn State Health Neurosurgery in Hershey"}],abns=None)
