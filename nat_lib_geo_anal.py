#!/usr/bin/env python

# import itertools
import json
# import sys
import os
# from collections import OrderedDict
from lib.csv_printer import *
from lib.geodata import *
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
                self.worksheet['data'][line[0]]['lat'] = None
                self.worksheet['data'][line[0]]['lon'] = None
        self.worksheet['header'].append('lat')
        self.worksheet['header'].append('lon')
        # self._fix_unidates()
        # self._serialize(output="csv")

    def _get_coordinates(self):
        for entry in self.worksheet['data'].values():
            if entry['lat'] and entry['lon'] is None:
                # self.worksheet['data'][entry['msID']] = fix_unidate(entry)
                _ = get_coordinate(entry)

    def _serialize(self, output="csv"):
        result = {
                    "json": _serialize_json,
                    "csv": self._serialize_csv
                }[output](self.worksheet)
        return result

    def _serialize_csv(self, data):
        pass
        output_dirname, output_filename = os.path.split(self.worksheet['file_name'])
        output_filename = "/".join([output_dirname, "outputs", output_filename])
    #     print(output_filename)
        print_csv_object(output_filename, self.worksheet)

if __name__ == "__main__":
    # filenames = sys.argv
    # filenames.pop(0)
    filenames = ['C:/Users/vinsburg/Documents/github/nat_lib_anal/database/locations.csv']
    for filename in filenames:
        print(filename)
        archive = Archive(filename)
        print(_serialize_json(archive.worksheet))
        # print_unidates(archive.worksheet['data'])


