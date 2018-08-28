import json
import os

import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import DictCursor

load_dotenv()

connection = psycopg2.connect(
    host=os.getenv('host'),
    database=os.getenv('database'),
    user=os.getenv('user'),
    password=os.getenv('password'),
)
cursor = connection.cursor(cursor_factory=DictCursor)


def hello(event, context):
    cursor.execute("SELECT * FROM book_book;")
    book = cursor.fetchone()
    response = {
        "statusCode": 200,
        "body": json.dumps(book)
    }

    return response
