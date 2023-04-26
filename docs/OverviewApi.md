# swagger_client.OverviewApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_endpoints**](OverviewApi.md#get_endpoints) | **GET** /api/rest/v1 | Get list of all endpoints

# **get_endpoints**
> InlineResponse20039 get_endpoints()

Get list of all endpoints

This endpoint allows you to get the list of all the available endpoints. No need to be authenticated to use this endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OverviewApi()

try:
    # Get list of all endpoints
    api_response = api_instance.get_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverviewApi->get_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, host, authentication, routes, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

