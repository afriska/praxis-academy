from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from pony.flask import Pony
from pony.orm import Database, Required, select, Optional
from http import HTTPStatus
from flask_json_schema import JsonSchema, JsonValidationError

app = Flask(__name__)
Pony(app)
schema = JsonSchema(app)

db = Database()
db.bind(provider='postgres', user='postgres',
        password='postgres', database='db', host='localhost')

class Todos(db.Entity):
    todo = Required(str)

todoSchema = {
    'required': ['todo','id'],
    'properties': {
        'todo': { 'type': 'string'},
        'id'  : {'type': 'integer' } 
    }
}
db.generate_mapping(create_tables=True)

def getAllData():  # dictionary in list
    isiTodos = select(i for i in Todos)  # multiobject
    lst_data = []
    for n in isiTodos:  # looping tiap object
        dct = {}
        dct['id'] = n.id
        dct['todo'] = n.todo
        lst_data.append(dct)
    return lst_data

@app.route('/', methods = ['GET'])
def readTodo():
    try:
        response = {
            "data" : getAllData(),
            "message" : "success"
        }
        return jsonify(response), HTTPStatus.OK
    except Exception as err:
        return str(err), HTTPStatus.BAD_GATEWAY

@app.errorhandler(JsonValidationError)
def validation_error(e):
    return jsonify({ 'error': e.message, 'errors': [validation_error.message for validation_error  in e.errors]})

@app.route('/', methods=["POST"])
@schema.validate(todoSchema)
def createTodo():
    try:
        # raw = request.json
        # if raw["todo"] != '':
        #     todo = Todos(todo=raw["todo"])
        #     response = {
        #     "message" : "Todo berhasil ditambahkan"
        #     }
        #     return jsonify(response), HTTPStatus.OK
        # else:
        #     response = {
        #         "message" : "Todo tidak boleh kosong"
        #     }
        #     return jsonify(response), HTTPStatus.BAD_REQUEST
        raw = request.json
        todo = Todos(todo=raw["todo"])
        response = {
            "message" : "Todo berhasil ditambahkan"
        }
        return jsonify(response), HTTPStatus.OK
    except Exception as err:
        return str(err), HTTPStatus.BAD_GATEWAY