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
        Data = get_data(filename)
        archive = Archive(filename, Header, Data)
        serialize(archive.worksheet, output="csv")
