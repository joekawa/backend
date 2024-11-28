from django.shortcuts import render
from django.http import HttpResponse


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


def login(request):
    return render(request, 'login.html')