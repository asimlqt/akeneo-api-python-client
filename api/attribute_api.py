import json
from collections.abc import Iterable
from pagination.resource_cursor import ResourceCursor
from api.request.dict_serialize import DictSerialize
from api.request.line_serialize import LineSerialize

class AttributeApi:

    ATTRIBUTES_URI = "api/rest/v1/attributes"
    ATTRIBUTE_URI = "api/rest/v1/attributes/%s"

    def __init__(self, resource_client, page_factory):
        self.resource_client = resource_client
        self.page_factory = page_factory

    def get(self, code: str) -> dict[str, any]:
        response = self.resource_client.get_resource(self.ATTRIBUTE_URI, [code])

        return json.loads(response.content)

    def all(self, page_size: int = 10, query_params: dict = {}) -> Iterable[list]:
        response = self.resource_client.get_resources(self.ATTRIBUTES_URI, [], query_params, page_size)
        page = self.page_factory.create_page(response.json())

        return iter(ResourceCursor(page_size, page))

    def create(self, data: dict = {}) -> None:
        self.resource_client.create_resource(self.ATTRIBUTES_URI, [], DictSerialize(data))

    def upsert(self, code: str, data: dict = {}) -> None:
        self.resource_client.upsert_resource(self.ATTRIBUTE_URI, [code], DictSerialize(data))

    def upsert_batch(self, data: list[dict]) -> list[dict]:
        batch = LineSerialize()
        batch.add_items(data)

        response = self.resource_client.upsert_batch_resource(self.ATTRIBUTES_URI, [], batch)

        return [json.loads(item) for item in response.content.decode('utf-8').split("\n")]