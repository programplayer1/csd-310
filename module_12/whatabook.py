"""
Author:  Paul Lorenz III
Date: August 12, 2023
Assignment Number: Module 12.3
Description: Connecting to the MySQL and working with the WhatABook database by creating the methods.

"""


import mysql.connector
from mysql.connector import errorcode

class WhatABook:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="127.0.0.1",
            user="whatabook_user",
            password="MySQL8IsGreat!",
            database="whatabook"
           
        )
        self.cursor = self.db.cursor()
    """ Creating a method show_menu, which will show the list of menu """
    def show_menu(self):
        print("\nWelcome to WhatABook!")
        print("\n1. Show Books")
        print("2. Show Locations")
        print("3. My Account")
        print("4. Exit")
    """ Creating the method show_books , which will list the books from the table """
    def show_books(self):
        self.cursor.execute("SELECT * FROM book")
        books = self.cursor.fetchall()
        print("\nBooks in WhatABook:")
        for book in books:
           print(f"\nBook ID: {book[0]}, Book Name: {book[1]}, Book Author: {book[2]}, Details: {book[3]}")
        print()
    """ Creating the method show_locations , which will list all the locations from the table """

    def show_locations(self):
        self.cursor.execute("SELECT * FROM store")
        locations = self.cursor.fetchall()
        print("\nLocations of WhatABook stores:")
        for location in locations:
            print(f"\nStore ID: {location[0]}, Location: {location[1]}")
        print()
    """ Creating the method validate_user, which will check if the given user is present in the table """

    def validate_user(self, userid):
        query = "SELECT * FROM user WHERE user_id = %s"
        values = (userid,)
        self.cursor.execute(query, values)
        user = self.cursor.fetchone()
        if user:
            return True
        else:
            return False
    """ Creating the method show_account_meny, which will list the account menu """

    def show_account_menu(self):
        print("\nMy Account Menu")
        print("\n1. View Wishlist")
        print("2. Add Book to Wishlist")
        print("3. Back to Main Menu")

    """ Creating the method show_wishlist , which will provide  all the wishlist of the given user from the table """

    def show_wishlist(self, _cursor, _user_id):
        query = "SELECT book.book_id, book.book_name, book.author, book.details FROM book JOIN wishlist ON book.book_id = wishlist.book_id WHERE wishlist.user_id = %s"
        values = (_user_id,)
        _cursor.execute(query, values)
        wishlist = _cursor.fetchall()
        if not wishlist:
            print("\nYour wishlist is empty.")
        else:
            print("\nYour Wishlist:")
            for item in wishlist:
                print(f"\nBook ID: {item[0]}, Book Name: {item[1]}, Book Author: {item[2]}, Details: {item[3]}")
        print()
    
    """ Creating the method show_books_to_add , which will list all  books from the table  which are not in the wishlist of the given user """

    def show_books_to_add(self, _cursor, _user_id):
        query = "SELECT * FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = %s)"
        values = (_user_id,)
        _cursor.execute(query, values)
        books_to_add = _cursor.fetchall()
        if not books_to_add:
            print("\nNo books available to add to your wishlist.")
        else:
            print("\nBooks available to add to your wishlist:")
            for book in books_to_add:
               print(f"\nBook ID: {book[0]}, Book Name: {book[1]}, Book Author: {book[2]}, Details: {book[3]}")
        print()
    """ Creating the method add_book_to_wishlist , which will add given books to the user wishlist to the wishlist table """

    def add_book_to_wishlist(self, _cursor, _user_id, _book_id):
        query = "INSERT INTO wishlist (book_id, user_id) VALUES (%s, %s)"
        values = (_book_id, _user_id)
        try:
            _cursor.execute(query, values)
            self.db.commit()
            print("\nBook added to your wishlist successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.db.rollback()



if __name__ == "__main__":
     whatabook = WhatABook()
     while True:
        whatabook.show_menu()
        choice = input("\nEnter your choice (1-3): ")
        if choice == "1":
            whatabook.show_books()
        elif choice == "2":
            whatabook.show_locations()
        elif choice == "3":
            user_id = input("\nEnter your user ID: ")
            if whatabook.validate_user(user_id):
                while True:
                    whatabook.show_account_menu()
                    account_choice = input("\nEnter your choice (1-4): ")
                    if account_choice == "1":
                        # View Wishlist
                        whatabook.show_wishlist(whatabook.cursor, user_id)
                    elif account_choice == "2":
                        whatabook.show_books_to_add(whatabook.cursor, user_id)
                        # Add Book to Wishlist
                        book_id = input("Enter the Book ID you want to add to your wishlist: ")
                        try:
                            book_id = int(book_id)
                            whatabook.add_book_to_wishlist(whatabook.cursor, user_id, book_id)
                        except ValueError:
                            print("Invalid Book ID. Please try again.")
                    
                        
                    elif account_choice == "3":
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid user ID. Please try again.")
        elif choice == "4":
            print("\nThank you for using WhatABook. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")




