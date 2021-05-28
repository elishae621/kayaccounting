from datetime import datetime
from pytz import timezone as pytz_timezone

afri_tz = pytz_timezone('Africa/Lagos')


def current_time():
    return afri_tz.localize(datetime.now())
