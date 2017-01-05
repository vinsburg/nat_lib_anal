
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


def print_date_coverage(data):
    unidate_counter = 0
    entry_counter = 0
    for entry in data.values():
        entry_counter += 1
        if entry['unidate'] is not None:
            unidate_counter += 1
    print('unidate coverage is', '{:.1%}'.format(unidate_counter/entry_counter))
    print(unidate_counter, 'entries out of', entry_counter, 'now conform.')


def print_unidates(data):
    for entry in data.values():
        if entry['unidate'] is not None:
            print(entry['unidate'])
