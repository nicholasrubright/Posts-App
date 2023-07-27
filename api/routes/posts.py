from http import HTTPStatus
from flask import Blueprint
from dependency_injector.wiring import inject, Provide
from api.services.jsonapi import JsonApiService
from api.containers.containers import Container

posts_bp = Blueprint("posts_bp", __name__, url_prefix="/posts")


@posts_bp.route("/")
@inject
def get(jsonApi_service: JsonApiService = Provide[Container.jsonApi_service]):
    posts = jsonApi_service.getPosts()
    return posts[:3], HTTPStatus.OK
