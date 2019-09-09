from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, HiddenField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('title')
    date_written = StringField('date written')
    body = HiddenField('body', validators=[DataRequired()])
    author_display_name = StringField('author')
    language = StringField('language')
    post_type = StringField('post type')
    submit = SubmitField('save')
