#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# twitter streaming api
# https://dev.twitter.com/docs/streaming-apis/parameters#locations

import tweepy
import pymongo
import sys
import json

class CustomStreamListener(tweepy.StreamListener):

    def __init__(self):
        tweepy.StreamListener.__init__(self)
        self.scount=-1
        self.__init_db_con()

    def __init_db_con(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        print(self.client.database_names())
        self.db = self.client.tgather
        self.posts = self.db.posts


    def on_data(self, status):
        status=json.loads(status)
        self.posts.insert(status)
        self.scount+=1
        if self.scount%10==0:
            print(status["created_at"]+"\n"+status["user"]["screen_name"]+": "+status["text"])
            print("\n\n")


    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

def get_words(fname):

    #with codecs.open(fname,'r','ascii') as fi:
    with open(fname) as fi:

        words = [ line.strip().lower() \
                    for line in fi.readlines() ]

    return words

def main():

    #uspw   = 'intelcom'
    #t      = 'oslo'
    #us     = 'jeg_kan_edb'
    #pw     = 'intelcom'

    consumer_key="xOZiXiNU6VnOBnTq62cX0EeNv"
    consumer_secret="DxpLViOkEOjVtrXDluoFIMuwzsmbZ7aQ24hGhXWGmjPPzQdG6r"
    access_key = "1490017938-cwb0b9cGbV0q2EnHN7WHGbRq011Qa4U3AQkvygb"
    access_secret = "GFlS1IFhq9yVe0SnycNxaSUHcn0uoFpm44CTVmBweTqL9"

    norsk = get_words('/tgather/words/norsk.txt')
    target = get_words('/tgather/words/target.txt')
    words = norsk+target
    words = sorted(words)

    #words = get_words('./words/test.txt')

    for w in words:
        print(w)
    print

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    sapi = tweepy.streaming.Stream(auth, CustomStreamListener())

    while True:

        try:
            sapi.filter( track=words, languages=['no'] )

        except Exception as e:
            print(e)
            pass
    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_key, access_secret)
    #
    # api = tweepy.API(auth)
    #
    # public_tweets = api.home_timeline()
    # for tweet in public_tweets:
    #     print( tweet.text)



if __name__ == '__main__' :
  main()
