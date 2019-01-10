from django.db import models
from user.models import MyUser
from cards.models import Card

# Create your models here.

class Match(models.Model):
	id = models.AutoField(primary_key=True, blank=True)
	player1 = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='player1_match')
	player2 = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='player2_match')
	points_player1 = models.IntegerField(default=0)
	points_player2 = models.IntegerField(default=0)
	winner = models.IntegerField(default=0)
	nb_plays = models.IntegerField(default=0)
	statut = models.IntegerField(default=0)
	accept = models.IntegerField(null=True)

class Turns(models.Model):
	id = models.AutoField(primary_key=True, blank=True)
	match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='match_turns', null=True)
	play_player1 = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='card1_turns', null=True)
	play_player2 = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='card2_turns', null=True)
	winner_turns = models.IntegerField(default=0, null=True)
	statut = models.IntegerField(default=0, null=True)

