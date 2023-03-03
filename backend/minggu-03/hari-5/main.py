from flask import Flask, render_template, request, redirect, url_for, flash #import flask package
from pony.flask import Pony
from pony.orm import Database, Required, db_session, select

app = Flask(__name__) #create object app
Pony(app)

db = Database()
db.bind(provider='postgres', user='postgres', password='postgres', database='db', host='localhost')

class Todos(db.Entity):
    todo = Required(str);

db.generate_mapping(create_tables=True)

def getTable(): #dictionary in list
    # with db_session:
    isiTodos = select(i for i in Todos); #multiobject
    lst_data = []
    for n in isiTodos: #looping tiap object
        dct={}        
        dct['id']= n.id
        dct['todo']= n.todo
        lst_data.append(dct) 
     
    return lst_data

@app.route('/')
def home():
    return f'Welcome to Home'

@app.route('/ToDo', methods=['GET'])
def read():
    return render_template('ToDo.html', data = getTable())

@app.route('/ToDo', methods=['POST'])
def add():
    item = request.form['todo']
    if item != '':
        item = Todos(todo=request.form['todo'])
       
    return redirect(url_for('read'))

@app.route('/ToDo/delete/<id>')
def dell(id):
    Todos[id].delete()
    return redirect(url_for('read'))

@app.route('/ToDo/update/<id>', methods=['GET'])
def update(id):
    temp = Todos[id] #object dari id tertentu
    lst = [id]
    lst.append(temp.todo)
    return render_template('Update_ToDo.html', item = lst)

@app.route('/ToDo/update/<id>', methods = ['POST'])
def put(id):
    item = request.form['update']
    if item != '':
        temp = Todos[id]
        temp.todo = item
            
    return redirect(url_for('read'))