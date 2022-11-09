from django.contrib import admin

from my.models import userdata,userpost

class dataAdmin(admin.ModelAdmin):
    list_display=['username','profile','name']

admin.site.register(userdata,dataAdmin)

class postAdmin(admin.ModelAdmin):
    list_display=['username','post']

admin.site.register(userpost,postAdmin)