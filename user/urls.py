from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
    path('players', views.user_list, name='user_list'),
    path('my-account', views.my_account, name='my_account'),
    path('players/<int:id_user>', views.show_player, name='show_player'),
    path('accounts/', include('django.contrib.auth.urls')),
]
