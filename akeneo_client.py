from security.authentication import Authentication
from api import (asset_api,
                 asset_attribute_api,
                 asset_attribute_option_api,
                 asset_family_api,
                 attribute_api,
                 attribute_group_api,
                 attribute_option_api,
                 family_api,
                 family_variant_api,
                 product_model_api,
                 product_uuid_api,
                 reference_entity_api,
                 reference_entity_attribute_api,
                 reference_entity_attribute_option_api,
                 reference_entity_record_api)


class AkeneoClient:

    def __init__(
        self,
        authentication: Authentication,
        _asset_api: asset_api.AssetApi,
        _asset_attribute_api: asset_attribute_api.AssetAttributeApi,
        _asset_attribute_option_api: asset_attribute_option_api.AssetAttributeOptionApi,
        _asset_family_api: asset_family_api.AssetFamilyApi,
        _attribute_api: attribute_api.AttributeApi,
        _attribute_group_api: attribute_group_api.AttributeGroupApi,
        _attribute_option_api: attribute_option_api.AttributeOptionApi,
        _family_api: family_api.FamilyApi,
        _family_variant_api: family_variant_api.FamilyVariantApi,
        _product_model_api: product_model_api.ProductModelApi,
        _product_uuid_api: product_uuid_api.ProductUuidApi,
        _reference_entity_api: reference_entity_api.ReferenceEntityApi,
        _reference_entity_attribute_api: reference_entity_attribute_api.ReferenceEntityAttributeApi,
        _reference_entity_attribute_option_api: reference_entity_attribute_option_api.ReferenceEntityAttributeOptionApi,
        _reference_entity_record_api: reference_entity_record_api.ReferenceEntityRecordApi
    ):
        self.authentication = authentication
        self.asset_api = _asset_api
        self.asset_attribute_api = _asset_attribute_api
        self.asset_attribute_option_api = _asset_attribute_option_api
        self.asset_family_api = _asset_family_api
        self.attribute_api = _attribute_api
        self.attribute_option_api = _attribute_option_api
        self.attribute_group_api = _attribute_group_api
        self.family_api = _family_api
        self.family_variant_api = _family_variant_api
        self.product_model_api = _product_model_api
        self.product_uuid_api = _product_uuid_api
        self.reference_entity_api = _reference_entity_api
        self.reference_entity_attribute_api = _reference_entity_attribute_api
        self.reference_entity_attribute_option_api = _reference_entity_attribute_option_api
        self.reference_entity_record_api = _reference_entity_record_api
