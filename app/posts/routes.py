import json
from uuid import uuid4
from flask import Flask, request, jsonify
from app.posts import bp
from app.models.post import Post
from app.extensions import db

from sqlalchemy import inspect

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}

@bp.route('', methods=['GET', 'POST'])
def create_post():
    try:
        unique_id = str(uuid4())
        data = json.loads(request.data)
        msg = data["msg"]
        if not msg:
            return jsonify({"msg": "bad request", "status": 400})
        new_post = Post(msg=msg, key=unique_id)
        db.session.add(new_post)
        db.session.commit()
        post = Post.query.get(new_post.id)
        return object_as_dict(post)
    except KeyError:
        return jsonify({"msg": "bad request", "status": 400})

@bp.route('/<id>', methods=['GET'])
def get_post(id):
    post = Post.query.get(id)
    if not post:
        return jsonify({"msg": "Post not found", "status": 404})
    return object_as_dict(post)

@bp.route('/<id>/delete/<key>', methods=['DELETE'])
def delete_post(id, key):
    post = Post.query.filter_by(id=id)
    if not post:
        return jsonify({"msg": "Post not found", "status": 404})
    _ = Post.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({"msg": "post deleted successfully.", "status": 200})