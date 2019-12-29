from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Optional


class AuthorForm(FlaskForm):
    """form for author biographical details"""
    display_name = StringField('display name', validators=[DataRequired()])
    first_name = StringField('first', validators=[Optional()])
    last_name = StringField('last', validators=[Optional()])
    middle_name = StringField('middle', validators=[Optional()])
    birth_year = IntegerField('birth year', validators=[Optional()])
    death_year = IntegerField('death year', validators=[Optional()])
    nasod = StringField('place of birth', validators=[DataRequired()])
    photo = FileField('upload photo', validators=[FileAllowed(['png', 'jpg', 'jpeg', 'gif'],
                                                              'That image type is not supported.')])
    submit = SubmitField('save')
