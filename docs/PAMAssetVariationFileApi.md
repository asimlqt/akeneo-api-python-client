# swagger_client.PAMAssetVariationFileApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_variation_files_channel_code_locale_code**](PAMAssetVariationFileApi.md#get_variation_files_channel_code_locale_code) | **GET** /api/rest/v1/assets/{asset_code}/variation-files/{channel_code}/{locale_code} | Get a variation file
[**get_variation_files_channel_code_locale_code_download**](PAMAssetVariationFileApi.md#get_variation_files_channel_code_locale_code_download) | **GET** /api/rest/v1/assets/{asset_code}/variation-files/{channel_code}/{locale_code}/download | Download a variation file
[**post_variation_files_channel_code_locale_code**](PAMAssetVariationFileApi.md#post_variation_files_channel_code_locale_code) | **POST** /api/rest/v1/assets/{asset_code}/variation-files/{channel_code}/{locale_code} | Upload a new variation file

# **get_variation_files_channel_code_locale_code**
> InlineResponse20035 get_variation_files_channel_code_locale_code(authorization, asset_code, channel_code, locale_code)

Get a variation file

This endpoint allows you to get the information about a variation file of a given PAM asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PAMAssetVariationFileApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
asset_code = 'asset_code_example' # str | Code of the asset
channel_code = 'channel_code_example' # str | Code of the channel
locale_code = 'locale_code_example' # str | Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable

try:
    # Get a variation file
    api_response = api_instance.get_variation_files_channel_code_locale_code(authorization, asset_code, channel_code, locale_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PAMAssetVariationFileApi->get_variation_files_channel_code_locale_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **asset_code** | **str**| Code of the asset | 
 **channel_code** | **str**| Code of the channel | 
 **locale_code** | **str**| Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable | 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variation_files_channel_code_locale_code_download**
> get_variation_files_channel_code_locale_code_download(authorization, asset_code, channel_code, locale_code)

Download a variation file

This endpoint allows you to download a given variation file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PAMAssetVariationFileApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
asset_code = 'asset_code_example' # str | Code of the asset
channel_code = 'channel_code_example' # str | Code of the channel
locale_code = 'locale_code_example' # str | Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable

try:
    # Download a variation file
    api_instance.get_variation_files_channel_code_locale_code_download(authorization, asset_code, channel_code, locale_code)
except ApiException as e:
    print("Exception when calling PAMAssetVariationFileApi->get_variation_files_channel_code_locale_code_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **asset_code** | **str**| Code of the asset | 
 **channel_code** | **str**| Code of the channel | 
 **locale_code** | **str**| Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_variation_files_channel_code_locale_code**
> post_variation_files_channel_code_locale_code(content_type, asset_code, channel_code, locale_code, body=body)

Upload a new variation file

This endpoint allows you to upload a new variation file for a given PAM asset, channel and locale.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PAMAssetVariationFileApi()
content_type = 'content_type_example' # str | Equal to 'multipart/form-data', no other value allowed
asset_code = 'asset_code_example' # str | Code of the asset
channel_code = 'channel_code_example' # str | Code of the channel
locale_code = 'locale_code_example' # str | Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable
body = swagger_client.ChannelCodeLocaleCodeBody() # ChannelCodeLocaleCodeBody |  (optional)

try:
    # Upload a new variation file
    api_instance.post_variation_files_channel_code_locale_code(content_type, asset_code, channel_code, locale_code, body=body)
except ApiException as e:
    print("Exception when calling PAMAssetVariationFileApi->post_variation_files_channel_code_locale_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Equal to &#x27;multipart/form-data&#x27;, no other value allowed | 
 **asset_code** | **str**| Code of the asset | 
 **channel_code** | **str**| Code of the channel | 
 **locale_code** | **str**| Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable | 
 **body** | [**ChannelCodeLocaleCodeBody**](ChannelCodeLocaleCodeBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

