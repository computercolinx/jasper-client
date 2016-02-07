# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 21:37:02 2016

@author: compu_000
"""
import googlemaps
import re
import datetime
WORDS = ["TRAFFIC"]

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
    mic.say("Getting time to work")
    gmaps = googlemaps.Client(key=profile['keys']['GOOGLE_SPEECH'])
    now = datetime.datetime.now()
    directions_result = gmaps.distance_matrix(profile['home'],
                                     profile['work'],
                                     mode="driving",
                                     departure_time=now)
    message = "It will take " + directions_result['rows'][0]['elements'][0]['duration']['text'] + " to get to work"

    mic.say(message)

def isValid(text):
    """
        Returns True if the input is related to email.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\btraffic\b', text, re.IGNORECASE))
