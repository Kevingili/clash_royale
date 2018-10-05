from django.db import models
from user.models import MyUser

class Card(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    url = models.CharField(max_length=100)
    users = models.ManyToManyField(MyUser)
