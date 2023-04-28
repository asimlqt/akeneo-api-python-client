# swagger_client.MeasurementFamilyApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**measurement_families_get_list**](MeasurementFamilyApi.md#measurement_families_get_list) | **GET** /api/rest/v1/measurement-families | Get list of measurement families
[**patch_measurement_families**](MeasurementFamilyApi.md#patch_measurement_families) | **PATCH** /api/rest/v1/measurement-families | Update/create several measurement families

# **measurement_families_get_list**
> InlineResponse20018 measurement_families_get_list(authorization)

Get list of measurement families

This endpoint allows you to get a list of measurement families.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MeasurementFamilyApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.

try:
    # Get list of measurement families
    api_response = api_instance.measurement_families_get_list(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeasurementFamilyApi->measurement_families_get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_measurement_families**
> list[InlineResponse20019] patch_measurement_families(body=body)

Update/create several measurement families

This endpoint allows you to update and/or create several measurement families at once.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MeasurementFamilyApi()
body = [swagger_client.V1MeasurementfamiliesBody()] # list[V1MeasurementfamiliesBody] |  (optional)

try:
    # Update/create several measurement families
    api_response = api_instance.patch_measurement_families(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeasurementFamilyApi->patch_measurement_families: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[V1MeasurementfamiliesBody]**](V1MeasurementfamiliesBody.md)|  | [optional] 

### Return type

[**list[InlineResponse20019]**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

