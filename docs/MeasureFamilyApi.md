# swagger_client.MeasureFamilyApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**measure_families_get**](MeasureFamilyApi.md#measure_families_get) | **GET** /api/rest/v1/measure-families/{code} | Get a measure family
[**measure_families_get_list**](MeasureFamilyApi.md#measure_families_get_list) | **GET** /api/rest/v1/measure-families | Get list of measure familiy

# **measure_families_get**
> InlineResponse20017 measure_families_get(authorization, code)

Get a measure family

This endpoint allows you to get the information about a given measure family.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MeasureFamilyApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
code = 'code_example' # str | Code of the resource

try:
    # Get a measure family
    api_response = api_instance.measure_families_get(authorization, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeasureFamilyApi->measure_families_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **measure_families_get_list**
> MeasureFamilies measure_families_get_list(authorization)

Get list of measure familiy

This endpoint allows you to get a list of measure families. Measure families are paginated and sorted by code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MeasureFamilyApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.

try:
    # Get list of measure familiy
    api_response = api_instance.measure_families_get_list(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeasureFamilyApi->measure_families_get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 

### Return type

[**MeasureFamilies**](MeasureFamilies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _links, current_page, _embedded, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

