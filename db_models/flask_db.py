import datetime
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# initialise the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = True
# creating database intsance
db = SQLAlchemy(app)

# creating the tables
class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    door_number = db.Column(db.String(5), nullable=False)
    street_name = db.Column(db.String(36), nullable=False)
    town = db.Column(db.String(60))
    city = db.Column(db.String(60), nullable=False)
    post_code = db.Column(db.String(10), nullable=False)
    review = db.relationship('PropertyReview', backref='author', lazy=True)

    def __repr__(self):
        return f"Building('{self.door_number}', '{self.street_name}', '{self.town}', '{self.city}', '{self.post_code}')"

class PropertyReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text, nullable=False)
    review_by = db.Column(db.String(10), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='BondRobotics_logo.jpg')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    property_id = db.Column(db.Integer, db.ForeignKey('building.id'), nullable=False)

    def __repr__(self):
        return f"PropertyReview('{self.property_rating}', '{self.review}', '{self.review_by}', '{self.date_posted}')"

@app.route("/")
def homepage():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)
