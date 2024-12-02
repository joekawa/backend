from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Select
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Select

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, required=True,
                               widget=TextInput(
                                     attrs={'class': "form-control",
                                            'placeholder': "Username"}))

    password = forms.CharField(max_length=30, required=True,
                               widget=PasswordInput(
                                     attrs={'class': "form-control",
                                            'placeholder': "Enter Password"}))


class CreateUserForm(UserCreationForm):
      username = forms.CharField(max_length=30, required=True,
                              widget=TextInput(
                                    attrs={'class': "form-control",
                                            'placeholder': "Username"}))
      password1 = forms.CharField(max_length=30, required=True,
                               widget=PasswordInput(
                                     attrs={'class': "form-control",
                                            'placeholder': "Enter Password"}))
      password2 = forms.CharField(max_length=30, required=True,
                                widget=PasswordInput(
                                     attrs={'class': "form-control",
                                            'placeholder': "Repeat Password"}))
      email = forms.EmailField(required=True,
                             widget=EmailInput(
                                attrs={'class': "form-control",
                                       'placeholder': "Email"}))
      first_name = forms.CharField(max_length=30, required=False,
                                 widget=TextInput(
                                     attrs={'class': "form-control",
                                            'placeholder': "First Name"}))
      last_name = forms.CharField(max_length=30, required=False,
                                widget=TextInput(
                                    attrs={'class': "form-control",
                                           'placeholder': "Last Name"}))
      team = forms.CharField(max_length=30, required=False,
                                widget=TextInput(
                                    attrs={'class': "form-control",
                                           'placeholder': "Team Name"}))


class UpdateUserForm(forms.Form):
      username = forms.CharField(max_length=30, disabled=True,
                                 required=True,
                              widget=TextInput(
                                    attrs={'class': "form-control",
                                            'placeholder': "Username"}))
      email = forms.EmailField(required=True,
                             widget=EmailInput(
                                attrs={'class': "form-control",
                                       'placeholder': "Email"}))
      first_name = forms.CharField(max_length=30, required=False,
                                 widget=TextInput(
                                     attrs={'class': "form-control",
                                            'placeholder': "First Name"}))
      last_name = forms.CharField(max_length=30, required=False,
                                widget=TextInput(
                                    attrs={'class': "form-control",
                                           'placeholder': "Last Name"}))
      team = forms.CharField(max_length=30, required=False,
                                widget=TextInput(
                                    attrs={'class': "form-control",
                                           'placeholder': "Team Name"}))
      is_active = forms.BooleanField(required=True,
                                     widget=Select(attrs={'class': ("form-select")},
                                     choices=[(1, "Active"), (0, "Inactive")]))