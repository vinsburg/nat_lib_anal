from geopy.geocoders import Nominatim
from geopy import exc
from time import sleep


def get_coordinate(entry):
    geolocator = Nominatim()
    city = entry['City']
    city = city if city != 'N/A' else ''
    country = entry['Country']
    country = country if country != 'N/A' else ''
    # print(entry['msID'], city + ' ' + country)
    while True:
        try:
            location = geolocator.geocode(' '.join((city,country)))
            sleep(1)
            break
        except exc.GeocoderServiceError:
            return True
    if location is not None:
        entry['lat'] = location.latitude
        entry['lon'] = location.longitude
        entry['address'] = location.address
    return False
