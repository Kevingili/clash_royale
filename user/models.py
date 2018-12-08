from django.db import models
from clan.models import Clan

# Create your models here.
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    gold = models.IntegerField(default=500)
    clan = models.ForeignKey(Clan, null=True, on_delete=models.CASCADE)