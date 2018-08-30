import os

from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField
from playhouse.db_url import connect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

load_dotenv()
Base = declarative_base()
peewee_db = connect(os.getenv('DATABASE_URL'))


class Book(Base):
    __tablename__ = 'book_book'

    id = Column(Integer, primary_key=True)
    name = Column(String())

    def __repr__(self):
        return '<id {}>'.format(self.id)


def make_table_name(model_class):
    return 'book_book'


class BookPeewee(Model):
    id = IntegerField(primary_key=True)
    name = CharField()

    class Meta:
        database = peewee_db
        table_function = make_table_name

    def __repr__(self):
        return '<id {}>'.format(self.id)
