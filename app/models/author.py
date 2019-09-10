from app import db
from datetime import datetime
import pytz


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    display_name = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    middle_name = db.Column(db.String(50), nullable=True)
    pseudonym = db.Column(db.String(128), nullable=True)
    birth_year = db.Column(db.Integer, nullable=True)
    death_year = db.Column(db.Integer, nullable=True)
    nationality = db.Column(db.String(50), nullable=True)
    works = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Author name={}>'.format(self.display_name)

    def as_dict(self):
        return {
            'id': self.id,
            'display_name': self.display_name,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'middle_name': self.middle_name,
            'pseudonym': self.pseudonym,
            'birth_year': self.birth_year,
            'death_year': self.death_year,
            'nationality': self.nationality
        }

    @staticmethod
    def get_by_display_name(p_name):
        return Author.query.filter(Author.display_name == p_name).first_or_404()
