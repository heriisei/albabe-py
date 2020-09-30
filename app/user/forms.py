from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField, BooleanField
from wtforms.validators import DataRequired

class EditProfilForm(FlaskForm):
    """
    Form edit profil
    """
    username = StringField('Username', validators=[DataRequired()])
    namaDepan = StringField('Nama Depan', validators=[DataRequired()])
    namaBelakang = StringField('Nama Belakang', validators=[DataRequired()])
    noHp = IntegerField('Nomor HP', validators=[DataRequired()])
    tglLahir = DateField('Tanggal Lahir', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Simpan Profil')