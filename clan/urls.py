from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.clan_list, name='clan_list'),
    path('show/<int:id_clan>', views.show_clan, name='show_clan'),
]
