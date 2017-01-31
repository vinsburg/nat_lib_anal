#!/usr/bin/env python

# import itertools
# import json
# import sys
# import os
# from collections import OrderedDict

from lib.worksheet_reader import *
from lib.worksheet_printer import *
from lib.geodata import *
from lib.diagnostics import *
from lib.archive import *


if __name__ == "__main__":
    # filenames = sys.argv
    # filenames.pop(0)
    loc_dic = 'C:/Users/vinsburg/Documents/github/nat_lib_anal/database/dropbox_files/msLocations.tsv'
    dHeader = get_header(loc_dic)
    dData = get_data(loc_dic)
    dic = Archive(loc_dic, dHeader, dData)
    dic.clean_keys()

    filenames = ['C:/Users/vinsburg/Documents/github/nat_lib_anal/database/dropbox_files/locations.tsv']
    for filename in filenames:
        print(filename)
        Header = get_header(filename)
        Header.append('locationType')
        Header.append('local_uri')
        Header.append('uri_matched')
        Data = get_data(filename)
        archive = Archive(filename, Header, Data)
        remove_na(archive.worksheet['data'])
        geo_dict = get_geo_facet_dict(archive.worksheet['data'])
        check_uris(dic.worksheet['data'], archive.worksheet['data'])
        serialize(archive.worksheet, output="csv")

        exceptions = get_exceptions_geo_facet_dict(archive.worksheet['data'])
        exceptions['header'] = Header
        address = filename.split('/')
        address[len(address)-1] = 'exception_' + address[len(address)-1]
        address = '/'.join(address)
        exceptions['file_name'] = address
        serialize(exceptions, output="csv")
        # for key, value in geo_dict.items():
        #     print(value)

        # archive.get_coordinates()
        # print_coverage_for_key(archive.worksheet['data'], 'lat')
