from django.shortcuts import render

from service.models import Timeline

# Create your views here.
def main_view(request):
    #content = Timeline.objects.create(message=request)
    return render(request, 'main.html', {})
