from http import HTTPStatus
from flask import Blueprint
from api.models.post import PostModel
from api.schemas.post import PostSchema

posts_api = Blueprint("posts", __name__)


@posts_api.route("/")
def get():
    t = PostModel(0, 0, "Test", "This is a test post")
    t2 = PostModel(1, 1, "Test 2", "This is another test post!!")
    l = [t, t2]
    return PostSchema(many=True).dump(l), HTTPStatus.OK
