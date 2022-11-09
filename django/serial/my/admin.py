from django.contrib import admin

from my.models import data

class dataAdmin(admin.ModelAdmin):
    list_display=['name','age']

admin.site.register(data,dataAdmin)
