from flask import Blueprint

# Routes
from .posts import posts_bp

api_bp = Blueprint("api_bp", __name__)

api_bp.register_blueprint(posts_bp)
