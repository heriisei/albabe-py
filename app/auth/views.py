from flask import flash, redirect, render_template, url_for, jsonify
from flask_login import login_required, login_user, logout_user, current_user

from . import auth
from forms import LoginForm, RegistrationForm
from .. import db
from ..models import User, Fakultas, Jurusan

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Menangani request route /register
    Menambah user ke database melalui from registerasi
    """
    form = RegistrationForm()
    form.fakultas.choices = [(fakultas.id_fakultas, fakultas.nama_fakultas) for fakultas in Fakultas.query.all()]
    form.jurusan.choices = [(jurusan.id_jurusan, jurusan.nama_jurusan) for jurusan in Jurusan.query.filter_by(id_fakultas=1).all()]

    if form.validate_on_submit():
        user = User(useremail=form.email.data,
                    username=form.username.data,
                    nama_depan=form.nama_depan.data,
                    nama_belakang=form.nama_belakang.data,
                    tgl_lahir=form.tgl_lahir.data,
                    no_hp=form.no_hp.data,
                    id_jurusan=form.jurusan.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Akun kamu berhasil dibuat, silakan login')

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form, title='Register')

@auth.route('/jurusan/<idfakultas>')
def jurusan(idfakultas):
    jurusanList = Jurusan.query.filter_by(id_fakultas=idfakultas).all()

    jurusanArray = []

    for jurusan in jurusanList:
        jurusanObj = {}
        jurusanObj['id_jurusan'] = jurusan.id_jurusan
        jurusanObj['nama_jurusan'] = jurusan.nama_jurusan
        jurusanArray.append(jurusanObj)

    return jsonify({'jurusan' : jurusanArray})

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        #cek apakah user terdaftar dan mencocokkan password
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            #user dapat login
            login_user(user)

            #redirect ke profil setelah login
            if user.is_admin:
                return redirect(url_for('admin.dashboard'))
            else:
                return redirect(url_for('user.profil', u=current_user.username))

        #apabila form login tidak sesuai
        else:
            flash('Username atau Password salah')

    #load template login
    return render_template('auth/login.html', form=form, title='Masuk')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Kamu berhasil keluar')

    return redirect(url_for('auth.login'))