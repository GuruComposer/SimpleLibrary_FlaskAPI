from flask_restful import Resource
from datetime import datetime, timedelta, timezone
from config import db

# Models
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_book_limit = db.Column(db.Integer, nullable=False, default=3)
    books_checked_out = db.relationship("Book", backref="owner", lazy=True)

    def serialize(self):
        user = {
            "user_id": str(self.user_id),
            "user_name": str(self.user_name),
            "user_book_limit": str(self.user_book_limit),
            "books_checked_out": str(
                [book.serialize() for book in self.books_checked_out]
            ),
        }
        return user


class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    book_genre = db.Column(db.String(50), nullable=False, default="generic")
    owner_id = db.Column(
        db.Integer,
        db.ForeignKey("user.user_id"),
        nullable=True,
        default=None,
    )
    book_checked_out = db.Column(db.Boolean, nullable=True, default=False)
    date_checked_out = db.Column(db.DateTime, nullable=True, default=None)
    due_date = db.Column(db.DateTime, nullable=True, default=None)

    def serialize(self):
        book = {
            "book_id": str(self.book_id),
            "book_name": str(self.book_name),
            "book_genre": str(self.book_genre),
            "owner_id": str(self.owner_id),
            "book_checked_out": str(self.book_checked_out),
            "date_checked_out": str(self.date_checked_out),
            "ude_date": str(self.due_date),
        }
        return book

    def checkout(self, user_id, days=28):
        user = User.query.filter_by(user_id=user_id).first()
        if user and len(user.books_checked_out) < user.user_book_limit:
            if self.book_checked_out:
                return {"Error": "This book is already checked out..."}, 400
            self.book_checked_out = True
            self.date_checked_out = datetime.utcnow()
            self.due_date = self.date_checked_out + timedelta(days)
            self.owner = user
            db.session.commit()
            return {"Message": f"{self.book_name} was checked out by {user.user_name}"}
        if user:
            return {
                "error": f"{user.user_name} cannot checkout any more books.",
                "message": f"{user.user_name} already has {len(user.books_checked_out)} books checked out. Limit = {user.user_book_limit}.",
            }, 400
        else:
            return {"error": f"user_id: {user_id} was not found..."}, 404