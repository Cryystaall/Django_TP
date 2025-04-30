from django import forms
from django.contrib.auth.forms import AuthenticationForm

class ParticipationForm(forms.Form):
    is_coming = forms.BooleanField(required=False, label="Je viens")

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
