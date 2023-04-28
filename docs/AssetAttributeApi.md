# swagger_client.AssetAttributeApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_families_code_attributes**](AssetAttributeApi.md#get_asset_families_code_attributes) | **GET** /api/rest/v1/asset-families/{asset_family_code}/attributes | Get the list of attributes of a given asset family
[**get_asset_family_attributes_code**](AssetAttributeApi.md#get_asset_family_attributes_code) | **GET** /api/rest/v1/asset-families/{asset_family_code}/attributes/{code} | Get an attribute of a given asset family
[**patch_asset_family_attributes_code**](AssetAttributeApi.md#patch_asset_family_attributes_code) | **PATCH** /api/rest/v1/asset-families/{asset_family_code}/attributes/{code} | Update/create an attribute of a given asset family

# **get_asset_families_code_attributes**
> list[InlineResponse20028] get_asset_families_code_attributes(authorization, asset_family_code)

Get the list of attributes of a given asset family

This endpoint allows you to get the list of attributes of a given asset family.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAttributeApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
asset_family_code = 'asset_family_code_example' # str | Code of the asset family

try:
    # Get the list of attributes of a given asset family
    api_response = api_instance.get_asset_families_code_attributes(authorization, asset_family_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAttributeApi->get_asset_families_code_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **asset_family_code** | **str**| Code of the asset family | 

### Return type

[**list[InlineResponse20028]**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_family_attributes_code**
> InlineResponse20029 get_asset_family_attributes_code(authorization, asset_family_code, code)

Get an attribute of a given asset family

This endpoint allows you to get the information about a given attribute for a given asset family.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAttributeApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
asset_family_code = 'asset_family_code_example' # str | Code of the asset family
code = 'code_example' # str | Code of the resource

try:
    # Get an attribute of a given asset family
    api_response = api_instance.get_asset_family_attributes_code(authorization, asset_family_code, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAttributeApi->get_asset_family_attributes_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **asset_family_code** | **str**| Code of the asset family | 
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_asset_family_attributes_code**
> patch_asset_family_attributes_code(body, asset_family_code, code)

Update/create an attribute of a given asset family

This endpoint allows you to update a given attribute for a given asset family. Note that if the attribute does not already exist for the given asset family, it creates it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAttributeApi()
body = swagger_client.AttributesCodeBody2() # AttributesCodeBody2 | 
asset_family_code = 'asset_family_code_example' # str | Code of the asset family
code = 'code_example' # str | Code of the resource

try:
    # Update/create an attribute of a given asset family
    api_instance.patch_asset_family_attributes_code(body, asset_family_code, code)
except ApiException as e:
    print("Exception when calling AssetAttributeApi->patch_asset_family_attributes_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttributesCodeBody2**](AttributesCodeBody2.md)|  | 
 **asset_family_code** | **str**| Code of the asset family | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

