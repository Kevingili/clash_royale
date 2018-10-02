from django.db import models

class Card(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
