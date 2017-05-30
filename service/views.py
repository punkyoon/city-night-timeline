from django.shortcuts import render

from service.models import Timeline
from service.forms import MessageForm

# view and uploa
def main_view(request):
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.cleaned_data
            print(msg)  # just for test
    #content = Timeline.objects.create(message=request)
    return render(request, 'main.html', {'msg_form': form})

def search_view(request):
    form = SearchForm()

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data
            print(query)    # just for test

    return render(request, 'search.html', {'search_form': form})

def load_view(request, param):
    print(param)
    return render(request, 'list.html', {})
