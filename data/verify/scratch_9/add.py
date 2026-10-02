import json,sys
rows=json.load(open('scratch_9/rows.json')) if __import__('os').path.exists('scratch_9/rows.json') else []
new=json.load(sys.stdin)
rows.extend(new if isinstance(new,list) else [new])
json.dump(rows,open('scratch_9/rows.json','w'),indent=1)
json.dump(rows,open('batch_9_out.json','w'),indent=1)
print(len(rows))
