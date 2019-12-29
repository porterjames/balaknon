from app import db
from . import base


class Post(db.Model, base.ModelMixin):
    """a post, usually a poem that has been uploaded to the site"""
    title = db.Column(db.String(256), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    date_written = db.Column(db.String(256), nullable=True)

    def __repr__(self):
        return '<Post id={} ({})>'.format(self.id, self.body_short(10))

    def body_short(self, chars):
        """a short preview of the post body

        args:
            chars (int): maximum number of characters to output
        """
        if len(self.body) < chars:
            return self.body
        return self.body[:chars] + '...'

    def title_short(self, chars):
        """a short preview of the post title

        args:
            chars (int): maximum number of characters to output
        """
        if len(self.title) < chars:
            return self.title
        return self.title[:chars] + '...'

    def _dict_vals(self):
        """create a dictionary representation of the object"""
        return {
            'title': self.title,
            'title_short': self.title_short(60),
            'body': self.body,
            'author_id': self.author_id,
            'language': self.language.as_dict(),
            'country': self.country.as_dict(),
            'date_written': self.date_written
        }

    def next_id(self):
        """get the id of the next post, ordered by IDs"""
        next_post = Post.query.filter(Post.id > self.id).order_by(Post.id.asc()).first()
        return None if next_post is None else next_post.id

    def prev_id(self):
        """get the id of the previous post, ordered by IDs"""
        prev_post = Post.query.filter(Post.id < self.id).order_by(Post.id.desc()).first()
        return None if prev_post is None else prev_post.id
