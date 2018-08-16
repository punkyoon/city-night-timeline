import pytz
import datetime

from django.http import JsonResponse


class TimeCheckMiddleware(object):
    tz = pytz.timezone('Asia/Seoul')
    service_time = [
        datetime.time(21, 0, 0, tzinfo=tz),
        datetime.time(6, 0, 0, tzinfo=tz)
    ]

    def __init__(self, response):
        self.get_response = response

    def __call__(self, request):
        response = self.get_response(request)

        if self.time_check() or request.path != '/':
            return response
        else:
            return JsonResponse({'info': 'not a service time'})

    def time_check(self):
        now = datetime.datetime.now(self.tz).time()

        if now > self.service_time[0] or now < self.service_time[1]:
            return True

        return False
