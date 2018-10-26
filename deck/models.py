from django.db import models
from user.models import MyUser
from cards.models import Card

# Create your models here.
class Deck(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    cards = models.ManyToManyField(Card)
