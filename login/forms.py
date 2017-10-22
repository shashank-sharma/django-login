from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from login.models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', help_text = "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'phone_number')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio',)
