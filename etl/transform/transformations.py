from datetime import datetime

def parse_date(date_str):
    return datetime.strptime(date_str, '%d-%b-%y')
