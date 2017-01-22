# !/usr/bin/env python
import csv
import json
import os


def make_csv_object(worksheet):
    csv_object = [[]]
    csv_object[0] += worksheet['header']
    current_row_index = 0
    for entry in worksheet['data'].values():
        current_row_index += 1
        csv_object += [[]]
        for key in worksheet['header']:
            csv_object[current_row_index] += [entry[key]]
    # print(csv_object[1])
    return csv_object


def print_csv_object(output_filename, worksheet):
    # with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
    #     csvwriter = csv.writer(csvfile, dialect='excel')
    with open(output_filename, 'w', newline='', encoding='utf-8', errors='ignore') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter='\t', quotechar='"')
        csvwriter.writerows(make_csv_object(worksheet))


def serialize(worksheet, output="csv"):
    result = {
                "json": serialize_json,
                "csv": serialize_csv
            }[output](worksheet)
    return result


def serialize_json(data):
    return json.dumps(data, indent=4)


def serialize_csv(worksheet):
    output_dirname, output_filename = os.path.split(worksheet['file_name'])
    output_filename = "/".join([output_dirname, "outputs", output_filename])
#     print(output_filename)
    print_csv_object(output_filename, worksheet)