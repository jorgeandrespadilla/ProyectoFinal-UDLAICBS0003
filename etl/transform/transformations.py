from datetime import datetime

date_format = "%Y-%m-%d"

def parse_date(date_str):
    return datetime.strptime(date_str, date_format)
