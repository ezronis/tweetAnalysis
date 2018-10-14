import json
from textblob import *

with open('data/clean_tweets.json') as json_data:
    tweets = json.load(json_data)

tweet = tweets[3]
print(tweet)

wiki = TextBlob(tweet['text'])
print(wiki)
print(wiki.sentiment)
