
def get_date_types(worksheet):
    field_entries = {}
    for item in worksheet['header']:
        field_entries[item] = list()
    for entry in worksheet['data'].values():
        for item in worksheet['header']:
            field_entries[item].append(entry[item])
    for item in worksheet['header']:
        field_entries[item] = list(set(field_entries[item]))
    return field_entries


def print_coverage_for_key(data,key):
    key_counter = 0
    entry_counter = 0
    for entry in data.values():
        entry_counter += 1
        if entry[key] is not None:
            key_counter += 1
    print(key, 'coverage is', '{:.1%}'.format(key_counter/entry_counter))
    print(key_counter, 'entries out of', entry_counter, 'now conform.')


def print_items_for_key(data, key):
    for entry in data.values():
        if entry[key] is not None:
            print(entry[key])


def print_date_exceptions(data):
    for entry in data.values():
        f1 = entry['unidate'] != entry['latDate']
        f2 = entry['unidate'] != entry['hebDate']
        f3 = entry['unidate_range'] != entry['latDate']
        f4 = entry['unidate_range'] != entry['hebDate']
        f5 = entry['yearType'] != 'Century'
        if f1 and f2 and f3 and f4 and f5:
            unidate = entry['unidate'] if entry['unidate_range'] is None else entry['unidate_range']
            print('|lat:', entry['latDate'], '|heb:', entry['hebDate'], '|unidate:', unidate)
