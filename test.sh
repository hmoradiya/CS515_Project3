#!/bin/sh

set -e # exit immediately if newman complains
trap 'kill $PID' EXIT # kill the server on exit

./run.sh &
PID=$! # record the PID

newman run Forum.postman_collection.json -e env.json # use the env file
# newman run forum_multiple_posts.postman_collection.json -e env.json # use the env file
# newman run forum_post_read_delete.postman_collection.json
newman run search.json
newman run Threaded-replies.postman_collection.json
newman run user.postman_collection.json
newman run fulltext_search.postman_collection.json