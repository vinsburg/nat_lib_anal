#!/usr/bin/env python

# import itertools
import json
# import sys
import os
# from collections import OrderedDict
from lib.worksheet_printer import *
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
        with open(file_name, "r", encoding='utf-8', newline='', errors='ignore') as csv_file:
            for row in csv.reader(csv_file, delimiter='\t', quotechar='"'):
                data.append(row)
        self.worksheet['header'] = data.pop(0)
        self.worksheet['header'].append('lat')
        self.worksheet['header'].append('lon')
        self.worksheet['header'].append('address')
        print(self.worksheet['header'])
        self.worksheet['data'] = {}
        header_length = len(self.worksheet['header'])
        for line in data:
            self.worksheet['data'][line[0]] = {}
            line_length = len(line)
            for item_ind in range(line_length):
                self.worksheet['data'][line[0]][self.worksheet['header'][item_ind]] = line[item_ind]
            for item_ind in range(line_length, header_length):
                self.worksheet['data'][line[0]][self.worksheet['header'][item_ind]] = ''
            self.worksheet['data'][line[0]]['lat'] = None
        self._get_coordinates()
        serialize(self.worksheet, output="csv")

    def _get_coordinates(self):
        for entry in self.worksheet['data'].values():
            if entry['lat'] is None:
                emergency_dump = get_coordinate(entry)
                if emergency_dump is True:
                    break


if __name__ == "__main__":
    # filenames = sys.argv
    # filenames.pop(0)
    filenames = ['C:/Users/vinsburg/Documents/github/nat_lib_anal/database/dropbox_files/locations.csv']
    for filename in filenames:
        print(filename)
        archive = Archive(filename)
        # print(serialize_json(archive.worksheet))
        print_coverage_for_key(archive.worksheet['data'], 'lat')



