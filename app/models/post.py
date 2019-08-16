from app import db
from datetime import datetime
import pytz


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(2000), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now(pytz.timezone('Asia/Manila')), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('blog_user.id'), nullable=False)

    def __repr__(self):
        return '<Post id={} ({})>'.format(self.id, self.body_short(10))

    def body_short(self, chars):
        if len(self.body) < chars:
            return self.body
        return self.body[:chars] + '...'
