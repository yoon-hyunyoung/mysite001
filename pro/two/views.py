from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status #,viewsets
# from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
# from rest_framework.viewsets import ModelViewSet
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication


from .models import User
from .serializers import UserSerializer , SingupSerializer
# Create your views here.
#회원가입
@api_view(['GET','POST'])
def RegistView(request):
    if request.method == 'GET':
        qs = User.objects.all()
        serializer = UserSerializer(qs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        #직렬화 생성
        serializer = UserSerializer(data=request.data)
        #vailidation 체크
        if serializer.is_valid():
            #저장
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 로그인
@api_view(['GET','POST'])
def signUp(request):

    if request.method == 'GET':
        users = SingupSerializer(User.objects.all(), many=True)
        return Response(users.data)

    elif request.method == 'POST':
        signup = SingupSerializer(data=request.data)
        if signup.is_valid():
            signup.save()
            return Response(signup.data, status=201)