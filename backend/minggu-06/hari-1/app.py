from flask import Flask, jsonify, request
from flask_restx import Api, Resource
from http import HTTPStatus

app = Flask(__name__)
api = Api(app)

todos = {
    '1': "makan"
}

@api.route('/a')
class Home(Resource):
    def get(self):
        return jsonify(data = "ini isi datanya")
    
@api.route('/<string:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}, HTTPStatus.BAD_REQUEST

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}