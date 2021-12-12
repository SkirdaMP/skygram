from flask import Blueprint, request


skygram_blueprint = Blueprint("skygram", __name__)


@skygram_blueprint.get("/")
def index():
    pass


@skygram_blueprint.get("/users/<username>")
def users(username: str):
    pass


@skygram_blueprint.get("/posts/<post_id>")
def get_post(post_id: int):
    pass


@skygram_blueprint.get("/search")
def search():
    pass
