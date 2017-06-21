import rest_credentials
import tweepy


#auth = tweepy.OAuthHandler(credentials.TWITTER_APP_KEY, credentials.TWITTER_APP_SECRET)
#auth.set_access_token(credentials.TWIITER_KEY, credentials.TWITTER_SECRET)
#api = tweepy.API(auth)

auth = tweepy.OAuthHandler(rest_credentials.CONSUMER_KEY, rest_credentials.CONSUMER_SECRET)
auth.set_access_token(rest_credentials.ACCESS_TOKEN_KEY, rest_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
	print tweet.text
