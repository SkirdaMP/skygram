from typing import (
    Union
)

from flask import current_app

from app.models import (
    Post, 
    PostsModel,
    Comment,
    CommentsModel,
    PostsJsonWorker,
    CommentsJsonWorker
)

# DATA_PATH = "data"
DATA_PATH = current_app.config.get("DATA_PATH")
posts_worker = PostsJsonWorker(path_to_json=f"{DATA_PATH}/data.json")
comments_worker = CommentsJsonWorker(path_to_json=f"{DATA_PATH}/comments.json")


def get_all_posts() -> Union[PostsModel, None]:
    return PostsModel(posts=posts_worker.data_from_json)


def get_post_by_id(post_id: int) -> Union[Post, None]:
    posts = PostsModel(posts=posts_worker.data_from_json).posts
    post = next(filter(lambda x: x.pk == post_id, posts))
    return post
