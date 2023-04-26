# DeprecatedAssetList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | PAM asset code | 
**categories** | **list[str]** | Codes of the PAM asset categories in which the asset is classified | [optional] 
**description** | **str** | Description of the PAM asset | [optional] 
**localizable** | **bool** | Whether the asset is localized or not, meaning if you want to have different reference files for each of your locale | [optional] [default to False]
**tags** | **list[str]** | Tags of the PAM asset | [optional] 
**end_of_use** | **str** | Date on which the PAM asset expire | [optional] 
**variation_files** | [**list[Apirestv1assetsVariationFiles]**](Apirestv1assetsVariationFiles.md) | Variations of the PAM asset | [optional] 
**reference_files** | [**list[Apirestv1assetsReferenceFiles]**](Apirestv1assetsReferenceFiles.md) | Reference files of the PAM asset | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

