from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class LoginForm(AuthenticationForm):
    # def __init__(self, *args, **kwargs):
    #     super(CustomAuthForm, self).__init__(*args, **kwargs)
    username = forms.CharField(widget=TextInput(attrs={'placeholder':'Username', 'class':'form-control'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password', 'class':'form-control'}))
