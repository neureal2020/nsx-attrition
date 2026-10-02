import sys
sys.path.insert(0,".")
from ps1 import comp, PS
comp("53:san:savaliya","Doximity/Independence Health/ResearchGate: Penn State College of Medicine MD 2014, Penn State Hershey neurosurgery residency 2014-2021; Doximity publications co-authored with Penn State Hershey residents",
 [{"institution":PS,"specialty":"neurosurgery","start":2014,"end":2021}],"Completed neurosurgery residency at Penn State Hershey 2014-2021 (per search snippet of Doximity); ABNS certified; practising neurosurgeon.",
 "neurosurgeon, Flagstaff AZ / Texas Neurological Spine (Independence Health System from 2026)","found",
 [{"url":"https://www.doximity.com/pub/sandip-savaliya-md-f1cd0317","type":"doximity","evidence":"Penn State College of Medicine Class of 2014; American Board of Neurological Surgery; co-authored with Penn State Hershey neurosurgery residents"},
  {"url":"https://www.doximity.com/pub/sandip-savaliya-md-15041085","type":"search_snippet","evidence":"completed his residency in Neurological Surgery at Penn State Milton S Hershey Medical Center from 2014-2021"}],abns=True)
comp("53:chr:mau","Doximity: Penn State Hershey neurosurgery residency 2015-2022, Rutgers NJMS 2015; Maimonides bio; PSU X post 'Chief'",
 [{"institution":PS,"specialty":"neurosurgery","start":2015,"end":2022}],"Completed neurosurgery residency at Penn State Hershey 2015-2022 (chief 2021); fellowships Adelaide and Moffitt; practising neurosurgeon. DB entry_year 2015 (first seen 2016-17 as PGY-2) consistent with 2015 start.",
 "attending neurosurgeon, Maimonides Medical Center, Brooklyn NY","found",
 [{"url":"https://www.doximity.com/pub/christine-mau-md","type":"doximity","evidence":"Residency, Neurological Surgery, Penn State Milton S Hershey Medical Center 2015 - 2022 (page also lists an anomalous ABPN Psychiatry cert)"},
  {"url":"https://maimo.org/provider-spotlight-dr-christine-mau-neurosurgeon/","type":"search_snippet","evidence":"completed her neurosurgical residency at Penn State in Hershey, PA"}],abns=None)
comp("53:jes:lane","Doximity: Penn State Hershey neurosurgery residency 2015-2022, UVM MD 2015, pediatric neurosurgery fellowship CHLA; VCU faculty bio (namesake risk resolved by program+years+school)",
 [{"institution":PS,"specialty":"neurosurgery","start":2015,"end":2022}],"Completed neurosurgery residency at Penn State Hershey 2015-2022; pediatric neurosurgery fellowship CHLA 2022-23; practising pediatric neurosurgeon.",
 "pediatric neurosurgeon, VCU / Children's Hospital of Richmond, VA","found",
 [{"url":"https://www.doximity.com/pub/jessica-lane-md-172bc65f","type":"doximity","evidence":"Residency, Neurological Surgery, Penn State Milton S Hershey Medical Center 2015 - 2022; Fellowship Pediatric Neurosurgery CHLA 2022-2023; UVM Class of 2015 (page also lists an anomalous ABA cert)"}],abns=None)
