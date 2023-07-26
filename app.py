from flask import Flask
from api.routes.posts import posts_api


def create_app():
    app = Flask(__name__)

    app.register_blueprint(posts_api, url_prefix="/api")

    return app


if __name__ == "__main__":
    port = 8080
    app = create_app()

    app.run(host="0.0.0.0", port=port)
