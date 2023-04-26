# InlineResponse2004

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Product model code | 
**family** | **str** | &lt;a href&#x3D;&#x27;api-reference.html#Family&#x27;&gt;Family&lt;/a&gt; code  from which the product inherits its attributes and attributes requirements (since the 3.2) | [optional] 
**family_variant** | **str** | Family variant code from which the product model inherits its attributes and variant attributes | 
**parent** | **str** | Code of the parent &lt;a href&#x3D;&#x27;api-reference.html#Productmodel&#x27;&gt;product model&lt;/a&gt;. This parent can be modified since the 2.3. | [optional] 
**categories** | **list[str]** | Codes of the &lt;a href&#x3D;&#x27;api-reference.html#Category&#x27;&gt;categories&lt;/a&gt; in which the product model is categorized | [optional] 
**values** | [**Apirestv1productmodelsValues**](Apirestv1productmodelsValues.md) |  | [optional] 
**associations** | [**Apirestv1productmodelsAssociations**](Apirestv1productmodelsAssociations.md) |  | [optional] 
**quantified_associations** | [**Apirestv1productmodelsQuantifiedAssociations**](Apirestv1productmodelsQuantifiedAssociations.md) |  | [optional] 
**created** | **str** | Date of creation | [optional] 
**updated** | **str** | Date of the last update | [optional] 
**metadata** | [**Apirestv1productmodelsMetadata**](Apirestv1productmodelsMetadata.md) |  | [optional] 
**quality_scores** | **object** | Product model quality scores for each channel/locale combination (&lt;strong&gt;only available since the 7.0 version&lt;/strong&gt; and when the \&quot;with_quality_scores\&quot; query parameter is set to \&quot;true\&quot;) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

