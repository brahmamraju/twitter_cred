import pandas as pd
import vector as v
import preprocessing as p
import cluster2 as c
import classifier as r
a=pd.read_csv("Z:/TermPaper/twitter_cred-master/data.csv")
print("cleaning....")
doc,id1=p.clean(a)
print("vectorizing....")
dvec,global_vector=v.vectorize(doc)
print("clustering....")
g,t=c.cluster(dvec,global_vector,id1)
cnt=0
x=[]
print(len(t))
print("credibility calculating")
r.classifier(g)
