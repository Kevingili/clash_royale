from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.card_list, name='card_list'),
    path('show/<int:id_card>', views.show_card, name='show_card'),
    path('mycards', views.my_card_list, name='my_card_list'),
    path('shop', views.show_shop, name='show_shop'),
    path('create', views.card_create, name='card_create'),
    path('exchange/<int:id_player>', views.exchange, name='exchange'),
    path('exchange', views.exchange_list, name='exchange_list'),
    path('update/<int:id_card>', views.card_update, name='card_update'),
    path('delete/<int:id_card>', views.card_delete, name='card_delete'),
]
