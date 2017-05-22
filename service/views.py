from django.shortcuts import render

from service.models import Timeline
from service.forms import MessageForm


def main_view(request):
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.cleand_data
            print(msg)  # just for test
    #content = Timeline.objects.create(message=request)
    return render(request, 'main.html', {'msg_form': form})
