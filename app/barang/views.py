from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import barang
from forms import FormBarang
from .. import db, photos
from ..models import User, Barang, Jurusan

def check_admin():
    """
    Mencegah non-admin user untuk masuk
    """
    if not current_user.is_admin:
        abort(403)

@barang.route('/barang/details/<idbarang>', methods=['GET', 'POST'])
def detail_barang(idbarang):

    barang = db.session.query(Barang).filter(Barang.id_barang==idbarang)

    return render_template('barang/detail_barang.html', barang=barang, title='Detail Barang')

@barang.route('/jual/jual_barang', methods=['GET', 'POST'])
@login_required
def jual_barang():
    """
    Tambah barang ke database
    """
    jual_barang = True

    form = FormBarang()
    if form.validate_on_submit():
        filename = photos.save(form.fotoBarang.data)
        barang = Barang(nama_barang=form.namaBarang.data,
                        harga_barang=form.hargaBarang.data,
                        garansi_barang=form.garansiBarang.data,
                        foto_barang=photos.url(filename),
                        id_user=current_user.id_user,
                        id_jurusan=current_user.id_jurusan)
        try:
            db.session.add(barang)
            db.session.commit()
            flash('Barang sudah berhasil diposting')
        except:
            flash('Error: Barang gagal diposting')
        # return redirect(url_for('user.list_barang'))

    return render_template('barang/form_barang.html', action="Jual", jual_barang=jual_barang, form=form, title="Jual Barang" )

@barang.route('/barang/edit/<idbarang>', methods=['GET', 'POST'])
@login_required
def edit_barang(idbarang):
    """
    Edit Barang
    """

    jual_barang = False

    barang = db.session.query(Barang).filter(Barang.id_barang==idbarang).first()
    form = FormBarang(obj=barang)
    if form.validate_on_submit():
        barang.nama_barang = form.namaBarang.data
        barang.harga_barang = form.hargaBarang.data
        barang.garansi_barang = form.garansiBarang.data
        filename = photos.save(form.fotoBarang.data)
        barang.foto_barang = photos.url(filename)
        db.session.commit()
        flash('Barang berhasil diedit')

        return redirect(url_for('user.profil', username=current_user.username))

    form.namaBarang.data = barang.nama_barang
    form.hargaBarang.data = barang.harga_barang
    form.garansiBarang.data = barang.garansi_barang
    form.fotoBarang.data = barang.foto_barang
    return render_template('barang/form_barang.html', action="Edit", jual_barang=jual_barang, form=form, barang=barang, title="Edit Barang")

@barang.route('/barang/hapus/<idbarang>', methods=['GET', 'POST'])
@login_required
def hapus_barang(idbarang):
    """
    Hapus barang
    """
    barang = Barang.query.get_or_404(idbarang)
    db.session.delete(barang)
    db.session.commit()
    flash("Barang sudah berhasil dihapus")

    return redirect(url_for('user.list_barang'))

    return render_template(title="Hapus Barang")