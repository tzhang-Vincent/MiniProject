# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:51:49 2019

@author: haikm
"""

import tweepy
import private
import json


def get_tweets(username): 
          
        # Authorization to consumer key and consumer secret 
        auth=tweepy.OAuthHandler(private.TWITTER_APP_KEY, private.TWITTER_APP_SECRET)
        
        # Access to user's access key and access secret 
        auth.set_access_token(private.TWITTER_KEY, private.TWITTER_SECRET)
  
        # Calling api 
        api = tweepy.API(auth) 
  
        textlist=[]
        for status in tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode="extended").items():
            textlist.append( status.full_text )

        
         
        user = api.get_user(username)
        print("Name:",user.name)
        print("Location:",user.location)
        print("Following:",user.friends_count)
        print("Followers:",user.followers_count)
        
        with open(username, "w") as file:
            for i in range(len(textlist)):
                file.write(textlist[i] + '\n')
                    
  
# Driver code 
if __name__ == '__main__': 
  
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted. 
    get_tweets("frugaltraveler") 