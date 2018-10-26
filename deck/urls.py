from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.deck_list, name='deck_list'),
    path('create', views.deck_create, name='deck_create'),
    path('show/<int:id_deck>', views.show_deck, name='show_deck'),
    path('update/<int:id_deck>', views.deck_update, name='deck_update'),
    path('delete/<int:id_deck>', views.deck_delete, name='deck_delete'),
]
