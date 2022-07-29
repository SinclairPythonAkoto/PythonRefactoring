from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")


def home(request):
    return HttpResponse("Welcome to the home page!")


def educative(request):
    return HttpResponse("Welcome to the Eductaive page!")


def show_age(request, age):
    return HttpResponse("I am %s years old" % age)
    # return HttpResponse(f"I am {age} years old") # f-string can also be used
