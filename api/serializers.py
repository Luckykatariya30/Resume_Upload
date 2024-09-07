from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [ 'id','name','email','dob','state','gender','location','pro_image','pro_doc']
