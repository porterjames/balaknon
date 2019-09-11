from app import db
from . import base


class Post(db.Model, base.ModelMixin):
    title = db.Column(db.String(256), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    date_written = db.Column(db.String(256), nullable=True)

    def __repr__(self):
        return '<Post id={} ({})>'.format(self.id, self.body_short(10))

    def body_short(self, chars):
        if len(self.body) < chars:
            return self.body
        return self.body[:chars] + '...'

    def _dict_vals(self):
        return {
            'title': self.title,
            'body': self.body,
            'author_id': self.author_id,
            'language': self.language.as_dict(),
            'country': self.country.as_dict(),
            'date_written': self.date_written
        }

    def next_id(self):
        next_post = Post.query.filter(Post.id > self.id).order_by(Post.id.asc()).first()
        return None if next_post is None else next_post.id

    def prev_id(self):
        prev_post = Post.query.filter(Post.id < self.id).order_by(Post.id.desc()).first()
        return None if prev_post is None else prev_post.id
