""" A mock comments board section. """

import datetime

comments = []
users = []
moderators = []


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
        if comment.author.name == self._name:
            self._can_edit = True
            return self._can_edit

    def can_delete(self, comment):
        """ Checks user's delete privileges over the comment (True/False) """
        if comment.author.name == self._name:
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
    pass

