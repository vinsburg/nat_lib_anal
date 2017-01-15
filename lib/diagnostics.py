
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


def print_unidates(data):
    for entry in data.values():
        if entry['unidate'] is not None:
            print(entry['unidate'])
