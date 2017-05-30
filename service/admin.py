from django.contrib import admin
from service.models import Timeline

class TimelineAdmin(admin.ModelAdmin):
    list_display = (
        '_id',
        'message',
        'time'
    )

admin.site.register(Timeline, TimelineAdmin)
