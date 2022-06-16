import urllib.request
import json

def iss_loc():

    url = "http://api.open-notify.org/iss-now.json"
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())

    #print(result)

    lat = result['iss_position']['latitude']
    lon = result['iss_position']['longitude']
    
    return lat, lon