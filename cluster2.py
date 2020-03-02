def cluster(doc_vector,global_vector,id1):
    N=len(doc_vector)
    cnt=N
    group={}
    temp_vector=list(doc_vector)
    df={}
    for i in id1:
        group[i]=0
    m=90    
    while(m>=25):
        
        for i in global_vector:
            df[i]=0
#finding document frequency in temp_vector
        for i in temp_vector:
            #i=list(set(i))
            for j in i:
                df[j]+=i[j]    
        m=0
#finding topic with maxium frequency
        for i in df:
            if(m<df[i]):
                m=df[i]
                topic=i
#        print(m)
        cnt=[]
        for i in range(0,len(id1)):
            if(temp_vector[i][topic]>=1):
                group[id1[i]]=topic
                cnt.append(id1[i])
                temp_vector[i]=0
        for i in cnt:
            id1.remove(i)
            temp_vector.remove(0)
    print(len(temp_vector))
    return group,temp_vector
