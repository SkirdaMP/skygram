"""
Module for crate models and work with data.
"""
import json
from typing import List, Dict
from pydantic import BaseModel, ValidationError


class Post(BaseModel):
    """
    Model that contains data about post.
    """
    pk: int
    poster_name: str
    poster_avatar: str
    pic: str
    content: str = ""
    views_count: int = 0
    likes_count: int = 0


class PostsModel(BaseModel):
    """
    Model that contains list of posts
    """
    posts: List[Post]


class Comment(BaseModel):
    """
    Model that contains data about comment.
    """
    post_id: int
    commenter_name: str
    comment: str
    pk: int


class CommentsModel(BaseModel):
    """
    Model that contains list of comments
    """
    comments: List[Comment]


class BaseJsonWorker:
    """
    Base class for read and write data from/to json file.
    """
    def __init__(self, path_to_json: str):
        self.data_path = path_to_json

    @property
    def raw_json_data(self) -> List[Dict]:
        with open(self.data_path) as f:
            return json.load(f)

    def insert_into_json(self, data):
        json_data = self.raw_json_data
        json_data.append(data)
        with open(self.data_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False)


class PostsJsonWorker(BaseJsonWorker):
    """
    Class for work with posts of user
    """
    def insert_into_json(self, data: Dict):
        try:
            Post(**data)
        except ValidationError as e:
            print(e.json())
            return False
        super().insert_into_json(data)
        return True


class CommentsJsonWorker(BaseJsonWorker):
    """
    Class for work with comments of user
    """
    def insert_into_json(self, data: Dict):
        try:
            Comment(**data)
        except ValidationError as e:
            print(e.json())
            return False
        super().insert_into_json(data)
        return True
