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
            "number": "10",
            "ignorePantry": "true",
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
            data = data[1]

            title = data["title"]

            img = data["image"]

            for x in data:
                for y in data["usedIngredients"]:
                    print(y["original"])

            return render_template("home.html", data=data, title=title, img=img)
        except:
            data = "No results"
            return render_template("home.html", data=data)
