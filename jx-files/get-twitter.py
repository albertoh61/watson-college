#!/usr/bin/env python2.7

import sys
import requests
import json
import twitter
import re



# Get previous 200 tweets from specified user
def getTweets(user):
  twitter_consumer_key = 'RU02u4DcvQbglyj8IdvD6KN9M'
  twitter_consumer_secret = '4z0cpEAFb3BpBp5p4jfnjVoX32NsmWG2DKpkzab7FyepFHmesf'
  twitter_access_token = '464146004-hwW2ZdEGoX30iP3O7hnXSaQ1bs7Fa62Roj9mx5Vk'
  twitter_access_secret = 'zY81KH0KYSErvmWceasTird0toxWrx2dsO5CMKRxi7z1W'

  twitter_api=twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)
  tweets = twitter_api.GetUserTimeline(screen_name=user, count=500, include_rts=True)
  tweet_text = ''
  for tweet in tweets:
    tweet_text += tweet.text.encode('utf-8').strip() + ' '

  return tweet_text


# Main

# For each specified user download tweets as string
for twitter_handle in sys.argv[1:]:
  try:
    user_tweets=getTweets(twitter_handle)
    print re.sub('http[s]?[^ ]*', '', user_tweets)


  except:
    print "Download failed..."





    
