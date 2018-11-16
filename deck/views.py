from django.shortcuts import render, redirect, get_object_or_404
from deck.models import Deck
from deck.models import Card
from django.forms import ModelForm
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

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

@staff_member_required
def deck_list(request):
	decks = Deck.objects.all()
	return render(request, 'deck_list.html', {'decks': decks})

def my_deck_list(request):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		u1 = request.user
		deck = u1.deck
		return render(request, 'my_deck_list.html', {'deck': deck})

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
			#form = DeckForm()
			form = DeckForm()
			form.fields["user"].initial = [request.user.id]
			form.fields["cards"].queryset = request.user.card_set.all()
		return render(request, 'deck_create.html', {'form': form})

def deck_update(request, id_deck):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		deck = get_object_or_404(Deck, id=id_deck)
		form = DeckForm(request.POST or None, instance=deck)
		form.fields["user"].initial = [request.user.id]
		form.fields["cards"].queryset = request.user.card_set.all()
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