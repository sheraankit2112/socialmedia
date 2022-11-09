from django.contrib import admin

# Register your models here.
from database.models import userdata,userposts,userbio

class userdataAdmin(admin.ModelAdmin):
    list_display=['username','token']

admin.site.register(userdata,userdataAdmin)

class userpostAdmin(admin.ModelAdmin):
    list_display=['username','post','caption']

admin.site.register(userposts,userpostAdmin)

class userbioAdmin(admin.ModelAdmin):
    list_display=['name','username','email','profile','mobile']

admin.site.register(userbio,userbioAdmin)
