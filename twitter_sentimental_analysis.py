import tweepy
from textblob import TextBlob
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'acess_token'

access_token_secret = 'access_token_secret'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('imVkohli')
for tweet in public_tweets:
   print(tweet.text)
   analysis = TextBlob(tweet.text)
   print(analysis.sentiment)

