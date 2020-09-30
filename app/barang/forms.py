from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, IntegerField, SubmitField, BooleanField, FileField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from .. import db, photos

class FormBarang(FlaskForm):
    """
    Form barang baru / edit
    """
    namaBarang = StringField('Nama Barang', validators=[DataRequired()])
    hargaBarang = IntegerField('Harga Barang', validators=[DataRequired()])
    garansiBarang = BooleanField('Garansi')
    fotoBarang = FileField('Foto Barang', validators=[FileAllowed(photos, 'Hanya upload file gambar!'), FileRequired('Belum ada gambar barang!')])
    submit = SubmitField('Posting')
