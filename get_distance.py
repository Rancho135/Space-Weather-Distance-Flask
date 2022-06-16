import geopy.distance

def dist(coords_1_lat,coords_1_lon,coords_2_lat,coords_2_lon):

    coords_1 = (coords_1_lat, coords_1_lon)
    coords_2 = (coords_2_lat, coords_2_lon)

    #print(geopy.distance.distance(coords_1, coords_2).km)
    return round(geopy.distance.distance(coords_1, coords_2).km,2)
    #https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
