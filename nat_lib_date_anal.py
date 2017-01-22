#!/usr/bin/env python

# import itertools
# import sys
# from collections import OrderedDict
from lib.worksheet_reader import *
from lib.worksheet_printer import *
from lib.unidate import *
from lib.diagnostics import *
from lib.archive import *


if __name__ == "__main__":
    # filenames = sys.argv
    # filenames.pop(0)
    filenames = ['C:/Users/vinsburg/Documents/github/nat_lib_anal/database/dropbox_files/heb_dates.csv']
    for filename in filenames:
        print(filename)
        Header = get_header(filename)
        Header.append('unidate')
        Header.append('unidate_range')
        Data = get_data(filename)
        archive = Archive(filename, Header, Data)
        fix_unidates(archive)
        serialize(archive.worksheet, output="csv")
        # print(_serialize_json(archive.worksheet))
        # for field in archive.worksheet:
        # for key in archive.worksheet['data']['3530522'].items():
        #     print(key)
        entries = get_date_types(archive.worksheet)
        print('accuracyType', entries['accuracyType'])
        print('yearType', entries['yearType'])
        print('referenceType', entries['referenceType'])

        print_coverage_for_key(archive.worksheet['data'], 'unidate')
        print_items_for_key(archive.worksheet['data'], 'unidate')
        print_coverage_for_key(archive.worksheet['data'], 'unidate_range')
        print_items_for_key(archive.worksheet['data'], 'unidate_range')
        # print('\u05ea\u05ea\u05ea\u05f2\u05ea')

