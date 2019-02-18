## Agile Group Project

## Design
The project focuses on the following aspects:

## Users:
1) Users come in 3 roles: normal users, moderators, and admins. Normal users can only create new comments, and edit their own comments.
2) Moderators have the added ability to delete comments (to remove trolls), while admins have the ability to edit or delete any comment.
Users can log in and out, and we track when they last logged in


## Comments:
1) Comments are simply a message, a timestamp, and the author.
2) Comments can also be a reply, so we'll store what the parent comment was.

### User

1) Users can be logged in and out.
2) When logging in, set the lastLoggedInAt timestamp. Do not modify this timestamp when logging out
3) Users can only edit their own comments
4) Users cannot delete any comments

## Moderator is a User

1) Moderators can only edit their own comments
2) Moderators can delete any comments

## Admin
1) Admin is both a User and a Moderator
2) Admins can edit any comments
3) Admins can delete any comments
4) Comments contain a reference to the User who created it (author)


### Contributors

1) Alois Mburu
2) Erick Loningo Lomunyak
3) Kelvin Otieno
4) Peter kiarie
5) Arthur Ngondo 
