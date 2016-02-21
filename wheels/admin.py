from django.contrib import admin
from .models import Visit

class VisitAdmin(admin.ModelAdmin):
	list_display = ('name', 'date', 'dailyCount')

admin.site.register(Visit, VisitAdmin)