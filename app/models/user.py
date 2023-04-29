import json
from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    realname = db.Column(db.String(50), nullable=False, unique=True)
    key = db.Column(db.String(150), unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __str__(self):
        return json.dumps(dict(self))

    def __repr__(self):
        return self.__str__()
    
    @classmethod
    def is_username_taken(cls, username):
        return cls.query.filter_by(username=username).first() is not None
    
    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_by_key(cls, key):
        return cls.query.filter_by(key=key).first()

