"""
Author:  Paul Lorenz III
Date: July 30, 2023
Assignment Number: Module 9.2
Description: Connecting to the MySQL and getting data by Joining the player and team tables from pysports database.

"""

""" import statements"""
import sys
import mysql.connector
from mysql.connector import errorcode

config = { 
    "user":"pysports_user",
    "password":"MySQL8IsGreat!",
    "host":"127.0.0.1",
    "database":"pysports",
    "raise_on_warnings":True
}

def show_menu():
    
    print("\n -- Main Menu --")

    print(" 1. View Books\n  2. View Store Location\n  3. My Account\n  4. Exit Program")

    try:
        choice = int(input("Please enter a valid option from the main menu: "))

        return choice
    
    except ValueError:
        print("\n Invalid option.  Please enter a valid option from the main menu.\n")

        sys.exit(0)
    
def show_books(_cursor):
    
    """  Inner Table Join Query  """

    _cursor.execute("SELECT book_id, book_name, details, author from book")

    """  Obtain results from cursor object"""
    books = _cursor.fetchall()

    print("\n  -- DISPLAYING BOOK LISTING --")

    """  Executes the job to repeat the process to look over the player data set and display the results in the output of the program.  """
    for book in books:
        print("  Book Name: {}\n  Author: {}\n Details: {}\n".format(book[0], book[1], book[2]))

def show_locations(_cursor):

    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n  -- DISPLAYING STORE LOCATIONS --")

    for location in locations:
        print("  Locale: {}\n".format(location[1]))

def validate_user():
    """ validate the users ID. """

    try:
        user_id = int(input("Please enter a valid user id: "))

        if user_id < 0 or user_id > 3:
            print("\n Invalid user id. Please enter a valid user id.")
            sys.exit(0)
        
        return user_id
    
    except ValueError:
        print("\n Invalid user id. Please enter a valid user id.")

        sys.exit(0)

def show_account_menu():
    """ Display the users account menu"""

    try: 
        print("\n  -- Customer Menu --")
        print("   1. WIshlist\n  2. Add Book\n  3. Main Menu")

        account_option = int(input("Please enter a valid account menu option: "))
        
        return account_option
    
    except ValueError:
        print("\n Invalid account menu option. Please enter a valid account menu option.")

        sys.exit(0)

def show_wishlist(_cursor, _user_id):
    """ Create a query for a list of books that were added to the user's whatabook wishlist. """

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " +
                    "INNER JOIN user ON wishlist.user_id = user.user_id " +
                    "INNER JOIN book ON wishlist.book_id = book.book_id" +
                    "WHERE user.user_id = {}".format(_user_id))
    wishlist = _cursor.fetchall()

    print("  Book Name: {}\n  Author: {}\n".format(book[4], book[5]))

def show_books_to_add(_cursor, _user_id):
    """ Creating database queries for a list of books that are not listed in the user wishlist. """

    query = ("SELECT book_id, book_name, details, author "
             "FROM book "
             "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    
    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n  -- DISPLAYING AVAILABLE BOOKS  --")
    
    for book in books_to_add:
        print("  Book Id: {}\n  Book Name:  {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id)) VALUES({}, {})".format(_user_id, _book_id))

try:
    """ Inserting a try/catch block to detect any potential MySQL database errors. """

""" Establishes connection to the WhatABook database"""
db = mysql.connector.connect(**config) 

""" Created the cursor for MySQL queries. """
cursor = db.cursor()

print("\n Welcome to the WhatABook Store. ")

""" Displays the Main Menu. """
user_selection = show_menu()

"""While Loop to display that the user's selection is not equal to 4. """

while user_selection !=4:
    

