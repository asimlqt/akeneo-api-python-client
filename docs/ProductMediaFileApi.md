# swagger_client.ProductMediaFileApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_media_files**](ProductMediaFileApi.md#get_media_files) | **GET** /api/rest/v1/media-files | Get a list of product media files
[**get_media_files_code**](ProductMediaFileApi.md#get_media_files_code) | **GET** /api/rest/v1/media-files/{code} | Get a product media file
[**get_media_files_code_download**](ProductMediaFileApi.md#get_media_files_code_download) | **GET** /api/rest/v1/media-files/{code}/download | Download a product media file
[**post_media_files**](ProductMediaFileApi.md#post_media_files) | **POST** /api/rest/v1/media-files | Create a new product media file

# **get_media_files**
> MediaFiles get_media_files(authorization, page=page, limit=limit, with_count=with_count)

Get a list of product media files

This endpoint allows you to get a list of media files that are used as attribute values in products or product models.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductMediaFileApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
page = 1 # int | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section (optional) (default to 1)
limit = 10 # int | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to 10)
with_count = false # bool | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way (optional) (default to false)

try:
    # Get a list of product media files
    api_response = api_instance.get_media_files(authorization, page=page, limit=limit, with_count=with_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductMediaFileApi->get_media_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **page** | **int**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **int**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **with_count** | **bool**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**MediaFiles**](MediaFiles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _links, current_page, _embedded, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_files_code**
> InlineResponse2006 get_media_files_code(authorization, code)

Get a product media file

This endpoint allows you to get the information about a given media file that is used as an attribute value of a product or a product model.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductMediaFileApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
code = 'code_example' # str | Code of the resource

try:
    # Get a product media file
    api_response = api_instance.get_media_files_code(authorization, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductMediaFileApi->get_media_files_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_files_code_download**
> get_media_files_code_download(authorization, code)

Download a product media file

This endpoint allows you to download a given media file that is used as an attribute value of a product or a product model.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductMediaFileApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
code = 'code_example' # str | Code of the resource

try:
    # Download a product media file
    api_instance.get_media_files_code_download(authorization, code)
except ApiException as e:
    print("Exception when calling ProductMediaFileApi->get_media_files_code_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_media_files**
> post_media_files(content_type, body=body)

Create a new product media file

This endpoint allows you to create a new media file and associate it to an attribute value of a given product or product model.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductMediaFileApi()
content_type = 'content_type_example' # str | Equal to 'multipart/form-data', no other value allowed
body = swagger_client.V1MediafilesBody() # V1MediafilesBody |  (optional)

try:
    # Create a new product media file
    api_instance.post_media_files(content_type, body=body)
except ApiException as e:
    print("Exception when calling ProductMediaFileApi->post_media_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Equal to &#x27;multipart/form-data&#x27;, no other value allowed | 
 **body** | [**V1MediafilesBody**](V1MediafilesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

