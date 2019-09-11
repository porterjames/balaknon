from app import db
from sqlalchemy import Table
from . import base
from . import geo


class Author(db.Model, base.ModelMixin):
    display_name = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    middle_name = db.Column(db.String(50), nullable=True)
    birth_year = db.Column(db.Integer, nullable=True)
    death_year = db.Column(db.Integer, nullable=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    works = db.relationship('Post', backref='author', lazy='dynamic')
    languages = db.relationship('Language', secondary='author_language', backref='authors')

    def __repr__(self):
        return '<Author name={}>'.format(self.display_name)

    def as_dict(self):
        return self.base_dict().update({
            'display_name': self.display_name,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'middle_name': self.middle_name,
            'birth_year': self.birth_year,
            'death_year': self.death_year,
            'country': self.country.as_dict()
        })

    @staticmethod
    def get_by_display_name(p_name):
        return Author.query.filter(Author.display_name == p_name).first_or_404()


author_language = Table('author_language', db.Model.metadata,
                        db.Column('author_id', db.Integer, db.ForeignKey(Author.id)),
                        db.Column('language_id', db.Integer, db.ForeignKey(geo.Language.id)))
