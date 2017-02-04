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
    dHeader.append('Source')
    dData = get_data(loc_dic)
    dic = Archive(loc_dic, dHeader, dData)
    dic.clean_keys()

    # filename = 'C:/Users/vinsburg/Documents/github/nat_lib_anal/database/dropbox_files/outputs/geopy_results/locations3.tsv'
    # Header = get_header(filename)
    # Data = get_data(filename)
    # archive = Archive(filename, Header, Data)

    for key, entry in dic.worksheet['data'].items():
        if entry['Column 7'] == '':
            print(entry['Column 1'])
            lon, lat, dat = get_nominatim_data(entry['City - Eng'], entry['State - Eng'])
            if lon is not False:
                entry['Column 7'] = entry['Column 9'] = lon
                entry['Column 8'] = entry['Column 10'] = lat
                entry['Source'] = 'openstreetmap.org|'+dat

        serialize(dic.worksheet, output="csv")
