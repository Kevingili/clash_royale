from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.card_list, name='card_list'),
    path('create', views.card_create, name='card_create'),
    path('update/<int:id_card>', views.card_update, name='card_update'),
    path('delete/<int:id_card>', views.card_delete, name='card_delete'),
]
