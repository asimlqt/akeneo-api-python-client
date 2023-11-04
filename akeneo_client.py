from security.authentication import Authentication
from api import (attribute_api,
                 attribute_group_api,
                 attribute_option_api,
                 family_api,
                 family_variant_api,
                 product_model_api,
                 product_uuid_api)


class AkeneoClient:

    def __init__(
        self,
        authentication: Authentication,
        _attribute_api: attribute_api.AttributeApi,
        _attribute_group_api: attribute_group_api.AttributeGroupApi,
        _attribute_option_api: attribute_option_api.AttributeOptionApi,
        _family_api: family_api.FamilyApi,
        _family_variant_api: family_variant_api.FamilyVariantApi,
        _product_model_api: product_model_api.ProductModelApi,
        _product_uuid_api: product_uuid_api.ProductUuidApi
    ):
        self.authentication = authentication
        self.attribute_api = _attribute_api
        self.attribute_option_api = _attribute_option_api
        self.attribute_group_api = _attribute_group_api
        self.family_api = _family_api
        self.family_variant_api = _family_variant_api
        self.product_model_api = _product_model_api
        self.product_uuid_api = _product_uuid_api
