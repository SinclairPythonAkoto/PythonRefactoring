from crypt import methods
import typing
from flask import Blueprint, render_template, url_for, request, redirect


create_user: Blueprint = Blueprint(
    "create_user", __name__, static_folder="static", template_folder="templates"
)


@create_user.route("/create_user", methods=["GET", "POST"])
def new_user():
    if request.method == "GET":
        return "New user created!"
    else:
        pass
