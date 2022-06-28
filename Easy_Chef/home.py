from turtle import title
import typing
from flask import Flask, Blueprint, render_template, request, url_for
import requests


home: Blueprint = Blueprint("home", __name__)


@home.route("/")
@home.route("/home", methods=["GET", "POST"])
def homepage():
    if request.method == "GET":
        return render_template("home.html")
    else:
        ing = request.form.get("ingredients")
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"
        querystring = {
            "ingredients": f"{ing}",
            "number": "3",  # number of recipes
            "ignorePantry": "false",
            "ranking": "1",
        }

        headers = {
            "X-RapidAPI-Key": "670505dc3fmsh9cd923658f74705p10c323jsnc8539188f679",
            "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        try:
            # accessing the recipe dictionary
            data = data[0]

            title = data["title"]

            img = data["image"]

            for x in data:
                for y in data["usedIngredients"]:
                    print(y["original"])

            return render_template("home.html", data=data, title=title, img=img)
        except:
            void = "No results"
            return render_template("home.html", void=void)


@home.route("/", methods=["POST"])
def random_recipe():
    meal_options = request.form.get("meal_options")
    breakfast = request.form.get("breakfast")
    brunch = request.form.get("brunch")
    starter = request.form.get("starter")
    main_course = request.form.get("main_course")
    dessert = request.form.get("dessert")
    vege = request.form.get("vege")
    vegan = request.form.get("vegan")

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

    querystring = {"tags": "", "number": "1"}

    headers = {
        "X-RapidAPI-Key": "670505dc3fmsh9cd923658f74705p10c323jsnc8539188f679",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()

    try:
        data = response.json()
        data1 = data["recipes"][0]

        title = data1["title"]
        img = data1["image"]
        servings = data1["servings"]
        prepare_time = data1["preparationMinutes"]
        cook_time = data1["cookingMinutes"]
        ready_in = data1["readyInMinutes"]
        instructions = data1["instructions"]
        return render_template(
            "home.html",
            data1=data1,
            title=title,
            img=img,
            servings=servings,
            prepare_time=prepare_time,
            cook_time=cook_time,
            ready_in=ready_in,
            instructions=instructions,
        )
    except:
        void = "No Results"
        return render_template("home.html", void=void)
