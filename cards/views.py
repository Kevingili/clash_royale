from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from cards.models import Card
from django import forms

class CardForm(ModelForm):
    class Meta:
    	model = Card
    	fields = "__all__" 

def card_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        cards = Card.objects.all()
        return render(request, 'card_list.html', {'cards': cards})


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
