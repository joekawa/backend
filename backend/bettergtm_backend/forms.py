from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Select
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Select
from .models import Profile, Customer, Team, Release, ReleaseActivity, Goals, Outputs, Team, Role, Release, ReleaseActivity, Goals
from django.contrib.auth.models import User

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


class UpdateProfileForm(ModelForm):

      class Meta:
            model = Profile
            fields = ['first_name', 'last_name', 'team']


class UpdateUserForm(ModelForm):

      class Meta:
            model = User
            fields = ['username', 'email', 'is_active']


class CreateCustomerForm(ModelForm):

      class Meta:
            model = Customer
            fields = ['name', 'country', 'city', 'state', 'zip_code']
            widgets = {
                  "name": TextInput(attrs={"class": "form-control",
                                           "placeholder":"Customer Name"}),
                  "country": TextInput(attrs={"class": "form-control",
                                              "placeholder": "Country"}),
                  "city": TextInput(attrs={"class": "form-control",
                                           "placeholder": "City"}),
                  "state": TextInput(attrs={"class": "form-control",
                                            "placeholder": "State"}),
                  "zip_code": TextInput(attrs={"class": "form-control",
                                               "placeholder": "Zip Code"}),
            }

#! FORM NOT FINISHED
class UpdateCustomerForm(ModelForm):

      class Meta:
            model = Customer
            fields = ['name', 'country', 'city', 'state', 'zip_code']
            widgets = {
                  "name": TextInput(attrs={"class": "form-control",
                                           "placeholder":"Customer Name"}),
                  "country": TextInput(attrs={"class": "form-control",
                                              "placeholder": "Country"}),
                  "city": TextInput(attrs={"class": "form-control",
                                           "placeholder": "City"}),
                  "state": TextInput(attrs={"class": "form-control",
                                            "placeholder": "State"}),
                  "zip_code": TextInput(attrs={"class": "form-control",
                                               "placeholder": "Zip Code"}),
            }


#! FORM NOT FINISHED
class CreateTeamForm(ModelForm):

      class Meta:
            model = Team
            fields = ['name']


#! FORM NOT FINISHED
class UpdateTeamForm(ModelForm):
      class Meta:
            model = Team
            fields = ['name']

#! FORM NOT FINISHED
class CreateReleaseForm(ModelForm):

      class Meta:
            model = Release
            fields = ['name', 'status', 'release_date']


#! FORM NOT FINISHED
class UpdateReleaseForm(ModelForm):

      class Meta:
            model = Release
            fields = ['name']


#! FORM NOT FINISHED
class CreateReleaseActivityForm(ModelForm):

      class Meta:
            model = ReleaseActivity
            fields = ['name']


#! FORM NOT FINISHED
class UpdateReleaseActivityForm(ModelForm):

      class Meta:
            model = ReleaseActivity
            fields = ['name']


#* FORMS TO BUILD
#* CREATE:  Team, Role, Release, ReleaseActivity, Goals, Outputs
#* EDIT: Team, Role, Release, ReleaseActivity, Goals, Outputs
#! NOTE I THINK I CAN REUSUE THE BASE FORMS FOR BOTH CREATE AND EDIT FUNCTIONS

class TeamForm(ModelForm):

      class Meta:
            model = Team
            fields = ['name', 'short_name', 'description']
            widgets = {
                  "name": TextInput(attrs={"class": "form-control",
                                           "placeholder":"Team Name"}),
                  "short_name": TextInput(attrs={"class": "form-control",
                                              "placeholder": "Short Name"}),
                  "description": TextInput(attrs={"class": "form-control",
                                           "placeholder": "Description"})
            }


class RoleForm(ModelForm):

      class Meta:
            model = Role
            fields = ['name', 'description']


class ReleaseForm(ModelForm):

      class Meta:
            model = Release
            fields = ['name', 'release_date', 'description', 'status', 'type']


class ReleaseActivityForm(ModelForm):

      class Meta:
            model = ReleaseActivity
            fields = ['name', 'description', 'due_date', 'status', 'assigned_to', 'team_assignment']


class GoalsForm(ModelForm):

      class Meta:
            model = Goals
            fields = ['name', 'description', 'goal_value', 'goal_type', 'actual_value', 'goal_due_date']