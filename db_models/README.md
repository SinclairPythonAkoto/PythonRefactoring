# Creating A Database Model With Flask SQL Alchemy #

A qucik test to create a DB using Flask SQL Alchemy.

I am using this as a test to see if I can parse data from one form into 2x tables.
This is a quick overview on how to create the tables and retrieve data from them.
As this is for an evolving project, some of the logic might not be applicable to other projects in the future; 
but the logic for building the database and tables will be the same.

#### Flask SQLAlchemy ####
Make sure you install **Flask SQLAlchemy** in order to create a database and tables in Flask.
```
pip install flask-sqlalchemy
```

With this installed, now you want to import it into your Flask app.
```
from flask_sqlalchemy import SQLAlchemy
```

Now we want to initialise the database.  Below where we configure our Flask app we will set our configuration for the database.
```
app = Flask(__name__)

app.config['SECRET_KEY'] = 'somepassword'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
```
We have used SQLite because it is quick and easy to set up; however we can replace `sqlite:///test.db` with a MySQL database path.
`test.db` is the name of the database; this will be stored in the same directory as your Flask file.
`somepassword` is going to be the password for your session.  At a later date we will update this to become a private variable.

Now we can set up the database instance.
```
db = SQLAlchemy(app)
```

#### Creating Tables ####
To create a table with Flask SQLAlchemy we use classes.

The idea is for each property review the data will be sent to two tables, one for the properties, the other for the reviews.

```
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
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    property_id = db.Column(db.Integer, db.ForeignKey('building.id'), nullable=False)

    def __repr__(self):
        return f"PropertyReview('{self.property_rating}', '{self.rewiew}', '{self.review_by}', '{self.date_posted')"
```
To be able to connect the two tables together we have to use the `db.relationship()` keyword in the `review` variable within the `building` class.  Within the brackets we state the other db model *(the other table)* we wish to have the relationship with.  ***Make sure the*** `backref` ***is set to*** `'author'` ***and*** `lazy` ***is set to*** `True`***.***

#### Creating the database ####
Now that we have the tables written, we have to create the database in the Python interpreter.  Make sure you are in the same directory as your Flask app then follow these steps:
```
from flask_app import db
db.create_all()
```
Replace `flask_app` with the name of your Flask app.  With this created you can now start applying your database tables to your Flask app.
Ideally we should be making a separate file to house all your database tables, then you just import the whole file into your Flask app, or again ideally just import the tables that you need.
This is just a brief example of how the tables would work, so all is created within the Flask app file.

#### Creating & getting the data ####
As mentioned before, we will import the tables from the Flask app, but normally this would be a separate file.
```
from flask_app import Building, PropertyReview

property1 = Building(door_number='83C', street_name='Manorside Close', city='London', post_code='SE2 9HD')

db.session.add(property1)
db.session.commit()

prop1 = Building.query.get(property1.id) # this will dynamically get the id of the property review created
review1 = PropertyReview(property_rating=4, review='The house is well kept and the neighbours are really friendly', rating_by='visitor', property_id=prop1.id)

db.session.add(review1)
db.session.commit()

# getting the property rating from the review
for rev in property1.review:
    print(rev.property_rating)
```
