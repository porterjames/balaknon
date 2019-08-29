from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class BlogUser(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    posts = db.relationship('Post', backref='poster', lazy='dynamic')

    def __repr__(self):
        return '<BlogUser {}>'.format(self.username)

    def set_password(self, password):
        """save hashed password"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """check given password against stored hash"""
        return check_password_hash(self.password_hash, password)

    def as_dict(self):
        return {
            'id': self.id,
            'username': self.username
        }


@login.user_loader
def load_user(p_id):
    return BlogUser.query.get(int(p_id))
