from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from .forms import LoginForm

def index(request):
    return render(request, 'index.html')


def customer(request):
    return HttpResponse("Hello, customer.")


def team(request):
    return HttpResponse("Hello, team.")


def profilt(request):
    return HttpResponse("Hello, profile.")

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