from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Database Model
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name}-{self.description}"


# 1. HOME ROUTE
@app.route("/")
def hello():
    return "Welcome to the Drinks API!"


# 2. GET ALL DRINKS
@app.route("/drinks", methods=["GET"])
def get_drinks():
    drinks = Drink.query.all()
    output = []
    for drink in drinks:
        drink_data = {"id": drink.id, "name": drink.name, "description": drink.description}
        output.append(drink_data)
    return {"drinks": output}


# 3. GET A SINGLE DRINK BY ID
@app.route("/drinks/<int:id>", methods=["GET"])
def get_drink(id):
    drink = db.get_or_404(Drink, id)
    return {"id": drink.id, "name": drink.name, "description": drink.description}


# 4. POST (CREATE A NEW DRINK)
@app.route("/drinks", methods=["POST"])
def add_drink():
    data = request.get_json()
    
    if not data or "name" not in data:
        return {"error": "Name field is required"}, 400

    new_drink = Drink(name=data["name"], description=data.get("description", ""))
    
    try:
        db.session.add(new_drink)
        db.session.commit()
        return {"id": new_drink.id, "message": "Drink created successfully!"}, 201
    except:
        db.session.rollback()
        return {"error": "Drink name already exists!"}, 400


# 5. PUT (UPDATE AN EXISTING DRINK)
@app.route("/drinks/<int:id>", methods=["PUT"])
def update_drink(id):
    drink = db.get_or_404(Drink, id)
    data = request.get_json()

    if "name" in data:
        drink.name = data["name"]
    if "description" in data:
        drink.description = data["description"]

    try:
        db.session.commit()
        return {"id": drink.id, "name": drink.name, "description": drink.description}
    except:
        db.session.rollback()
        return {"error": "Could not update. Name might be a duplicate."}, 400


# 6. DELETE (REMOVE A DRINK)
@app.route("/drinks/<int:id>", methods=["DELETE"])
def delete_drink(id):
    drink = db.get_or_404(Drink, id)
    db.session.delete(drink)
    db.session.commit()
    return {"message": f"Drink '{drink.name}' was successfully deleted!"}

