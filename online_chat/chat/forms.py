from django import forms
from . import models as db

class SearchForm(forms.ModelForm):
    room_code = forms.CharField(label="",max_length=6,widget=forms.TextInput(attrs={"placeholder":"enter your room code here"}))
    class Meta():
        model = db.Room
        fields = ("room_code",)