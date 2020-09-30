from flask import Blueprint

barang = Blueprint('barang', __name__)

from . import views