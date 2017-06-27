import datetime

from django.shortcuts import render

from service.models import Timeline
from service.forms import SearchForm

def main_view(request):
    if request.method == 'POST':
        msg = request.POST['message']
        content = Timeline.objects.create(message=msg)
    
    result = Timeline.objects.filter(time__contains=datetime.date.today())

    return render(request, 'main.html', {'result': result})

def search_view(request):
    form = SearchForm()

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['date']
            result = Timeline.objects.filter(time__contains=query)
            context = {
                'search_form': form,
                'result': result
            }

            return render(request, 'search.html', context)

    return render(request, 'search.html', {'search_form': form})

def help_view(request):
    return render(request, 'help.html')
