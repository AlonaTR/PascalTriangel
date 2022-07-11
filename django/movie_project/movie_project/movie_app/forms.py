import re
from urllib import request
from django import forms
from .models import Movie

class NewForm(forms.Form):
    name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    rating = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Rating'}))
    year = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Year'}))
    budget= forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Budget'}))