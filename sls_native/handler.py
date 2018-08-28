import json
import os

import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import DictCursor
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Book

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


engine = create_engine(os.getenv('DATABASE_URL'))
Session = sessionmaker(bind=engine)
session = Session()


def hello_alchemy(event, context):
    book = session.query(Book).first()
    response = {
        "statusCode": 200,
        "body": json.dumps({'id': book.id, 'name': book.name})
    }

    return response
