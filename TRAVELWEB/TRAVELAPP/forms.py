from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

