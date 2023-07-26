from flask import Flask
from api.routes.posts import posts_api
from api.containers.containers import Container


def create_app():
    container = Container()

    app = Flask(__name__)
    app.container = container  # type: ignore
    app.register_blueprint(posts_api, url_prefix="/api/posts")

    return app


if __name__ == "__main__":
    port = 8080
    app = create_app()

    app.run(host="0.0.0.0", port=port)
