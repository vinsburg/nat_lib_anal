#!/usr/bin/env python

# import itertools
import json
# import sys
# import os
# from collections import OrderedDict
from lib.csv_printer import *
from lib.unidate import *
from lib.diagnostics import *


def _serialize_json(data):
    return json.dumps(data, indent=4)


class Archive(object):

    def __init__(self, file_name):
        # lets read all the worksheet exported data
        self.worksheet = {"file_name": file_name}
        data = []
        # with open(file_name, "r", newline='') as csv_file:
        with open(file_name, "r", encoding='utf-8', errors='ignore') as csv_file:
            for row in csv.reader(csv_file, dialect='excel'):
                data.append(row)
        self.worksheet['header'] = data.pop(0)
        self.worksheet['data'] = {}
        for line in data:
            self.worksheet['data'][line[0]] = {}
            for item_ind, item in enumerate(line):
                self.worksheet['data'][line[0]][self.worksheet['header'][item_ind]] = item
                self.worksheet['data'][line[0]]['unidate'] = None
        self.worksheet['header'].append('unidate')
        self._fix_unidates()

    def _fix_unidates(self):
        for entry in self.worksheet['data'].values():
            if entry['unidate'] is None:
                # self.worksheet['data'][entry['msID']] = fix_unidate(entry)
                _ = fix_unidate(entry)
            pass
        pass

    def _serialize(self, output="csv"):
        result = {
                    "json": _serialize_json,
                    "csv": self._serialize_csv
                }[output](self.worksheet)
        return result

    def _serialize_csv(self, data):
        pass
    #     output_dirname, output_filename = os.path.split(self.worksheet['file_name'])
    #     output_filename = "/".join([output_dirname, "outputs", output_filename])
    #     print(output_filename)
    #     csv_line_list = students_per_category_line_list_constructor(self.worksheet['students_per_category'])
    #     csv_line_list += ['\#\#']  # this will indicate the csv_line_matrix method to add a blank line
    #     csv_line_list += students_line_list_constructor(self.worksheet)
    #     csv_line_matrix = make_csv_line_matrix(csv_line_list)
    #     make_csv_from_line_matrix(csv_line_matrix, output_filename)

if __name__ == "__main__":
    # filenames = sys.argv
    # filenames.pop(0)
    filenames = ['C:/Users/vinsburg/Documents/github/nat_lib_anal/database/heb_dates.csv']
    for filename in filenames:
        print(filename)
        archive = Archive(filename)
        # print(_serialize_json(archive.worksheet))
        # for field in archive.worksheet:
        for key in archive.worksheet['data']['3530522'].items():
            print(key)
        entries = get_date_types(archive.worksheet)
        print('accuracyType', entries['accuracyType'])
        print('yearType', entries['yearType'])
        print('referenceType', entries['referenceType'])
        print_date_coverage(archive.worksheet['data'])
        print_unidates(archive.worksheet['data'])
        # print('\u05ea\u05ea\u05ea\u05f2\u05ea')

