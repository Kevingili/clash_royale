from django.db import models
from user.models import MyUser

class Topic(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)

class Comment(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    content = models.TextField(null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='topic_comment')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_comment')