import os
import typing
from flask import Flask
from hello_world import hello_world
from home import home
from users.user import user
from users.create_user import create_user


app: Flask = Flask(__name__)
app.register_blueprint(hello_world)
app.register_blueprint(home)
app.register_blueprint(user, prefix="/")
app.register_blueprint(create_user, prefix="/")


if __name__ == "__main__":
    app.run(debug=True)
