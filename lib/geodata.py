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


def get_geo_facet_dict(data):
    geo_dict = {}
    for entry in data.values():
        sep = '.'
        key = ''
        if entry['Country'] != '':
            if entry['Area'] == '':
                key = sep.join((entry['City'].strip(), entry['Country'].strip()))
            else:
                key = sep.join((entry['City'].strip(), entry['Area'].strip(), entry['Country'].strip()))
        elif entry['HebCity'] != '':
            key = sep.join((entry['HebCity'].strip(), entry['HebCountry'].strip()))
        elif entry['City'] != '':
            key = entry['City'].strip()
        key = key.strip('.')
        geo_dict[key] = [key, entry['City'], entry['Area'], entry['Country'], entry['HebCity'], entry['HebCountry']]
        entry['local_uri'] = key
    return geo_dict


def check_uris(dic_data, data):
    for value in data.values():
        if value['local_uri'] in dic_data:
            value['uri_matched'] = 'True'
        else:
            value['uri_matched'] = 'False'


def get_exceptions_geo_facet_dict(data):
    geo_dict = {}
    for entry in data.values():
        if entry['uri_matched'] == 'False':
            geo_dict[entry['local_uri']] = entry
    worksheet = dict()
    worksheet['data'] = geo_dict
    return worksheet

def get_nominatim_data(city, country):
    geolocator = Nominatim()
    while True:
        try:
            if city is not '' or country is not '':
                location = geolocator.geocode(' '.join((city, country)))
                sleep(1)
            else:
                location = None
            break
        except exc.GeocoderServiceError:
            return True, True, True
    if location is not None:
        return location.longitude, location.latitude, location.address
    return False, False, False
