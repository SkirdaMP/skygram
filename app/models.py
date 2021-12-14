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
        with open(self.data_path, encoding="utf-8") as f:
            self.__data_from_json = json.load(f)
    
    @property
    def data_from_json(self):
        return self.__data_from_json
    
    def insert_into_json(self, data):
        self.__data_from_json = data
        with open(self.data_path, "w", encoding="utf-8") as f:
            json.dump(self.__data_from_json, f, ensure_ascii=False)


class PostsJsonWorker(BaseJsonWorker):
    """
    Class for work with posts of user
    """
    def insert_into_json(self, data: List[Dict]):
        try:
            PostsModel(posts=data)
        except ValidationError as e:
            print(e.json())
            return
        super().insert_into_json(data)
        


class CommentsJsonWorker(BaseJsonWorker):
    """
    Class for work with comments of user
    """
    def insert_into_json(self, data: List[Dict]):
        try:
            CommentsModel(comments=data)
        except ValidationError as e:
            print(e.json())
            return
        super().insert_into_json(data)
