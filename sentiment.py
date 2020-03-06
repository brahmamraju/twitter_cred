import textblob as t
def cal_sentiment(text):
    x=t.TextBlob(text).sentiment.polarity
    if(x<0):
        return "negative"
    return "positive"

