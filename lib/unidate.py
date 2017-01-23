from re import search
from re import sub


class UnidateRE:
    def __init__(self):
        self.range_delimiters = r'[\-/\\]'
        self.lat_dmy_delimiters = r'[\.\\/]'
        self.lat_day = self.lat_month = r'\d{1,2}'
        self.lat_century = r'\d{1,2}'
        self.lat_century_range = self.date_range(self.lat_century)
        self.lat_dates = ['' for _ in range(3)]
        self.lat_dates[2] = self.lat_year = r'\d{4}'
        self.lat_dates[1] = self.lat_month_year = self.lat_month+self.lat_dmy_delimiters+self.lat_year
        self.lat_dates[0] = self.lat_day_month_year = self.lat_day + self.lat_dmy_delimiters + self.lat_month_year
        self.general_lat_year_range = r'('+r')|('.join(map(self.date_range, self.lat_dates))+r')'
        self.heb_year = r'[\u05d0-\u05ea]["\u05f2-\u05f4]{0,2}[\u05d0-\u05ea]{1,3}'
        self.heb_year_range = self.date_range(self.heb_year)
        self.heb_century = r'[\u05d0-\u05ea]{1,2}'
        self.heb_century_range = self.date_range(self.heb_century)

    def date_range(self, date):
        return r'(' + date + self.range_delimiters + r')?' + date


def fix_unidates(archive):
    for entry in archive.worksheet['data'].values():
        if entry['unidate'] is None and entry['unidate_range'] is None:
            fix_unidate(entry)


def fix_unidate(entry):
    date = None
    if entry['yearType'] == 'Year':
        date = get_year_unidates(entry)
    if entry['yearType'] == 'Century':
        date = get_century_unidates(entry)
    if entry['yearType'] == 'Shtarot':
        date = get_year_unidates(entry)
    if date == '':
        date = None
    if date is not None:
        impossible_date = search(r'([3-9]\d{3})|(2[1-9]\d{2})|(20[1-9]\d)|(^-100$)', date)
        if impossible_date:
            return
        slash_date = search(r'/', date)
        if slash_date:
            date = sub(r'/', r'-', date)
            print(date)
            entry['accuracyType'] = 'Range'
        hyphen_match = search(r'-', date)
        if entry['accuracyType'] == 'Range' and hyphen_match:
            entry['unidate_range'] = date
        else:
            entry['unidate'] = date


def get_year_unidates(entry):
    regex = UnidateRE()
    lat_year_date_list = date_getter(regex.general_lat_year_range, entry['latDate'])
    lat_year_date_list += date_getter(regex.general_lat_year_range, entry['hebDate'])
    # print(lat_year_date_list, 'lat:',entry['latDate'], 'heb:', entry['hebDate'])
    if lat_year_date_list is '' or len(lat_year_date_list) > 1:
        return None
    return ', '.join(lat_year_date_list)


def get_century_unidates(entry):
    regex = UnidateRE()
    lat_year_date_list = date_getter(regex.general_lat_year_range, entry['latDate'])
    if lat_year_date_list == []:
        lat_century_date_list = date_getter(regex.lat_century_range, entry['latDate'])
        # lat_century_date_list += date_getter(regex.lat_century_range, entry['hebDate'])
        lat_year_date_list = lat_cent2year(regex.lat_century, lat_century_date_list)
        # print(lat_year_date_list, lat_century_date_list, 'lat:',entry['latDate'], 'heb:', entry['hebDate'])
    if lat_year_date_list is '' or len(lat_year_date_list) > 1:
        return None
    return ', '.join(lat_year_date_list)


def date_getter(regex_pattern, date_string):
    clean_date_string = sub(r'[\[\]]', '', date_string)
    date_list = list()
    while True:
        date_match = search(regex_pattern, clean_date_string)
        if date_match:
            start_ind, end_ind = date_match.span()
            date_list.append(clean_date_string[start_ind:end_ind])
            clean_date_string = clean_date_string[end_ind:]
        else:
            break
    return date_list


def lat_cent2year(regex_pattern, century_date_list):
    year_date_list = list()
    for item in century_date_list:
        year_date_list.append(sub(regex_pattern, lambda x: str((int(x.group(0)) - 1) * 100), item))
    return year_date_list


def get_shtarot_unidates(entry):
    regex = UnidateRE()
    lat_shtarot_date_list = date_getter(regex.general_lat_year_range, entry['latDate'])
    lat_shtarot_date_list += date_getter(regex.general_lat_year_range, entry['hebDate'])
    if lat_shtarot_date_list is '' or len(lat_shtarot_date_list) > 1:
        return None
    #  prepare to fix ranges
    return ', '.join(lat_shtarot_date_list)


def print_date_info(entry):
    print('lat:', entry['latDate'], 'heb:', entry['hebDate'], 'yearType', entry['yearType'])


'''
hebrew code indexes next
print(list(map(chr, range(1488, 1514 + 1))))
1488 - א
1514 - ת
'''