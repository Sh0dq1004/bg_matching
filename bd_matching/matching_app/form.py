from django import forms

class User(forms.Form):
    name = forms.CharField(max_length=128)
    table_num = forms.IntegerField(default=0)
    favorite = forms.IntegerField(default=8) # 8 == なんでも