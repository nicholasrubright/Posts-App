from dependency_injector import containers, providers
from api.services.jsonapi import JsonApiService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["api.routes.posts"])

    jsonApi_service = providers.Factory(JsonApiService)
