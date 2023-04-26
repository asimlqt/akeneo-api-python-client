# swagger_client.PAMAssetCategoryApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_categories**](PAMAssetCategoryApi.md#get_asset_categories) | **GET** /api/rest/v1/asset-categories | Get list of PAM asset categories
[**get_asset_categories_code**](PAMAssetCategoryApi.md#get_asset_categories_code) | **GET** /api/rest/v1/asset-categories/{code} | Get a PAM asset category
[**patch_asset_categories**](PAMAssetCategoryApi.md#patch_asset_categories) | **PATCH** /api/rest/v1/asset-categories | Update/create several PAM asset categories
[**patch_asset_categories_code**](PAMAssetCategoryApi.md#patch_asset_categories_code) | **PATCH** /api/rest/v1/asset-categories/{code} | Update/create a PAM asset category
[**post_asset_categories**](PAMAssetCategoryApi.md#post_asset_categories) | **POST** /api/rest/v1/asset-categories | Create a new PAM asset category

# **get_asset_categories**
> PAMAssetCategories get_asset_categories(page=page, limit=limit, with_count=with_count)

Get list of PAM asset categories

This endpoint allows you to get a list of PAM asset categories. PAM asset categories are paginated and sorted by `root/left`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PAMAssetCategoryApi()
page = 1 # int | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section (optional) (default to 1)
limit = 10 # int | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to 10)
with_count = false # bool | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way (optional) (default to false)

try:
    # Get list of PAM asset categories
    api_response = api_instance.get_asset_categories(page=page, limit=limit, with_count=with_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PAMAssetCategoryApi->get_asset_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **int**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **with_count** | **bool**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**PAMAssetCategories**](PAMAssetCategories.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _links, current_page, _embedded, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_categories_code**
> InlineResponse20036 get_asset_categories_code(code)

Get a PAM asset category

This endpoint allows you to get the information about a given PAM asset category.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PAMAssetCategoryApi()
code = 'code_example' # str | Code of the resource

try:
    # Get a PAM asset category
    api_response = api_instance.get_asset_categories_code(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PAMAssetCategoryApi->get_asset_categories_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_asset_categories**
> InlineResponse200 patch_asset_categories(body=body)

Update/create several PAM asset categories

This endpoint allows you to update several PAM asset categories at once.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PAMAssetCategoryApi()
body = swagger_client.V1AssetcategoriesBody1() # V1AssetcategoriesBody1 |  (optional)

try:
    # Update/create several PAM asset categories
    api_response = api_instance.patch_asset_categories(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PAMAssetCategoryApi->patch_asset_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1AssetcategoriesBody1**](V1AssetcategoriesBody1.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_asset_categories_code**
> patch_asset_categories_code(body, code)

Update/create a PAM asset category

This endpoint allows you to update a given PAM asset category. Know more about <a href=\"/documentation/update.html#update-behavior\">Update behavior</a>. Note that if no category exists for the given code, it creates it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PAMAssetCategoryApi()
body = swagger_client.AssetcategoriesCodeBody() # AssetcategoriesCodeBody | 
code = 'code_example' # str | Code of the resource

try:
    # Update/create a PAM asset category
    api_instance.patch_asset_categories_code(body, code)
except ApiException as e:
    print("Exception when calling PAMAssetCategoryApi->patch_asset_categories_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssetcategoriesCodeBody**](AssetcategoriesCodeBody.md)|  | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_asset_categories**
> post_asset_categories(body=body)

Create a new PAM asset category

This endpoint allows you to create a new PAM asset category.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PAMAssetCategoryApi()
body = swagger_client.V1AssetcategoriesBody() # V1AssetcategoriesBody |  (optional)

try:
    # Create a new PAM asset category
    api_instance.post_asset_categories(body=body)
except ApiException as e:
    print("Exception when calling PAMAssetCategoryApi->post_asset_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1AssetcategoriesBody**](V1AssetcategoriesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

