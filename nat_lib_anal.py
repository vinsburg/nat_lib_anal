#!/usr/bin/env python

import itertools
import json
import sys
import os
# from collections import OrderedDict
from lib.csv_printer import *


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
        # pop the titles of the columns , we don't need those, maybe later :)
        self.header = data.pop(0)
        for line in data:
            self.worksheet[line[0]] = {}
            for item_ind, item in enumerate(line):
                self.worksheet[line[0]][self.header[item_ind]] = item
        # self._precalculate_all()

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
    filenames = sys.argv
    filenames.pop(0)
    # filenames = ['C:/Users/vinsburg/Documents/github/nat_lib_anal/database/heb_dates.csv']
    for filename in filenames:
        print(filename)
        archive = Archive(filename)
        print(_serialize_json(archive.worksheet))
