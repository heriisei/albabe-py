#3rd party imports
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

#local imports
from app import db, login_manager

class User(UserMixin, db.Model):
    """
    Tabel user
    """

    __tablename__ = 'tb_users'

    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), index=True, unique=True)
    useremail = db.Column(db.String(60), index=True, unique=True)
    nama_depan = db.Column(db.String(60), index=True)
    nama_belakang = db.Column(db.String(60), index=True)
    tgl_lahir = db.Column(db.Date)
    no_hp = db.Column(db.String(15))
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    id_jurusan = db.Column(db.Integer, db.ForeignKey('tb_jurusan.id_jurusan'))
    barang = db.relationship('Barang', backref='barang', lazy='dynamic')

    def get_id(self):
        """
        override get_id -> id dari usermixin
        """
        return (self.id_user)

    @property
    def password(self):
        """
        Mencegah akses ke password
        """
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        """
        Merubah password ke bentuk hashed
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Cek kecocokan password dan hashed
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

# User Loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Barang(db.Model):
    """
    Tabel barang
    """

    __tablename__ = 'tb_barang'

    id_barang = db.Column(db.Integer, primary_key=True)
    nama_barang = db.Column(db.String(60), index=True)
    harga_barang = db.Column(db.Integer, index=True)
    garansi_barang = db.Column(db.Boolean, default=False)
    foto_barang = db.Column(db.String(100), index=True)
    id_user = db.Column(db.Integer, db.ForeignKey('tb_users.id_user'))
    id_jurusan = db.Column(db.Integer, db.ForeignKey('tb_jurusan.id_jurusan'))

    def __repr__(self):
        return '<Barang: {}>'.format(self.nama_barang)

class Fakultas(db.Model):
    """
    Tabel Fakultas
    """

    __tablename__ = 'tb_fakultas'

    id_fakultas = db.Column(db.Integer, primary_key=True)
    nama_fakultas = db.Column(db.String(60), index=True)
    jurusan = db.relationship('Jurusan', backref='fakultas', lazy='dynamic')

    def __repr__(self):
        return '<Fakultas: {}>'.format(self.nama_fakultas)

class Jurusan(db.Model):
    """
    Tabel Jurusan
    """

    __tablename__ = 'tb_jurusan'

    id_jurusan = db.Column(db.Integer, primary_key=True)
    nama_jurusan = db.Column(db.String(60), index=True)
    id_fakultas = db.Column(db.Integer, db.ForeignKey('tb_fakultas.id_fakultas'))
    user = db.relationship('User', backref='jurusan', lazy='dynamic')
    barang = db.relationship('Barang', backref='jurusan', lazy='dynamic')

    def __repr__(self):
        return '<Jurusan: {}>'.format(self.nama_jurusan)
