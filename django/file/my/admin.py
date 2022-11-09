from django.contrib import admin

from my.models import filename

class filenameAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(filename,filenameAdmin)
