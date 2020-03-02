import csv
import math as m
import pandas as pd
def classifier(g):
    j=0
    df=pd.read_csv('h:/project k/data.csv')
    maxfoll={}
    fav={}
    maxretweet={}
    N=len(df['Follower_count'])

    for i in list(g.values()):
        maxfoll[i]=0
        maxretweet[i]=0
        fav[i]=0
    for i in df['Tweet_id']:
        df['Topic_name'][j]=g[i]
        df['Cred_score']=0
        j+=1

    for i in range(0,N):
        if(df['Follower_count'][i]>maxfoll[df['Topic_name'][i]]):
            maxfoll[df['Topic_name'][i]]=df['Follower_count'][i]
        if(df['Retweet_count'][i]>maxretweet[df['Topic_name'][i]]):
            maxretweet[df['Topic_name'][i]]=df['Retweet_count'][i]
        if(df['Favourites_count'][i]>fav[df['Topic_name'][i]]):
            fav[df['Topic_name'][i]]=df['Favourites_count'][i]

    for i in range(0,N):
        df['Fav_R'][i]=m.log(df['Favourites_count'][i]+1)/m.log(1+fav[df['Topic_name'][i]])
        df['Fol_R'][i]=m.log(df['Follower_count'][i]+1)/m.log(1+maxfoll[df['Topic_name'][i]])
        df['Ret_R'][i]=m.log(df['Retweet_count'][i]+1)/m.log(1+maxretweet[df['Topic_name'][i]])

    df.to_csv('h:/project k/clg/out.csv',index=False)
