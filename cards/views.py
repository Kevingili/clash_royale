from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from cards.models import Card
from django import forms
from user.models import MyUser

class CardForm(ModelForm):
	class Meta:
		model = Card
		#fields = ['name', 'url', 'description']
		fields = "__all__" 

def card_list(request):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		cards = Card.objects.all()
		return render(request, 'card_list.html', {'cards': cards})

def show_shop(request):
	if request.method == 'POST':
		card = Card.objects.order_by('?').first()
		card.users.add(request.user)
		return render(request, 'shop.html', {'card': card})
	else:
		return render(request, 'shop.html')

def show_card(request, id_card):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		card = Card.objects.get(id=id_card)
		return render(request, 'show_card.html', {'card': card})

def my_card_list(request):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		u1 = request.user
		cards = u1.card_set.all()
		return render(request, 'my_card_list.html', {'cards': cards})

def card_create(request):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		if request.POST:
			form = CardForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('card_list')
		else:
			form = CardForm()
		return render(request, 'card_create.html', {'form': form})


def card_update(request, id_card):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		card = get_object_or_404(Card, id=id_card)
		form = CardForm(request.POST or None, instance=card)
		if form.is_valid():
			form.save()
			return redirect('card_list')
		return render(request, "card_create.html", {'form': form})


def card_delete(request, id_card):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		card = Card.objects.get(id=id_card)
		card.delete()
		return redirect('card_list')
