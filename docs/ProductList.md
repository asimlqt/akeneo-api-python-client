# ProductList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Product UUID | [optional] 
**identifier** | **str** | Product identifier, i.e. the value of the only &#x60;pim_catalog_identifier&#x60; attribute | 
**enabled** | **bool** | Whether the product is enabled | [optional] [default to True]
**family** | **str** | &lt;a href&#x3D;&#x27;api-reference.html#Family&#x27;&gt;Family&lt;/a&gt; code from which the product inherits its attributes and attributes requirements. | [optional] [default to 'null only in the case of a non variant product']
**categories** | **list[str]** | Codes of the &lt;a href&#x3D;&#x27;api-reference.html#Category&#x27;&gt;categories&lt;/a&gt; in which the product is classified | [optional] 
**groups** | **list[str]** | Codes of the groups to which the product belong | [optional] 
**parent** | **str** | Code of the parent &lt;a href&#x3D;&#x27;api-reference.html#Productmodel&#x27;&gt;product model&lt;/a&gt; when the product is a variant (only available since the 2.0). This parent can be modified since the 2.3. | [optional] 
**values** | [**Apirestv1productsValues**](Apirestv1productsValues.md) |  | [optional] 
**associations** | [**Apirestv1productsAssociations**](Apirestv1productsAssociations.md) |  | [optional] 
**quantified_associations** | [**Apirestv1productsQuantifiedAssociations**](Apirestv1productsQuantifiedAssociations.md) |  | [optional] 
**created** | **str** | Date of creation | [optional] 
**updated** | **str** | Date of the last update | [optional] 
**metadata** | [**Apirestv1productsMetadata**](Apirestv1productsMetadata.md) |  | [optional] 
**quality_scores** | **object** | Product quality scores for each channel/locale combination (only available since the 5.0 and when the \&quot;with_quality_scores\&quot; query parameter is set to \&quot;true\&quot;) | [optional] 
**completenesses** | [**list[Apirestv1productsCompletenesses]**](Apirestv1productsCompletenesses.md) | Product completenesses for each channel/locale combination (only available since the 7.0 version, and when the \&quot;with_completenesses\&quot; query parameter is set to \&quot;true\&quot;) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

