# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 21:37:02 2016

@author: compu_000
"""
import re
from wakeonlan import wol
WORDS = ["COMPUTER"]

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
    wol.send_magic_packet('00.24.1D.D1.2D.CA')

    mic.say('Turning on your desktop')

def isValid(text):
    """
        Returns True if the input is related to email.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bcomputer\b', text, re.IGNORECASE))
