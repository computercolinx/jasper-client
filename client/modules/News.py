# -*- coding: utf-8-*-
import re
import feedparser
import string
WORDS = ["NEWS", "YES", "NO", "FIRST", "SECOND", "THIRD"]

PRIORITY = 3


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, with a summary of
        the day's top news headlines, sending them to the user over email
        if desired.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    mic.say("Pulling up the news")
    try:
        cnn_feed = feedparser.parse('http://rss.cnn.com/rss/cnn_topstories.rss')
        all_titles = ''
        for i in range(3):
            headline = cnn_feed.entries[i].description
            headline = headline[:string.find(headline,"<")]
            all_titles = all_titles + headline + ' '
        mic.say("Here are the current top headlines. " + all_titles)            
    except:
        mic.say("Error retrieving articles")



def isValid(text):
    """
        Returns True if the input is related to the news.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b(news|headline)\b', text, re.IGNORECASE))
