from flask import Blueprint, render_template


user: Blueprint = Blueprint(
    "user", __name__, static_folder="static", template_folder="templates"
)


@user.route("/user")
def user_page():
    return "User page!"
