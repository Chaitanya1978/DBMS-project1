from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from .models import Member

class MemberCreationForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True,widget=forms.TextInput(attrs={'placeholder': 'First Name of member'}))
    last_name = forms.CharField(max_length=50, required=True,widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.EmailField(max_length=254, required=True,widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    mobile_number = forms.CharField(max_length=12, required=True,widget=forms.TextInput(attrs={'placeholder': 'Mobile Number'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))