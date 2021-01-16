from views import db
from models import User, Book
import requests

# Reset db.
db.drop_all()
db.create_all()

# Create users
wes = User(user_name="Wes")
joe = User(user_name="Joe")
sally = User(user_name="Sally")
bob = User(user_name="Bob")
jim = User(user_name="Jim")
tt = User(user_name="Tt")
sarah = User(user_name="Sarah")
john = User(user_name="John")
deb = User(user_name="Deb")
bryan = User(user_name="Bryan")
users = [wes, joe, sally, bob, jim, tt, sarah, john, deb, bryan]


# Create books
book1 = Book(book_name="Book1")
book2 = Book(book_name="Book2")
book3 = Book(book_name="Book3")
book4 = Book(book_name="Book4")
book5 = Book(book_name="Book5")
book6 = Book(book_name="Book6")
book7 = Book(book_name="Book7")
book8 = Book(book_name="Book8")
book9 = Book(book_name="Book9")
book10 = Book(book_name="Book10")
book11 = Book(book_name="Book11")
book12 = Book(book_name="Book12")
book13 = Book(book_name="Book13")
book14 = Book(book_name="Book14")
book15 = Book(book_name="Book15")
book16 = Book(book_name="Book16")
book17 = Book(book_name="Book17")
book18 = Book(book_name="Book18")
book19 = Book(book_name="Book19")
book20 = Book(book_name="Book20")
books = [
    book1,
    book2,
    book3,
    book4,
    book5,
    book6,
    book7,
    book8,
    book9,
    book10,
    book11,
    book12,
    book13,
    book14,
    book15,
    book16,
    book17,
    book18,
    book19,
    book20,
]

for user in users:
    db.session.add(user)
db.session.commit()

for book in books:
    db.session.add(book)
db.session.commit()

BASE = "http://127.0.0.1:5000/"

# Checkout some books
# User1 tries to check out books(1-5)
for book in range(1, 6):
    endpoint = f"library/checkout_book/1/{book}"
    response = requests.put(BASE + endpoint)
    print(response.json())

# User2 tries to check out books(6-9)
for book in range(6, 10):
    endpoint = f"library/checkout_book/2/{book}"
    response = requests.put(BASE + endpoint)
    print(response.json())

# User3 tries to check out books(10-12)
for book in range(10, 13):
    endpoint = f"library/checkout_book/3/{book}"
    response = requests.put(BASE + endpoint)
    print(response.json())

# User4 tries to check out books(13-14)
for book in range(13, 15):
    endpoint = f"library/checkout_book/4/{book}"
    response = requests.put(BASE + endpoint)
    print(response.json())

# User5 tries to check out book(15)
for book in range(15, 16):
    endpoint = f"library/checkout_book/5/{book}"
    response = requests.put(BASE + endpoint)
    print(response.json())

# User 6 tries to check out already checked out book, book2
print("User 6 tries to check out already checked out book, book2.")
endpoint = f"library/checkout_book/6/2"
response = requests.put(BASE + endpoint)
print(response.json())

# User7 tries to check out a non-existant book
endpoint = f"library/checkout_book/7/100"
response = requests.put(BASE + endpoint)
print(response.json())

# User1 tries to checkout book they already have checked out.
print("User1 tries to checkout book they already have checked out.")
endpoint = f"library/checkout_book/1/2"
response = requests.put(BASE + endpoint)
print(response.json())

# Non-Existent user tries to check out a book
endpoint = f"library/checkout_book/100/5"
response = requests.put(BASE + endpoint)
print(response.json())


# Test Checkout with Put - FAILURE
endpoint = f"library/checkout_book/1/1"
response = requests.put(BASE + endpoint)
print(response.json())

# Test Checkout with Put - SUCCESS
endpoint = f"library/checkout_book/4/12"
response = requests.put(BASE + endpoint)
print(response.json())

# Test delete book
# Delete unchecked out book.
endpoint = f"library/delete_book/20"
response = requests.delete(BASE + endpoint)
print(response.json())

# Delete checked out book.
endpoint = f"library/delete_book/1"
response = requests.delete(BASE + endpoint)
print(response.json())

# Delete non-existant book
endpoint = f"library/delete_book/55"
response = requests.delete(BASE + endpoint)
print(response.json())
