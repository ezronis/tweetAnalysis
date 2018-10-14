from utils.df_methods import *


cols = ['sentiment','id','date','location','username','text', 'isRetweet']

# loading data from json
df = json_to_df('data/tweets.json')
print(df)

# creating sentiment column with default value
df['sentiment'] = 0

# dropping unnecessary cols
df.drop(['id','date','location','username', 'isRetweet'],axis=1,inplace=True)

# adding col w. string len before clean and printing data_dict
create_string_len_col(df, 'preclean_len')

# cleaning tweets
clean_tweets = get_clean_tweets(df, 'preclean_len')

# getting tweet length post cleanse
create_string_len_col(clean_tweets, 'afterclean_len')

print('means')
print(clean_tweets['preclean_len'].mean())
print(clean_tweets['afterclean_len'].mean())
print((clean_tweets['preclean_len'] - clean_tweets['afterclean_len']).mean())
clean_tweets.info()
df_to_file(clean_tweets, 'data/clean_tweets.json')