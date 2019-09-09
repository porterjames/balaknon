from flask import render_template, jsonify
from flask_login import login_required
from app.models.author import Author
from app import app


@app.route('/author')
def author_list():
    authors = Author.query.order_by(Author.last_name.asc(), Author.first_name.asc(), Author.display_name.asc()).all()
    return render_template('author_list.html', authors=authors)


@app.route('/author/<int:author_id>')
def author(author_id):
    the_author = Author.query.get(author_id)
    return render_template('author.html', author=the_author)


@app.route('/author/new', methods=['GET', 'POST'])
@login_required
def new_author():
    # to do
    return render_template('author.html')


@app.route('/author/<int:author_id>/edit')
@login_required
def edit_author():
    # to do
    return render_template('author.html')


@app.route('/author/autocomplete')
@login_required
def autocomplete_author():
    author_names = [a.display_name for a in Author.query.all()]
    return jsonify(author_names=author_names)

