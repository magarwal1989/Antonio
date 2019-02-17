import datetime
from datetime import timedelta

def get_current_date():
    return datetime.datetime.today().strftime('%m/%d/%Y')

def get_next_week_date():
    date_1 = datetime.datetime.today()
    end_date =  date_1 + timedelta(days=7)
    return end_date.strftime('%m/%d/%Y')
