#!/usr/bin/env python3
""" A mock comments board section. """

import datetime
import getpass


users = [
    {"user_id": 1, "name": "admin", "password": "adminpassword", "type": "admin"},
    {"user_id": 2, "name": "chronixx", "password": "chronology", "type": "moderator"},
    {"user_id": 3, "name": "kdot", "password": "topdawg", "type": "user"}
]
moderators = []
admin = []
comments = []


class user:
    """ Holds methods for normal users
    """
    def __init__(self, name):
        pass


    def name(self):
        """ Getter - Returns username """
        pass


    def name(self, value):
        """ Sets the username """
        pass

    def is_logged_in(self):
        """ Returns the login status - True/False """
        pass

    def last_logged_in_at(self):
        """ Returns the timestamp for the last time a user logged in. """
        pass

    def log_in(self):
        """ Logs in  a user."""
        pass

    def log_out(self):
        pass

    def can_edit(self, comment):
        """ Checks user's edit privileges over the comment (True/False) """
        pass

    def can_delete(self, comment):
        """ Checks user's delete privileges over the comment (True/False) """
        pass

    def __repr__(self):
        """ String output to stdout """
        pass

class moderator(user):
    """ Holds methods for moderator users

        Moderators can perform all operations of a normal user.
        Moderators can delete comments (remove trolls).
    """
    def __init__(self, name):
        pass

    def can_edit(self, comment):
        """ Checks user's edit privileges over the comment (True/False) """
        pass

    def can_delete(self, comment):
        """ Checks user's delete privileges over the comment (True/False) """
        pass


class admin(moderator):
    """ Holds methods for Administrator users

        Admins can perform all operations of a normal user and moderator.
        Admins can edit and or delete any comment
    """
    def __init__(self, name):
        pass

    def can_delete(self, comment):
        """ Checks user's delete privileges over the comment (True/False) """
        pass

    def can_edit(self, comment):
        """ Checks user's edit privileges over the comment (True/False) """
        pass


class comment:
    """ Holds methods for comments

        A comment is a message, a timestamp and the author.
        A comment can be a reply (which tracks the parent comment).
    """
    def __init__(self, author, message, replied_to=None):
        pass

    def author(self):
        """ Returns author of comment """
        pass


    def author(self, value):
        """ Sets the comment's author's name """
        pass


    def message(self):
        """ Returns the comment's message body """
        pass


    def message(self, value):
        """ Sets the comment's message body """
        pass

    def created_at(self):
        """ Returns the comment's creation timestamp """
        pass


    def replied_to(self):
        """ Returns the Parent comment being replied to """
        pass


    def replied_to(self, value):
        """ Sets the Parent comment being replied to """
        pass

    def to_string(self):
        """ Returns a formated string """
        pass


if __name__ == "__main__":

    loop = True # Controls program temination
    while loop == True:
        print("*" * 80)
        print(f"{'Welcome to the Band of brothers Comments boards':^80}")
        print("*" * 80)
        print(" \n Please Enter Login details ")

        username = input("Enter user Name (blank space to exit):  ")
        if username.strip() == "":
            loop = False

        password = getpass.getpass("Password: ")

        if username in [_["name"] for _ in users] and \
                password in [_["password"] for _ in users]:
            print("What wold you like to do?")
            print('\t 1 - Write a Comment')
            print('\t 2 - Edit a comment')
            print('\t 3 - Reply to a comment')
            print('\t 4 - exit')
            print('=' * 80)
            menu_selection = input('Enter a selection [0-6]: ')


            if menu_selection == 1:
                pass

            elif menu_selection == 2:
                pass

            elif menu_selection == 3:
                pass

            elif menu_selection == 4:
                pass

            elif menu_selection == '0': # Exit
                print(f"{' Good-Bye ':*^80}")
                loop = False # Terminate program

            else:
                print(f"{'UNRECOGNIZED COMMAND':*^80'}")
                print(f'{menu_selection} is NOT a valid menu selection.')
                print(f"{' Try Again ':-^80}")

        else:
            print("Invalid login details Please try again.")
            continue



