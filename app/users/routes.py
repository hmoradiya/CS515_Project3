import json
import secrets
from flask import request, jsonify
from app.users import bp
from app.models.user import User
from app.extensions import db
from datetime import datetime

from sqlalchemy import inspect

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}

# Create a new user
@bp.route('', methods=['POST'])
def create_user():
    # check if request body is JSON
    if not request.is_json:
        return jsonify({"error": "Request body must be JSON"}), 400
    
    # get username and realname from request body
    username = request.json.get('username')
    realname = request.json.get('realname')
    
    if not username or not isinstance(username, str):
        return jsonify({"error": "Must have a string-valued username"}), 400

    if User.is_username_taken(username):
        return jsonify({"error": "Username must be unique"}), 400
    
    # generate random key and id
    key = secrets.token_hex(16)
    new_user = User(username=username, realname=realname, key=key)
    db.session.add(new_user)
    db.session.commit()
    user = User.query.get(new_user.id)
    return object_as_dict(user)

@bp.route('/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.get_or_404(user_id)
    return object_as_dict(user)


@bp.route('/update/<key>', methods=['PUT'])
def update_user(key):

    new_username = request.json.get('new_username')
    new_realname = request.json.get('new_realname')

    if not new_username or not isinstance(new_username, str):
        return jsonify({"error": "Must have a string-valued username"}), 400
    
    if User.is_username_taken(new_username):
        return jsonify({"error": "Username must be unique"}), 400
    
    udate_user = User.get_by_key(key)

    udate_user.username = new_username
    udate_user.realname = new_realname

    db.session.commit()
    user = User.query.get(udate_user.id)
    return object_as_dict(user)