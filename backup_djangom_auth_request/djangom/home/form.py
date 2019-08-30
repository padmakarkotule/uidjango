from django import forms
from django.contrib.admin import widgets


class UserForm(forms.Form):
    username = forms.CharField(required=True, max_length=25)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    email = forms.EmailField(required=False)

class LogoutForm(forms.Form):
    username = forms.CharField(required=True, max_length=25)
