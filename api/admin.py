from django.contrib import admin

from api.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [ 'id','name','state','gender','location','pro_image','pro_doc']



 

