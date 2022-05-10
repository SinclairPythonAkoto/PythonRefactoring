from datetime import datetime
from flask import Flask
from flask import render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# initialise the database
app.config['SECRET_KEY'] = 'somepassword'
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
    property_rating = db.Column(db.String, nullable=False)
    review = db.Column(db.Text, nullable=False)
    review_by = db.Column(db.String(10), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='BondRobotics_logo.jpg')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    property_id = db.Column(db.Integer, db.ForeignKey('building.id'), nullable=False)

    def __repr__(self):
        return f"PropertyReview('{self.property_rating}', '{self.review}', '{self.review_by}', '{self.date_posted}')"

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/write_review", methods=['GET', 'POST'])
def write_review():
    if request.method == 'GET':
        return render_template("writeReview.html")
    else:
        # collecting data from the form
        door = request.form['propertyNumber']
        street = request.form['streetName']
        town = request.form['town']
        city = request.form['city']
        postcode = request.form['postcode']
        rating = request.form.get('propertyrating')
        review = request.form['reviewText']
        review_by = request.form['selection']
        img = request.form['imgUpload']

        # saving the data into the property table
        user_property = Building(door_number=door, street_name=street, town=town, city=city, post_code=postcode)
        db.session.add(user_property)
        db.session.commit()
        get_user_property = Building.query.get(user_property.id)
        user_review = PropertyReview(property_rating=rating, review=review, review_by=review_by, image_file=img, property_id=get_user_property.id)
        db.session.add(user_review)
        db.session.commit()
        # logic above dynamically adds the user property & user review into the tables


        return render_template("writeReview.html", get_user_property=get_user_property, user_review=user_review)
        # now need to create logic to print all reviews with matching door number and postcode

if __name__ == "__main__":
    app.run(debug=True)
