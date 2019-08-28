from flask import render_template
from flask import jsonify
from app import app
from app.models.post import Post


@app.route('/')
@app.route('/home')
def home():
    post = Post.query.order_by(Post.timestamp.desc()).first()
    return render_template('home.html', post=post, author=post.author, poster=post.poster)


@app.route('/post/prev/<post_id>')
def prev_post(post_id):
    post = Post.query.filter(Post.id < post_id).order_by(Post.id.desc()).first()
    return jsonify({'post': post.as_dict(),
                    'author': post.author.as_dict(),
                    'poster': post.poster.as_dict()})


@app.route('/post/next/<post_id>')
def next_post(post_id):
    post = Post.query.filter(Post.id > post_id).order_by(Post.id.asc()).first()
    return jsonify({'post': post.as_dict(),
                    'author': post.author.as_dict(),
                    'poster': post.poster.as_dict()})
