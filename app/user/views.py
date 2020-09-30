from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import user
from forms import EditProfilForm
from .. import db
from ..models import Barang, User


@user.route('/profil')
@login_required
def profil():
    """
    Profil User
    """
    #query barang jualan si user
    jualan = db.session.query(Barang).filter(Barang.id_user==current_user.id_user).all()
    return render_template('user/profil.html', jualan=jualan, title='Profil')

@user.route('/profil/edit/<user>', methods=['GET', 'POST'])
@login_required
def edit_profil(user):
    """
    Edit Profil
    """
    user = db.session.query(User).filter(User.username==user).first()
    form = EditProfilForm(obj=user)
    if form.validate_on_submit():
        user.username=form.username.data,
        user.nama_depan=form.namaDepan.data,
        user.nama_belakang=form.namaBelakang.data,
        user.tgl_lahir=form.tglLahir.data,
        user.no_hp=form.noHp.data,
        db.session.commit()
        flash('Profil berhasil diedit')

        return redirect(url_for('user.profil', username=current_user.username))

    form.username.data=user.username
    form.namaDepan.data=user.nama_depan
    form.namaBelakang.data=user.nama_belakang
    form.tglLahir.data=user.tgl_lahir
    form.noHp.data=user.no_hp
    return render_template('user/edit_profil.html', action="Edit", form=form, user=user, title="Edit Profil")

