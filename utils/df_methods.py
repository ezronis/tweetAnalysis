import json
import pandas as pd
import os.path
import inspect
import matplotlib.pyplot as plt
from utils.tweet_cleaner import *
from utils.data_dict import *


def json_to_df(file_name):
    if os.path.isfile(file_name):
        # loading tweets from json
        with open(file_name) as json_data:
            tweets = json.load(json_data)
        data = []
        for r in tweets:
            data.append(r)
        # reading data into data frame
        df = pd.DataFrame(data)
        # creating sentiment column with default value
        df['sentiment'] = 0
        # dropping unnecessary cols
        # df.drop(['id','date','location','username', 'isRetweet'],axis=1,inplace=True)
        return df
    else:
        print('this file does not exist')


def create_string_len_col(df, col_name):
    ## data prep
    # adding column for length of tweet before prep
    df[col_name] = [len(t) for t in df.text]
    print('dimensions of df: ')
    print(df.shape)  # dim (1762,2)
    # taking a look at our data using data_dict
    data_dict(df, col_name)
    return df


def create_box_plot(df, col_name):
    # printing box plot distribution of length of strings in each entry
    fig, ax = plt.subplots(figsize=(5, 5))
    plt.boxplot(df[col_name])
    plt.show()


def get_clean_tweets(df, col_name):
    # applying tweet_cleaner to data
    clean_tweet_texts = []
    dim = range(df.shape[0])
    print('dim of df: ')
    print(df.shape)
    for i in dim:
        clean_tweet_texts.append(tweet_cleaner(df['text'][i]))
        print(len(clean_tweet_texts))
    clean_df = pd.DataFrame(clean_tweet_texts, columns=['text'])
    clean_df['sentiment'] = df['sentiment']
    clean_df[col_name] = df[col_name]
    print('tweets are clean!')
    print(clean_df.head())
    return clean_df


def df_to_file(df, file_name):
    print('make sure you included a file extension! json/txt')
    if os.path.isfile(file_name):
        print(file_name + ' already exists')
    else:
        ## TRY THIS AGAIN
        out = df.to_json(orient='records')[1:-1].replace('},{', '},{')
        with open(file_name, 'w') as f:
            f.write(out)
