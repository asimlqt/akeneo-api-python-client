from security.authentication import Authentication
from client.uri_generator import UriGenerator
from client.http_client import HttpClient
from client.resource_client import ResourceClient
from client.authenticated_http_client import AuthenticatedHttpClient
from pagination.page_factory import PageFactory
from akeneo_client import AkeneoClient
from api import (attribute_api,
                 attribute_group_api,
                 attribute_option_api,
                 authentication_api,
                 family_api,
                 family_variant_api,
                 product_model_api,
                 product_uuid_api)


class ClientBuilder:

    def __init__(self, base_uri):
        self.base_uri = base_uri

    def build_authenticated_by_password(self, username, password, client_id, secret):
        authentication = Authentication.from_password(username, password, client_id, secret)
        return self.build(authentication)

    def build(self, authentication):
        uri_generator = UriGenerator(self.base_uri)
        http_client = HttpClient()

        authenticated_http_client = AuthenticatedHttpClient(
            http_client,
            authentication,
            authentication_api.AuthenticationApi(http_client, uri_generator)
        )

        resource_client = ResourceClient(uri_generator, authenticated_http_client)
        page_factory = PageFactory(authenticated_http_client)

        return AkeneoClient(
            authentication=authentication,
            _attribute_api=attribute_api.AttributeApi(resource_client, page_factory),
            _attribute_group_api=attribute_group_api.AttributeGroupApi(resource_client, page_factory),
            _attribute_option_api=attribute_option_api.AttributeOptionApi(resource_client, page_factory),
            _family_api=family_api.FamilyApi(resource_client, page_factory),
            _family_variant_api=family_variant_api.FamilyVariantApi(resource_client, page_factory),
            _product_model_api=product_model_api.ProductModelApi(resource_client, page_factory),
            _product_uuid_api=product_uuid_api.ProductUuidApi(resource_client, page_factory)
        )