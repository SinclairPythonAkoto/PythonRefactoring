from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# initialise the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

# creating database intsance
db = SQLAlchemy(app)

# creating the tables
class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    door_number = db.Column(db.String(5), nullable=False)
    street_name = db.Column(db.String(36), nullable=False)
    town = db.Column(db.String(60))
    city = db.Column(db.String(60), nullable=False)
    post_code = db.Column(db.String(7), nullable=False)
    review = db.relationship('PropertyReview', backref='author', lazy=True)

    def __init__(self, door_number, street_name, town, city, post_code):
        self.door_number = door_number
        self.street_name = street_name
        self.town = town
        self.city = city
        self.post_code

class PropertyReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_rating = db.Column(db.Integer(1), nullable=False)
    review = db.Colum(db.Text, nullable=False)
    review_by = db.Column(db.String(10), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='BondRobotics_logo.jpg')
    property_id = db.Column(db.Integer, db.ForiegnKey('building.id'), nullable=False)

    def __init__(self, property_rating, review, review_by):
        self.property_rating = property_rating
        self.review = review
        self.review_by = review_by

@app.route("/")
def homepage():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)
