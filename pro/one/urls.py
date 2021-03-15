from django.urls import path

from . import views

urlpatterns = [
    path('k1/1', views.ListPost1_1, name='k1_1'),
    path('k1/2', views.ListPost1_2, name='k1_2'),
    path('k1/3', views.ListPost1_3, name='k1_3'),

    path('k2/1', views.ListPost2_1, name='k2_1'),
    path('k2/2', views.ListPost2_2, name='k2_2'),

    # path('create/', views.createUser),

]