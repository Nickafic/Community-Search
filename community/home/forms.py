from tkinter import HIDDEN, Widget
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import CharField
from django.forms.widgets import HiddenInput

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AddForm(forms.Form):
    add = forms.CharField(widget=HiddenInput, max_length=100)

class CommForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'search'}),max_length= 100)

class RemoveForm(forms.Form):
    remove = forms.CharField(max_length=100)