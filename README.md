Hardik Moradiya hmoradiy@stevens.edu Prashanth Pulikonda ppulikon1@stevens.edu

**URL of GitHub repo** https://github.com/hmoradiya/CS515_Project3

**hr. to complate project** 45hr

**Description of testing**

For testing, first of all use below comand to complate basic instalation.

We have used Flask to build web forum and Integration with Flask-SQLalchemy

Step 1: We need Install with pip
>>> pip install -r requirements.txt

step 2: In the next step we going to setup Database, We used SQL lite Database.
Follow the step one by one, which is mentioned below,
>>> from app.extensions import db

>>> from app.models.post import Post

>>> from app.models.user import User

>>> db.create_all()

step 3: After complate these two steps, we run our server using the below comand,
flask run

A Basic API tested commands
1. Create Simple Post:
   1. Route: /post
      1. It is used to create post and for success we are returning id, msg, timestamp, key, parents and replies with status 200.

      --> Ubuntu: 
      >>> curl -X POST -H "Content-type: application/json" -d "{\"msg\" : \"Hardik\"}" "localhost:5000/post"
      
      --> Windows: 
      >>> Invoke-WebRequest -Method POST -Uri "http://localhost:5000/post" -Headers @{"Content-Type"="application/json"} -Body '{"msg" : "post"}'

      2. If request is not valid json or there no msg present in request params than it will return error bad request with status 400.

2. Get Post:
   1. Route: /post/<post-id>
      1. It is used to get post by it's id. for success response we return id, msg, timestamp, key, parents and replies with status 200.

      --> Ubuntu: 
      >>> curl -v http://localhost:5000/post/2

      --> Windows: 
      >>> Invoke-WebRequest -Method GET -Uri "http://localhost:5000/post/2" -Verbose

      2. If no post found for that particular id than it will return error Post not found with status 404.

3. Delete Post:
   1. Route: /post/<post-id>/delete/<post-key>
      1. It is used to delete post by it's id. for success response msg post deleted successfully with status 200.

      --> Ubuntu: 
      >>> curl -X DELETE http://localhost:5000/post/1/delete/<post-key>

      --> Windows: 
      >>> Invoke-WebRequest -Method DELETE -Uri "http://localhost:5000/post/2/delete/<post:key>" -Verbose

      2. If no post found for that particular id than it will return error Post not found with status 404.

-> For baseline we test our codes with,
1. forum_multiple_posts.postmane_collection.json
2. forum_post_read_delete.postman_collection.json

-> For each Extention we test our code with diffrent postman collection, which is listed below,
1. User and User Keys -> user.postman_collection.json
2. Threaded Replies -> Threaded-replies.postman_collection.json
3. Full text search -> fulltext_search.postman_collection.json
4. search.json


**Bugs or Issues - not resolve**

No

**Difficult issue or bug and how you resolved**

NO

**List of 5 extensions which are we used in this project**
1. User and User Keys
2. Threaded Replies
3. Date and time based range queries
4. Thread based range queries
5. Full text search

**Detailed summaries of our tests for each of your extensions**

1. User and User Keys
   1. Route: /user
      1. It is used to create new user. for success we are returning id, username, realname, key, timestamp with status 200.

      --> Ubuntu: 
      >>> curl -X POST -H "Content-type: application/json" -d "{\"username\" : \"hardik612\", \"realname\" : \"hardik612\"}" "localhost:5000/user"

      --> Windows: 
      >>> Invoke-WebRequest -Method POST -Uri "http://localhost:5000/user" -Headers @{"Content-Type"="application/json"} -Body '{"username":"hardik612", "realname":"hardik612"}'
      
      2. If request is not valid json or username already exists than it will return error bad request with status 400.

   2. Route: /user/<user-id>
      1. It is used to get user by it's id. for success we are returning id, username, realname, key, timestamp with status 200.

      --> Ubuntu: 
      >>> curl -v http://localhost:5000/user/1

      --> Windows: 
      >>> Invoke-WebRequest -Method GET -Uri "http://127.0.0.1:5000/user/1" -Verbose

      2. If no user found for that id we are returning 404 error.

   3. Route: /user/update/<user-key>
      1. It is used to update user based on user key and for success we are returning id, username, realname, key, timestamp with status 200.

      --> Ubuntu: 
      >>> curl -X PUT -H "Content-type: application/json" -d "{\"new_username\" : \"hardik1007\", \"new_realname\" : \"hardik\"}" "localhost:5000/user/update/f501d15eb52e870908b04efcda316cb7"

      --> Windows: 
      >>> Invoke-WebRequest -Method PUT -Uri "http://localhost:5000/user/update/f501d15eb52e870908b04efcda316cb7" -Headers @{"Content-Type"="application/json"} -Body '{"new_username":"hardik1007", "new_realname":"hardik"}'

      2. If request is not valid json or username already exists than it will return error bad request with status 400.

2. Threaded Replies
   1. Route: /post/<post-id>
      1. It is used to get post by it's id. for success response we return id, msg, timestamp, key, parents and replies with status 200.

      --> Ubuntu: 
      >>> curl -X POST -H "Content-type: application/json" -d "{\"msg\" : \"Moradiya\", \"parent\" : 1}" "localhost:5000/post"

      --> Windows: 
      >>> Invoke-WebRequest -Method POST -Uri "http://localhost:5000/post" -Headers @{"Content-Type"="application/json"} -Body '{"msg":"Moradiya", "parent":1}'

      2. If no post found for that particular id than it will return error Post not found with status 404.
   
3. Date and time based range queries
   1. Route: /post/search
      1. For success response we are returning list of matching posts.

      --> Ubuntu: 
      >>> curl -X POST -H "Content-type: application/json" -d "{\"start_time\" : \"2023-04-29 00:00:00\", \"end_time\" : \"2023-04-29 19:19:00\"}" "localhost:5000/post/search"
      
      --> Windows: 
      >>> Invoke-WebRequest -Method POST -Uri "http://localhost:5000/post/search" -Headers @{"Content-Type"="application/json"} -Body '{"start_time":"2023-04-29 00:00:00", "end_time":"2023-04-29 19:19:00"}'

      2. To tell wheather it is valid start time and end time, if the start time is after the end time it raise an error, if the user didn't provide the time, it raise an error.
   
4. Thread based range queries
   1. Route: /post/thread/<post-id>
      1. For success response it will give full thread (list of all posts in that thread) with status 200.
      
      --> Ubuntu: 
      >>> List of thread post for a post: curl -v http://localhost:5000/post/thread/2

      --> Windows: 
      >>> Invoke-WebRequest -Method GET -Uri "http://localhost:5000/post/thread/2" -Verbose

      2. If there is no post with that particular id than it will return Post not found with status 400.
   
5. Full text search
   1. Route: /post/full_search
      1. It searches the message by text, if a message include the text, than that post will be returned. We expect the result code is 200 and the return list is correct.

      --> Ubuntu: 
      >>> curl -X POST -H "Content-type: application/json" -d "{\"q\" : \"Hardik\"}" "localhost:5000/post/full_search"
      
      --> Windows: 
      >>> Invoke-WebRequest -Method POST -Uri "http://localhost:5000/post/full_search" -Headers @{"Content-Type"="application/json"} -Body '{"q":"Hardik"}'

      2. If no matching post found than we are returning empty list.