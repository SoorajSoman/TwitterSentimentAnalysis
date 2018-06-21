import tweepy
from textblob import TextBlob
import numpy as np

consumer_key="YOUR-CONSUMER-KEY"
consumer_secret="YOUR-CONSUMER-SECRET-KEY"

access_token="YOUR-ACCESS-TOKEN"
access_token_secret="YOUR-ACCESS-TOKEN-SECRET"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

public_tweets=api.search("Trump")

for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
   
