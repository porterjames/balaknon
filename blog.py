from app import app, db
from app.models.blog_user import BlogUser
from app.models.post import Post
from app.models.author import Author


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'BlogUser': BlogUser, 'Post': Post, 'Author': Author}
