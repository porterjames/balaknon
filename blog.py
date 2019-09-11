from app import app, db
from app.models.site_user import SiteUser
from app.models.post import Post
from app.models.author import Author
from app.models.geo import Language, Country


@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'SiteUser': SiteUser,
            'Post': Post,
            'Author': Author,
            'Language': Language,
            'Country': Country}
