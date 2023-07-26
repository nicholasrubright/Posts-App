from flask_marshmallow import Schema
from marshmallow.fields import Str, Int


class PostSchema(Schema):
    class Meta:
        fields = ["id", "userId", "title", "body"]

    id = Int()
    userId = Int()
    title = Str()
    body = Str()
