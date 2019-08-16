import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'vm9erER393#931d!!e3'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'postgresql://postgres:admin@localhost:5432/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
