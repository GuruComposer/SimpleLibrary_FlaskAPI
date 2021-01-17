import requests, unittest
from populatedb import populatedb
from models import User, Book

populatedb()

BASE = "http://127.0.0.1:5000/"


class TestApp(unittest.TestCase):
    def test_checkout(self):
        # User 6 tries to check out an already checked out book, book2.
        print("User 6 tries to check out an already checked out book, book2.")
        endpoint = f"library/checkout_book/6/2"
        response = requests.put(BASE + endpoint)
        print(response.json())
        user1 = User.query.filter_by(user_id=1).first()
        user6 = User.query.filter_by(user_id=6).first()
        book2 = Book.query.filter_by(book_id=2).first()
        self.assertEqual(book2 in user1.books_checked_out, True)
        self.assertEqual(book2 not in user6.books_checked_out, True)

    def test_checkout_non_existent_book(self):
        # User7 tries to check out a non-existant book.
        endpoint = f"library/checkout_book/7/100"
        response = requests.put(BASE + endpoint)
        user7 = User.query.filter_by(user_id=7).first()
        book100 = Book.query.filter_by(book_id=100).first()
        print(response.json())
        self.assertEqual(response.status_code, 404)
        self.assertEqual(book100 not in user7.books_checked_out, True)

    def test_checkout_already_checked_out_book(self):
        # User1 tries to checkout book they already have checked out.
        print("User1 tries to checkout book they already have checked out.")
        endpoint = f"library/checkout_book/1/2"
        response = requests.put(BASE + endpoint)
        print(response.json())
        self.assertEqual(response.status_code, 400)

    def test_not_existent_user(self):
        # Non-Existent user tries to check out a book.
        endpoint = f"library/checkout_book/100/5"
        response = requests.put(BASE + endpoint)
        print(response.json())
        user1 = User.query.filter_by(user_id=1).first()
        book5 = Book.query.filter_by(book_id=5).first()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(book5.book_checked_out, False)

    def test_normal_checkout(self):
        # Test Checkout with Put - SUCCESS.
        endpoint = f"library/checkout_book/6/16"
        response = requests.put(BASE + endpoint)
        user6 = User.query.filter_by(user_id=6).first()
        book16 = Book.query.filter_by(book_id=16).first()
        print(response.json())
        self.assertEqual(book16.book_checked_out, True)
        self.assertEqual(book16 in user6.books_checked_out, True)

    # Test delete book
    def test_delete_unchecked_book(self):
        # Delete unchecked out book.
        endpoint = f"library/delete_book/20"
        response = requests.delete(BASE + endpoint)
        print(response.json())
        book20 = Book.query.filter_by(book_id=20).first()
        self.assertEqual(book20, None)

    def test_delete_checked_out_book(self):
        # Delete checked out book.
        endpoint = f"library/delete_book/1"
        response = requests.delete(BASE + endpoint)
        print(response.json())
        book1 = Book.query.filter_by(book_id=1).first()
        self.assertEqual(book1, None)

    def test_delete_non_existent_book(self):
        # Delete non-existant book
        endpoint = f"library/delete_book/55"
        response = requests.delete(BASE + endpoint)
        print(response.json())
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()