# -*- coding: utf-8-*-
import re
import forecastio
import datetime
WORDS = ["WEATHER", "TODAY", "TOMORROW"]


def handle(text, mic, profile):
    """
    Responds to user-input, typically speech text, with a summary of
    the relevant weather for the requested date (typically, weather
    information will not be available for days beyond tomorrow).

    Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    api_key = profile['keys']['forecastio']
    lat = profile['loc']['lat']
    long = profile['loc']['long']
    forecast_time = datetime.datetime.now()
    if bool(re.search(r'\b(tonight)\b', text, re.IGNORECASE)):
        forecast_time = datetime.datetime.combine(datetime.datetime.now().date(),datetime.time(hour=21))
    elif bool(re.search(r'\b(tomorrow)\b', text, re.IGNORECASE)):
        forecast_time = datetime.datetime.combine(datetime.datetime.now().date(),datetime.time(hour=12))
        forecast_time = forecast_time + datetime.timedelta(days=1)
    forecast = forecastio.load_forecast(api_key,lat, long,time=forecast_time)
    response = "The forecast is " + forecast.currently().summary + " with a temperature of " \
    forecast.currently().temperature + " and a %d chance of precipitation" % forecast.currently().precipProbability
    mic.say(response)
    
def isValid(text):
    """
        Returns True if the text is related to the weather.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b(weathers?|temperature|forecast|outside|hot|' +
                          r'cold|jacket|coat|rain)\b', text, re.IGNORECASE))
