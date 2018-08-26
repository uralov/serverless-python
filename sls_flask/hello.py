import json

from flask import Flask, Response

app = Flask(__name__)


@app.route('/flask_view')
def hello_world():
    message = {
        'message': 'Execution started successfully!'
    }
    return Response(json.dumps({
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': message
    }))
