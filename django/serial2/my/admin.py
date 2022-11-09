from django.contrib import admin

from my.models import userdata

class dataAdmin(admin.ModelAdmin):
    list_display=['name','age']

admin.site.register(userdata,dataAdmin)
