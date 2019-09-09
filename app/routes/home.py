from flask import render_template, jsonify, redirect, url_for, request, flash
from app import app, db
from app.models.post import Post
from app.models.author import Author
from app.forms.post import PostForm
from flask_login import login_required
from werkzeug.datastructures import MultiDict


@app.route('/')
@app.route('/home')
def home():
    first_post = Post.query.order_by(Post.timestamp.desc()).first()
    return render_template('home.html', post=first_post, author=first_post.author, poster=first_post.poster,
                           next_id=None, prev_id=first_post.prev_id())


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
            'author_display_name': the_post.author.display_name
        }))
    else:
        form = PostForm()
    if form.validate_on_submit():
        the_author = Author.query.filter(Author.display_name == form.author_display_name.data).first_or_404()
        the_post.author_id = the_author.id
        the_post.title = form.title.data
        the_post.date_written = form.date_written.data
        the_post.body = form.body.data
        db.session.commit()
        # flash('changes saved to "{}"'.format(form.title.data))
        return redirect(url_for('post', post_id=post_id))
    return render_template('post.html', form=form, post=the_post, author=the_post.author, poster=the_post.poster)
