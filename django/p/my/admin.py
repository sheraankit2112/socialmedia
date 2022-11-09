from django.contrib import admin

from my.models import mydata

class dataAdmin(admin.ModelAdmin):
    list_display=['name','age']

admin.site.register(mydata,dataAdmin)
