# Twitter Sentiment Analysis Utility

The goal of this python utility is to clean tweets and analyze the sentiment each tweet.

### On the to do list: 
  - look for methods to remove emoticons
  - compare what the sentiment classification is with and without emoticons
  - there are 1762 tweets in tweets.json
  - the data is from http://help.sentiment140.com/for-students
  - first column is the polarity of the tweet (0-negative, 2-neutral, 4-positive)  

Result: clean_tweets.json
Snippet of initial DF:
                            date    id    ...            username sentiment
0     2018-03-10T22:33:29.178145Z     5    ...                 shy         0
1     2018-03-10T22:34:13.494308Z     6    ...               RinaS         0
2     2018-03-23T01:04:30.989333Z     7    ...              @RinaS         0
3     2018-03-23T01:04:30.995952Z     8    ...              @RinaS         0
4     2018-03-23T01:04:30.998789Z     9    ...              @RinaS         0
5     2018-03-23T01:04:31.001682Z    10    ...              @RinaS         0
6     2018-03-23T01:04:31.004963Z    11    ...              @RinaS         0
7     2018-03-23T01:04:31.008200Z    12    ...              @RinaS         0

[1762 rows x 7 columns]

Data Dict output:
{'dataset_shape': (1762, 3),
 'pre_clean_len': {'description': 'Length of the tweet before cleaning',
                   'type': dtype('int64')},
 'sentiment': {'description': 'sentiment class - 0:negative, 1:positive',
               'type': dtype('int64')},
 'text': {'description': 'tweet text', 'type': dtype('O')}}

means:
pre-clean tweet length = 120.11691259931895 chars
post-clean tweet length = 73.88081725312145 chars
average # of chars removed =  46.2360953461975 chars

Sample Readme from https://github.com/x0rz/tweets_analyzer below:

# Simple Twitter Profile Analyzer

The goal of this simple python script is to analyze a Twitter profile through its tweets by detecting:
  - Average tweet activity, by hour and by day of the week
  - Timezone and language set for the Twitter interface
  - Sources used (mobile application, web browser, ...)
  - Geolocations
  - Most used hashtags, most retweeted users and most mentioned users
  - Friends analysis based on most frequent timezones/languages

There are plenty of things that could be added to the script, feel free to contribute! 👍

### Usage

```
usage: tweets_analyzer.py -n <screen_name> [options]

Simple Twitter Profile Analyzer

optional arguments:
  -h, --help            show this help message and exit
  -l N, --limit N       limit the number of tweets to retreive (default=1000)
  -n screen_name, --name screen_name
                        target screen_name
  -f FILTER, --filter FILTER
                        filter by source (ex. -f android will get android
                        tweets only)
  --no-timezone         removes the timezone auto-adjustment (default is UTC)
  --utc-offset UTC_OFFSET
                        manually apply a timezone offset (in seconds)
  --friends             will perform quick friends analysis based on lang and
                        timezone (rate limit = 15 requests)
  -e path/to/file, --export path/to/file
                        exports results to file
  -j, --json            outputs json
  -s, --save            saves tweets to tweets/{twitter_handle}/{yyyy-mm-
                        dd_HH-MM-SS}.json
  --no-color            disables colored output
  --no-retweets         does not evaluate retweets
```

### Example output

![Twitter account activity](https://cdn-images-1.medium.com/max/800/1*KuhfDr_2bOJ7CPOzVXnwLA.png)

License
----
GNU GPLv3


If this tool has been useful for you, feel free to thank me by buying me a coffee

[![Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoff.ee/x0rz)