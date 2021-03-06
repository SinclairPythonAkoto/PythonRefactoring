# using Blueprint to create a singular page to import into main.py Flask app
# This can be good for creating your landing page / home page
from flask import Blueprint, render_template, url_for


hello_world: Blueprint = Blueprint("hello_world", __name__)


@hello_world.route("/")
@hello_world.route("/hello")
def hello():
    return render_template("hello_world.html")
