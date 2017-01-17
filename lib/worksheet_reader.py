import csv


def get_header(file_name):
    with open(file_name, "r", encoding='utf-8', newline='', errors='ignore') as csv_file:
        for row in csv.reader(csv_file, delimiter='\t', quotechar='"'):
            return row


def get_data(file_name):
    data = []
    with open(file_name, "r", encoding='utf-8', newline='', errors='ignore') as csv_file:
        for row in csv.reader(csv_file, delimiter='\t', quotechar='"'):
            data.append(row)
    data.pop(0)  # dump the header
    return data
