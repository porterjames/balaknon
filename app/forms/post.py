from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, HiddenField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    date_written = StringField('date written')
    body = HiddenField('body', validators=[DataRequired()])
    author_display_name = StringField('author')
    language = StringField('language')
    country = StringField('country')
    post_type = StringField('post type')
    submit = SubmitField('save')
