from math import cos, asin, sqrt

def distance(lat1, lon1, lat2, lon2):
    """Calculates the distance between 2 latlng coordinates."""
    p = 0.017453292519943295
    hav = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(hav))

def nearest(coordinates, country_object):
    """Sorting function."""
    lat1, lng1 = coordinates[0], coordinates[1]
    lat2, lng2 = country_object.latlng[0], country_object.latlng[1]
    return float(distance(lat1, lng1, lat2, lng2))