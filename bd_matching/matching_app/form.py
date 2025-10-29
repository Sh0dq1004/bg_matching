from django import forms
from .models import Person

choices = (
    ("0", "なんでも"),
    ("1", "重ボドゲ"),
    ("2", "軽ボドゲ"),
)

from django.db import models
from django.conf import settings 

class Topic(models.Model):

    #都道府県の選択肢をchoicesオプションにてセット
    prefecture  = models.CharField(verbose_name="都道府県",choices=settings.PREFECTURES,max_length=4)
    comment     = models.CharField(verbose_name="コメント",max_length=2000)

    def __str__(self):
        return self.comment

class User(forms.ModelForm):
    class meta:
        model = Person
        fields = ("name",)
    #favorite = forms.RadioSelect(choices=choices) #0:なんでも 1:重ボドゲ 2:軽ボドゲ 4+id:specific



