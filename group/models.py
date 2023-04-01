from django.db import models

from account.models import User

# Create your models here.

class Group(models.Model):
    name=models.CharField(max_length=100)
    id=models.CharField(max_length=100,unique=True,primary_key=True)
    subscription=models.IntegerField(default=0)
    type=models.CharField(max_length=20)

    def __str__(self):
        return self.id


class usergroupinfo(models.Model):
    pass


class GroupPermission(models.Model):
    foruser=models.ForeignKey(User,on_delete=models.CASCADE)



