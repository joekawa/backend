from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")


def customer(request):
    return HttpResponse("Hello, customer.")