from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.getstudent,name='This is my single json reposnse page'),
    path('save',views.savedata,name='getting data from 3rd party application'),
    path('newapp',views.alldata,name='getting all data in API-Application programming Interface ')
]