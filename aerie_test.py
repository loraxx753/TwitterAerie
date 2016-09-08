import tweepy

import nest
from nest import utils as nest_utils

twitter_consumer_key = "<YOUR TWITTER CONSUMER KEY>"
twitter_consumer_secret = "<YOUR TWITTER CONSUMER SECRET>"


twitter_access_token_key = "<YOUR TWITTER ACCESS TOKEN (THESE DON'T EXPIRE)>"
twitter_access_token_secret = "<YOUR TWITTER ACCESS TOKEN SECRET (THESE DON'T EXPIRE)>"


auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_access_token_key, twitter_access_token_secret)


class MyStreamListener(tweepy.StreamListener):

    _napi = nest.Nest("<NEST ACCOUNT USERNAME>", "<NEST ACCOUNT PASSWORD>")

    def on_status(self, status):
        print(status.text)

    def on_direct_message(self, status):
        new_temp = status.direct_message['text']
        print("Nest is changing the temp to {temp}".format(temp=new_temp))
        self._napi.devices[0].temperature = nest_utils.f_to_c(new_temp)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=auth, listener=myStreamListener)

u = myStream.userstream()
