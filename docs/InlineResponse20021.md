# InlineResponse20021

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Attribute code | 
**labels** | [**Apirestv1attributesLabels**](Apirestv1attributesLabels.md) |  | [optional] 
**type** | **str** | Attribute type. See &lt;a href&#x3D;&#x27;/concepts/reference-entities.html#reference-entity-attribute&#x27;&gt;type&lt;/a&gt; section for more details. | 
**value_per_locale** | **bool** | Whether the attribute is localizable, i.e. can have one value by locale | [optional] [default to False]
**value_per_channel** | **bool** | Whether the attribute is scopable, i.e. can have one value by channel | [optional] [default to False]
**is_required_for_completeness** | **bool** | Whether the attribute should be part of the record&#x27;s completeness calculation | [optional] [default to False]
**max_characters** | **int** | Maximum number of characters allowed for the value of the attribute when the attribute type is &#x60;text&#x60; | [optional] 
**is_textarea** | **bool** | Whether the UI should display a text area instead of a simple field when the attribute type is &#x60;text&#x60; | [optional] [default to False]
**is_rich_text_editor** | **bool** | Whether the UI should display a rich text editor instead of a simple text area when the attribute type is &#x60;text&#x60; | [optional] 
**validation_rule** | **str** | Validation rule type used to validate the attribute value when the attribute type is &#x60;text&#x60; | [optional] [default to 'none']
**validation_regexp** | **str** | Regexp expression used to validate the attribute value when the attribute type is &#x60;text&#x60; | [optional] 
**allowed_extensions** | **list[str]** | Extensions allowed when the attribute type is &#x60;image&#x60; | [optional] 
**max_file_size** | **str** | Max file size in MB when the attribute type is &#x60;image&#x60; | [optional] 
**reference_entity_code** | **str** | Code of the linked reference entity when the attribute type is &#x60;reference_entity_single_link&#x60; or &#x60;reference_entity_multiple_links&#x60; | [optional] 
**decimals_allowed** | **bool** | Whether decimals are allowed when the attribute type is &#x60;number&#x60; | [optional] [default to False]
**min_value** | **str** | Minimum value allowed when the attribute type is &#x60;number&#x60; | [optional] 
**max_value** | **str** | Maximum value allowed when the attribute type is &#x60;number&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

