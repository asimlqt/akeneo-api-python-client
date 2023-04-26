# AssetfamiliesCodeBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Asset family code | 
**labels** | [**Apirestv1assetfamiliescodeLabels**](Apirestv1assetfamiliescodeLabels.md) |  | [optional] 
**attribute_as_main_media** | **str** | Attribute code that is used as the main media of the asset family. | [optional] [default to 'First media file or media link attribute that was created']
**naming_convention** | [**Apirestv1assetfamiliescodeNamingConvention**](Apirestv1assetfamiliescodeNamingConvention.md) |  | [optional] 
**product_link_rules** | [**list[Apirestv1assetfamiliescodeProductLinkRules]**](Apirestv1assetfamiliescodeProductLinkRules.md) | The rules that will be run after the asset creation, in order to automatically link the assets of this family to a set of products. To understand the format of this property, see &lt;a href&#x3D;&#x27;/concepts/asset-manager.html#focus-on-the-product-link-rule&#x27;&gt;here&lt;/a&gt;. | [optional] 
**transformations** | [**list[Apirestv1assetfamiliescodeTransformations]**](Apirestv1assetfamiliescodeTransformations.md) | The transformations to perform on source files in order to generate new files into your asset attributes (only available since v4.0). To understand the format of this property, see &lt;a href&#x3D;&#x27;/concepts/asset-manager.html#focus-on-the-transformations&#x27;&gt;here&lt;/a&gt;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

