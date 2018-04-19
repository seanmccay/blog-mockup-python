from django.db import models

class User(models.Model):
    username: models.CharField(max_length=25, primary_key=True)
    display_name: models.CharField(max_length=50)

class BlogPost(models.Model):
    title: models.CharField(max_length=50)
    content: models.CharField(max_length=max)
    date: models.DateTimeField()
    user: models.ForeignKey(User, on_delete=models.CASCADE)
    
class Comment(models.Model):
    blogpost_id: models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    content: models.CharField(max_length=250)
    date: models.DateTimeField()
    user: models.ForeignKey(User, on_delete=models.CASCADE) 

