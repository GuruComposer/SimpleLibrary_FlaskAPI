import requests
from config import db
from models import User, Book

BASE = "http://127.0.0.1:5000/"


# BUILD THE LIBRARY, REGISTER USERS, REGISTER BOOKS, CHECKOUT SOME BOOKS
def populatedb():
    # Reset db.
    print("==========")
    print("Dropping db...")
    db.drop_all()
    print("db dropped!")
    print("Creating db...")
    db.create_all()
    print("db created!")

    print("Creating users...")
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

    print("Creating books...")
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

    # CHECKOUT SOME BOOKS
    # User1 tries to check out books(1-5)
    print("Attempting to check out books to users...")
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
        print("==========")
