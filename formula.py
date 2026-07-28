import numpy as np
from construct import tids
from construct import dids

def bm25(query,did,d,k1=1.2):
    score=0
    for q in query.split():
        score+=np.log(len(dids)/len(d[tids[q]]))*((k1+1)*d[tids[q]][did]/(k1 + d[tids[q]][did]))
    return score