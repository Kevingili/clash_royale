from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('cards/', include('cards.urls')),
    path('decks/', include('deck.urls')),
    path('forum/', include('forum.urls')),
    path('clan/', include('clan.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
