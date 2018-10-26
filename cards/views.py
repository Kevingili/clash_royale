from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from cards.models import Card
from django import forms
from user.models import MyUser
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

class CardForm(ModelForm):
	class Meta:
		model = Card
		widgets = {
          'description': forms.Textarea(attrs={'rows':4, 'placeholder':'Description de la carte'}),
        }
		#fields = ['name', 'url', 'description', 'users']
		fields = "__all__" 

@login_required
def card_list(request):
	card_list = Card.objects.all()
	paginator = Paginator(card_list, 2)

	page = request.GET.get('page')
	cards = paginator.get_page(page)

	return render(request, 'card_list.html', {'cards': cards, 'range': range(paginator.num_pages)})

def show_shop(request):
	if request.method == 'POST':
		u1 = request.user
		if(u1.gold > 0):
			card = Card.objects.order_by('?').first()
			card.users.add(request.user)
			u1.gold = u1.gold - 50
			u1.save()
			return render(request, 'shop.html', {'card': card})
		else:
			error = "You don't have enough money"
			return render(request, 'shop.html', {'error': error})
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
		action = "Create"
		if request.POST:
			form = CardForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('card_list')
		else:
			form = CardForm()
		return render(request, 'card_create.html', {'form': form, 'action': action})


def card_update(request, id_card):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		card = get_object_or_404(Card, id=id_card)
		form = CardForm(request.POST or None, instance=card)
		action = "Update"
		if form.is_valid():
			form.save()
			return redirect('card_list')
		return render(request, "card_create.html", {'form': form, 'action': action})


def card_delete(request, id_card):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		card = Card.objects.get(id=id_card)
		card.delete()
		return redirect('card_list')
