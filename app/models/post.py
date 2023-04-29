import json
from app.extensions import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(150), unique=True)
    msg = db.Column(db.String(150))
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    parent_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=True)
    parent = db.relationship('Post', remote_side=[id], backref='replies')


    
    def __str__(self):
        return json.dumps(dict(self))

    def __repr__(self):
        return self.__str__()
    
    def to_dict(self):
        data = {
            'id': self.id,
            'msg': self.msg,
            'key': self.key,
            'timestamp': self.timestamp
        }
        if self.parent:
            data['parent_id'] = self.parent.id
        if self.replies:
            data['replies'] = [reply.id for reply in self.replies]
        return data
