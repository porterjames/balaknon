from flask import render_template
from flask import jsonify
from app import app
from app.models.post import Post


@app.route('/')
@app.route('/home')
def home():
    first_post = Post.query.order_by(Post.timestamp.desc()).first()
    return render_template('home.html', post=first_post, author=first_post.author, poster=first_post.poster,
                           next_id=None, prev_id=first_post.prev_id())


@app.route('/post/<post_id>')
def post(post_id):
    post = Post.query.get(post_id)
    return render_template('home.html', post=post, author=post.author, poster=post.poster,
                           next_id=post.next_id(), prev_id=post.prev_id())


@app.route('/post/<post_id>/prev')
def prev_post(post_id):
    post = Post.query.filter(Post.id < post_id).order_by(Post.id.desc()).first()
    return jsonify({'post': post.as_dict(),
                    'author': post.author.as_dict(),
                    'poster': post.poster.as_dict(),
                    'next_id': post.next_id(),
                    'prev_id': post.prev_id()})


@app.route('/post/<post_id>/next')
def next_post(post_id):
    post = Post.query.filter(Post.id > post_id).order_by(Post.id.asc()).first()
    return jsonify({'post': post.as_dict(),
                    'author': post.author.as_dict(),
                    'poster': post.poster.as_dict(),
                    'next_id': post.next_id(),
                    'prev_id': post.prev_id()})
