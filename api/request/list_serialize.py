import json
from api.request.json_serializable import JsonSerializable


class ListSerialize(JsonSerializable):

    def __init__(self):
        self.items = []

    def add_item(self, item: dict) -> None:
        self.items.append(item)

    def add_items(self, items: list[dict]) -> None:
        for item in items:
            self.add_item(item)

    def serialize(self) -> str:
        return json.dumps(self.items)
