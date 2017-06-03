import pytz
import datetime

from django.http import HttpResponseRedirect

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
        print(response)
        return response

    def time_check(self):
        now = datetime.datetime.now(tz).time()

        if now>service_time[0] or now<service_time[1]:
            return True
        else:
            return False

    def process_request(self, request):
        print('process request(self, request)')
        return

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(request, view_args, view_func, view_kwargs)
        response=None
        return response

    def process_template_response(self, request, response):
        print('process_template_response(self, request, response)')
        print(reqest, response)
        return response

    def process_response(self, request, response):
        print('process_response(self, request, response)')
        print(request, response)
        return response
