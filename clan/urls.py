from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.clan_list, name='clan_list'),
]
