from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired#, Length, Email, EqualTo, ValidationError
# from wtforms.widgets import TextArea


# Crate A Search From
class SearchForm(FlaskForm):
    searched = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')