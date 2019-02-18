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
    pass
