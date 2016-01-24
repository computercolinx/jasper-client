# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 21:37:02 2016

@author: compu_000
"""
import random
import re
WORDS = ["LOVE"]

def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, with a summary of
        the user's Gmail inbox, reporting on the number of unread emails
        in the inbox, as well as their senders.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., Gmail
                   address)
    """
    messages = ["I love you too!",
                "I know",
                "Who doesn't love you?"]
    message = random.choice(messages)

    mic.say(message)

def isValid(text):
    """
        Returns True if the input is related to email.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\blove\b', text, re.IGNORECASE))
