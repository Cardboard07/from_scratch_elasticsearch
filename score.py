import json
import re
from construct import tids
from construct import dids 
from formula import bm25

file=r"C:\Users\hrish\Projects\IR\BM25\BM25_scratch\meta_Video_Games.jsonl"

print('enter search query: ')

query=input()

query=re.sub(r'[^A-Za-z0-9 ]', ' ', query.lower())

d={}
with open(file, 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            d.update(json.loads(line))

#union of documents 
doclist=set()

for q in query.split():
    if q in tids:
        id=tids[q]
    else:
        id="28214" #hardcoding it for now
    for doc in d[id].keys():
        doclist.add(doc)

#retreival 
ranklist={}
for docs in doclist:
    ranklist[docs]=bm25(query,docs,d)
    
#ranking
results = dict(sorted(ranklist.items(), key=lambda x: x[1], reverse=True))

idsd = {v: k for k, v in dids.items()}

#return
top=10
i=0
for k,v in results.items():
    print(f"{idsd[k]} : {v}")
    i+=1
    if(i>top):
        break