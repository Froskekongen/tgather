#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# twitter streaming api
# https://dev.twitter.com/docs/streaming-apis/parameters#locations

import tweepy
import pymongo
import sys
import json
import pickle as pkl

class CustomStreamListener(tweepy.StreamListener):

    def __init__(self,host):
        tweepy.StreamListener.__init__(self)
        self.scount=-1
        self.__init_db_con(host)

    def __init_db_con(self,host):
        self.client = pymongo.MongoClient(host, 27017)
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
        print(sys.stderr, 'Encountered error with status code:', status_code)
        return True # Don't kill the stream

    def on_timeout(self):
        print(sys.stderr, 'Timeout...')
        return True # Don't kill the stream



def main():

    #uspw   = 'intelcom'
    #t      = 'oslo'
    #us     = 'jeg_kan_edb'




    nArgs=len(sys.argv)
    hh=sys.argv[1]
    if nArgs==2:
        baseDir="/tgather"
    else:
        baseDir=sys.argv[2]
    with open(baseDir+'/words/norsk.pkl',mode='rb') as ff:
        norsk=pkl.load(ff)
    with open(baseDir+'/words/target.pkl',mode='rb') as ff:
        target=pkl.load(ff)
    print(norsk)
    words = norsk+target
    words = sorted(words)


    #words = get_words('./words/test.txt')

    for w in words:
        print(w)
    print

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    sapi = tweepy.streaming.Stream(auth, CustomStreamListener(hh))

    while True:

        try:
            sapi.filter( track=words, languages=['no'] )

        except Exception as e:
            print(e)
            pass




if __name__ == '__main__' :
  main()
