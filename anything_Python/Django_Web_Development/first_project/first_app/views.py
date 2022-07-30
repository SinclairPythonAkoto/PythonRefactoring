from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "first_app/home.html")


def search(request):
    return render(request, "first_app/search.html")


def about(request):
    return render(request, "first_app/about.html")


# def index(request):
#     filters = {"value": "We are learning filters!"}
#     return render(request, "first_app/index.html", context=filters)


# def home(request):
#     return HttpResponse("Welcome to the home page!")


# def educative(request):
#     return HttpResponse("Welcome to the Eductaive page!")


# def show_age(request, age):
#     return HttpResponse("I am %s years old" % age)
# return HttpResponse(f"I am {age} years old") # f-string can also be used


def even_or_odd(request, num):
    if num % 2 == 0:
        output = "%s is an even number." % num
    else:
        output = "%s is an odd number." % num
    return HttpResponse(output)
