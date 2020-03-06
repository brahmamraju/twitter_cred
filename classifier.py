import math as m
import pandas as pd
import sentiment as s
def classifier(g):
    j=0
    df=pd.read_csv('Z:/TermPaper/twitter_cred-master/data.csv')
    maxfoll={}
    fav={}
    maxretweet={}
    topic_count={}
    N=len(df['Follower_count'])
    for i in list(g.values()):
        maxfoll[i]=0
        maxretweet[i]=0
        fav[i]=0
        topic_count[i]={}
    for i in topic_count:
        topic_count[i]['negative']=0
        topic_count[i]['positive']=0

    x={}
    for i in g.values():
        x[i]=0
    for i in g:
        x[g[i]]+=1
    for i in df['Tweet_id']:
        df['Topic_name'][j]=g[i]
        j+=1

    for i in range(0,N):
        if(df['Follower_count'][i]>maxfoll[df['Topic_name'][i]]):
            maxfoll[df['Topic_name'][i]]=df['Follower_count'][i]
        if(df['Retweet_count'][i]>maxretweet[df['Topic_name'][i]]):
            maxretweet[df['Topic_name'][i]]=df['Retweet_count'][i]
        if(df['Favourites_count'][i]>fav[df['Topic_name'][i]]):
            fav[df['Topic_name'][i]]=df['Favourites_count'][i]
                        
    for i in range(0,N):
#        print(polarity)
        df['Fav_R'][i]=m.log(df['Favourites_count'][i]+1)/m.log(1+fav[df['Topic_name'][i]])
        df['Fol_R'][i]=m.log(df['Follower_count'][i]+1)/m.log(1+maxfoll[df['Topic_name'][i]])
        df['Ret_R'][i]=m.log(df['Retweet_count'][i]+1)/m.log(1+maxretweet[df['Topic_name'][i]])
        df['Event_Engagement'][i]=df['Fav_R'][i]+df['Ret_R'][i]
        df['User_Activity'][i]=list(df['Name']).count(df['Name'][i])/x[df['Topic_name'][i]]
        df['Polarity'][i]=s.cal_sentiment(df['Tweet'][i])
        df['User_Influence'][i]=(df['Ret_R'][i]+df['User_Activity'][i]+df['Event_Engagement'][i])/m.log(x[df['Topic_name'][i]])
        topic_name=df['Topic_name'][i]
        polarity=df['Polarity'][i]
        topic_count[topic_name][polarity]+=1

    for i in range(0,N):
        topic_name=df['Topic_name'][i]
        polarity=df['Polarity'][i]
        df['Sentiment_Score'][i]=topic_count[topic_name][polarity]/(topic_count[topic_name]['negative']+topic_count[topic_name]['positive'])
        df['Cred_Score'][i]=df['Sentiment_Score'][i]*df['User_Influence'][i]
    
    df.to_csv('Z:/TermPaper/twitter_cred-master/out.csv',index=False)
