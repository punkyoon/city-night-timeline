import json
import datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from service.models import Timeline


@csrf_exempt
def timeline_view(request):
    result = []
    if request.method == 'POST':
        msg = json.loads(request.body.decode('utf-8'))['message']
        Timeline.objects.create(message=msg)
    
    timelines = Timeline.objects.filter(time__contains=datetime.date.today())
    #timelines = Timeline.objects.all()

    for timeline in timelines:
        result.append({
            '_id': timeline._id,
            'message': timeline.message,
            'time': timeline.time
        })

    return JsonResponse({'timelines': result})

def search_view(request):
    result = []
    if request.method == 'GET':
        data = request.GET['date']
        data = datetime.datetime.strptime(data, "%Y-%m-%d").date()
        timelines = Timeline.objects.filter(time__contains=data)

    for timeline in timelines:
        result.append({
            '_id': timeline._id,
            'message': timeline.message,
            'time': timeline.time
        })

    return JsonResponse({'timelines': result})


def info_view(request):
    return HttpResponse()
