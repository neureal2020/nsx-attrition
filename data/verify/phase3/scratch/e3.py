import sys; sys.path.insert(0,'scratch')
from add052 import add
add("51:can:carpenter",identity="probable",identity_basis="Univ. of Cincinnati MD 2016 (matches 2016 OSU entry); WebMD/US News list Candice D. Carpenter neurosurgeon at OSU Wexner; distinctive name; Doximity (cv/c88cmd) Neurosurgery Cincinnati, Class of 2016 only",
 residency_stated=[{"institution":"Ohio State University Hospital","specialty":"neurosurgery","start":2016,"end":None}],
 outcome="unknown",outcome_detail="No residency dates or ABNS on Doximity; UCLA Biodesign 2023-24 Discovery Fellow (MD, MBA Oxford, MPH Harvard, EdM Harvard); co-CEO Boston Congress of Public Health; 'physician-serial entrepreneur'. Not on OSU current roster or alumni list. Pattern suggests she left clinical neurosurgery training for degrees/entrepreneurship, but no source states it.",
 year_left=2019,destination_program=None,destination_start_year=None,current="physician-entrepreneur, Co-CEO Boston Congress of Public Health; UCLA Biodesign fellow 2023-24",
 agrees_with_db=True,disagreement="",
 checks={"google":"found","doximity":"found"},abns_certified=False,
 sources=[{"url":"https://www.doximity.com/cv/c88cmd","type":"doximity","evidence":"Candice Danielle Carpenter MD Neurosurgery Cincinnati; University of Cincinnati College of Medicine Class of 2016 (no residency listed)"},{"url":"https://bcph.org/bcph-co-ceo-dr-candice-d-carpenter/","type":"bio","evidence":"BCPH Co-CEO, Chief of Strategy and Innovation; MD Cincinnati, MBA Oxford, MPH Harvard Chan, Ed.M. Harvard"}],searches_used=2)
add("51:ore:zaninovich",identity="confirmed",identity_basis="Doximity Orel Anthony Zaninovich: Univ. of Arizona MD 2017, OH license 2019-2022 (matches OSU 2019 entry), NM license 2018-2020; neurosurgery publications",
 residency_stated=[],
 outcome="switched_specialty",outcome_detail="Now board-certified anesthesiologist (ABA), Oro Valley AZ; left OSU neurosurgery after PGY-1 2019-20; anesthesiology residency program/dates not stated on public page.",
 year_left=2020,destination_program=None,destination_start_year=None,current="anesthesiologist, Oro Valley AZ",
 agrees_with_db=True,disagreement="DB: did not complete; destination now found: anesthesiology",
 checks={"google":"found","doximity":"found"},abns_certified=False,
 sources=[{"url":"https://www.doximity.com/pub/orel-zaninovich-md","type":"doximity","evidence":"Anesthesiology, Oro Valley AZ; University of Arizona College of Medicine Class of 2017; OH State Medical License 2019 - 2022; American Board of Anesthesiology"}],searches_used=2)
add("51:ahm:jorge",identity="probable",identity_basis="OSU Neurosurgery X post: Match 2021 welcomed Mark Damante, Ahmed Jorge, Josh Weinberg; Pitt MD 2021; Doximity Ahmed Jorge at OSU Doan Hall address",
 residency_stated=[{"institution":"Ohio State University Hospital","specialty":"neurosurgery","start":2021,"end":None}],
 outcome="unknown",outcome_detail="Classmates Damante and Weinberg are PGY-6 on the current OSU roster; Jorge is absent from the roster and OSU alumni list. Doximity profile is empty (Other MD/DO, OSU address). No destination found. (Match-2021 class implies July 2021 or 2022 start.)",
 year_left=2024,destination_program=None,destination_start_year=None,current="unknown",
 agrees_with_db=True,disagreement="",
 checks={"google":"found","doximity":"found"},abns_certified=None,
 sources=[{"url":"https://x.com/NeurosurgeryOSU/status/1372971646819004420","type":"search_snippet","evidence":"We are so thrilled to welcome Mark Damante, Ahmed Jorge, and Josh Weinberg to our Neurosurgery family! #NeuroMatch2021"},{"url":"https://medicine.osu.edu/departments/neurosurgery/education/residency/residents","type":"program_page","evidence":"PGY 6: Mark Damante, Joshua Weinberg; Jorge not listed"},{"url":"https://www.doximity.com/pub/ahmed-jorge-md","type":"doximity","evidence":"Ahmed Jorge MD, Other MD/DO, Columbus OH, 410 W 10th Ave Doan Hall; no education listed"}],searches_used=3)
add("51:chr:swann",identity="probable",identity_basis="Doximity 'Christen O'Neal MD' OSU neurosurgery 2022-2028, Univ. of Oklahoma MD 2022; search results link Christen O'Neal Swann to the same OSU neurosurgery research profile (listed under a different surname at OSU)",
 residency_stated=[{"institution":"Ohio State University Hospital","specialty":"neurosurgery","start":2022,"end":2028}],
 outcome="unknown",outcome_detail="Doximity (possibly stale) shows OSU neurosurgery residency 2022-2028, PGY-4, OH license 2026-2028. She is not on the current OSU resident roster page (PGY-5 class shows other names), so her status after 2025-26 is unresolved; may have left or be on a leave/research track.",
 year_left=2026,destination_program=None,destination_start_year=None,current="OSU neurosurgery resident per Doximity (unverified/stale)",
 agrees_with_db=False,disagreement="DB: left after 2025-26; Doximity still lists her as continuing OSU 2022-2028 (may be stale)",
 checks={"google":"found","doximity":"found"},abns_certified=False,
 sources=[{"url":"https://www.doximity.com/pub/christen-o-neal-md","type":"doximity","evidence":"Ohio State University Hospital Residency, Neurological Surgery, 2022 - 2028; University of Oklahoma College of Medicine Class of 2022; PGY-4"},{"url":"https://medicine.osu.edu/departments/neurosurgery/education/residency/residents","type":"program_page","evidence":"current OSU roster does not list her"}],searches_used=4)
