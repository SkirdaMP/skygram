from pydantic import BaseModel

from flask import current_app

DATA_DIR = current_app.config.get("DATA_PATH")


class User(BaseModel):
    pass


class Post(BaseModel):
    pass


class Comment(BaseModel):
    pass
