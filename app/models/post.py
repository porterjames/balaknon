from app import db
from datetime import datetime
import pytz


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=True)
    date_written = db.Column(db.String(256), nullable=True)
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now(pytz.timezone('Asia/Manila')), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('blog_user.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    language = db.Column(db.String(40), nullable=False, default='English')
    post_type = db.Column(db.String(40), nullable=False, default='poem')

    def __repr__(self):
        return '<Post id={} ({})>'.format(self.id, self.body_short(10))

    def body_short(self, chars):
        if len(self.body) < chars:
            return self.body
        return self.body[:chars] + '...'

    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'date_written': self.date_written,
            'body': self.body,
            'timestamp': self.timestamp,
            'created_by': self.created_by,
            'author_id': self.author_id
        }
