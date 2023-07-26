import requests
from requests import Response
from typing import List, Any
from api.models.post import Post, PostSchema
from marshmallow import ValidationError


class ApiError(Exception):
    pass


class JsonApiService:
    url = "https://jsonplaceholder.typicode.com"
    postSchema = PostSchema()

    def _checkStatus(self, response: Response) -> Any:
        if response.status_code > 299 or response.status_code < 200:
            raise ApiError(f"Status Code: {response.status_code}")
        return response.json()

    def getPosts(self) -> List[Post]:
        endpoint = f"{self.url}/posts"
        r = requests.get(endpoint)
        try:
            data = self._checkStatus(r)
            results = self.postSchema.load(data, many=True)
        except ApiError as err:
            print("ApiError: ", err)
            return []
        except ValidationError as err:
            print(err.messages)
            return []

        return self.postSchema.dump(results, many=True)  # type: ignore
