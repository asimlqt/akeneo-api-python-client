# InlineResponse2009

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Attribute code | 
**type** | **str** | Attribute type. See &lt;a href&#x3D;&#x27;/concepts/catalog-structure.html#attribute&#x27;&gt;type&lt;/a&gt; section for more details. | 
**labels** | [**Apirestv1attributesLabels**](Apirestv1attributesLabels.md) |  | [optional] 
**group** | **str** | Attribute group | 
**group_labels** | [**Apirestv1attributesGroupLabels**](Apirestv1attributesGroupLabels.md) |  | [optional] 
**sort_order** | **int** | Order of the attribute in its group | [optional] 
**localizable** | **bool** | Whether the attribute is localizable, i.e. can have one value by locale | [optional] [default to False]
**scopable** | **bool** | Whether the attribute is scopable, i.e. can have one value by channel | [optional] [default to False]
**available_locales** | **list[str]** | To make the attribute locale specfic, specify here for which locales it is specific | [optional] 
**unique** | **bool** | Whether two values for the attribute cannot be the same | [optional] 
**useable_as_grid_filter** | **bool** | Whether the attribute can be used as a filter for the product grid in the PIM user interface | [optional] 
**max_characters** | **int** | Number maximum of characters allowed for the value of the attribute when the attribute type is &#x60;pim_catalog_text&#x60;, &#x60;pim_catalog_textarea&#x60; or &#x60;pim_catalog_identifier&#x60; | [optional] 
**validation_rule** | **str** | Validation rule type used to validate any attribute value when the attribute type is &#x60;pim_catalog_text&#x60; or &#x60;pim_catalog_identifier&#x60; | [optional] 
**validation_regexp** | **str** | Regexp expression used to validate any attribute value when the attribute type is &#x60;pim_catalog_text&#x60; or &#x60;pim_catalog_identifier&#x60; | [optional] 
**wysiwyg_enabled** | **bool** | Whether the WYSIWYG interface is shown when the attribute type is &#x60;pim_catalog_textarea&#x60; | [optional] 
**number_min** | **str** | Minimum integer value allowed when the attribute type is &#x60;pim_catalog_metric&#x60;, &#x60;pim_catalog_price&#x60; or &#x60;pim_catalog_number&#x60; | [optional] 
**number_max** | **str** | Maximum integer value allowed when the attribute type is &#x60;pim_catalog_metric&#x60;, &#x60;pim_catalog_price&#x60; or &#x60;pim_catalog_number&#x60; | [optional] 
**decimals_allowed** | **bool** | Whether decimals are allowed when the attribute type is &#x60;pim_catalog_metric&#x60;, &#x60;pim_catalog_price&#x60; or &#x60;pim_catalog_number&#x60; | [optional] 
**negative_allowed** | **bool** | Whether negative values are allowed when the attribute type is &#x60;pim_catalog_metric&#x60; or &#x60;pim_catalog_number&#x60; | [optional] 
**metric_family** | **str** | Metric family when the attribute type is &#x60;pim_catalog_metric&#x60; | [optional] 
**default_metric_unit** | **str** | Default metric unit when the attribute type is &#x60;pim_catalog_metric&#x60; | [optional] 
**date_min** | **datetime** | Minimum date allowed when the attribute type is &#x60;pim_catalog_date&#x60; | [optional] 
**date_max** | **datetime** | Maximum date allowed when the attribute type is &#x60;pim_catalog_date&#x60; | [optional] 
**allowed_extensions** | **list[str]** | Extensions allowed when the attribute type is &#x60;pim_catalog_file&#x60; or &#x60;pim_catalog_image&#x60; | [optional] 
**max_file_size** | **str** | Max file size in MB when the attribute type is &#x60;pim_catalog_file&#x60; or &#x60;pim_catalog_image&#x60; | [optional] 
**reference_data_name** | **str** | Reference entity code when the attribute type is &#x60;akeneo_reference_entity&#x60; or &#x60;akeneo_reference_entity_collection&#x60; OR Asset family code when the attribute type is &#x60;pim_catalog_asset_collection&#x60; | [optional] 
**default_value** | **bool** | Default value for a Yes/No attribute, applied when creating a new product or product model (only available since the 5.0) | [optional] 
**table_configuration** | [**list[Apirestv1attributesTableConfiguration]**](Apirestv1attributesTableConfiguration.md) | Configuration of the Table attribute (columns) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

