from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    ''' custom user cretaion form '''
    required_css_class = 'required-field'
    username = forms.CharField(max_length = 20)
    email = forms.EmailField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    password1 = forms.CharField(max_length = 20)
    password2 = forms.CharField(max_length = 20)

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

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

    def __init__(self, *args, **kwargs):
        """
        remove labels, add placeholders
        """
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
