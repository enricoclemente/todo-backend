from flask import Blueprint, jsonify, request
from extensions import db
from models import Todo

api_bp = Blueprint('api', __name__)

@api_bp.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.as_dict() for todo in todos])

@api_bp.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    data = data['todo']
    todo = Todo(id=data['id'], text=data['text'], date=data['date'])
    db.session.add(todo)
    db.session.commit()
    print("Added new todo: " + data)
    return jsonify(todo.as_dict())

@api_bp.route('/todos/<string:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = Todo.query.get(todo_id)
    data = request.get_json()
    todo.done = data['done']
    todo.important = data['important']
    db.session.commit()
    print("Modified todo with id: " + todo_id)
    return jsonify(todo.as_dict())

@api_bp.route('/todos/<string:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    print("Deleted todo with id: " + todo_id)
    return jsonify({'message': 'Todo deleted successfully'})