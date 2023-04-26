# swagger_client.AssetAttributeOptionApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_attributes_attribute_code_options_code**](AssetAttributeOptionApi.md#get_asset_attributes_attribute_code_options_code) | **GET** /api/rest/v1/asset-families/{asset_family_code}/attributes/{attribute_code}/options/{code} | Get an attribute option for a given attribute of a given asset family
[**get_asset_family_attributes_attribute_code_options**](AssetAttributeOptionApi.md#get_asset_family_attributes_attribute_code_options) | **GET** /api/rest/v1/asset-families/{asset_family_code}/attributes/{attribute_code}/options | Get a list of attribute options of a given attribute for a given asset family
[**patch_asset_attributes_attribute_code_options_code**](AssetAttributeOptionApi.md#patch_asset_attributes_attribute_code_options_code) | **PATCH** /api/rest/v1/asset-families/{asset_family_code}/attributes/{attribute_code}/options/{code} | Update/create an asset attribute option for a given asset family

# **get_asset_attributes_attribute_code_options_code**
> InlineResponse20031 get_asset_attributes_attribute_code_options_code(asset_family_code, attribute_code, code)

Get an attribute option for a given attribute of a given asset family

This endpoint allows you to get the information about a given asset attribute option.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAttributeOptionApi()
asset_family_code = 'asset_family_code_example' # str | Code of the asset family
attribute_code = 'attribute_code_example' # str | Code of the attribute
code = 'code_example' # str | Code of the resource

try:
    # Get an attribute option for a given attribute of a given asset family
    api_response = api_instance.get_asset_attributes_attribute_code_options_code(asset_family_code, attribute_code, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAttributeOptionApi->get_asset_attributes_attribute_code_options_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_family_code** | **str**| Code of the asset family | 
 **attribute_code** | **str**| Code of the attribute | 
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_family_attributes_attribute_code_options**
> list[InlineResponse20030] get_asset_family_attributes_attribute_code_options(asset_family_code, attribute_code)

Get a list of attribute options of a given attribute for a given asset family

This endpoint allows you to get a list of attribute options for a given asset family.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAttributeOptionApi()
asset_family_code = 'asset_family_code_example' # str | Code of the asset family
attribute_code = 'attribute_code_example' # str | Code of the attribute

try:
    # Get a list of attribute options of a given attribute for a given asset family
    api_response = api_instance.get_asset_family_attributes_attribute_code_options(asset_family_code, attribute_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAttributeOptionApi->get_asset_family_attributes_attribute_code_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_family_code** | **str**| Code of the asset family | 
 **attribute_code** | **str**| Code of the attribute | 

### Return type

[**list[InlineResponse20030]**](InlineResponse20030.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_asset_attributes_attribute_code_options_code**
> patch_asset_attributes_attribute_code_options_code(body, asset_family_code, attribute_code, code)

Update/create an asset attribute option for a given asset family

This endpoint allows you to update a given option for a given attribute and a given asset family. Learn more about the <a href=\"/documentation/update.html#update-behavior\">Update behavior</a>. Note that if the option does not already exist for the given attribute of the given asset family, it creates it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAttributeOptionApi()
body = swagger_client.OptionsCodeBody2() # OptionsCodeBody2 | 
asset_family_code = 'asset_family_code_example' # str | Code of the asset family
attribute_code = 'attribute_code_example' # str | Code of the attribute
code = 'code_example' # str | Code of the resource

try:
    # Update/create an asset attribute option for a given asset family
    api_instance.patch_asset_attributes_attribute_code_options_code(body, asset_family_code, attribute_code, code)
except ApiException as e:
    print("Exception when calling AssetAttributeOptionApi->patch_asset_attributes_attribute_code_options_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OptionsCodeBody2**](OptionsCodeBody2.md)|  | 
 **asset_family_code** | **str**| Code of the asset family | 
 **attribute_code** | **str**| Code of the attribute | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

