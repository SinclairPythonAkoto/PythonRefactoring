"""Testing the functionality of the Easy Chef app"""

from wsgiref import headers
import pytest
import requests
import main
from flask import Flask, Blueprint
from homepage import home
import json

# validate response

# validate route (webpage)
def test_base_route():
    app = Flask(__name__, template_folder="../templates")
    app.register_blueprint(home)
    client = app.test_client()
    base_url = "/"
    home_url = "/home"

    response = client.get(base_url)
    response2 = client.get(home_url)

    # print(response.get_data())
    assert response.status_code == 200
    assert response2.status_code == 200


# validate successful post
def test_post_route_success():
    app = Flask(__name__, template_folder="../templates")
    app.register_blueprint(home)
    client = app.test_client()
    base_url = "/"
    home_url = "/home"

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

    mock_request_headers = {
        "X-RapidAPI-Key": "670505dc3fmsh9cd923658f74705p10c323jsnc8539188f679",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    }

    mock_request_querystring = {
        "ingredients": "apples,flour,sugar",
        "number": "3",
        "ignorePantry": "false",
        "ranking": "1",
    }

    response = requests.request(
        "GET", url, headers=mock_request_headers, params=mock_request_querystring
    )

    # check to see if request was successful
    assert response.status_code == 200
    print("test 1")


def test_mock_headers():
    app = Flask(__name__, template_folder="../templates")
    app.register_blueprint(home)
    client = app.test_client()
    base_url = "/"
    home_url = "/home"

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

    mock_request_headers = {
        "X-RapidAPI-Key": "670505dc3fmsh9cd923658f74705p10c323jsnc8539188f679",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    }

    # check if the RapidAPI-Key for headers is up to date & works
    assert (
        mock_request_headers["X-RapidAPI-Key"]
        == "670505dc3fmsh9cd923658f74705p10c323jsnc8539188f679"
    )
    print("test 2")

    # check if the RapidAPI-Host for headers is up to date & works
    assert (
        mock_request_headers["X-RapidAPI-Host"]
        == "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    )
    print("test 3")


def test_request_querystring():
    app = Flask(__name__, template_folder="../templates")
    app.register_blueprint(home)

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

    mock_request_headers = {
        "X-RapidAPI-Key": "670505dc3fmsh9cd923658f74705p10c323jsnc8539188f679",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    }

    mock_request_querystring = {
        "ingredients": "apples,flour,sugar",
        "number": "3",
        "ignorePantry": "false",
        "ranking": "1",
    }

    response = requests.request(
        "GET", url, headers=mock_request_headers, params=mock_request_querystring
    )

    data = response.json()

    # check to make sure same number of recipes as number of mock_request_querystring["number"]
    assert mock_request_querystring["number"] == str(
        len(data)
    )  # convert to str because mock_request_querystring["number"] is a str

    # check the ingredients
    assert mock_request_querystring["ingredients"] == "apples,flour,sugar"


def test_unauthorized_api_call():
    """Check if correct unauthorised request message is given back if
    no data in mock_request_headers.
    """
    app = Flask(__name__, template_folder="../templates")
    app.register_blueprint(home)
    client = app.test_client()
    base_url = "/"
    home_url = "/home"

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

    mock_request_headers = {}

    mock_request_querystring = {
        "ingredients": "apples,flour,sugar",
        "number": "3",
        "ignorePantry": "false",
        "ranking": "1",
    }

    response = requests.request(
        "GET", url, headers=mock_request_headers, params=mock_request_querystring
    )

    assert response.status_code == 401


def test_bad_request_api_call():
    """Check if correct bad request is 404 - page not avaiable"""
    app = Flask(__name__, template_folder="../templates")
    app.register_blueprint(home)
    client = app.test_client()
    base_url = "/"
    home_url = "/home"

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

    mock_request_headers = {
        "X-RapidAPI-Key": "670505dc3fmsh9cd923658f74705p10c323jsnc8539188f679",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    }

    mock_request_querystring = {
        "ingredients": "apples,flour,sugar",
        "number": "3",
        "ignorePantry": "false",
        "ranking": "1",
    }

    # response = requests.request("GET", url, headers=mock_request_headers, params=None)
    response = client.post(
        url, data=json.dumps(mock_request_querystring), headers=mock_request_headers
    )

    assert response.status_code == 404
