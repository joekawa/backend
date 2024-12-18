from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from .forms import *
from .models import Profile, Customer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
def index(request):
    return render(request, 'index.html')


def customer(request):
    return HttpResponse("Hello, customer.")


def team(request):
    return HttpResponse("Hello, team.")


#*POPULATE TWO FORMS AND RETURN WITH EDITABLE FIELDS TO THE HTML
def profile(request):
    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'profile.html',
                  {'user_form': user_form, 'profile_form': profile_form})

def release(request):
    return HttpResponse("Hello, release.")


def release_activity(request):
    return HttpResponse("Hello, release activity.")


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('bettergtm_backend:index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('bettergtm_backend:login')


def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            team = form.cleaned_data.get('team')
            user = User.objects.create_user(username=username, password=password)
            profile = Profile.objects.create(user=user, first_name=first_name,
                                             last_name=last_name,
                                             team=team)
            user.save()
            profile.save()
            return redirect('bettergtm_backend:create_user')
    else:
        form = CreateUserForm()
    return render(request, 'create_user.html', {'form': form})


def deactivate_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return render(request, 'index.html')


def change_password(request):
    return render(request, 'index.html')

def forgot_password(request):
    return render(request, 'index.html')



#* GET DATA FROM PROFILE VIEW AND UPDATE PROFILE IF DATA IS VALID
#! NEED TO ADD TEAM SWITCHING FUNCTIOINALITY BUT THIS WORKS AND IS TESTED
#! INCOMPLETE FUNCTIONALITY
@login_required
def update_user(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('bettergtm_backend:index')
        else:
            profile_form = UpdateProfileForm(instance=request.user.profile)
            user_form = UpdateUserForm(instance=request.user)
            return render(request, 'profile.html',
                        {'user_form': user_form})
    return render(request, 'profile.html', {'user_form': user_form,
                                            'profile_form': profile_form})


@login_required
def create_customer(request):
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bettergtm_backend:create_customer')
    else:
        form = CreateCustomerForm()
    return render(request, 'create_customer.html', {'form': form})


@login_required
def customer_list_view(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})


def customer_detail(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    form = UpdateCustomerForm(instance=customer)

    return render(request, 'customer_detail.html', {'form': form, 'customer': customer})


@login_required
def update_customer(request, customer_id):
    if request.method == 'POST':
        customer = Customer.objects.get(id=customer_id)
        form = UpdateCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('bettergtm_backend:index')
        else:
            form = UpdateCustomerForm(instance=customer)
            return render(request, 'customer_detail.html',
                        {'form': form})
    return render(request, 'customer_detail.html', {'form': form})




def teams(request):
    teams = Team.objects.all()
    return render(request, 'teams.html', {'teams': teams})


#* NEED TO CREATE VIEWS FOR CRUD FOR ROLE, ACTIVITY, RELEASE, RELEASE ACTIVITY, GOALS

def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bettergtm_backend:create_team')
    else:
        form = TeamForm()
    return render(request, 'create_team.html', {'form': form})


def team_detail(request, team_id):
    team = Team.objects.get(id=team_id)
    form = TeamForm(instance=team)

    return render(request, 'team_detail.html', {'form': form, 'team': team})


@login_required
def update_team(request, team_id):
    if request.method == 'POST':
        team = Team.objects.get(id=team_id)
        form = TeamForm(request.POST, instance=team,)
        if form.is_valid():
            form.save()
            return redirect('bettergtm_backend:team_detail', team_id=team.id)
        else:
            form = TeamForm(instance=team)
            return render(request, 'team_detail.html',
                        {'form': form})
    return render(request, 'team_detail.html', {'form': form}) #*NEED TO FIX


def create_activity(request):
    if request.method == 'POST':
        form = ReleaseActivityForm(request.POST)
        if form.is_valid():
            form.request = request
            form.save()
            return redirect('bettergtm_backend:create_activity')
    else:
        form = ReleaseActivityForm()
    return render(request, 'create_activity.html', {'form': form})


def create_release(request):
    if request.method == 'POST':
        form = ReleaseForm(request.POST)
        if form.is_valid():
            form.request = request
            form.save()
            return redirect('bettergtm_backend:create_release')
    else:
        form = ReleaseForm()
    return render(request, 'create_release.html', {'form': form})


def create_role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bettergtm_backend:create_role')
    else:
        form = RoleForm()
    return render(request, 'create_role.html', {'form': form})



def create_goal(request):
    if request.method == 'POST':
        form = GoalsForm(request.POST)
        if form.is_valid():
            form.request = request
            form.save()
            return redirect('bettergtm_backend:create_goal')
    else:
        form = GoalsForm()
        print('diidnt save goal')
    return render(request, 'create_goal.html', {'form': form})


@login_required
def release_list_view(request):
    releases = Release.objects.all()
    return render(request, 'release_list.html',  {'releases': releases})


@login_required
def activity_list_view(request):
    activities = ReleaseActivity.objects.all()
    return render(request, 'activity_list.html',  {'activities': activities})

@login_required
def goal_list_view(request):
    goals = Goal.objects.all()
    return render(request, 'goal_list.html',  {'goals': goals})


def release_detail(request, release_id):
    release = Release.objects.get(id=release_id)
    form = ReleaseForm(instance=release)

    return render(request, 'release_detail.html', {'form': form, 'release': release})


@login_required
def update_release(request, release_id):
    if request.method == 'POST':
        release = Release.objects.get(id=release_id)
        form = ReleaseForm(request.POST, instance=release)
        if form.is_valid():
            form.request = request
            form.created_by = release.created_by
            form.save()
            return redirect('bettergtm_backend:release_detail', release_id=release.id)
        else:
            form = ReleaseForm(instance=release)
            return render(request, 'release_detail.html',
                        {'form': form})
    return render(request, 'release_detail.html', {'form': form}) #*NEED TO FIX


@login_required
def update_activity(request, activity_id):
    if request.method == 'POST':
        activity = ReleaseActivity.objects.get(id=activity_id)
        form = ReleaseActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.request = request
            form.created_by = activity.created_by
            form.save()
            return redirect('bettergtm_backend:activity_detail', activity_id=activity.id)
        else:
            form = ReleaseForm(instance=release)
            return render(request, 'activity_detail.html',
                        {'form': form})
    return render(request, 'activity_detail.html', {'form': form}) #*NEED TO FIX


def activity_detail(request, activity_id):
    activity = ReleaseActivity.objects.get(id=activity_id)
    form = ReleaseActivityForm(instance=activity)

    return render(request, 'activity_detail.html', {'form': form, 'activity': activity})


def goal_detail(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    form = GoalsForm(instance=goal)

    return render(request, 'goal_detail.html', {'form': form, 'goal': goal})


#! NEED TO POPULATE RELEASE AND GOAL ACTUAL VALUE
@login_required
def update_goal(request, goal_id):
    if request.method == 'POST':
        goal = Goal.objects.get(id=goal_id)
        form = GoalsForm(request.POST, instance=goal)
        if form.is_valid():
            form.request = request
            form.created_by = goal.created_by
            form.save()
            return redirect('bettergtm_backend:goal_detail', goal_id=goal.id)
        else:
            form = ReleaseForm(instance=goal)
            return render(request, 'goal_detail.html',
                        {'form': form})
    return render(request, 'goal_detail.html', {'form': form}) #*NEED TO FIX