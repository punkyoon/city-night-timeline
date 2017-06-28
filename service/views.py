import datetime

from django.shortcuts import render

from service.models import Timeline

def main_view(request):
    if request.method == 'POST':
        msg = request.POST['message']
        content = Timeline.objects.create(message=msg)
    
    result = Timeline.objects.filter(time__contains=datetime.date.today())

    return render(request, 'main.html', {'result': result})

def search_view(request):
    if request.method == 'POST':
        data = request.POST['date']
        data = datetime.datetime.strptime(data, "%B %d, %Y").date()

        result = Timeline.objects.filter(time__contains=data)

        return render(request, 'search.html', {'result': result})

    return render(request, 'search.html')

def help_view(request):
    return render(request, 'help.html')
