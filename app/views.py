from flask import Blueprint, jsonify, request, render_template

from app.crud import (
    get_all_posts,
    get_post_by_id
)


skygram_blueprint = Blueprint("skygram", __name__)


@skygram_blueprint.get("/")
def index():
    posts = [post.dict() for post in get_all_posts().posts]
    return render_template("index.html", posts=posts, comments_count=13)


@skygram_blueprint.get("/users/<username>")
def user_posts(username: str):
    pass


@skygram_blueprint.get("/posts/<int:post_id>")
def get_post(post_id: int):
    post = get_post_by_id(post_id)
    return jsonify(post.dict()), 200


@skygram_blueprint.get("/search")
def search():
    pass
