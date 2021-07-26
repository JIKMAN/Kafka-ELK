import tweepy

twitter_api_key = '<twitter_api_key>'
twitter_api_secret_key = '<twitter_api_secret_key>'
twitter_access_token = '<twitter_access_token>'
twitter_access_token_secret = '<twitter_access_token_secret>'

class SimpleStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status)

stream_listener = SimpleStreamListener()

auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret_key)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)

twitterStream = tweepy.Stream(auth, stream_listener)
twitterStream.filter(track=['data'])