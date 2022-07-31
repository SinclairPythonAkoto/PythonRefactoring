from django.urls import path
from first_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("about/", views.about, name="about"),
    path("educative/", views.educative, name="educative"),
    path("index/", views.index, name="index"),
    path("forms/", views.forms, name="form"),
]
