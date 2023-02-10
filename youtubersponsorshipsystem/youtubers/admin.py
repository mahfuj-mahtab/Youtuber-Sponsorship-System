from django.contrib import admin
from .models import Youtubers
# Register your models here.

class YtAdmin(admin.ModelAdmin):
    list_display = ('id','name','sub_count','is_featured') 
    search_fields = ('name','camera')
    list_filter = ('camera_type',)
    list_display_links = ('id','name')
    list_editable = ('is_featured',)

admin.site.register(Youtubers,YtAdmin)