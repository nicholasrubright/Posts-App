from flask import Flask
from api.containers.containers import Container
from api.routes import api_bp
from config import Config


def create_app():
    container = Container()

    container.wire()

    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(Config)

    app.container = container  # type: ignore

    # Routes
    app.register_blueprint(api_bp, url_prefix="/api")

    return app


if __name__ == "__main__":
    port = 8080
    app = create_app()

    app.run(host="0.0.0.0", port=port)
