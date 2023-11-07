import json
from collections.abc import Iterable

import client.resource_client
import pagination.page_factory
from pagination.resource_cursor import ResourceCursor
from api.request.dict_serialize import DictSerialize
from api.request.list_serialize import ListSerialize


class AssetApi:

    ASSETS_URI = "api/rest/v1/asset-families/%s/assets"
    ASSET_URI = "api/rest/v1/asset-families/%s/assets/%s"

    def __init__(
        self,
        resource_client: client.resource_client.ResourceClient,
        page_factory: pagination.page_factory.PageFactory
    ):
        self.resource_client = resource_client
        self.page_factory = page_factory

    def get(self, asset_family_code: str, asset_code: str) -> dict[str, any]:
        response = self.resource_client.get_resource(self.ASSET_URI, [asset_family_code, asset_code])

        return json.loads(response.content)

    def all(self, asset_family_code: str, query_params: dict = {}) -> Iterable[list]:
        response = self.resource_client.get_resources(self.ASSETS_URI, [asset_family_code], query_params)
        page = self.page_factory.create_page(response.json())

        return iter(ResourceCursor(0, page))

    def upsert(self, asset_family_code: str, asset_code: str, data: dict = {}) -> None:
        self.resource_client.upsert_resource(
            self.ASSET_URI,
            [asset_family_code, asset_code],
            DictSerialize(data)
        )

    def upsert_batch(self, asset_family_code: str, data: list[dict]) -> list[dict]:
        batch = ListSerialize()
        batch.add_items(data)

        response = self.resource_client.upsert_batch_json_resource(
            self.ASSETS_URI,
            [asset_family_code],
            batch
        )

        return [json.loads(item) for item in response.content.decode('utf-8').split("\n")]

    def delete(self, asset_family_code: str, asset_code: str) -> None:
        self.resource_client.delete_resource(self.ASSET_URI, [asset_family_code, asset_code])