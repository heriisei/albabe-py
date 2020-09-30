# 3rd party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, configure_uploads, IMAGES
import os

#local imports
from config import app_config

#db variable initialization
db = SQLAlchemy()
login_manager = LoginManager()

photos = UploadSet('photos', IMAGES)

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/app/static/img/barang'

    configure_uploads(app, photos)

    Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "Kamu harus Masuk akun untuk mengakses halaman ini."
    login_manager.login_view = "auth.login"
    migrate = Migrate(app, db)

    from app import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    from .barang import barang as barang_blueprint
    app.register_blueprint(barang_blueprint)
    
    return app