from wordcloud import WordCloud


def word_cloud(df):
    neg_tweets = df[df.target == 0]
    neg_string = []
    for t in neg_tweets.text:
        neg_string.append(t)
    neg_string = pd.Series(neg_string).str.cat(sep=' ')
    
    wordcloud = WordCloud(width=1600, height=800,max_font_size=200).generate(neg_string)
    plt.figure(figsize=(12,10))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()