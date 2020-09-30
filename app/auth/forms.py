from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, IntegerField, ValidationError, SelectField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms.fields.html5 import DateField

from ..models import User

class MySelectField(SelectField):
    def pre_validate(self, form):
        pass

class RegistrationForm(FlaskForm):
    """
    Register akun baru
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=60)])
    nama_depan = StringField('Nama Depan', validators=[DataRequired(), Length(max=60)])
    nama_belakang = StringField('Nama Belakang', validators=[DataRequired(), Length(max=60)])
    no_hp = IntegerField('Nomor HP', validators=[DataRequired()])
    fakultas = MySelectField('Fakultas', choices=[], validators=[DataRequired()], coerce=int)
    jurusan = MySelectField('Jurusan', choices=[], validators=[DataRequired()], coerce=int)
    tgl_lahir = DateField('Tanggal Lahir', format='%Y-%m-%d', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Konfirmasi Password', validators=[EqualTo('password')])
    submit = SubmitField('Buat Akun')

    def validate_email(self, field):
        if User.query.filter_by(useremail=field.data).first():
            raise ValidationError('Email sudah digunakan')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username sudah digunakan')

class LoginForm(FlaskForm):
    """
    Login User
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Masuk')