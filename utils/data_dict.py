# https://towardsdatascience.com/another-twitter-sentiment-analysis-bb5b01ebad90
from pprint import pprint

def data_dict(df, col_name):
    data_dict = {
        'sentiment':{
            'type':df.sentiment.dtype,
            'description':'sentiment class - 0:negative, 1:positive'
        },
        'text':{
            'type':df.text.dtype,
            'description':'tweet text'
        },
        'pre_clean_len':{
            'type':df[col_name].dtype,
            'description':'Length of the tweet before cleaning'
        },
        'dataset_shape':df.shape
    }
    pprint(data_dict)