from flask import Blueprint, request, render_template
from flask.helpers import url_for
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

from app.crud import (
    get_all_posts,
    get_post_by_id,
    get_comments_for_post,
    get_all_comments,
    set_comment_for_post
)


skygram_blueprint = Blueprint("skygram", __name__)
skygram_blueprint.add_app_template_global(get_comments_for_post)


@skygram_blueprint.get("/")
def index():
    posts = [post.dict() for post in get_all_posts().posts]
    return render_template("index.html", posts=posts)


@skygram_blueprint.get("/users/<username>")
def user_posts(username: str):
    user_posts = [
        post.dict()
        for post in get_all_posts().posts if post.poster_name == username
    ]
    return render_template("user-feed.html", posts=user_posts)


@skygram_blueprint.route("/posts/<int:post_id>", methods=["GET", "POST"])
def get_post(post_id: int):
    post = get_post_by_id(post_id)
    return render_template("post.html", post=post)


@skygram_blueprint.get("/search")
def search():
    pass


@skygram_blueprint.post("/posts/<int:post_id>/add_comment")
def set_comment(post_id: int):
    if not request.form:
        abort(403, "Form data is empty.Fill form and try again")
    old_pk = max(comment.pk for comment in get_all_comments().comments)
    comment_data = {
        "post_id": post_id,
        "commenter_name": request.form.get("username"),
        "comment": request.form.get("comment_text"),
        "pk": old_pk+1
    }
    if not set_comment_for_post(comment_data):
        abort(403, "Comment data is invalid")
    return redirect(url_for("skygram.get_post", post_id=post_id))
