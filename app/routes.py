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
    todo = Todo(title=data['title'])
    db.session.add(todo)
    db.session.commit()
    return jsonify({'message': 'Todo created successfully'})

@api_bp.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = Todo.query.get(todo_id)
    data = request.get_json()
    todo.title = data['title']
    todo.done = data['done']
    todo.important = data['important']
    db.session.commit()
    return jsonify({'message': 'Todo updated successfully'})

@api_bp.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo deleted successfully'})