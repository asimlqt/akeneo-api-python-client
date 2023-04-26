# swagger_client.AuthenticationApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_token**](AuthenticationApi.md#post_token) | **POST** /api/oauth/v1/token | Get authentication token

# **post_token**
> InlineResponse20040 post_token(content_type, authorization, body=body)

Get authentication token

This endpoint allows you to get an authentication token. No need to be authenticated to use this endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
content_type = 'content_type_example' # str | Equal to 'application/json' or 'application/x-www-form-urlencoded', no other value allowed
authorization = 'authorization_example' # str | Equal to 'Basic xx', where 'xx' is the base 64 encoding of the client id and secret. Find out how to generate them in the <a href=\"/documentation/authentication.html#client-idsecret-generation\">Client ID/secret generation</a> section.
body = swagger_client.V1TokenBody() # V1TokenBody |  (optional)

try:
    # Get authentication token
    api_response = api_instance.post_token(content_type, authorization, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->post_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Equal to &#x27;application/json&#x27; or &#x27;application/x-www-form-urlencoded&#x27;, no other value allowed | 
 **authorization** | **str**| Equal to &#x27;Basic xx&#x27;, where &#x27;xx&#x27; is the base 64 encoding of the client id and secret. Find out how to generate them in the &lt;a href&#x3D;\&quot;/documentation/authentication.html#client-idsecret-generation\&quot;&gt;Client ID/secret generation&lt;/a&gt; section. | 
 **body** | [**V1TokenBody**](V1TokenBody.md)|  | [optional] 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, access_token, expires_in, token_type, scope, refresh_token, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

