# Web Forum

Using Flask to build web forum

Integration with Flask-SQLalchemy

## Installation
Install with pip:

```
$ pip install -r requirements.txt
```

## Database setup
```
$ flask shell
>>> from app.extensions import db
>>> from app.models.post import Post
>>> from app.models.user import User
>>> db.create_all()
```

## A List Extensions added in this assignment
1. User and User Keys
   1. In this extension we can create users and return their id, key, username and realname for the success result.
   2. For error result we are returning 400 and other status code with thier respective message. 
2. Threaded Replies
   1. In this extension we can reply on post by creating post with parent. It will create thread accordingly
3. Date and time based range queries
   1. In this extension we are checking for start time and end time according to given date time range we are taking posts from the database.
4. Thread based range queries
   1. In this extension we are passing any post and get thier full thread in return.
5. Full text search
   1. In this extension we are passing any query that filters or matches on msg of post and return post that are similar to our query.

## Run Flask
```
$ flask run
