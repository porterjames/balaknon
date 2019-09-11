from app import db
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime


class ModelMixin(object):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow(), nullable=False)
    modify_timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow(), nullable=False)

    @declared_attr
    def created_by(self):
        return db.Column(db.Integer, db.ForeignKey('site_user.id'), nullable=False)

    @declared_attr
    def modified_by(self):
        return db.Column(db.Integer, db.ForeignKey('site_user.id'), nullable=False)

    def as_dict(self):
        b = {
            'id': self.id,
            'timestamp': self.timestamp,
            'created_by': self.created_by,
            'modify_timestamp': self.modify_timestamp,
            'modified_by': self.modified_by
        }
        b.update(self._dict_vals())
        return b

    def _dict_vals(self):
        return {}
