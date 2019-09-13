from flask import render_template, jsonify, send_from_directory, request, redirect, url_for
from flask_login import login_required, current_user
from os import path
from datetime import datetime
from werkzeug.utils import secure_filename

from app.models.author import Author
from app.models.geo import Country, Language
from app.models.post import Post
from app.forms.author import AuthorForm
from app import app, db


ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']


def allowed_image_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def validate_author_on_submit(the_author, form):
    the_author.display_name = form.display_name.data
    the_author.first_name = form.first_name.data
    the_author.last_name = form.last_name.data
    the_author.middle_name = form.middle_name.data
    the_author.birth_year = form.birth_year.data
    the_author.death_year = form.death_year.data
    the_country = Country.query.filter(Country.name == form.nasod.data).first_or_404()
    the_author.country_id = the_country.id
    the_author.modified_by = current_user.id
    the_author.modify_timestamp = datetime.utcnow()
    the_photo = form.photo.data
    if the_photo is not None:
        if allowed_image_file(the_photo.filename):
            the_author.photo_path = secure_filename(the_photo.filename)
            the_photo.save(path.join(app.config['UPLOAD_FOLDER'], 'author', the_author.photo_path))
        else:
            form.photo.errors.append('Photo has invalid file extension.')
            render_template('author_edit.html', form=form, author=the_author.as_dict())
    db.session.commit()
    return redirect(url_for('author', author_id=the_author.id))


@app.route('/author')
def author_list():
    authors = Author.query.order_by(Author.last_name.asc(), Author.first_name.asc(), Author.display_name.asc()).all()
    return render_template('author_list.html', authors=authors)


@app.route('/author/<int:author_id>')
def author(author_id):
    the_author = Author.query.get(author_id)
    languages = [l.as_dict() for l in the_author.languages]
    works = [p.as_dict() for p in Post.query.filter(Post.author_id==the_author.id).order_by(Post.id.asc())]
    return render_template('author.html', author=the_author.as_dict(), languages=languages, works=works)


@app.route('/author/new', methods=['GET', 'POST'])
@login_required
def new_author():
    # to do
    return render_template('author_edit.html')


@app.route('/author/<int:author_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_author(author_id):
    the_author = Author.query.get(author_id)
    form = AuthorForm()
    if request.method == 'GET':
        form.display_name.data = the_author.display_name
        form.first_name.data = the_author.first_name
        form.last_name.data = the_author.last_name
        form.middle_name.data = the_author.middle_name
        form.nasod.data = the_author.country.name
        form.birth_year.data = the_author.birth_year
        form.death_year.data = the_author.death_year
    if form.validate_on_submit():
        validate_author_on_submit(the_author, form)
    return render_template('author_edit.html', form=form, author=the_author.as_dict())


@app.route('/author/autocomplete')
@login_required
def autocomplete_author():
    author_names = [a.display_name for a in Author.query.all()]
    return jsonify(author_names=author_names)


@app.route('/author/<int:author_id>/photo')
def author_photo(author_id):
    the_author = Author.query.get(author_id)
    if the_author.photo_path is None:
        return None
    return send_from_directory(path.join(app.config['UPLOAD_FOLDER'], 'author'), the_author.photo_path)
