from django.db import models
from user.models import MyUser
from cards.models import Card

# Create your models here.
class Deck(models.Model):
	name = models.CharField(max_length=100)
	user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
	cards = models.ManyToManyField(Card)

class Exchange(models.Model):
	applicant = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='applicant_exchanges')
	applicant_card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='applicant_card_exchanges')
	validator = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='validator_exchanges')
	validator_card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='validator_card_exchanges')
	status = models.NullBooleanField(null=True)

	@classmethod
	def create(cls, applicant, applicant_card, validator, validator_card):
		exchange = cls(applicant=applicant, applicant_card=applicant_card, validator=validator, validator_card=validator_card)
		return exchange