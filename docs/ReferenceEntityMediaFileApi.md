# swagger_client.ReferenceEntityMediaFileApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reference_entity_media_files_code**](ReferenceEntityMediaFileApi.md#get_reference_entity_media_files_code) | **GET** /api/rest/v1/reference-entities-media-files/{code} | Download the media file associated to a reference entity or a record
[**post_reference_entity_media_files**](ReferenceEntityMediaFileApi.md#post_reference_entity_media_files) | **POST** /api/rest/v1/reference-entities-media-files | Create a new media file for a reference entity or a record

# **get_reference_entity_media_files_code**
> get_reference_entity_media_files_code(authorization, code)

Download the media file associated to a reference entity or a record

This endpoint allows you to download a given media file that is associated with a reference entity or a record.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceEntityMediaFileApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
code = 'code_example' # str | Code of the resource

try:
    # Download the media file associated to a reference entity or a record
    api_instance.get_reference_entity_media_files_code(authorization, code)
except ApiException as e:
    print("Exception when calling ReferenceEntityMediaFileApi->get_reference_entity_media_files_code: %s\n" % e)
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

# **post_reference_entity_media_files**
> post_reference_entity_media_files(authorization, content_type, body=body)

Create a new media file for a reference entity or a record

This endpoint allows you to create a new media file and associate it to the image of a reference entity, or to the main image or to an attribute value of a record.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceEntityMediaFileApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
content_type = 'content_type_example' # str | Equal to 'multipart/form-data', no other value allowed
body = swagger_client.V1ReferenceentitiesmediafilesBody() # V1ReferenceentitiesmediafilesBody |  (optional)

try:
    # Create a new media file for a reference entity or a record
    api_instance.post_reference_entity_media_files(authorization, content_type, body=body)
except ApiException as e:
    print("Exception when calling ReferenceEntityMediaFileApi->post_reference_entity_media_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **content_type** | **str**| Equal to &#x27;multipart/form-data&#x27;, no other value allowed | 
 **body** | [**V1ReferenceentitiesmediafilesBody**](V1ReferenceentitiesmediafilesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

