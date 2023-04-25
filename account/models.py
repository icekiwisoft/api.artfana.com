from django.db import models

from django.contrib.auth.models import AbstractUser

from store.models import Theme
# Create your models here.

class Notification(models.Model):
    title = models.CharField(max_length=100)
    fromuser=models.ForeignKey()
    touser=models.ForeignKey()
    def __str__(self) -> str:
        return super().__str__()
class Message(models.Model):
    fromuser=models.ForeignKey()
    responseto=models.TextField()
    senddate=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()
    
    
class User(AbstractUser):
    pseudo = models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    role=models.CharField(max_length=30,default="simple")
    phonenumber=models.CharField(max_length=20)
    fancoins=models.IntegerField(default=0)
    themes=models.ManyToManyField(Theme)
    type=models.IntegerField(default=0)
    subsciption=models.IntegerField(default=0)
    bio=models.TextField(default="hello i'm an artfana user")
    sex=models.CharField(max_length=1)
    following = models.ManyToManyField(
        "self", blank=True, related_name="followers", symmetrical=False
    )

    def __str__(self) -> str:
        return super().__str__()
    


    


    
