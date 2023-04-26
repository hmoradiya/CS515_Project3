import json
from app.extensions import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(150), unique=True)
    msg = db.Column(db.String(150))
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    
    def __str__(self):
        return json.dumps(dict(self))

    def __repr__(self):
        return self.__str__()