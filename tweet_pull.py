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
  
        # 200 tweets to be extracted 
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username) 
  
        # Empty Array 
        tmp=[]  
  
        # create array of tweet information: username,  
        # tweet id, date/time, textxt 
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
        for j in tweets_for_csv: 
  
            # Appending tweets to the empty array tmp 
            tmp.append(j)  
  
        # Printing the tweets 
        x=print(tmp) 
        
        with open("example. txt", "w") as file:
                for i in range(len(tmp)):
                    file.write(tmp[i] + '\n')
                    
  
# Driver code 
if __name__ == '__main__': 
  
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted. 
    get_tweets("BostonGlobe") 