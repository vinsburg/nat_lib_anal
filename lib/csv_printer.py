# !/usr/bin/env python
import csv


def make_csv_object(worksheet):
    csv_object = [[]]
    csv_object[0] += worksheet['header']
    current_row_index = 0
    for entry in worksheet['data'].values():
        current_row_index += 1
        csv_object += [[]]
        for key in worksheet['header']:
            csv_object[current_row_index] += [entry[key]]
    print(csv_object[1])
    return csv_object


def print_csv_object(output_filename, worksheet):
    with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile, dialect='excel')
        csvwriter.writerows(make_csv_object(worksheet))
