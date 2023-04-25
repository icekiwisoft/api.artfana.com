from email.mime import image
from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=100,unique=True)
    shortdescription=models.CharField(max_length=200,default="a new awesome artfana item")
    pricing=models.IntegerField(default=0)
    image=models.ImageField(default="noimage.png",upload_to="/item")
    class Meta:
        abstract = True


# Create your models here.
class Theme(Item):
   pass
    

class Fancoins(Item):
    value=models.IntegerField(default=0)
    pass    

class ThemesPack(Item):
    Themes=models.ManyToManyField(Theme)

