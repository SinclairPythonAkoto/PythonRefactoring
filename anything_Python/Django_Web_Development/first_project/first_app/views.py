from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    tv_shows_list = {
        "tv_shows": {
            "Game of Thrones": "9.3",
            "Blacklist": "8",
            "Suits": "8.5",
            "The Witcher": "8.5",
        }
    }
    return render(request, "first_app/index.html", context=tv_shows_list)


def home(request):
    return HttpResponse("Welcome to the home page!")


def educative(request):
    return HttpResponse("Welcome to the Eductaive page!")


# def show_age(request, age):
#     return HttpResponse("I am %s years old" % age)
# return HttpResponse(f"I am {age} years old") # f-string can also be used


def even_or_odd(request, num):
    if num % 2 == 0:
        output = "%s is an even number." % num
    else:
        output = "%s is an odd number." % num
    return HttpResponse(output)
