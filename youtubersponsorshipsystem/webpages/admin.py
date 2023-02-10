from django.contrib import admin
from .models import Slider, Team
# Register your models here.
#this function show extra info in admin panel
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','firstname','role','created_date') # this will show these info;
    list_display_links = ('firstname','id') # this make clickable
    search_fields = ('firstname','lastname','role') # this add search function in admin panel
    list_filter = ('role',) #add filter role in admin


admin.site.register(Slider)
admin.site.register(Team,TeamAdmin)