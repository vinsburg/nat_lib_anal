from lib.unidate import *

RE = UnidateRE()
s = '17.07.1934-17.07.1934'

regex_pattern = RE.general_lat_year_range
# regex_pattern = r'\d{1,2}[\.\\/]\d{1,2}[\.\\/]\d{4}'
print(regex_pattern)

date_match = search(regex_pattern, s)
if date_match:
    start_ind, end_ind = date_match.span()
    print(s[start_ind:end_ind])
    print(start_ind, end_ind)
