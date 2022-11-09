from django.contrib import admin

from my.models import tumor

class tumorAdmin(admin.ModelAdmin):
    list_display=["model"]

admin.site.register(tumor,tumorAdmin)
