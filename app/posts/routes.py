import json
import secrets
from flask import request, jsonify
from app.posts import bp
from app.models.post import Post
from app.extensions import db
from datetime import datetime

from sqlalchemy import inspect

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


@bp.route('', methods=['GET', 'POST'])
def create_post():
    """Creating Post and Replying to Post
    """
    try:
        if not request.is_json:
            return jsonify({"error": "Request body must be JSON"}), 400
        data = json.loads(request.data)
        msg = data["msg"]
        if not msg:
            return jsonify({"error": "Bad Request"}), 400
        key = secrets.token_hex(16)
        if data.get('parent'):
            parent_id = data.get('parent')
            new_post = Post(msg=msg, key=key, parent_id=parent_id)
        else:
            new_post = Post(msg=msg, key=key)
        db.session.add(new_post)
        db.session.commit()
        post = Post.query.get(new_post.id)
        return object_as_dict(post)
    except KeyError:
        return jsonify({"error": "bad request"}), 400


@bp.route('/<id>', methods=['GET'])
def get_post(id):
    """Get Post By ID

    Args:
        id (int): Integer unique id
    """
    post = Post.query.get(id)
    if not post:
        return jsonify({"error": "Post not found"}), 404
    data = post.to_dict()
    if post.parent:
        data['parent'] = post.parent.id
    if post.replies:
        data['replies'] = [reply.id for reply in post.replies]
    return data


@bp.route('/<id>/delete/<key>', methods=['DELETE'])
def delete_post(id, key):
    """Delete post by ID

    Args:
        id (int): integer id of post
        key (str): unique secreat token hex string
    """
    post = Post.query.filter_by(id=id)
    if not post:
        return jsonify({"error": "Post not found"}), 404
    _ = Post.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({"msg": "post deleted successfully."}), 200


@bp.route('/search', methods=['POST'])
def search_posts():
    """Time based searching on post
    """
    # get start and end timestamps from query parameters
    start_time = request.json.get('start_time')
    end_time = request.json.get('end_time')
    if not end_time:
        return jsonify({"error": "Please provide end time"}), 400
    try:
        if start_time:
            start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        if end_time:
            end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        if start_time and end_time < start_time:
            raise ValueError
    except ValueError:
        return jsonify({"error": "Invalid timestamp format"}), 400

    # search for posts within the given time range
    results = Post.query.filter(Post.timestamp<=end_time, 
                                Post.timestamp>= start_time).all()
    # return list of matching posts
    result_list = [object_as_dict(res) for res in results]
    return jsonify(result_list)


@bp.route('/full_search', methods=['POST'])
def search():
    """Full text search on msg of post
    """
    # get query from query parameters
    query = request.json.get('q')
    if not query:
        return jsonify([])
    results = Post.query.filter(Post.msg.like(f"%{query}%")).all()
    return jsonify([object_as_dict(res) for res in results])


@bp.route('/thread/<id>', methods=['GET'])
def get_threads(id):
    """Thread based range queries API

    Args:
        id (int): integer id of post to get their thread
    """
    post = Post.query.get(id)
    if not post:
        return jsonify({"error": "Post not found"}), 404
    if post.parent:
        parent_id = post.parent.id
        parent_post = Post.query.get(parent_id)
        data = parent_post.to_dict()
        thread_list = [reply.to_dict() for reply in parent_post.replies]
    else:
        data = post.to_dict()
        thread_list = [reply.to_dict() for reply in post.replies]
    thread_list.insert(0, data)
    return thread_list