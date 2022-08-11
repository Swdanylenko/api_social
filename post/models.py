from django.db import models
from user.models import User


class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    user_added = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    votes = models.ManyToManyField(User, through='Vote', related_name='votes')
    

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    date_voted = models.DateTimeField(auto_now_add=True)