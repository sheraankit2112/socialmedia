import imp
from django.contrib import admin
from result_data.models import studentData
from result_data.models import studentBio
from result_data.models import topperData,signup

class StudentbioAdmin(admin.ModelAdmin):
    list_display=['uid','name','father_name','mother_name','department_name']

admin.site.register(studentBio,StudentbioAdmin)

class studentdataAdmin(admin.ModelAdmin):
    list_display=['subject','theory','practical','total','grade']

admin.site.register(studentData,studentdataAdmin)

class topperAdmin(admin.ModelAdmin):
    list_display=['uid','sum']

admin.site.register(topperData,topperAdmin)

class signupAdmin(admin.ModelAdmin):
    list_display=['names','email','username','password']

admin.site.register(signup,signupAdmin)
