# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:17:31 2019

@author: haikm
"""
import private
import tweepy


#Twitter Access
auth=tweepy.OAuthHandler(private.TWITTER_APP_KEY, private.TWITTER_APP_SECRET)
    
# Access to user's access key and access secret 
auth.set_access_token(private.TWITTER_KEY, private.TWITTER_SECRET)
  
api = tweepy.API(auth)


msgs = []
msg =[]
keyword=["London"]
key=keyword[0] +".txt"



for tweet in tweepy.Cursor(api.search, q=keyword, count=100, lang='en', result_type='popular', tweet_mode='extended').items(100):
    msg = [tweet.full_text] 
    msg = str(msg)                    
    msgs.append(msg)

with open(key, "w", encoding="utf-8") as file:
    for i in range(len(msgs)):
        file.write(msgs[i])
        file.write('\n')