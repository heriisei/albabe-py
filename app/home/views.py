from flask import render_template, abort, send_from_directory
from flask_login import login_required, current_user
import os

from . import home
from .. import db
from ..models import Barang, Jurusan

@home.route('/')
def homepage():
    """
    render homepage template
    """

    # query = db.session.query(Barang).filter(Barang.laku==True).all()
    query = db.session.query(Barang).all()

    return render_template('home/index.html', query=query, title="Jual Beli Barang Bekas")

@home.route('/static/<path:filename>', methods=['GET'])
def sw(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static'), filename)

@home.route('/templates/<path:filename>', methods=['GET'])
def template(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'templates'), filename)