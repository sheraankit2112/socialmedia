from django.contrib import admin

from my.models import studentdata

class dataAdmin(admin.ModelAdmin):
    list_display=["name","age"]

admin.site.register(studentdata,dataAdmin)
