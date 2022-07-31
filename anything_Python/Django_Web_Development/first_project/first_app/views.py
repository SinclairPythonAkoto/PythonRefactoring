from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


from .forms import TestForm


def home(request):
    return render(request, "first_app/home.html")


def search(request):
    return render(request, "first_app/search.html")


def about(request):
    return render(request, "first_app/about.html")


def educative(request):
    return render(request, "first_app/educative.html")


def index(request):
    return render(request, "first_app/index.html")


def forms(request):
    form = TestForm(request.POST or None)
    data = "None"
    text = "None"
    if form.is_valid():
        data = form.cleaned_data
        text = data.get("text")
    return render(
        request, "first_app/forms.html", {"form": form, "data": data, "text": text}
    )


# def home(request):
#     return HttpResponse("Welcome to the home page!")

# def show_age(request, age):
#     return HttpResponse("I am %s years old" % age)
# return HttpResponse(f"I am {age} years old") # f-string can also be used


# def even_or_odd(request, num):
#     if num % 2 == 0:
#         output = "%s is an even number." % num
#     else:
#         output = "%s is an odd number." % num
#     return HttpResponse(output)
