import os
import typing
from flask import Flask, render_template
from hello_world import hello_world
from home import home


app: Flask = Flask(__name__)
app.register_blueprint(hello_world)
app.register_blueprint(home)


if __name__ == "__main__":
    app.run(debug=True)
