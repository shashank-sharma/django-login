from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from login.models import Profile, PhoneDetails


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio',)

class PhoneDetailsForm(forms.ModelForm):
    class Meta:
        model = PhoneDetails
        fields = ('phone_number',)
