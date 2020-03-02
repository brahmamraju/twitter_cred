import pandas as pd
from nltk.corpus import stopwords
import re

def clean(a):
    stop_words=set(stopwords.words('english'))
    documents=[]
    for i in a['Tweet']:
        i=re.sub('[^A-Za-z0-9 ]+', '', i)
        i=i.lower()
        documents.append(i.split())
    p_doc=[]
    N=len(documents)
    for i in range(0,N):
        p_doc.append([])
        for j in documents[i]:
            if j not in stop_words:
                p_doc[i].append(j)
    id1=[]
    for i in a['Tweet_id']:
        id1.append(i)
    return p_doc,id1
