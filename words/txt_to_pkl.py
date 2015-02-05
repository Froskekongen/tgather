#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pickle as pkl
import codecs

def get_words(fname):

    with codecs.open(fname,'r','utf8') as fi:
    #with open(fname) as fi:

        words = [ line.strip().lower() \
                    for line in fi.readlines() ]
    print(words)
    return words

norsk=get_words('norsk.txt')
target=get_words('target.txt')

with open('norsk.pkl',mode='wb') as ff:
    pkl.dump(norsk,ff,protocol=-1)

with open('target.pkl',mode='wb') as ff:
    pkl.dump(target,ff,protocol=-1)
