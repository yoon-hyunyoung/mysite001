from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User
from rest_framework.serializers import ModelSerializer

User=get_user_model()
class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    def create(self,validated_data):
        user=User.objects.create(
        username=validated_data['username'], #username이 디폴트로 들어가있는데 name으로 바꾼후 원래 username이던'YHY'를 name에 수작업 추가!(django admin)
        # phone_number=validated_data['phone_number'],
        email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model=get_user_model()
        fields=['username','email','password']