# swagger_client.PAMAssetReferenceFileApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reference_files_channel_code_locale_code_download**](PAMAssetReferenceFileApi.md#get_reference_files_channel_code_locale_code_download) | **GET** /api/rest/v1/assets/{asset_code}/reference-files/{locale_code}/download | Download a reference file
[**get_reference_files_locale_code**](PAMAssetReferenceFileApi.md#get_reference_files_locale_code) | **GET** /api/rest/v1/assets/{asset_code}/reference-files/{locale_code} | Get a reference file
[**post_reference_files_locale_code**](PAMAssetReferenceFileApi.md#post_reference_files_locale_code) | **POST** /api/rest/v1/assets/{asset_code}/reference-files/{locale_code} | Upload a new reference file

# **get_reference_files_channel_code_locale_code_download**
> get_reference_files_channel_code_locale_code_download(authorization, asset_code, locale_code)

Download a reference file

This endpoint allows you to download a given reference file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PAMAssetReferenceFileApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
asset_code = 'asset_code_example' # str | Code of the asset
locale_code = 'locale_code_example' # str | Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable

try:
    # Download a reference file
    api_instance.get_reference_files_channel_code_locale_code_download(authorization, asset_code, locale_code)
except ApiException as e:
    print("Exception when calling PAMAssetReferenceFileApi->get_reference_files_channel_code_locale_code_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **asset_code** | **str**| Code of the asset | 
 **locale_code** | **str**| Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_files_locale_code**
> InlineResponse20034 get_reference_files_locale_code(authorization, asset_code, locale_code)

Get a reference file

This endpoint allows you to get the information about a reference file of a given PAM asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PAMAssetReferenceFileApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
asset_code = 'asset_code_example' # str | Code of the asset
locale_code = 'locale_code_example' # str | Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable

try:
    # Get a reference file
    api_response = api_instance.get_reference_files_locale_code(authorization, asset_code, locale_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PAMAssetReferenceFileApi->get_reference_files_locale_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **asset_code** | **str**| Code of the asset | 
 **locale_code** | **str**| Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable | 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reference_files_locale_code**
> InlineResponse201 post_reference_files_locale_code(content_type, asset_code, locale_code, body=body)

Upload a new reference file

This endpoint allows you to upload a new reference file for a given PAM asset and locale. It will also automatically generate all the variation files corresponding to this reference file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PAMAssetReferenceFileApi()
content_type = 'content_type_example' # str | Equal to 'multipart/form-data', no other value allowed
asset_code = 'asset_code_example' # str | Code of the asset
locale_code = 'locale_code_example' # str | Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable
body = swagger_client.ReferencefilesLocaleCodeBody() # ReferencefilesLocaleCodeBody |  (optional)

try:
    # Upload a new reference file
    api_response = api_instance.post_reference_files_locale_code(content_type, asset_code, locale_code, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PAMAssetReferenceFileApi->post_reference_files_locale_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Equal to &#x27;multipart/form-data&#x27;, no other value allowed | 
 **asset_code** | **str**| Code of the asset | 
 **locale_code** | **str**| Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable | 
 **body** | [**ReferencefilesLocaleCodeBody**](ReferencefilesLocaleCodeBody.md)|  | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

