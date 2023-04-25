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

from django.contrib.auth.forms import UserChangeForm

class MemberChangeForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254, required=True)
    mobile_number = forms.CharField(max_length=12, required=True,)


class MemberTasksForm(forms.Form):
    name = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder': 'Task Name'}))
    due_date = forms.DateField(required=True,widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}))
    is_task_completed = forms.BooleanField(required=False)
    description = forms.CharField(max_length=200, required=False,widget=forms.TextInput(attrs={'placeholder': 'Task Description'}))