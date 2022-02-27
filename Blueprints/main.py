from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__)

# test if the the flask app works with hello world!
@app.route("/hello")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
