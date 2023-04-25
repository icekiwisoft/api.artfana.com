from pyclbr import Class
from pydoc import describe
from django.db import models
from account.models import User

import group

# Create your models here.

class Post(models.Model):
    
    title=models.CharField(max_length=100)
    description=models.TextField()
    file=models.FileField(upload_to="posts/file")
    presentimg=models.ImageField(upload_to="post/presentation")
    user=models.ForeignKey()
    group=models.ForeignKey()
    def __str__(self) -> str:
        return super().__str__()

class Like(models.Model):
    fromuser=models.ForeignKey(User,on_delete=models.CASCADE)


class Comment(models.Model):
    fromuser=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.TextField()
    replyto=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

class Donation(models.Model):
    to=models.ForeignKey(User,on_delete=models.CASCADE)
    fromuser=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    accepted=models.BooleanField(default=False)
    value=models.IntegerField(default=1)


class Category(models.Models):
    name=models.CharField(default="")
    description=models.TextField(default="")

class SubCategory(models.Model):
    name=models.CharField(default="")
    description=models.CharField(default="")








