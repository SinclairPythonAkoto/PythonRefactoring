import typing
from flask import Blueprint, render_template, url_for, request, redirect, session

# from users.user import user


create_user: Blueprint = Blueprint(
    "create_user", __name__, static_folder="static", template_folder="templates"
)


@create_user.route("/create_user", methods=["GET", "POST"])
def new_user():
    if request.method == "GET":
        return render_template("create_user.html")
    else:
        username: request = request.form.get("username")
        return redirect(url_for("create_user.new_user", username=username))