import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config: 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
 
class ProdConfig(Config): 
    pass 
 
class DevConfig(Config): 
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL')

config = {
    'development'   : DevConfig,
    'production'    : ProdConfig
}