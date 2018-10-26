from django.shortcuts import render, redirect, get_object_or_404
from deck.models import Deck
from deck.models import Card
from django.forms import ModelForm
from django import forms

# Create your views here.

class DeckForm(ModelForm):
	#cards = forms.ModelMultipleChoiceField(Card.objects.filter(id__in=(1,2,3)))
	class Meta:
		model = Deck
		fields = ['name', "user", "cards"]
		#fields = "__all__" 

def show_deck(request, id_deck):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		deck = Deck.objects.get(id=id_deck)
		return render(request, 'show_deck.html', {'deck': deck})

def deck_list(request):
	decks = Deck.objects.all()
	return render(request, 'deck_list.html', {'decks': decks})

def deck_create(request):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		if request.POST:
			form = DeckForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('deck_list')
		else:
			form = DeckForm()
		return render(request, 'deck_create.html', {'form': form})

def deck_update(request, id_deck):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		deck = get_object_or_404(Deck, id=id_deck)
		form = DeckForm(request.POST or None, instance=deck)
		if form.is_valid():
			form.save()
			return redirect('deck_list')
		return render(request, "deck_create.html", {'form': form})

def deck_delete(request, id_deck):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		deck = Deck.objects.get(id=id_deck)
		deck.delete()
		return redirect('deck_list')