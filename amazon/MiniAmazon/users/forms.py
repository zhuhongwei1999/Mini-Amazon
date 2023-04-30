from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class UserNameForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['email']

class ProfileForm(forms.ModelForm): 
    class Meta:
        model = Profile
        fields = ('ups_account', 'bank_account', 'default_x', 'default_y')
        labels = {'ups_account': 'UPS Account', 'bank_account': 'Bank Account','default_x':'Address X','default_y':'Address Y'}

