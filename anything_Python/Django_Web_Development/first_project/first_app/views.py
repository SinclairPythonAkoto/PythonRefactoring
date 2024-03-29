from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import TestForm, PostModelForm


from .forms import TestForm


def homepage(request):
    return render(request, "first_app/home.html")


def home(request):
    try:
        user = User.objects.create_user(
            username="Sinclair", email="sinclair@gmail.com", password="mac12"
        )
        user.save()
    except IntegrityError as e:
        print(e)
    return HttpResponse("Welcome to the Home page!")


def search(request):
    return render(request, "first_app/search.html")


def about(request):
    return render(request, "first_app/about.html")


def educative(request):
    user = User.objects.get(username="Ulrich")
    user.email = "hello@gmail.com"
    user.save()
    return HttpResponse("Welcome to Educative page!")


def index(request):
    return render(request, "first_app/index.html")


def forms(request):
    initial_dict = {
        "text": "Some initail data",
        "integer": 123,
    }
    form = TestForm(request.POST or None, initial=initial_dict)
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
