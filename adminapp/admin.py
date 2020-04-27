from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Calendar)
admin.site.register(DaysOff)
admin.site.register(WorkingTime)
admin.site.register(Resource)
admin.site.register(CalendarDefWT)
admin.site.register(DaySpecWT)
