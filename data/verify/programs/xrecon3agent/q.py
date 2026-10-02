import json,sys
d=json.load(open('/Users/neureal/Documents/Residency Application Study/data/verify/phase3/merged_final.json'))
a=sys.argv[1]
for r in d:
    if (a.isdigit() and r['program_id']==int(a)) or (not a.isdigit() and a.lower() in r['name'].lower()):
        print(r['program_id'],r['name'],r['entry_year'],r['first_seen'],r['last_seen'],r['last_pgy'],r.get('outcome_2025'),r['program'][:40])
