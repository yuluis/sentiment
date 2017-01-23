import tweepy
from textblob import TextBlob

consumer_key = 'kuipY7CmZTS8yZUVwQ56cWWoU'
consumer_secret = 'STF8I4s3PTqrNaez01YhIbz2ZE0FmDjiHH5htG4OXvopwvfKx7' 

access_token = '51710533-ABiT2Bbu4n8ESnP7bAShJKABHqWf1uEao96v3Pm0W' 
access_token_secret = '73IR1uzH9CQKGg5CukNGMb3Qolv98SLNX9GrlmpfLr7zL' 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Hillary')

import csv

with open('sentiment.csv', 'wb') as csvfile:
    sentwriter = csv.writer(csvfile, delimiter = ' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    sentwriter.writerow('blah1')
    sentwriter.writerow('blah2')

    for tweet in public_tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment.polarity)
        if (analysis.sentiment.polarity > 0):
            sent = 'POSITIVE : '
        else:
            sent = 'NEGATIVE : '
        row = (unicode(sent) + tweet.text )
        print(row)
        # !!! csv.writerow doesn't support unicode
