from flask import render_template, jsonify, redirect, url_for, request, flash
from app import app, db
from app.models.post import Post
from app.models.author import Author
from app.forms.post import PostForm
from flask_login import login_required, current_user
from werkzeug.datastructures import MultiDict
from datetime import datetime
import pytz


@app.route('/')
@app.route('/home')
def home():
    the_post = Post.query.order_by(Post.timestamp.desc()).first()
    return render_template('home.html', post=the_post, author=the_post.author, poster=the_post.poster,
                           next_id=None, prev_id=the_post.prev_id())


@app.route('/post/<int:post_id>')
def post(post_id):
    the_post = Post.query.get(post_id)
    return render_template('home.html', post=the_post, author=the_post.author, poster=the_post.poster,
                           next_id=the_post.next_id(), prev_id=the_post.prev_id())


@app.route('/post/<int:post_id>/prev')
def prev_post(post_id):
    the_post = Post.query.filter(Post.id < post_id).order_by(Post.id.desc()).first()
    return jsonify({'post': the_post.as_dict(),
                    'author': the_post.author.as_dict(),
                    'poster': the_post.poster.as_dict(),
                    'next_id': the_post.next_id(),
                    'prev_id': the_post.prev_id()})


@app.route('/post/<int:post_id>/next')
def next_post(post_id):
    the_post = Post.query.filter(Post.id > post_id).order_by(Post.id.asc()).first()
    return jsonify({'post': the_post.as_dict(),
                    'author': the_post.author.as_dict(),
                    'poster': the_post.poster.as_dict(),
                    'next_id': the_post.next_id(),
                    'prev_id': the_post.prev_id()})


@app.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    the_post = Post.query.get(post_id)
    if request.method == 'GET':
        form = PostForm(formdata=MultiDict({
            'title': the_post.title,
            'date_written': the_post.date_written,
            'body': the_post.body,
            'author_display_name': the_post.author.display_name,
            'language': the_post.language
        }))
    else:
        form = PostForm()
    if form.validate_on_submit():
        the_author = Author.get_by_display_name(form.author_display_name.data)
        the_post.author_id = the_author.id
        the_post.title = form.title.data
        the_post.date_written = form.date_written.data
        the_post.body = form.body.data
        the_post.language = form.language.data
        db.session.commit()
        # flash('changes saved to "{}"'.format(form.title.data))
        return redirect(url_for('post', post_id=post_id))
    return render_template('post.html', form=form, post=the_post, author=the_post.author, poster=the_post.poster)


@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    the_post = Post()
    if form.validate_on_submit():
        the_author = Author.get_by_display_name(form.author_display_name.data)
        the_post.author_id = the_author.id
        the_post.title = form.title.data
        the_post.date_written = form.date_written.data
        the_post.body = form.body.data
        the_post.language = form.language.data
        the_post.created_by = current_user.id
        the_post.timestamp = datetime.now(pytz.timezone('Asia/Manila'))
        db.session.add(the_post)
        db.session.commit()
        return redirect(url_for('post', post_id=the_post.id))
    elif request.method == 'GET':
        the_post.title = form.title.data
        the_post.date_written = form.date_written.data
        the_post.body = form.body.data
        the_post.language = form.language.data
    return render_template('post.html', form=form, post=the_post, poster=current_user)
