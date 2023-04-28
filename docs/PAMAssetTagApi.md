# swagger_client.PAMAssetTagApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_tags**](PAMAssetTagApi.md#get_asset_tags) | **GET** /api/rest/v1/asset-tags | Get list of PAM asset tags
[**get_asset_tags_code**](PAMAssetTagApi.md#get_asset_tags_code) | **GET** /api/rest/v1/asset-tags/{code} | Get a PAM asset tag
[**patch_asset_tags_code**](PAMAssetTagApi.md#patch_asset_tags_code) | **PATCH** /api/rest/v1/asset-tags/{code} | Update/create a PAM asset tag

# **get_asset_tags**
> PAMAssetTags get_asset_tags(authorization, page=page, limit=limit, with_count=with_count)

Get list of PAM asset tags

This endpoint allows you to get a list of PAM asset tags. PAM asset tags are paginated.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PAMAssetTagApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
page = 1 # int | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section (optional) (default to 1)
limit = 10 # int | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to 10)
with_count = false # bool | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way (optional) (default to false)

try:
    # Get list of PAM asset tags
    api_response = api_instance.get_asset_tags(authorization, page=page, limit=limit, with_count=with_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PAMAssetTagApi->get_asset_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **page** | **int**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **int**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **with_count** | **bool**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**PAMAssetTags**](PAMAssetTags.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _links, current_page, _embedded, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_tags_code**
> InlineResponse20037 get_asset_tags_code(authorization, code)

Get a PAM asset tag

This endpoint allows you to get the information about a given PAM asset tag.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PAMAssetTagApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
code = 'code_example' # str | Code of the resource

try:
    # Get a PAM asset tag
    api_response = api_instance.get_asset_tags_code(authorization, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PAMAssetTagApi->get_asset_tags_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_asset_tags_code**
> patch_asset_tags_code(body, code)

Update/create a PAM asset tag

This endpoint allows you to update a given PAM asset tag. Know more about <a href=\"/documentation/update.html#update-behavior\">Update behavior</a>. Note that if no tag exists for the given code, it creates it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PAMAssetTagApi()
body = swagger_client.AssettagsCodeBody() # AssettagsCodeBody | 
code = 'code_example' # str | Code of the resource

try:
    # Update/create a PAM asset tag
    api_instance.patch_asset_tags_code(body, code)
except ApiException as e:
    print("Exception when calling PAMAssetTagApi->patch_asset_tags_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssettagsCodeBody**](AssettagsCodeBody.md)|  | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

