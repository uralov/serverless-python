import json

from flask import Response, jsonify
from app import app
from models import Book


@app.route('/')
def hello_world():
    message = {
        'message': 'Execution started successfully!'
    }
    book = Book.query.first()
    return jsonify({
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': {'id': book.id, 'name': book.name}
    })
