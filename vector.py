import math
def vectorize(documents):
    N=len(documents)
    global_vector=[]
    for i in documents:
        for j in i:
            global_vector.append(j)
    global_vector=list(set(global_vector))

    temp={}
    for i in global_vector:
        temp[i]=0

    doc_vector=[]
    for i in documents:
        doc_vector.append(dict(temp))
    for i in range(0,N):
        for j in documents[i]:
            doc_vector[i][j]+=1
    return doc_vector,global_vector
