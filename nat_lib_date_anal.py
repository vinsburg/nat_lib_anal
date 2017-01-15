#!/usr/bin/env python

# import itertools
# import sys
# from collections import OrderedDict
from lib.worksheet_printer import *
from lib.unidate import *
from lib.diagnostics import *


class Archive(object):

    def __init__(self, file_name):
        # lets read all the worksheet exported data
        self.worksheet = {"file_name": file_name}
        data = []
        # with open(file_name, "r", newline='') as csv_file:
        with open(file_name, "r", encoding='utf-8', newline='', errors='ignore') as csv_file:
            for row in csv.reader(csv_file, delimiter='\t', quotechar='"'):
                data.append(row)
        self.worksheet['header'] = data.pop(0)
        self.worksheet['header'].append('unidate')
        self.worksheet['data'] = {}
        header_length = len(self.worksheet['header'])
        for line in data:
            self.worksheet['data'][line[0]] = {}
            line_length = len(line)
            for item_ind in range(line_length):
                self.worksheet['data'][line[0]][self.worksheet['header'][item_ind]] = line[item_ind]
            for item_ind in range(line_length, header_length):
                self.worksheet['data'][line[0]][self.worksheet['header'][item_ind]] = ''
            self.worksheet['data'][line[0]]['unidate'] = None
        self._fix_unidates()
        serialize(self.worksheet, output="csv")

    def _fix_unidates(self):
        for entry in self.worksheet['data'].values():
            if entry['unidate'] is None:
                # self.worksheet['data'][entry['msID']] = fix_unidate(entry)
                _ = fix_unidate(entry)


if __name__ == "__main__":
    # filenames = sys.argv
    # filenames.pop(0)
    filenames = ['C:/Users/vinsburg/Documents/github/nat_lib_anal/database/dropbox_files/heb_dates.csv']
    for filename in filenames:
        print(filename)
        archive = Archive(filename)
        # print(_serialize_json(archive.worksheet))
        # for field in archive.worksheet:
        # for key in archive.worksheet['data']['3530522'].items():
        #     print(key)
        # entries = get_date_types(archive.worksheet)
        # print('accuracyType', entries['accuracyType'])
        # print('yearType', entries['yearType'])
        # print('referenceType', entries['referenceType'])
        # print_coverage_for_key(archive.worksheet['data'], 'unidate')
        # print_unidates(archive.worksheet['data'])
        # print('\u05ea\u05ea\u05ea\u05f2\u05ea')

