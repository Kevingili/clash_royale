from django.shortcuts import render
from deck.models import Deck

# Create your views here.

def deck_list(request):
	decks = Deck.objects.all()

	return render(request, 'deck_list.html', {'decks': decks})