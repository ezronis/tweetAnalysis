import json

with open('tweets.json') as json_data:
    tweets = json.load(json_data)
print tweets

