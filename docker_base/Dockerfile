FROM ubuntu:latest
MAINTAINER froskekongen <erlend.aune.1983@gmail.com>

# Necessary to add a ppa
RUN apt-get update && apt-get install -y python3-pip git

RUN easy_install3 -U pip
RUN pip3 install tweepy

RUN pip3 install requests --upgrade
RUN pip3 install requests-oauthlib --upgrade
RUN pip3 install six --upgrade


RUN pip3 install pymongo
