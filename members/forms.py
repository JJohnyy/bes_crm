from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            'password1',
            "password2",
            'first_name',
            'last_name',
            )
        field_classes = {
            'username': UsernameField(max_length=10),
            'email': forms.CharField,
            'password': forms.CharField(max_length=20),
            'first_name': forms.CharField(max_length=30),
            'last_name': forms.CharField(max_length=30),
            }
