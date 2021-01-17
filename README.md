# SimpleLibrary_FlaskAPI

## models.py

There are 3 data classes that I need to keep track of: User, Book and Checkouts.

I created two models in models.py, User, and Book. Checkouts is easily queryable by installing a "book_checked_out" property, and returning a queryset of all checked out books.

I created a serializer method for each model so I could easily return JSON representations of all pertinent information for each User and Book object.

I modeled the User and Book relationship as a One-To-Many relationship because one book can only be chekced out by one user at a time, but a user can check out many books at the same time.

If I were to expand this project, I would consider implementing a Many-To-Many relationship for Book and User, and use a through-table for Checkouts, modeling checkout data in the through table. This would allow the application to keep track of user history, and what books the user has checked out over time. In this scenario a book could have many users, and a user would have many books.

## views.py - API ROUTES

There are 4 API endpoints in this RESTful API.

1. You can view all books that a user has checked out:
   /library/checkedout/<int:user_id>

2. You can view all upcoming due books by providing a due date as parameter. All books between now and then will be returned as JSON.
   /library/upcoming_due_date/<int:days>

3. A user can check out a book by sending a PUT request:
   /library/checkout_book/<int:user_id>/<int:book_id>

4. Library administrator can delete a book from the collection:
   /library/delete_book/<int:book_id>

## test_api.py

Automated testing! test_api.py populates the database, and tests and validates all CRUD operations in the API and database. I used python's built in unittest module for this.

## run.py

To run this application without docker, create a virtual environment with python: "python -m venv venv"
Activate the virutal environment with the command: "source venv/bin/activate"
Navigate to the LIBRARY_MAIN directory that contains "requirements.txt". Run the command: "pip install -r requirements.txt"

To run the server application navigate to project directory in the bash shell. Once you are in /library, type "python run.py".
In a new terminal window navigate to the same directory, and type "python test_api.py" to populate the data base and run all the tests, which will pass.
The app should run at: http://0.0.0.0:5000/

## docker

Navitage to the directory, LIBRARY_MAIN, that contains the "Dockerfile".
Build the docker image with the command "docker build -t flaskapp:latest ."

To run the API with docker, use the command "docker run -it -d -p 5000:5000 flaskapp"
This will start the docker container, run the application, populate the database, and run all tests.
The app will run at: http://0.0.0.0:5000/

## important notes

I didn't use Python's json.dumps() to wrap the returned JSON intentionally so that it would be easier to view the JSON resopnse in a chrome browser. I would normally do this, however for demonstration purposes, I thought it would be best to return serialized dictionaries to maintain nice formatting.
