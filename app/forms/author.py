from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class AuthorForm(FlaskForm):
    display_name = StringField('display name', validators=[DataRequired()])
    first_name = StringField('first')
    last_name = StringField('last')
    middle_name = StringField('middle')
    birth_year = IntegerField('birth year')
    death_year = IntegerField('death year')
    nasod = StringField('place of birth', validators=[DataRequired()])
    photo = FileField('upload photo', validators=[FileAllowed(['png', 'jpg', 'jpeg', 'gif'],
                                                              'That image type is not supported.')])
    # languages = SelectMultipleField('languages', [(l.id, l.name) for l in Language.query.order_by(Language.name.asc())])
    submit = SubmitField('save')
