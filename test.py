import json
from textblob import TextBlob
import numpy

with open('data/clean_tweets.json') as json_data:
    tweets = json.load(json_data)

tweet = tweets[3]
print(tweet)

wiki = TextBlob(tweet['text'])
print(wiki)
print(wiki.sentiment)

wiki2 = TextBlob('rt lmao crazy bitch cant even lose right hillaryclinton lockherup')
print(wiki2.sentiment)

pol = []
sub = []
for i in tweets:
    wiki3= TextBlob(i['text'])
    print(wiki3.sentiment)
    pol.append(wiki3.sentiment.polarity)
    sub.append(wiki3.sentiment.subjectivity)
print('mean of polarity: ' + str(numpy.mean(pol)))
print('mean of subjectivity: ' + str(numpy.mean(sub)))