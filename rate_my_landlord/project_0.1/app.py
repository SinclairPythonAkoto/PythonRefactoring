from flask import Flask 
from flask import render_template, url_for

app = Flask(__name__)

@app.route("/")
def landingpage():
    return render_template("landingPage.html")

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

if __name__ == "__main__":
    app.run(debug=True)
