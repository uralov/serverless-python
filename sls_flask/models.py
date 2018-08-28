from app import db


class Book(db.Model):
    __tablename__ = 'book_book'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __repr__(self):
        return '<id {}>'.format(self.id)
