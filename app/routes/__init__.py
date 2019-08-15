from flask import render_template
from app import app


@app.route('/')
def index():
    user = {'username': 'prtr'}
    return render_template('index.html', user=user)
