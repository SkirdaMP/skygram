# must renamed to config.py
import os


class BaseConfig:
    SECRET_KEY = "secret_key"
    DATA_PATH = os.getenv("DATA_PATH")


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass
