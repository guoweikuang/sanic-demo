import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False

    # mysql config
    DB_URL = "mysql://root:2014081029@localhost:3306/sanic"

    # memcached config
    MEMCACHED_HOST = '127.0.0.1'
    MEMCACHED_PORT = 11211

    # redis config
    REDIS_URL = "redis://localhost:6379"

    # page
    PER_PAGE = 10

    # BASE DIR
    BASE_DIR = basedir

    # SITE MESSAGE
    SITE_TITLE = 'Guoweikuang'
    GOOGLE_ANALYTICS = ''
    SITE_NAV_MENUS = [('index.index', '首页')]
    BEIAN_ID = ''

class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    DB_URL = "mysql://root:2014081029@localhost:3306/sanic-test"


class ProConfig(Config):
    pass


level = os.getenv('LEVEL', 'development')
config = {
    'production': ProConfig,
    'development': DevConfig,
    'test': TestConfig,
}[level]
