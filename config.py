import os


class Config(object):
    DEBUG = False
    DB_URL = "mysql://root:2014081029@localhost:3306/sanic"


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
