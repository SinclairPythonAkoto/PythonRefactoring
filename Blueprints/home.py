import typing
from flask import Flask, Blueprint, render_template, url_for


home: Blueprint = Blueprint("home", __name__)


@home.route("/home")
def homepage():
    return render_template("home.html")
