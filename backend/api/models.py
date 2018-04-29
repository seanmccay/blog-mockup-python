from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Post(models.Model):
    title = models.TextField(max_length=50)
    body = models.TextField()
    published_on = models.DateTimeField('date published', auto_now_add=True)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    submitted_at = models.DateTimeField('date submitted', auto_now_add=True)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE) 
