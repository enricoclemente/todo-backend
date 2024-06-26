from flask import Blueprint, jsonify, request
from extensions import db
from models import Todo
from datetime import datetime

api_bp = Blueprint('api', __name__)

@api_bp.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.as_dict() for todo in todos])

@api_bp.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    data = data['todo']
    received_date = datetime(int(data['date'][:4]), int(data['date'][5:7]), int(data['date'][8:10]))
    todo = Todo(id=data['id'], text=data['text'], date=received_date)
    db.session.add(todo)
    db.session.commit()
    print("Added new todo: ")
    print(data)
    return jsonify(todo.as_dict())

@api_bp.route('/todos/<string:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = Todo.query.get(todo_id)
    data = request.get_json()
    if not (data.get('text') is None):
        todo.text = data['text']
    if not (data.get('date') is None):
        received_date = datetime(int(data['date'][:4]), int(data['date'][5:7]), int(data['date'][8:10]))
        todo.date = received_date
    if not (data.get('done') is None):
        todo.done = data['done']
    if not (data.get('important') is None):
        todo.important = data['important']
    db.session.commit()
    print("Modified todo with id: " + todo_id + "New data: ")
    print(data)
    return jsonify(todo.as_dict())

@api_bp.route('/todos/<string:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    print("Deleted todo with id: " + todo_id)
    return jsonify({'message': 'Todo deleted successfully'})