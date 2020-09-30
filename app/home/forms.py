from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired

from .. import db

class FilterBarang(FlaskForm):
    Jurusan = SelectField(choices=[])