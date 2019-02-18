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
    def __init__(self, user_id, name, is_admin=3):
        self._user_id = user_id
        self._name = name
        self._logged_in = False
        self._logged_in_date = None
        self._can_edit = None
        self._can_delete = None
        self._is_admin = is_admin
        

    @property
    def name(self):
        """ Getter - Returns username """
        return self._name


    @name.setter
    def name(self, value):
        """ Sets the username """
        self._name = value

    @property
    def user_id(self):
        """ Getter - Returns user_id """
        return self._user_id


    @user_id.setter
    def user_id(self, value):
        """ Sets the user_id """
        self._user_id = value

    @property
    def is_admin(self):
        """ Getter - Returns is_admin """
        return self._is_admin


    @is_admin.setter
    def is_admin(self, value):
        """ Sets the is_admin """
        self._is_admin = value

    def is_logged_in(self):
        """ Returns the login status - True/False """
        return self._logged_in

    def last_logged_in_at(self):
        """ Returns the timestamp for the last time a user logged in. """
        return self._logged_in_date

    def log_in(self):
        """ Logs in  a user."""
        self._logged_in = True
        self._logged_in_date = datetime.datetime.now()
        return self._logged_in


    def log_out(self):
        self._logged_in = False
        return self._logged_in

    def can_edit(self, comment):
        """ Checks user's edit privileges over the comment (True/False) """
        if comment.author.user_id == self._user_id:
            self._can_edit = True
            return self._can_edit

    def can_delete(self, comment):
        """ Checks user's delete privileges over the comment (True/False) """
        if comment.author.user_id == self._user_id:
            self._can_delete = True
            return self._can_delete


    def __repr__(self):
        """ String output to stdout """
        pass


class moderator(user):
    """ Holds methods for moderator users

        Moderators can perform all operations of a normal user.
        Moderators can delete comments (remove trolls).
    """

    def __init__(self, name):
        self.is_moderator = True
        self.name = name

    def can_edit(self, comment):
        """ Checks user's edit privileges over the comment (True/False) """
        if self.comment.author_id == self.user_id:
            self.edit_comment = True
            return self.edit_comment
    def can_delete(self, comment):
        """ Checks user's delete privileges over the comment (True/False) """
        if self.is_admin == 2:
            return True
        return False

class admin(moderator):
    """ Holds methods for Administrator users

        Admins can perform all operations of a normal user and moderator.
        Admins can edit and or delete any comment
    """

    def __init__(self, name):
        #here we initialize the isAdmin to true 
        self.is_admin = 1
        self.name = name

    def can_delete(self, comment):
        """ Checks user's delete privileges over the comment (True/False) """
        #here we check if user is admin
        if self.is_admin == 1:
            return True
        return False


    def can_edit(self,comment):
        """ Checks user's edit privileges over the comment (True/False)  """
        if self.is_admin == 1:
            return True
        return False




class Comment:
    """ Holds methods for comments

        A comment is a message, a timestamp and the author.
        A comment can be a reply (which tracks the parent comment).
    """

    def __init__(self, _author, _message, _replied_to=None):
        self._author = _author
        self._message = _message
        self._replied_to = _replied_to

    @author.getter
    def author(self):
        """ Returns author of comment """
        return self._author

    @author.setter
    def author(self, value):
        """ Sets the comment's author's name """
        self._author = value

    @message.getter
    def message(self):
        """ Returns the comment's message body """
        return self._message

    @message.setter
    def message(self, value):
        """ Sets the comment's message body """
        self._message = value

    def created_at(self):
        """ Returns the comment's creation timestamp """
        return datetime.datetime.now()

    @replied_to.getter
    def replied_to(self):
        """ Returns the Parent comment being replied to """
        return self._replied_to

    @replied_to.setter
    def replied_to(self, value):
        """ Sets the Parent comment being replied to """
        self._replied_to = value

    def __repr__(self):
        if self.replied_to:
            return "author : " + self.author + ", message " + self.message + ", replied to " + self.replied_to
        else:
            return "author : " + self.author + ", message " + self.message


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
            print('\t 0 - exit')
            print('=' * 80)
            menu_selection = input('Enter a selection [0-6]: ')


            if menu_selection == 1:
                pass

            elif menu_selection == 2:
                pass

            elif menu_selection == 3:
                pass

            elif menu_selection == '0': # Exit
                print(f"{' Good-Bye ':*^80}")
                loop = False # Terminate program

            else:
                print(f"{'UNRECOGNIZED COMMAND':*^80}")
                print(f'{menu_selection} is NOT a valid menu selection.')
                print(f"{' Try Again ':-^80}")

        else:
            print("Invalid login details Please try again.")





