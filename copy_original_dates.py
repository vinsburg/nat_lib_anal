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
    oFile = 'C:/Users/vinsburg/Documents/github/nat_lib_anal/database/dropbox_files/heb-dates.tsv'
    oHeader = get_header(oFile)
    print(oHeader)
    oData = get_data(oFile)
    oArchive = Archive(oFile, oHeader, oData)
    oArchive.clean_keys()

    filename = 'C:/Users/vinsburg/Documents/github/nat_lib_anal/database/dropbox_files/outputs/heb_dates.tsv'
    Header = get_header(filename)
    print(Header)
    Data = get_data(filename)
    archive = Archive(filename, Header, Data)
    archive.worksheet['header'] = [archive.worksheet['header'][0]] + ['Original'] + archive.worksheet['header'][1:]
    print(archive.worksheet['header'])
    archive.clean_keys()
    for key, value in archive.worksheet['data'].items():
        if key in oArchive.worksheet['data']:
            value['Original'] = oArchive.worksheet['data'][key]['Original']
        else:
            print(key)
            value['Original'] = ''

    serialize(archive.worksheet, output="csv")
