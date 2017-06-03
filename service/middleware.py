import pytz
import datetime

from django.http import HttpResponseRedirect

class TimeCheckMiddleware(object):
    tz = pytz.timezone('Asia/Seoul')
    service_time = [
        datetime.time(21, 0, 0, tzinfo=tz),
        datetime.time(6, 0, 0, tzinfo=tz)
    ]

    def __init__(self):
        pass

    def time_check(self):
        now = datetime.datetime.now(tz).time()

        if now>service_time[0] or now<service_time[1]:
            return True
        else:
            return False
