from geopy.geocoders import Nominatim
from geopy import exc
from time import sleep


def remove_na(data):
    for entry in data.values():
        for key, value in entry.items():
            if value == 'N/A':
                entry[key] = ''


def get_coordinates(archive):
    count = 0
    for key, entry in archive.worksheet['data'].items():
        # if max(self.key_dic[key[:self.key_length]]) != int(key[self.key_length+1:]):
        if entry['lat'] is None:
            emergency_dump = get_coordinate(entry)
            count += 1
            if emergency_dump is True:
                print('Emergency dump count is', count)
                return


def get_coordinate(entry):
    geolocator = Nominatim()
    city = entry['City']
    city = city if city != 'N/A' else ''
    country = entry['Country']
    country = country if country != 'N/A' else ''
    # print(entry['msID'], city + ' ' + country)
    while True:
        try:
            if city is not '' or country is not '':
                location = geolocator.geocode(' '.join((city, country)))
                sleep(2)
            else:
                location = None
            break
        except exc.GeocoderServiceError:
            return True
    if location is not None:
        entry['lat'] = location.latitude
        entry['lon'] = location.longitude
        entry['address'] = location.address
    return False
