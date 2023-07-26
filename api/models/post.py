from marshmallow_generic import GenericSchema, fields


class Post:
    def __init__(self, id: int, userId: int, title: str, body: str):
        self.id = id
        self.userId = userId
        self.title = title
        self.body = body

    def __str__(self):
        return f"<Post(id={self.id}, userId={self.userId}, title={self.title})>"

    def __repr__(self):
        return f"<Post(id={self.id}, userId={self.userId}, title={self.title})>"


class PostSchema(GenericSchema[Post]):
    id = fields.Int()
    userId = fields.Int()
    title = fields.Str()
    body = fields.Str()
