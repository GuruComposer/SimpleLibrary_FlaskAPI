import json
from flask import request, jsonify
from flask_restful import Resource, reqparse
from datetime import datetime, timedelta, timezone
from config import *
from models import User, Book


# Views
class CheckedOut(Resource):
    def get(self, user_id):
        user = User.query.filter_by(user_id=user_id).first()
        if user:
            result = user.books_checked_out
            books_checked_out = [book.serialize() for book in user.books_checked_out]
            print(books_checked_out)
            return {f"{user.user_name}": books_checked_out}, 200
        return {f"error": "User does not exist..."}, 404


class UpcomingDueDate(Resource):
    def get(self, days):
        books_due_soon = []
        books = Book.query.all()
        current_time = datetime.utcnow()
        for book in books:
            if book.book_checked_out:
                if book.due_date - current_time <= timedelta(days):
                    books_due_soon.append(book)
        return [book.serialize() for book in books_due_soon], 200


class CheckOutBook(Resource):
    def put(self, user_id, book_id):
        user = User.query.get_or_404(user_id)
        book = Book.query.get_or_404(book_id)
        if book.owner == user:
            return {
                "error": f"{book.book_name} is already chekced out by {user.user_name}.",
            }, 400
        if book.book_checked_out:
            return {
                "error": f"{book.book_name} is already chekced out by {book.owner.user_name}.",
            }, 400

        if (
            len(user.books_checked_out) < user.user_book_limit
            and not book.book_checked_out
        ):
            book.checkout(user_id)
            print("updated")
            return {
                "updated": f"{user.user_name} checked out {book.book_name}.",
            }, 202
        else:
            print("did not update")
            return {
                "error": f"{user.user_name} cannot checkout any more books.",
                "message": f"{user.user_name} already has {len(user.books_checked_out)} books checked out. Limit = {user.user_book_limit}.",
            }, 400


class DeleteBook(Resource):
    def delete(self, book_id):
        book = Book.query.filter_by(book_id=book_id).first()
        if book:
            book_name = book.book_name
            db.session.delete(book)
            db.session.commit()
            return {"success": f"{book_name} was successfully deleted."}, 202
        return {"error": "This book was not found..."}, 400


# API Routes
def add_resources():
    api.add_resource(CheckedOut, "/library/checkedout/<int:user_id>")
    api.add_resource(UpcomingDueDate, "/library/upcoming_due_date/<int:days>")
    api.add_resource(CheckOutBook, "/library/checkout_book/<int:user_id>/<int:book_id>")
    api.add_resource(DeleteBook, "/library/delete_book/<int:book_id>")
