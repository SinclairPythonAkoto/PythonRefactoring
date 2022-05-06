from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)
