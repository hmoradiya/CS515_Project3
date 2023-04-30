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

## A Basic API commands
1. Create Simple Post:
   1. Ubuntu: curl -X POST -H "Content-type: application/json" -d "{\"msg\" : \"Hardik\"}" "localhost:5000/post"
   2. Windows: Invoke-WebRequest -Method POST -Uri "http://localhost:5000/post" -Headers @{"Content-Type"="application/json"} -Body '{"msg" : "post"}'

2. Get Post:
   1. Ubuntu: curl -v http://localhost:5000/post/2
   2. Windows: Invoke-WebRequest -Method GET -Uri "http://localhost:5000/post/2" -Verbose

3. Delete Post:
   1. Ubuntu: curl -X DELETE http://localhost:5000/post/1/delete/<post-key>
   2. Windows: Invoke-WebRequest -Method DELETE -Uri "http://localhost:5000/post/2/delete/<post:key>" -Verbose


## A List Extensions added in this assignment
1. User and User Keys
   1. In this extension we can create users and return their id, key, username and realname for the success result.
   2. For error result we are returning 400 and other status code with thier respective message. 
   3. Commands:
      1. Ubuntu:
         1. Create User: curl -X POST -H "Content-type: application/json" -d "{\"username\" : \"hardik07\", \"realname\" : \"hardik\"}" "localhost:5000/user"
         2. Get User: curl -v http://localhost:5000/user/1
   
      2. Windows:
         1. Create User: Invoke-WebRequest -Method POST -Uri "http://localhost:5000/user" -Headers @{"Content-Type"="application/json"} -Body '{"username":"hardik07", "realname":"hardik"}'
         2. Get User: Invoke-WebRequest -Method GET -Uri "http://127.0.0.1:5000/user/1" -Verbose

2. Threaded Replies
   1. In this extension we can reply on post by creating post with parent. It will create thread accordingly
   2. Commands:
      1. Ubuntu:
         1. Create Thread Post: curl -X POST -H "Content-type: application/json" -d "{\"msg\" : \"Moradiya\", \"parent\" : 1}" "localhost:5000/post"
      2. Windows:
         1. Create Thread Post: Invoke-WebRequest -Method POST -Uri "http://localhost:5000/post" -Headers @{"Content-Type"="application/json"} -Body '{"msg":"Moradiya", "parent":1}'
   
3. Date and time based range queries
   1. In this extension we are checking for start time and end time according to given date time range we are taking posts from the database.
   2. Commands:
      1. Ubuntu:
         1. curl -X POST -H "Content-type: application/json" -d "{\"start_time\" : \"2023-04-29 00:00:00\", \"end_time\" : \"2023-04-29 19:19:00\"}" "localhost:5000/post/search"
      2. Windows:
         1. Invoke-WebRequest -Method POST -Uri "http://localhost:5000/post/search" -Headers @{"Content-Type"="application/json"} -Body '{"start_time":"2023-04-29 00:00:00", "end_time":"2023-04-29 19:19:00"}'
   
4. Thread based range queries
   1. In this extension we are passing any post and get thier full thread in return.
   2. Commands:
      1. Ubuntu: List of thread post for a post: curl -v http://localhost:5000/post/thread/2
      2. Windows: Invoke-WebRequest -Method GET -Uri "http://localhost:5000/post/thread/2" -Verbose
   
5. Full text search
   1. In this extension we are passing any query that filters or matches on msg of post and return post that are similar to our query.
   2. Commnads:
      1. Ubuntu: curl -X POST -H "Content-type: application/json" -d "{\"q\" : \"Hardik\"}" "localhost:5000/post/full_search"
      2. Windows: Invoke-WebRequest -Method POST -Uri "http://localhost:5000/post/full_search" -Headers @{"Content-Type"="application/json"} -Body '{"q":"Hardik"}'

## Run Flask
```
$ flask run
