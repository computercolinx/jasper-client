# -*- coding: utf-8-*-
import re
import ystockquote as ys
WORDS = ["STOCKS"]

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
    mic.say("Getting Stock Info")
    try:
        output = ''
        for symbol in profile['stocks']:
            print symbol
            stock_info = ys.get_all(symbol)
            print stock_info
            current_out = symbol + " Current Price is " + stock_info['price'] + \
            " with a daily change of " + stock_info['change'] + " ... "
            print current_out
            output = output + current_out
        mic.say(output)
    except:
        mic.say("Error retrieving stocks")



def isValid(text):
    """
        Returns True if the input is related to the news.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bstocks\b', text, re.IGNORECASE))
