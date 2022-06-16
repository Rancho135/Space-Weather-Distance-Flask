import urllib.request
import json
from get_iss import iss_loc
from get_weather import get_weather
from get_address import address
from get_distance import dist
from get_country import country
from flask import Flask, render_template

app = Flask('app')

@app.route('/')
def iss_data():
  data = []
  
  #distance from the iss
  distance = dist(46.474529,-80.945824,48.7575098,-91.6218292)
  dist_ = f"I am {distance}km from the ISS"
  data.append(dist_)
  print(data)

# weather below the space station in Celsius
  data1 = iss_loc()
  
  lat, lon = data1[0], data1[1]
  
  google_map = "https://www.google.com/maps/place/" + lat + "+" + lon
  print(google_map)
  
  #weather
  weather = get_weather(lat, lon)
  #print(weather)
  temp_c = round(weather["main"]["temp"] - 273.15,2)
  desc = weather["weather"][0]['description']
 
  weather_desc = f" The weather below the space station is {temp_c}C, {desc}"
  print(weather_desc)

  #address reverse geolocation
  addr = address(lat,lon)
  cont_code = addr["results"][0]['locations'][0]["adminArea1"]
  print(cont_code)
  
  if addr["results"][0]['locations'][0]["adminArea1"] == "XZ":
      print('the ISS is over water')
      flag = "https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/International_Space_Station/Where_is_the_International_Space_Station"
      print(flag)
  else:
      location = addr["results"][0]['locations'][0]["adminArea1"]
      flag = country(location)[0]["flags"]["png"]

      print(flag)
      print(location)
    

  return render_template("index.html",data=data, weather_desc=weather_desc,flag=flag, google_map=google_map,lat=lat,lon=lon,cont_code=cont_code, dist_=dist_)



 


app.run(host='0.0.0.0', port=8080)



