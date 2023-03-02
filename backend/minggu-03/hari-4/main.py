from flask import Flask, render_template, request, redirect, url_for #import flask package
from pony.flask import Pony
from pony.orm import *

app = Flask(__name__) #create object app

db = Database()
db.bind(provider='postgres', user='postgres', password='postgres', database='db', host='localhost')

class Todos(db.Entity):
    todo = Required(str);

db.generate_mapping(create_tables=True)

@app.route('/')
def home():
    return f'Welcome to Home'

@app.route('/ToDo', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        with db_session:
            act = Todos(todo=request.form['todo'])

        return f'{act.todo} berhasil ditambahkan'
    
    else:
        return render_template('ToDo.html')
    


