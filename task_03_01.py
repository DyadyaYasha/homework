import datetime

def get_days_to_new_year():
    n = datetime.datetime.now()
    dng = (datetime.datetime(n.year + 1, 1, 1))-n
    return dng.days