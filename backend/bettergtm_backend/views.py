from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from .forms import LoginForm, CreateUserForm, UpdateUserForm
from .models import Profile
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')


def customer(request):
    return HttpResponse("Hello, customer.")


def team(request):
    return HttpResponse("Hello, team.")


def profile(request):
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=user)
    form = UpdateUserForm()
    form.fields['username'].initial = user.username
    form.fields['email'].initial = user.email
    form.fields['first_name'].initial = profile.first_name
    form.fields['last_name'].initial = profile.last_name
    form.fields['team'].initial = profile.team.name
    form.fields['is_active'].initial = user.is_active
    return render(request, 'profile.html',
                  {'form': form})

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


def update_user(request):
    return render(request, 'index.html')

