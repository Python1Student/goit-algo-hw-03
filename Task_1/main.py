import re
from datetime import datetime


def get_days_from_today(date):
    pass

condition = True
while condition:
    date_input = input('Write date in format: YYYY-MM-DD\n>>> ')

    pattern = r'\d{4}\-\d{2}\-\d{2}'
    match = re.search(pattern, date_input)

    if match and date_input == match.group(): 
        condition = False
        get_days_from_today(date_input)
    else: print('Wrong format!')