from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from cards.models import Card
from forum.models import Topic
from forum.models import Comment
from match.models import Match
from match.models import Turns
from deck.models import Deck
from django import forms

class MatchForm(ModelForm):
	class Meta:
		model = Match
		fields = ['player1', 'player2']

# Create your views here.
@login_required
def match_index(request):
	matchs = Match.objects.all()
	return render(request, 'match_index.html', {'matchs': matchs})

@login_required
def match_create(request):
	if request.POST:
		form = MatchForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('match_index')
	else:
		form = MatchForm()
		form.fields["player1"].initial = [request.user.id]
	return render(request, 'match_create.html', {'form': form})

@login_required
def match_show(request, id_match):
	match = Match.objects.get(id=id_match)
	turn = Turns.objects.last()
	turn = Turns.objects.filter(statut=0).last()
	turns = Turns.objects.all().filter(match_id=match.id)
	id_card = request.POST.get("play")
	deck = Deck.objects.get(user_id=request.user.id)

	if request.POST:
		if request.user == match.player1:
			if turn is None:
				card = Card.objects.get(id=id_card)
				turn = Turns.objects.create()
				turn.play_player1 = card
				turn.match_id = match
				turn.save()
			else:
				if turn.play_player1 is None:
					card = Card.objects.get(id=id_card)
					turn.play_player1 = card
					turn.save()

		if request.user == match.player2:
			if turn is None:
				card = Card.objects.get(id=id_card)
				turn = Turns.objects.create()
				turn.play_player2 = card
				turn.match_id = match
				turn.save()
			else:
				if turn.play_player2 is None:
					card = Card.objects.get(id=id_card)
					turn.play_player2 = card
					turn.save()

		if turn.play_player2 is not None and turn.play_player1 is not None:
			turn.statut = 1

			#Algo par rapport au gagnant !!!!
			if turn.play_player2.tag > turn.play_player1.tag:
				turn.winner_turns = 2
			elif turn.play_player2.tag < turn.play_player1.tag:
				turn.winner_turns = 1
			else:
				turn.winner_turns = 3

			if turn.winner_turns == 1:
				match.points_player1 = match.points_player1 + 1
			elif turn.winner_turns == 2:
				match.points_player2 = match.points_player2 + 1
			else:
				None
				#aucune action
			
			match.nb_plays = match.nb_plays + 1
			if match.nb_plays == 5:
				match.statut = 2
			match.save()
			turn.save()

	if request.user != match.player1 and request.user != match.player2:
		return redirect('match_index')
	return render(request, 'match_show.html', {'match': match, 'deck': deck, 'turns': turns})

@login_required
def match_edit_statut(request, id_match, statut):
	match = Match.objects.get(id=id_match)
	deck = Deck.objects.get(user_id=request.user.id)
	if request.user == match.player2:
		match.statut = statut
		match.save()
	return render(request, 'match_show.html', {'match': match, 'deck': deck})