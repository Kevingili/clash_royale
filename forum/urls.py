from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.forum_index, name='forum_index'),
    path('create', views.forum_create, name='forum_create'),
    path('show/<int:id_forum>', views.forum_show, name='forum_show'),
]
