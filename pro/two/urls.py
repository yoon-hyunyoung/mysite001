from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token,  refresh_jwt_token, verify_jwt_token
from . import views

urlpatterns = [
    path('register', views.RegistView, name='RegistView'),

    path('login', views.signUp),
    
    path('api-jwt-auth', obtain_jwt_token),
    path('refresh-jwt-auth', refresh_jwt_token),
    path('verify-jwt-auth', verify_jwt_token)
]