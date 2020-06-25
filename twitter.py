
import tweepy 
from textblob import TextBlob
import pandas as pd
import numpy as np
import re


#Verify Credentials
consumer_key = "MMOm1EDQPrq4UCu2W3gWItlNl" 
consumer_secret = "yud6w8prkqCpZXizrTkTNbWqzUabLSO2Pdi8jOWhOrpdtDIhYl"
access_key = "993820627885637632-p642kGO3bO8hYy1Xph5tKOnXNQ0DJ1v"
access_secret = "PSl4QnAP1leuaVGKQ3yi5S77nhcb02P0fmq1vuLTlOjgJ"



#authorization
def authorize():

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
    auth.set_access_token(access_key, access_secret) 

    api = tweepy.API(auth) 
    
    return api

def user_info(username):
        api = authorize()
        user = api.get_user(screen_name = username)
        name = user.name
        print('Name : ' + name)
        ID = user.id_str
        print("The ID of the user is : " + ID)
        description = user.description 
        print("The description of the user is : " + description) 
        followers_count = user.followers_count 
        print("The number of followers of the user are : " + str(followers_count)) 
        created_at = user.created_at 
        print("The user was created on : " + str(created_at))
        location = user.location 
        print("The location of the user is : " + location)
        favourites_count = user.favourites_count
        print("The number of tweets the user has liked are : " + str(favourites_count))


# Function to extract tweets 
def get_tweets(username): 
        api = authorize()
        tweets = api.user_timeline(screen_name=username, tweet_mode="extended" , count=5) 
        i = 1
        for tweet in tweets: 
                print(str(i)+')' + tweet.full_text + '\n')   
                i = i + 1
                print('=============================================================================================')


def cleanTxt(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'https?:\/\/S+', '', text)
    
    return text



def getsubjectivity(text):
        return TextBlob(text).sentiment.subjectivity

def getPolarity(text):
        return TextBlob(text).sentiment.polarity



def getAnalysis(score):
        if score < 0:
                return 'Negative'
        elif score == 0 :
                return 'Neutral'
        else:
                return 'Positive'        

def get_polarity(username):  
        api = authorize()
        tweets = api.user_timeline(screen_name=username, tweet_mode="extended", count=5) 
      
        df = pd.DataFrame([tweet.full_text for tweet in tweets], columns=['Tweets'])
        
        df['Tweets'] = df['Tweets'].apply(cleanTxt)
        df['Polarity'] = df['Tweets'].apply(getPolarity)
        df['Analysis'] = df['Polarity'].apply(getAnalysis)
        df.drop(['Polarity'], axis=1, inplace=True)
        ptweets = df[df.Analysis == 'Positive']
        ptweets = ptweets['Tweets']
        print( '\n' + "TWEET ANALYSIS"  + '\n')
        round( (ptweets.shape[0] / df.shape[0])*100, 1)
        print(df.head(5))

def runt():
        print('''
========================================Twitter==============================================

                              For User Info Enter Twitter ID
=============================================================================================
        ''')
        Acct = input("Enter Account>>>> ")

        print('\n')
        print('\n')
        user_info(Acct)
        print('\n')
        print('=============================================================================================')
        print('=============================================================================================')

        get_tweets(Acct) 
        print('=============================================================================================') 
        get_polarity(Acct)