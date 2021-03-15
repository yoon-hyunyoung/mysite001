from django.shortcuts import render
from rest_framework.decorators import api_view,action,permission_classes
from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


from .models import Kleague1_2021_3r,Kleague2_2021_1r,Kleague2_2021_2r,Kleague1_2021_2r,Kleague1_2021_1r
from .serializers import PostSerializer1_3,PostSerializer1_1,PostSerializer1_2,PostSerializer2_1,PostSerializer2_2


# @api_view(['GET',POST'])




# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @uthentication_classes((JSONWebTokenAuthentication,))

@api_view(['GET'])
def ListPost1_1(request):
    if request.method == 'GET':
        data=Kleague1_2021_1r.objects.all()
        serializer= PostSerializer1_1(data, many=True)
        return Response(serializer.data)
        

@api_view(['GET', 'POST'])
def ListPost1_2(request):
    if request.method == 'GET':
        data=Kleague1_2021_2r.objects.all()
        serializer= PostSerializer1_1(data, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def ListPost1_3(request):
    if request.method == 'GET':
        data=Kleague1_2021_3r.objects.all()
        serializer= PostSerializer1_1(data, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def ListPost2_1(request):
    if request.method == 'GET':
        data=Kleague2_2021_1r.objects.all()
        serializer= PostSerializer1_1(data, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def ListPost2_2(request):
    if request.method == 'GET':
        data=Kleague2_2021_2r.objects.all()
        serializer= PostSerializer1_1(data, many=True)
        return Response(serializer.data)