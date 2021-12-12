import os


class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATA_PATH = os.getenv("DATA_PATH")


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass
