import typing
from flask import Blueprint, render_template, url_for, request, session


user: Blueprint = Blueprint(
    "user", __name__, static_folder="static", template_folder="templates"
)


@user.route("/user", methods=["GET", "POST"])
def user_page():
    username: request = request.form.get("username")
    return render_template("users.html", username=username)
