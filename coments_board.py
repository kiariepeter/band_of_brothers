""" A mock comments board section. """

import datetime

comments = []
users = []
moderators = []


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
        #here we initialize the isAdmin to true
        self.is_admin = 1
        self.name = name

    def can_delete(self, comment):
        """ Checks user's delete privileges over the comment (True/False) """
        #here we check
        if self.isAdmin == 1:
            return True
        return False


    def can_edit(self,comment):
        """ Checks user's edit privileges over the comment (True/False) """
        if self.isAdmin == 1:
            return True
        return False




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
    pass

