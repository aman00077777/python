from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name}-{self.description}"


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/drinks")
def get_drinks():
    drinks = Drink.query.all()

    output = []
    for drink in drinks:
        drink_data = {'name':drink.name,'description': drink.description}

        output.append(drink_data)

    return {"drinks": output}


from flask import request  # Make sure to add 'request' to your imports at the top!


@app.route("/drinks", methods=["POST"])
def add_drink():
    # 1. Grab the JSON data sent to the API
    data = request.get_json()

    # 2. Create a new Drink object instance
    new_drink = Drink(name=data["name"], description=data["description"])

    # 3. Add and commit to your database
    db.session.add(new_drink)
    db.session.commit()

    # 4. Return the newly created item and a 201 Created status code
    return {"id": new_drink.id}, 201

