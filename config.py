# Parent config class
class Config(object):
    pass

# Child config class (base on activated environement)
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True