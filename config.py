class Config(object):
    """
    Konfigurasi umum
    """

class DevelopmentConfig(Config):
    """
    Konfigurasi development
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Konfigurasi produksi
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}