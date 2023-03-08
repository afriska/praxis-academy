from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from pony.flask import Pony
from pony.orm import Database, Required, select, Optional
from http import HTTPStatus

app = Flask(__name__)
Pony(app)

db = Database()
db.bind(provider='postgres', user='postgres',
        password='postgres', database='db', host='localhost')

class Todos(db.Entity):
    todo = Required(str)

db.generate_mapping(create_tables=True)

def getAllData():  # dictionary in list
    # with db_session:
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

@app.route('/', methods=["POST"])
def createTodo():
    try:
        raw = request.json
        if raw["todo"] != '':
            todo = Todos(todo=raw["todo"])
            response = {
            "message" : "Todo berhasil ditambahkan"
            }
            return jsonify(response), HTTPStatus.OK
        else:
            response = {
                "message" : "Todo tidak boleh kosong"
            }
            return jsonify(response), HTTPStatus.BAD_REQUEST
    except Exception as err:
        return str(err), HTTPStatus.BAD_GATEWAY
    
@app.route('/update/<id>', methods=["GET"])
def readTodoTertentu(id):
    try:
        try:
            temp = Todos[id]  # object dari id tertentu
        except:
            response = {
                "message" : "Id tidak ditemukan"
            }
            return jsonify(response), HTTPStatus.BAD_REQUEST
        dct = {}
        dct['Id'] = temp.id
        dct['todo'] = temp.todo

        response = {
            "data" : dct,
            "message" : "success"
        }
        return jsonify(response), HTTPStatus.OK
    except Exception as err:
        return str(err), HTTPStatus.BAD_GATEWAY 
    
@app.route('/update/<id>', methods=["PUT"])
def updateTodo(id):
    try:
        raw = request.json
        item = Todos[id]
        item.todo = raw["todo"]
        response = {
            "message" : "Todo berhasil diupdate"
        }
        return jsonify(response), HTTPStatus.OK
    except Exception as err:
        return str(err), HTTPStatus.BAD_GATEWAY 
    
@app.route('/delete/<id>', methods=["DELETE"])
def dell(id):
    try:
        try:
            temp = Todos[id]  # object dari id tertentu
        except:
            response = {
                "message" : "Id tidak ditemukan"
            }
            return jsonify(response), HTTPStatus.BAD_REQUEST
        Todos[id].delete()
        response = {
            "message" : "Todo berhasil didelete"
        }
        return jsonify(response), HTTPStatus.OK
    
    except Exception as err:
        return str(err), HTTPStatus.BAD_GATEWAY