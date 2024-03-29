# Akeneo API Python Client

A simple Python client for the Akeneo PIM API

## Installation

```commandline
pip install akeneo-api-client
```

## Usage

### Initialise the client

```python
from akeneo_api_client.client_builder import ClientBuilder
from akeneo_api_client.client.akeneo_api_error import AkeneoApiError

cb = ClientBuilder(uri)
api = cb.build_authenticated_by_password(username, password, client_id, secret)
```

Or if you already have a cached version of the token you can use:

```python
api = cb.build_authenticated_by_token(client_id, secret, token, refresh_token)
```

### Fetch a product

```python
try:
    response = api.product_uuid_api.get(uuid)
    print(response)
except AkeneoApiError as e:
    print(e.response.status_code)
    print(e.response_body)
```

### Iterate over a list of products

```python
from akeneo_api_client.search.search_builder import SearchBuilder

sb = SearchBuilder()
sb.add_filter('updated', '>', '2023-11-29 00:00:00')
sb.add_filter('completeness', '=', 100, {"scope": "ecommerce"})
sb.add_filter('enabled', '=', True)
search = sb.get_filters()

try:
    for page in api.product_uuid_api.all(query_params={"search": search}):
        for item in page:
            print(item["uuid"])
except AkeneoApiError as e:
    print(e.message)
```

### Create a product

```python
try:
    response = api.product_uuid_api.create(data={"family":"my_family"})
    print(response.headers.get("location"))
except AkeneoApiError as e:
    print(e.response_body)
```

### Upsert a product

This call will create a product if it doesn't exist or update it if it does 

```python
data = {
    "values": {
        "Product_name": [
            {"scope": None, "locale": "en_GB", "data": "My product"}
        ]
    }
}

try:
    api.product_uuid_api.upsert(uuid, data)
except AkeneoApiError as e:
    print(e.message)
```

### Upsert a list of products

```python
products = [
    {
        "uuid": str(uuid.uuid4()),
        "values": {
            "Product_name": [
                {"scope": None, "locale": "en_GB", "data": "Product 1"}
            ]
        }
    },
    {
        "values": {
            "Product_name": [
                {"scope": None, "locale": "en_GB", "data": "Product 2"}
            ]
        }
    }
]

try:
    response = api.product_uuid_api.upsert_list(products)
    for item in response:
        if item['status_code'] >= 400:
            print(item)
except AkeneoApiError as e:
    print(e.response.reason)
```

### Delete a product

```python
try:
    api.product_uuid_api.delete(uuid)
except AkeneoApiError as e:
    print(e.response_body)
```

