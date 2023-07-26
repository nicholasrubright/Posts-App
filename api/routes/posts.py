from http import HTTPStatus
from flask import Blueprint, jsonify
from dependency_injector.wiring import inject, Provide
from api.services.jsonapi import JsonApiService
from api.containers.containers import Container

posts_api = Blueprint("posts", __name__)


@posts_api.route("/")
@inject
def get(jsonApi_service: JsonApiService = Provide[Container.jsonApi_service]):
    posts = jsonApi_service.getPosts()
    return posts[:3], HTTPStatus.OK
