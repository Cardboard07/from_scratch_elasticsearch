import json

file=r"C:\Users\hrish\Projects\IR\BM25\BM25_scratch\meta_Video_Games.jsonl"
input=r"C:\Users\hrish\Projects\IR\BM25\BM25_scratch\sample.txt"

terms=set()
tids={}
dids={}
d={}

with open(input,'r',encoding='utf-8') as i:
    for l in i:
        for w in l.split():
            terms.add(w)

for i,s in enumerate(terms):
    tids[s]=str(i)

with open(input,'r',encoding='utf-8') as i:
    for ln,l in enumerate(i):
        dids[l]=str(ln)

#with open(file,'w',encoding='utf-8') as f:
for s in terms:
    d[tids[s]]={}

with open(input,'r',encoding='utf-8') as i:
    for l in i:
        for w in l.split():
            if dids[l] in d[tids[w]]:
                d[tids[w]][dids[l]]+=1
            else:
                d[tids[w]][dids[l]]=1

with open(file, 'w', encoding='utf-8') as f:
    for tid, postings in d.items():
        obj = {tid: postings}
        f.write(json.dumps(obj) + "\n")

#extra term for robust
with open(file, 'a', encoding='utf-8') as f:
    obj ={"28214":{}}
    f.write(json.dumps(obj) + "\n")