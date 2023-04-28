# swagger_client.ChannelApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channels_patch**](ChannelApi.md#channels_patch) | **PATCH** /api/rest/v1/channels/{code} | Update/create a channel
[**channels_post**](ChannelApi.md#channels_post) | **POST** /api/rest/v1/channels | Create a new channel
[**get_channels**](ChannelApi.md#get_channels) | **GET** /api/rest/v1/channels | Get a list of channels
[**get_channels_code**](ChannelApi.md#get_channels_code) | **GET** /api/rest/v1/channels/{code} | Get a channel
[**several_channels_patch**](ChannelApi.md#several_channels_patch) | **PATCH** /api/rest/v1/channels | Update/create several channels

# **channels_patch**
> channels_patch(body, code)

Update/create a channel

This endpoint allows you to update a given channel. Know more about <a href=\"/documentation/update.html#update-behavior\">Update behavior</a>. Note that if no channel exists for the given code, it creates it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApi()
body = swagger_client.ChannelsCodeBody() # ChannelsCodeBody | 
code = 'code_example' # str | Code of the resource

try:
    # Update/create a channel
    api_instance.channels_patch(body, code)
except ApiException as e:
    print("Exception when calling ChannelApi->channels_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelsCodeBody**](ChannelsCodeBody.md)|  | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_post**
> channels_post(body=body)

Create a new channel

This endpoint allows you to create a new channel.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApi()
body = swagger_client.V1ChannelsBody() # V1ChannelsBody |  (optional)

try:
    # Create a new channel
    api_instance.channels_post(body=body)
except ApiException as e:
    print("Exception when calling ChannelApi->channels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ChannelsBody**](V1ChannelsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channels**
> Channels get_channels(authorization, page=page, limit=limit, with_count=with_count)

Get a list of channels

This endpoint allows you to get a list of channels. Channels are paginated and sorted by code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
page = 1 # int | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section (optional) (default to 1)
limit = 10 # int | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to 10)
with_count = false # bool | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way (optional) (default to false)

try:
    # Get a list of channels
    api_response = api_instance.get_channels(authorization, page=page, limit=limit, with_count=with_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelApi->get_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **page** | **int**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **int**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **with_count** | **bool**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**Channels**](Channels.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _links, current_page, _embedded, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channels_code**
> InlineResponse20013 get_channels_code(authorization, code)

Get a channel

This endpoint allows you to get the information about a given channel.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
code = 'code_example' # str | Code of the resource

try:
    # Get a channel
    api_response = api_instance.get_channels_code(authorization, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelApi->get_channels_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **several_channels_patch**
> InlineResponse200 several_channels_patch(body=body)

Update/create several channels

This endpoint allows you to update and/or create several channels at once.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApi()
body = swagger_client.V1ChannelsBody1() # V1ChannelsBody1 |  (optional)

try:
    # Update/create several channels
    api_response = api_instance.several_channels_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelApi->several_channels_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ChannelsBody1**](V1ChannelsBody1.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

