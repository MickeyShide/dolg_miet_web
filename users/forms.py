from django.contrib.auth.forms import UserCreationForm
from django.forms import forms, CharField, PasswordInput
from django.contrib.auth.forms import User

class LoginForm(forms.Form):
    username = CharField(max_length=65)
    password = CharField(max_length=65, widget=PasswordInput)