import json
import re

path = r"C:\Users\hrish\Projects\IR\BM25\BM25_scratch\meta_Video_Games.jsonl"
with open(path, 'r', encoding='utf-8') as fp, open('sample.txt','w', encoding='utf-8') as file:
    for line in fp:
        d=json.loads(line.strip())
        if d['main_category']=="Video Games":
            s = re.sub(r'[^A-Za-z0-9 ]', ' ', d['title'].lower())
            file.write(s+'\n')