from app import db
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime


class ModelMixin(object):
    """a mixin with fields that should be present on all tables, such as timestamp and created by user"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow(), nullable=False)
    modify_timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow(), nullable=False)

    @declared_attr
    def created_by(self):
        """the user who created the entitity"""
        return db.Column(db.Integer, db.ForeignKey('site_user.id'), nullable=False)

    @declared_attr
    def modified_by(self):
        """the user who last modified the entity. on initilization, this should equal created_by"""
        return db.Column(db.Integer, db.ForeignKey('site_user.id'), nullable=False)

    def as_dict(self):
        """represent the object as a dictionary"""
        b = {
            'id': self.id,
            'timestamp': self.timestamp,
            'created_by': self.created_by,
            'modify_timestamp': self.modify_timestamp,
            'modified_by': self.modified_by
        }
        # get specific fields from each model that uses the Mixin
        b.update(self._dict_vals())
        return b

    def _dict_vals(self):
        """each model should override this with any desired fields to include in the dict output"""
        return {}
