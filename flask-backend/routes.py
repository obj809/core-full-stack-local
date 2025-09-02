# flask-backend/routes.py

from flask import Blueprint, jsonify, request
from sqlalchemy import text

todos_bp = Blueprint('todos', __name__)

db = None

def init_db(app_db):
    global db
    db = app_db

@todos_bp.route('/helloworld')
def hello_world():
    return "Hello World"

@todos_bp.route('/')
def home():
    return jsonify(message="Home Page")

@todos_bp.route('/todo/', methods=['POST'])
def add_todo():
    data = request.json
    title = data['title']

    with db.engine.connect() as conn:
        # Begin a transaction
        trans = conn.begin()
        try:
            conn.execute(text('INSERT INTO todos (title) VALUES (:title)'), {'title': title})
            # Commit the transaction
            trans.commit()
        except:
            # Rollback the transaction if there's an error
            trans.rollback()
            return jsonify(message="Error occurred while adding todo"), 500

    return jsonify(message="Todo added successfully"), 201


@todos_bp.route('/todo/', methods=['GET'])
def get_todos():
    with db.engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM todos'))
        # Use the _mapping attribute to convert rows to dictionaries
        todos = [dict(row._mapping) for row in result]

    return jsonify(todos)

@todos_bp.route('/todo/<int:id>', methods=['GET'])
def get_todo_by_id(id):
    with db.engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM todos WHERE id = :id'), {'id': id})
        todo = result.fetchone()

    if todo:
        return jsonify(dict(todo._mapping))
    else:
        return jsonify(message="Todo not found"), 404

@todos_bp.route('/todo/<int:id>', methods=['PUT'])
def update_todo(id):
    data = request.json
    title = data['title']

    with db.engine.connect() as conn:
        # Begin a transaction
        trans = conn.begin()
        try:
            conn.execute(text('UPDATE todos SET title = :title WHERE id = :id'), {'title': title, 'id': id})
            # Commit the transaction
            trans.commit()
        except:
            # Rollback the transaction if there's an error
            trans.rollback()
            return jsonify(message="Error occurred while updating todo"), 500

    return jsonify(message="Todo updated successfully")


@todos_bp.route('/todo/<int:id>', methods=['DELETE'])
def delete_todo(id):
    with db.engine.connect() as conn:
        # Begin a transaction
        trans = conn.begin()
        try:
            conn.execute(text('DELETE FROM todos WHERE id = :id'), {'id': id})
            # Commit the transaction
            trans.commit()
        except:
            # Rollback the transaction if there's an error
            trans.rollback()
            return jsonify(message="Error occurred while deleting todo"), 500

    return jsonify(message="Todo deleted successfully")


