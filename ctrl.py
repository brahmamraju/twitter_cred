import pandas as pd
import vector as v
import preprocessing as p
import cluster2 as c
#import result as r
import classifier as r
a=pd.read_csv("H:\project k\data.csv")
print("cleaning....")
doc,id1=p.clean(a)
print("vectorizing....")
dvec,global_vector=v.vectorize(doc)
print("clustering....")
g,t=c.cluster(dvec,global_vector,id1)
cnt=0
x=[]
print("credibility calculating")
r.classifier(g)
