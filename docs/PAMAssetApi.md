# swagger_client.PAMAssetApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pam_assets**](PAMAssetApi.md#get_pam_assets) | **GET** /api/rest/v1/assets | Get list of PAM assets
[**get_pam_assets_code**](PAMAssetApi.md#get_pam_assets_code) | **GET** /api/rest/v1/assets/{code} | Get a PAM asset
[**patch_pam_assets**](PAMAssetApi.md#patch_pam_assets) | **PATCH** /api/rest/v1/assets | Update/create several PAM assets
[**patch_pam_assets_code**](PAMAssetApi.md#patch_pam_assets_code) | **PATCH** /api/rest/v1/assets/{code} | Update/create a PAM asset
[**post_pam_assets**](PAMAssetApi.md#post_pam_assets) | **POST** /api/rest/v1/assets | Create a new PAM asset

# **get_pam_assets**
> PAMAssets get_pam_assets(pagination_type=pagination_type, page=page, search_after=search_after, limit=limit, with_count=with_count)

Get list of PAM assets

This endpoint allows you to get a list of PAM assets. PAM assets are paginated.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PAMAssetApi()
pagination_type = 'page' # str | Pagination method type, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to page)
page = 1 # int | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section (optional) (default to 1)
search_after = 'cursor to the first page' # str | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to cursor to the first page)
limit = 10 # int | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to 10)
with_count = false # bool | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way (optional) (default to false)

try:
    # Get list of PAM assets
    api_response = api_instance.get_pam_assets(pagination_type=pagination_type, page=page, search_after=search_after, limit=limit, with_count=with_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PAMAssetApi->get_pam_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_type** | **str**| Pagination method type, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to page]
 **page** | **int**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **search_after** | **str**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to cursor to the first page]
 **limit** | **int**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **with_count** | **bool**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**PAMAssets**](PAMAssets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _links, current_page, _embedded, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pam_assets_code**
> InlineResponse20033 get_pam_assets_code(code)

Get a PAM asset

This endpoint allows you to get the information about a given PAM asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PAMAssetApi()
code = 'code_example' # str | Code of the resource

try:
    # Get a PAM asset
    api_response = api_instance.get_pam_assets_code(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PAMAssetApi->get_pam_assets_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_pam_assets**
> InlineResponse200 patch_pam_assets(body=body)

Update/create several PAM assets

This endpoint allows you to update several PAM assets at once.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PAMAssetApi()
body = swagger_client.V1AssetsBody1() # V1AssetsBody1 |  (optional)

try:
    # Update/create several PAM assets
    api_response = api_instance.patch_pam_assets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PAMAssetApi->patch_pam_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1AssetsBody1**](V1AssetsBody1.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_pam_assets_code**
> patch_pam_assets_code(body, code)

Update/create a PAM asset

This endpoint allows you to update a given PAM asset. Know more about <a href=\"/documentation/update.html#update-behavior\">Update behavior</a>. Note that if no asset exists for the given code, it creates it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PAMAssetApi()
body = swagger_client.AssetsCodeBody1() # AssetsCodeBody1 | 
code = 'code_example' # str | Code of the resource

try:
    # Update/create a PAM asset
    api_instance.patch_pam_assets_code(body, code)
except ApiException as e:
    print("Exception when calling PAMAssetApi->patch_pam_assets_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssetsCodeBody1**](AssetsCodeBody1.md)|  | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pam_assets**
> post_pam_assets(body=body)

Create a new PAM asset

This endpoint allows you to create a new PAM asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PAMAssetApi()
body = swagger_client.V1AssetsBody() # V1AssetsBody |  (optional)

try:
    # Create a new PAM asset
    api_instance.post_pam_assets(body=body)
except ApiException as e:
    print("Exception when calling PAMAssetApi->post_pam_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1AssetsBody**](V1AssetsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

