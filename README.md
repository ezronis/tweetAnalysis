# look for methods to remove emoticons
# compare what the sentiment classification is with and without emoticons
# there are 1762 tweets in tweets.json
# the data is from http://help.sentiment140.com/for-students
## first column is the polarity of the tweet (0-negative, 2-neutral, 4-positive)

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
8     2018-03-23T01:04:31.010738Z    13    ...              @RinaS         0
9     2018-03-23T01:04:31.013128Z    14    ...              @RinaS         0
10    2018-03-23T01:04:31.015570Z    15    ...              @RinaS         0
11    2018-03-23T01:04:31.017833Z    16    ...              @RinaS         0
12    2018-03-23T01:04:31.346717Z    17    ...              @RinaS         0
13    2018-03-23T01:04:31.350697Z    18    ...              @RinaS         0
14    2018-03-23T01:04:31.354496Z    19    ...              @RinaS         0

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
