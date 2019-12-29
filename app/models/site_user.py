from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import post


class SiteUser(UserMixin, db.Model):
    """a user of the site, capable of uploading/editing posts"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    posts = db.relationship('Post', backref='poster', lazy='dynamic', foreign_keys=post.Post.created_by)

    def __repr__(self):
        return '<BlogUser {}>'.format(self.username)

    def set_password(self, password):
        """save the user's hashed password

        Args:
            password (string): the user's raw password"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """check the given password against stored hash

        Args:
            password (string): the provided password, in raw format

        Return:
            true if the password matches, otherwise false"""
        return check_password_hash(self.password_hash, password)

    def as_dict(self):
        """create a dictionary representation of the object"""
        return {
            'id': self.id,
            'username': self.username
        }


@login.user_loader
def load_user(p_id):
    """returns the SiteUser object corresponding to the id of the authenticated user"""
    return SiteUser.query.get(int(p_id))
