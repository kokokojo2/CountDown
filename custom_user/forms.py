from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser


class RegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['email']
