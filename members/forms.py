from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    ''' custom user cretaion form '''
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            'password1',
            'password2',
            'first_name',
            'last_name',
            )

    def __init__(self, *args, **kwargs):
        """ remove labels, add placeholders """
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Password again',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].label = ''
            self.fields[field].widget.attrs['placeholder'] = placeholder
           

class CustomUserEditForm(UserChangeForm):
    class Meta:
        model = User
        exclude = {
            'password',
            'last_login',
            'is_superuser',
            'groups',
            'date_joined',
            'user_permissions',
            'is_active',
            'is_staff',
        }

    def __init__(self, *args, **kwargs):
        """ remove labels, add placeholders """
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'Username',
            'password': 'Password',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
        }
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].label = ''
            self.fields[field].widget.attrs['placeholder'] = placeholder