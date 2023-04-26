# PublishedProductList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Published product identifier, i.e. the value of the only &#x60;pim_catalog_identifier&#x60; attribute | 
**enabled** | **bool** | Whether the published product is enable | [optional] [default to True]
**family** | **str** | &lt;a href&#x3D;&#x27;api-reference.html#Family&#x27;&gt;Family&lt;/a&gt; code from which the published product inherits its attributes and attributes requirements | [optional] 
**categories** | **list[str]** | Codes of the &lt;a href&#x3D;&#x27;api-reference.html#Category&#x27;&gt;categories&lt;/a&gt; in which the published product is classified | [optional] 
**groups** | **list[str]** | Codes of the groups to which the published product belong | [optional] 
**values** | [**PublishedProductValues**](PublishedProductValues.md) |  | [optional] 
**associations** | [**PublishedProductAssociations**](PublishedProductAssociations.md) |  | [optional] 
**quantified_associations** | **object** | Warning: associations with quantities are not compatible with the published products. The response will always be empty. | [optional] 
**created** | **str** | Date of creation | [optional] 
**updated** | **str** | Date of the last update | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

