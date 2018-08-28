from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class Book(Base):
    __tablename__ = 'book_book'

    id = Column(Integer, primary_key=True)
    name = Column(String())

    def __repr__(self):
        return '<id {}>'.format(self.id)
