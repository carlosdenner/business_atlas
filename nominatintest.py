
from geopy.geocoders import Nominatim
from requests.models import LocationParseError

geolocator = Nominatim(user_agent="geoapiExercises")

Latitude = 25.594095
Longitude = 85.137566

def location(Latitude, Longitude):
    lat = str(Latitude)
    long = str(Longitude)
    print(lat + long)
    local = lat + "," + long
    print(local)
    location = geolocator.reverse(local)
    locStr = str(location)
    print(locStr)
    splitted = locStr.split(',')
    country = splitted[len(splitted) - 1]
    print(country)
    print("==============país==============")
    return country

location(Latitude, Longitude)
# Display
