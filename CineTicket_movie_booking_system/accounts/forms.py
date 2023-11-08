from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    email = forms.EmailField(label='Email Address',
                             widget=forms.TextInput(attrs={'placeholder': 'you@example.com'}))
    mobile_number = forms.CharField(max_length=10,
                                    validators=[RegexValidator(regex=r'^[0-9]{10}$',
                                                               message='Mobile number must be a 10-digit number')],
                                    label='Mobile Number: ', label_suffix='+91 -',
                                    widget=forms.TextInput(attrs={'placeholder': 'eg: 1234567890'}))
    first_name = forms.CharField(required=False, max_length=30, label='First Name (Optional)',
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter first name'}))
    last_name = forms.CharField(required=False, max_length=30, label='Last Name (Optional)',
                                widget=forms.TextInput(attrs={'placeholder': 'Enter last name'}))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Enter 8 characters or more'}))
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'mobile_number', 'password1', 'password2']





