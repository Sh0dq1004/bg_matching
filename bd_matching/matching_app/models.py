from django.db import models

# Create your models here.

class BoardGame(models.Model):
    title = models.CharField(max_length=64)
    weight = models.IntegerField(default=0)
    strategy = models.IntegerField(default=0)
    party = models.IntegerField(default=0)
    secret = models.IntegerField(default=0)
    token = models.IntegerField(default=0)
    adventure = models.IntegerField(default=0)
    max_p = models.IntegerField(default=0)
    min_p = models.IntegerField(default=0)

class Person(models.Model):
    name = models.CharField(max_length=128)
    table_num = models.IntegerField(default=0)
    favorite = models.IntegerField(default=0) #0:なんでも 1:重ボドゲ 2:軽ボドゲ 4:specific
    bg_id = models.IntegerField()
