import urllib.request
import json

def address(lat, lon):
    key = 'xbFpnVexSvz3m4GhIhOsSfRM9WqMAjvu'
    url = f'http://www.mapquestapi.com/geocoding/v1/reverse?key={key}&location={lat},{lon}&includeRoadMetadata=true&includeNearestIntersection=true'
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    return result