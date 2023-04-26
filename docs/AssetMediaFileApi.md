# swagger_client.AssetMediaFileApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_media_files_code**](AssetMediaFileApi.md#get_asset_media_files_code) | **GET** /api/rest/v1/asset-media-files/{code} | Download the media file associated to an asset
[**post_asset_media_files**](AssetMediaFileApi.md#post_asset_media_files) | **POST** /api/rest/v1/asset-media-files | Create a new media file for an asset

# **get_asset_media_files_code**
> get_asset_media_files_code(code)

Download the media file associated to an asset

This endpoint allows you to download a given media file that is associated with an asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetMediaFileApi()
code = 'code_example' # str | Code of the resource

try:
    # Download the media file associated to an asset
    api_instance.get_asset_media_files_code(code)
except ApiException as e:
    print("Exception when calling AssetMediaFileApi->get_asset_media_files_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_asset_media_files**
> post_asset_media_files(content_type, body=body)

Create a new media file for an asset

This endpoint allows you to create a new media file and associate it to a media file attribute value of an asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetMediaFileApi()
content_type = 'content_type_example' # str | Equal to 'multipart/form-data', no other value allowed
body = swagger_client.V1AssetmediafilesBody() # V1AssetmediafilesBody |  (optional)

try:
    # Create a new media file for an asset
    api_instance.post_asset_media_files(content_type, body=body)
except ApiException as e:
    print("Exception when calling AssetMediaFileApi->post_asset_media_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Equal to &#x27;multipart/form-data&#x27;, no other value allowed | 
 **body** | [**V1AssetmediafilesBody**](V1AssetmediafilesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

