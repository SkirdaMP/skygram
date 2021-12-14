from typing import (
    Union,
    Dict
)

from flask import current_app

from app.models import (
    Post,
    PostsModel,
    # Comment,
    CommentsModel,
    PostsJsonWorker,
    CommentsJsonWorker
)


DATA_PATH = current_app.config.get("DATA_PATH")
posts_worker = PostsJsonWorker(path_to_json=f"{DATA_PATH}/data.json")
comments_worker = CommentsJsonWorker(path_to_json=f"{DATA_PATH}/comments.json")


def get_all_posts() -> Union[PostsModel, None]:
    return PostsModel(posts=posts_worker.raw_json_data)


def get_post_by_id(post_id: int) -> Union[Post, None]:
    posts = PostsModel(posts=posts_worker.raw_json_data).posts
    post = next(p for p in posts if p.pk == post_id)
    return post


def get_comments_for_post(post_id: int) -> Union[CommentsModel, None]:
    comments = CommentsModel(comments=comments_worker.raw_json_data).comments
    return [comment for comment in comments if comment.post_id == post_id]


def get_all_comments() -> Union[CommentsModel, None]:
    return CommentsModel(comments=comments_worker.raw_json_data)


def set_comment_for_post(comment_data: Dict) -> bool:
    if comments_worker.insert_into_json(comment_data):
        return True
    return False
