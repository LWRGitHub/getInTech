from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from wtforms.validators import DataRequired#, Length, Email, EqualTo, ValidationError
# from wtforms.widgets import TextArea


# Crate A Search From
class SearchForm(FlaskForm):
    searched = StringField('Search', validators=[DataRequired()])
    # add Topic data not required
    topic = StringField('Topic')
    platform = StringField('Platform')
    language = StringField('Language')
    sort = StringField('Sort')

    submit = SubmitField('Search')