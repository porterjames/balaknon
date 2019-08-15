import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'vm9erER393#931d!!e3'
