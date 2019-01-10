from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.match_index, name='match_index'),
    path('create', views.match_create, name='match_create'),
    path('show/<int:id_match>', views.match_show, name='match_show'),
    path('edit/<int:id_match>/statut/<int:statut>', views.match_edit_statut, name='match_edit_statut'),
]
