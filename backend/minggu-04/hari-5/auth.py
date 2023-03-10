from flask import Flask, jsonify, request
from pony.flask import Pony
from pony.orm import Database, PrimaryKey, Required, select
from flask_json_schema import JsonSchema, JsonValidationError
import hashlib
import os
import uuid
from http import HTTPStatus

from flask_jwt_extended import create_access_token, jwt_required, JWTManager, set_access_cookies, unset_jwt_cookies, get_csrf_token



app = Flask(__name__)
Pony(app)
schema = JsonSchema(app)

app.config["JWT_SECRET_KEY"] = os.getenv("SALT_PASSWORD")
app.config["JWT_TOKEN_LOCATION"] = "cookies"
app.config["JWT_ACCESS_CSRF_HEADER_NAME"] = "csrfToken"

jwt = JWTManager(app)

db = Database()
db.bind(provider='postgres', user='postgres',
        password='postgres', database='db', host='localhost')


class Petugas(db.Entity):
    id = PrimaryKey(uuid.UUID, default=uuid.uuid4)
    username = Required(str, 45, unique=True)
    password = Required(str, 45)
    nama = Required(str, 100)
    telp = Required(str, 12)
    alamat = Required(str)
    role = Required(str)


schemaCreatePetugas = {
    'required': ["username", "password", "nama", "telp", "alamat"],
    'properties': {
        'username': {'type': 'string'},
        'password': {'type': 'string'},
        'nama': {'type': 'string'},
        'telp': {'type': 'string'},
        'alamat': {'type': 'string'},
        'role': {'type': 'string'}
    }
}

schemaLogin = {
    'required': ["username", "password"],
    'properties': {
        'username': {'type': 'string'},
        'password': {'type': 'string'},
    }
}


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

@app.errorhandler(JsonValidationError)
def valitationError(e):
    print(e, type(e))
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]})

@app.route('/signup', methods=["POST"])
@schema.validate(schemaCreatePetugas)
def createAdmin():
    try:
        jsonBody = request.json
        q = select(i for i in Petugas)
        if q.filter(username=jsonBody["username"]).exists():
            return 'username already exist'
        else:
            a = uuid.uuid4()
            hashpass = hashlib.md5(
                (jsonBody['password'] + os.getenv('SALT_PASSWORD')).encode('utf8')).hexdigest()
            petugas = Petugas(id=a, username=jsonBody['username'], password=hashpass, nama=jsonBody['nama'],
                              telp=jsonBody['telp'], alamat=jsonBody['alamat'], role=jsonBody['role'])
            return "data signup admin"
    except Exception as err:
        return str(err)


@app.route('/users', methods=["GET"])
def readAllUser():
    query = select(p for p in Petugas)[:]
    lst = []
    for user in query:
        dct = {
            "nama": user.nama,
            "telp": user.telp,
            "alamat": user.alamat,
            "role": user.role
        }
        lst.append(dct)
    print(lst)
    return lst


@app.route('/login', methods=["POST"])
@schema.validate(schemaLogin)
def login():
    jsonBody = request.json
    hashpass = hashlib.md5(
        (jsonBody["password"] + os.getenv("SALT_PASSWORD")).encode()).hexdigest()
    if select(p for p in Petugas if p.username == jsonBody["username"] and p.password == hashpass):
        user = select(p for p in Petugas if p.username == jsonBody["username"]).get()
        additionalClaims = {
            "id" : user.id,
            "role" : user.role
        }
        response = jsonify({"msg": "login berhasil"})
        accessToken = create_access_token(identity = user.username, fresh=True)
        csrfToken = get_csrf_token(accessToken)

        set_access_cookies(response, accessToken)
        return response
    else:
        return "login gagal"
    
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
@jwt_required()
def createTodo():
    try:
        jsonBody = request.json
        if jsonBody["todo"] != '':
            todo = Todos(todo = jsonBody["todo"])
            response = {
            "message" : "Todo berhasil ditambahkan"
            }
            return jsonify(response), HTTPStatus.OK
        else:
            response = {
                "message" : "Todo tidak boleh kosong"
            }
            return jsonify(response), HTTPStatus.BAD_REQUEST
    # return "create todo"
    except Exception as err:
        return str(err), HTTPStatus.BAD_GATEWAY
    # return "halaman create todo"
    
@app.route('/logout', methods = ["POST"])
@jwt_required()
def protected():
    # currentUser = get_jwt_identity()
    # claims = get_jwt()
    response = jsonify({
        # "id" : claims.id,
        # "role": claims.role,
        "msg" : "logout berhasil"
    })
    unset_jwt_cookies(response)
    return response
