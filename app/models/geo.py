from app import db
from . import base


class Language(db.Model, base.ModelMixin):
    """represents the language that a post is written in"""
    name = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(3))
    native_name = db.Column(db.String(50))
    posts = db.relationship('Post', backref='language', lazy='dynamic')

    def __repr__(self):
        return '<Language {}>'.format(self.name)

    def _dict_vals(self):
        """create dictionary representation of the object"""
        return {
            'name': self.name,
            'code': self.code,
            'native_name': self.native_name
        }


class Country(db.Model, base.ModelMixin):
    """represents the country of origin for a given author"""
    name = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(3))
    posts = db.relationship('Post', backref='country', lazy='dynamic')
    authors = db.relationship('Author', backref='country', lazy='dynamic')

    def __repr__(self):
        return '<Country {}>'.format(self.name)

    def _dict_vals(self):
        """create dictionary representation of the object"""
        return {
            'name': self.name,
            'code': self.code
        }
