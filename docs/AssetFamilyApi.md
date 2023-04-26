# swagger_client.AssetFamilyApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_families**](AssetFamilyApi.md#get_asset_families) | **GET** /api/rest/v1/asset-families | Get list of asset families
[**get_asset_family_code**](AssetFamilyApi.md#get_asset_family_code) | **GET** /api/rest/v1/asset-families/{code} | Get an asset family
[**patch_asset_family_code**](AssetFamilyApi.md#patch_asset_family_code) | **PATCH** /api/rest/v1/asset-families/{code} | Update/create an asset family

# **get_asset_families**
> AssetFamilies get_asset_families(search_after=search_after)

Get list of asset families

This endpoint allows you to get a list of asset families. Asset families are paginated.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetFamilyApi()
search_after = 'cursor to the first page' # str | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to cursor to the first page)

try:
    # Get list of asset families
    api_response = api_instance.get_asset_families(search_after=search_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetFamilyApi->get_asset_families: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_after** | **str**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to cursor to the first page]

### Return type

[**AssetFamilies**](AssetFamilies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _links, _embedded, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_family_code**
> InlineResponse20027 get_asset_family_code(code)

Get an asset family

This endpoint allows you to get the information about a given asset family.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetFamilyApi()
code = 'code_example' # str | Code of the resource

try:
    # Get an asset family
    api_response = api_instance.get_asset_family_code(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetFamilyApi->get_asset_family_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_asset_family_code**
> patch_asset_family_code(body, code)

Update/create an asset family

This endpoint allows you to update a given asset family. Note that if the asset family does not already exist, it creates it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetFamilyApi()
body = swagger_client.AssetfamiliesCodeBody() # AssetfamiliesCodeBody | 
code = 'code_example' # str | Code of the resource

try:
    # Update/create an asset family
    api_instance.patch_asset_family_code(body, code)
except ApiException as e:
    print("Exception when calling AssetFamilyApi->patch_asset_family_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssetfamiliesCodeBody**](AssetfamiliesCodeBody.md)|  | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

