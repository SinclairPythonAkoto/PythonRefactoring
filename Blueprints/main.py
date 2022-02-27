from distutils.log import debug
import os
import typing
from flask import Flask, render_template
from hello_world import hello_world


app: Flask = Flask(__name__)
app.register_blueprint(hello_world)


if __name__ == "__main__":
    app.run(debug=True)
