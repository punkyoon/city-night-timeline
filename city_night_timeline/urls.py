from django.urls import include, path
from django.contrib import admin

from service.views import timeline_view, search_view, info_view


urlpatterns = [
    path('', timeline_view, name='timeline'),
    path('search/', search_view, name='search'),
    path('admin/', admin.site.urls)
]
