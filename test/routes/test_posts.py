from unittest import TestCase
from app import create_app
from api.models.post import PostModel
from api.schemas.post import PostSchema


class TestPostsRoute(TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.setPosts()

    def setPosts(self):
        post_1 = PostModel(0, 0, "Test", "This is a test post")
        post_2 = PostModel(1, 1, "Test 2", "This is another test post!!")
        self.posts = PostSchema(many=True).dump([post_1, post_2])

    def test_getPosts(self):
        rv = self.app.get("/api/posts/")
        self.assertEqual(self.posts, rv.get_json())
