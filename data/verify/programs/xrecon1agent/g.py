import json,sys
d=json.load(open('/Users/neureal/Documents/Residency Application Study/data/verify/phase3/merged_final.json'))
for q in sys.argv[1:]:
  for r in d:
    if q.lower() in r['name'].lower(): print(q,'|',r['name'],r['program_id'],r['program'],r['entry_year'],r['first_seen'],r['last_seen'],r['last_pgy'],r['outcome'])
