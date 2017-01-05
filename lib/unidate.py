from re import match


def fix_unidate(entry):
    if entry['yearType'] == 'Year':
        entry['unidate'] = get_latDate(entry)


def get_latDate(entry):
    if valid_latDate(entry['latDate']):
        return entry['latDate']
    else:
        print(entry['latDate'])
    return None

def valid_latDate(date):
    date_range = lambda x: r'^('+x+r'-)?'+x+r'$'
    year = r'\d{4}'
    day = month = r'\d{1,2}\.'
    regex = date_range(year)+r'|'+date_range(month+year)+r'|'+date_range(day+month+year)
    # regex = year
    result = match(regex, date) is not None
    return result

'''
hebrew codes next
print('\u05d0','\u05ea')
print(list(map(chr, range(1488, 1514 + 1))))

'''