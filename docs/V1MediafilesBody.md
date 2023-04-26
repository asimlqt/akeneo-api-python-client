# V1MediafilesBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **str** | The product to which the media file will be associated. It is a JSON string that follows this format &#x27;{\&quot;identifier\&quot;:\&quot;product_identifier\&quot;, \&quot;attribute\&quot;:\&quot;attribute_code\&quot;, \&quot;scope\&quot;:\&quot;channel_code\&quot;,\&quot;locale\&quot;:\&quot;locale_code\&quot;}&#x27;. You have to either use this field or the &#x60;product_model&#x60; field, but not both at the same time. | [optional] 
**product_model** | **str** | The product model to which the media file will be associated. It is a JSON string that follows this format &#x27;{\&quot;code\&quot;:\&quot;product_model_code\&quot;, \&quot;attribute\&quot;:\&quot;attribute_code\&quot;, \&quot;scope\&quot;:\&quot;channel_code\&quot;,\&quot;locale\&quot;:\&quot;locale_code\&quot;}&#x27;. You have to either use this field or the &#x60;product&#x60; field, but not both at the same time. | [optional] 
**file** | **str** | The binaries of the file | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

