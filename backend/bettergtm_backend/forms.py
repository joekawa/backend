from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, DateInput, Select, CharField
from .models import Profile, Customer, Team, Release, ReleaseActivity, Goals, Outputs, Team, Role, Release, ReleaseActivity, Goals
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
      input_type='date'


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
            widgets = {
                  "name":  TextInput(attrs={"class": "form-control",
                                            "placeholder": "Role Name"}),
                  "description":  TextInput(attrs={"class": "form-control",
                                                   "placeholder": "Description"})
            }


class ReleaseForm(ModelForm):
      name = CharField(max_length=30, required=True,
                               widget=TextInput(
                                     attrs={'class': "form-control",
                                            'placeholder': "Release Name"}))
      release_date = forms.DateField(widget=DateInput)
      description = CharField(max_length=30, required=True,
                               widget=TextInput(
                                     attrs={'class': "form-control",
                                            'placeholder': "Description"}))
      status = CharField(max_length=30, required=True,
                               widget=Select(
                                     attrs={'class': "form-control",
                                            'placeholder': "Status"},
                               choices=[('Not Started', 'Not Started'),
                                        ('In Progress', 'In Progress'),
                                        ('Completed', 'Completed')]))
      type = CharField(max_length=30, required=True,
                               widget=Select(
                                     attrs={'class': "form-control",
                                            'placeholder': "Type"},
                                     choices=[('Tier1', 'Tier 1'),
                                              ('Tier2', 'Tier 2'),
                                              ('Tier3', 'Tier 3')]))

      class Meta:
            model = Release
            fields = ['name', 'release_date', 'description', 'status', 'type']

      def save(self, commit=True):
            instance = super().save(commit=False)
            instance.created_by = self.request.user
            if commit:
                  instance.save()
            return instance



class ReleaseActivityForm(ModelForm):
      name = CharField(max_length=30, required=True,
                               widget=TextInput(
                                     attrs={'class': "form-control",
                                            'placeholder': "Release Name"}))

      description = CharField(max_length=30, required=True,
                               widget=TextInput(
                                     attrs={'class': "form-control",
                                            'placeholder': "Description"}))

      due_date = forms.DateField(widget=DateInput)
      status = CharField(max_length=30, required=True,
                               widget=Select(
                                     attrs={'class': "form-control",
                                            'placeholder': "Status"},
                               choices=[('Not Started', 'Not Started'),
                                        ('In Progress', 'In Progress'),
                                        ('Completed', 'Completed')]))
      assigned_to = forms.ModelChoiceField(
            queryset=User.objects.all(),
            widget=Select(attrs={'class': 'form-control',
                                    'label':'Assigned To'}))
      release = forms.ModelChoiceField(
            queryset=Release.objects.all(),to_field_name='name',
            widget=Select(attrs={'class': 'form-control',
                                    'label':'Release'}))


      class Meta:
            model = ReleaseActivity
            fields = ['name', 'description', 'due_date', 'status', 'assigned_to',
                      'team_assignment', 'release']


class GoalsForm(ModelForm):

      name = CharField(max_length=30, required=True,
                               widget=TextInput(
                                     attrs={'class': "form-control",
                                            'placeholder': "Goal Name"}))

      description = CharField(max_length=30, required=True,
                               widget=TextInput(
                                     attrs={'class': "form-control",
                                            'placeholder': "Description"}))
      goal_value = CharField(max_length=30, required=True,
                               widget=TextInput(
                                     attrs={'class': "form-control",
                                            'placeholder': "Goal Value"}))
      goal_actual_value = CharField(max_length=30, required=True,
                               widget=TextInput(
                                     attrs={'class': "form-control",
                                            'placeholder': "Goal Actual Value"}))

      goal_due_date = forms.DateField(widget=DateInput)
      goal_type = CharField(max_length=30, required=True,
                               widget=Select(
                                     attrs={'class': "form-control",
                                            'placeholder': "Status"},
                               choices=[('Increase Revenue', 'Increase Revenue'),
                                        ('Raise NPS', 'Raise NPS'),
                                        ('REDUCE CHURN', 'REDUCE CHURN')]))

      class Meta:
            model = Goals
            fields = ['name', 'description', 'goal_value', 'goal_type', 'actual_value', 'goal_due_date']