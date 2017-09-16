import tweepy

consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'

access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Get the latest public tweets from your feed
public_tweets = api.home_timeline()

for tweet in public_tweets:
	print (tweet.text)

#Get your latest tweets
user_tweets = api.user_timeline()

for tweet in user_tweets:
	print (tweet.text)

#Update your status with a tweet
new_status = api.update_status('Hello World')
