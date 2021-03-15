from rest_framework import serializers
from .models import Kleague2_2021_1r,Kleague2_2021_2r,Kleague1_2021_2r,Kleague1_2021_1r,Kleague1_2021_3r
from rest_framework.serializers import ModelSerializer


# from rest_framework_jwt.settings import api_settings


class PostSerializer1_1(ModelSerializer):
    class Meta:
        model = Kleague1_2021_1r   
        fields = '__all__'
        
class PostSerializer1_2(ModelSerializer):
    class Meta:
        model = Kleague1_2021_2r
        fields = '__all__'
        

class PostSerializer1_3(ModelSerializer):
    class Meta:
        model = Kleague1_2021_3r
        fields = '__all__'
        
class PostSerializer2_1(ModelSerializer):
    class Meta:
        model = Kleague2_2021_1r
        fields = '__all__'
        
class PostSerializer2_2(ModelSerializer):
    class Meta:
        model = Kleague2_2021_2r
        fields = '__all__'
        model = Kleague2_2021_2r
