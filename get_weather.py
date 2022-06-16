import urllib.request
import json

def get_weather(lat, lon):
    """
    Get the weather at a given location
    """
    key = '4862887cedf2ef1a27d4b078649921f0'
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    return result