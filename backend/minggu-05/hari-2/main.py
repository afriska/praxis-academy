from flask import Flask, jsonify, request
from pony.orm import Database, Required, select
from pony.flask import Pony
from flask_json_schema import JsonSchema, JsonValidationError
from flask_cors import CORS

app = Flask(__name__)
Pony(app)
schema = JsonSchema(app)
CORS(app)

db = Database()
db.bind(provider="postgres", user="postgres",
        password='postgres', host="localhost", database="db")


class Employees(db.Entity):
    name = Required(str)
    email = Required(str)
    phone = Required(str)
    gender = Required(str)
    designation = Required(str)
    city = Required(str)


employeeSchema = {
    'required': ['name', 'email', 'phone', 'gender', 'designation', 'city'],
    'properties': {
        'name': {'type': 'string'},
        'email': {'type': 'string'},
        'phone': {'type': 'string'},
        'gender': {'type': 'string'},
        'designation': {'type': 'string'},
        'city': {'type': 'string'},
    }
}
db.generate_mapping(create_tables=True)


@app.errorhandler(JsonValidationError)
def validation_error(e):
    return jsonify({
        'error': e.message,
        'errors': [validation_error.message for validation_error in e.errors]
    })


@app.route('/employee', methods=["POST"])
@schema.validate(employeeSchema)
def createEmployee():
    # name = request.form["name"]
    # email = request.form["email"]
    # phone = request.form["phone"]
    # gender = request.form["gender"]
    # designation = request.form["designation"]
    # city = request.form["city"]

    # obj = Employees(name=name,
    #                 email=email,
    #                 phone=phone,
    #                 gender=gender,
    #                 designation=designation,
    #                 city=city)
    employee = request.json
    obj = Employees(name=employee["name"],
                    email=employee["email"],
                    phone=employee["phone"],
                    gender=employee["gender"],
                    designation=employee["designation"],
                    city=employee["city"])
    return "success"


@app.route('/employee', methods=["GET"])
def readEmployees():
    query = select(e for e in Employees)
    lst = []
    for employee in query:
        dct = {
            'id': employee.id,
            'name': employee.name,
            'email': employee.email,
            'phone': employee.phone,
            'gender': employee.gender,
            'designation': employee.designation,
            'city': employee.city
        }
        lst.append(dct)

    return jsonify(lst)


@app.route('/employee/<id>', methods=["DELETE"])
def delete(id):
    Employees[id].delete()
    return "delete success"


@app.route('/employee/<id>', methods=["GET"])
def viewUpdate(id):
    employee = select(e for e in Employees if e.id == id)[:]
    dct = {
        "id" : id,
        "name": employee[0].name,
        "email": employee[0].email,
        "phone": employee[0].phone,
        "gender": employee[0].gender,
        "designation": employee[0].designation,
        "city": employee[0].city
    }
    return jsonify(data=dct)


@app.route('/employee/<id>', methods=["PUT"])
@schema.validate(employeeSchema)
def update(id):
    # name = request.form["name"]
    # email = request.form["email"]
    # phone = request.form["phone"]
    # gender = request.form["gender"]
    # designation = request.form["designation"]
    # city = request.form["city"]
    # employee = Employees[id]
    # employee.name = name
    # employee.email = email
    # employee.phone = phone
    # employee.gender = gender
    # employee.designation = designation
    # employee.city = city

    jsonBody = request.json
    print(jsonBody)
    employee = Employees[id]
    print(employee, type(employee))
    print(jsonBody["name"], type(jsonBody["name"]))
    employee.name = jsonBody["name"]
    employee.email = jsonBody["email"]
    employee.phone = jsonBody["phone"]
    employee.gender = jsonBody["gender"]
    employee.designation = jsonBody["designation"]
    employee.city = jsonBody["city"]
    return "update berhasil"
