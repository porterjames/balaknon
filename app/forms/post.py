from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('title')
    date_written = StringField('date written')
    body = TextAreaField('body', validators=[DataRequired()])
    author_id = IntegerField('author')
    language = StringField('language')
    post_type = StringField('post type')
    submit = SubmitField('save')
