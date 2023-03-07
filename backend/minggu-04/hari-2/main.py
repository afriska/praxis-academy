# import flask package
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from pony.flask import Pony
from pony.orm import Database, Required, select, Optional
from http import HTTPStatus

app = Flask(__name__)  # create object app
Pony(app)

db = Database()
db.bind(provider='postgres', user='postgres',
        password='postgres', database='db', host='localhost')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

class Todos(db.Entity):
    todo = Required(str)


class Users(db.Entity):
    name = Required(str)
    job = Optional(str)
    username = Required(str)
    password = Required(str)


# kurang proteksi jika tabel sudah dibuat
db.generate_mapping(create_tables=True)


def getTable():  # dictionary in list
    # with db_session:
    isiTodos = select(i for i in Todos)  # multiobject
    lst_data = []
    for n in isiTodos:  # looping tiap object
        dct = {}
        dct['id'] = n.id
        dct['todo'] = n.todo
        lst_data.append(dct)
    return lst_data


@app.route('/')
def home():
    # print(username)
    if 'username' in session:
        return f"Welcome to Home, {session['username']}" 
    
    else:
        return 'You are not logged in'


@app.route('/ToDo', methods=['GET'])
def read():
    response = {
        'data' : getTable(),
    }
    return jsonify(response),HTTPStatus.OK


@app.route('/ToDo', methods=['POST'])
def add():
    item = request.json

    if item["todo"] != '':
        todo = Todos(todo=item["todo"])


    return redirect(url_for('read'))


@app.route('/ToDo/delete/<id>')
def dell(id):
    Todos[id].delete()
    return redirect(url_for('read'))


@app.route('/ToDo/update/<id>', methods=['GET'])
def update(id):
    try:
        try:
            temp = Todos[id]  # object dari id tertentu
            print(temp)
        except:
            return f'id {id} tidak ada di database'

        # lst = [id]
        # lst.append(temp.todo)
        dct = {}
        dct['Id'] = temp.id
        dct['todo'] = temp.todo

        # return render_template('Update_ToDo.html', item=lst)
        # return jsonify(id = lst[0], todo = lst[1])
        return jsonify(dct)

    except Exception as err:
        return str(err)


@app.route('/ToDo/update/<id>', methods=['PUT'])
def put(id):
    item = request.form['update']
    if item != '':
        temp = Todos[id]
        temp.todo = item
    return redirect(url_for('read'))


@app.route("/signup", methods=['GET'])
def signupView():
    return render_template('signup.html')

@app.route("/signup", methods = ["POST"])
def createUser():
    nm = request.form["name"]
    if nm =='':
        return 'nama tidak boleh kosong'
    elif len(nm) < 8:
        return 'nama minimal terdiri dari 8 huruf'
    
    jb = request.form["job"]

    usr = request.form["username"]
    if usr =='':
        return 'username tidak boleh kosong'
    elif len(usr) < 8:
        return 'username minimal terdiri dari 8 huruf'
    
    passw = request.form["password"]
    if passw =='':
        return 'password tidak boleh kosong'
    elif len(passw) < 8:
        return 'password minimal terdiri dari 8 huruf'

    user = Users(name = nm, job = jb, username = usr, password = passw )
    return 'sign up berhasil'


@app.route('/login', methods=['GET'])
def logView():
    return render_template('login.html')

def getUsernames():
    allUser = select(user for user in Users) #object berisi semua data di tabel Users
    listUsername = []
    for raw in allUser:
        listUsername.append(raw.username)
    
    print(listUsername)
    return listUsername  

@app.route('/login', methods = ['POST'])
def login():
    usr = request.form["username"]
    passw = request.form["password"]
    
    if usr in  getUsernames(): #getUsernames harus return list isi semua username   
        query = db.execute(f"SELECT password FROM users WHERE username = '{usr}'")
        for i in query:
            sandi = i[0]

        if passw == sandi:
            session['username']= usr
            return redirect(url_for('home'))

        else:
            return 'Password salah'
    
    else:
        return 'username tidak ada'
    
# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     return redirect(url_for('home'))