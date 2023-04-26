# swagger_client.ReferenceEntityAttributeApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reference_entities_code_attributes**](ReferenceEntityAttributeApi.md#get_reference_entities_code_attributes) | **GET** /api/rest/v1/reference-entities/{reference_entity_code}/attributes | Get the list of attributes of a given reference entity
[**get_reference_entity_attributes_code**](ReferenceEntityAttributeApi.md#get_reference_entity_attributes_code) | **GET** /api/rest/v1/reference-entities/{reference_entity_code}/attributes/{code} | Get an attribute of a given reference entity
[**patch_reference_entity_attributes_code**](ReferenceEntityAttributeApi.md#patch_reference_entity_attributes_code) | **PATCH** /api/rest/v1/reference-entities/{reference_entity_code}/attributes/{code} | Update/create an attribute of a given reference entity

# **get_reference_entities_code_attributes**
> list[InlineResponse20021] get_reference_entities_code_attributes(reference_entity_code)

Get the list of attributes of a given reference entity

This endpoint allows you to get the list of attributes of a given reference entity.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceEntityAttributeApi()
reference_entity_code = 'reference_entity_code_example' # str | Code of the reference entity

try:
    # Get the list of attributes of a given reference entity
    api_response = api_instance.get_reference_entities_code_attributes(reference_entity_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceEntityAttributeApi->get_reference_entities_code_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_entity_code** | **str**| Code of the reference entity | 

### Return type

[**list[InlineResponse20021]**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_entity_attributes_code**
> InlineResponse20022 get_reference_entity_attributes_code(reference_entity_code, code)

Get an attribute of a given reference entity

This endpoint allows you to get the information about a given attribute for a given reference entity.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceEntityAttributeApi()
reference_entity_code = 'reference_entity_code_example' # str | Code of the reference entity
code = 'code_example' # str | Code of the resource

try:
    # Get an attribute of a given reference entity
    api_response = api_instance.get_reference_entity_attributes_code(reference_entity_code, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceEntityAttributeApi->get_reference_entity_attributes_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_entity_code** | **str**| Code of the reference entity | 
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_reference_entity_attributes_code**
> patch_reference_entity_attributes_code(body, reference_entity_code, code)

Update/create an attribute of a given reference entity

This endpoint allows you to update a given attribute for a given renference entity. Note that if the attribute does not already exist for the given reference entity, it creates it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceEntityAttributeApi()
body = swagger_client.AttributesCodeBody1() # AttributesCodeBody1 | 
reference_entity_code = 'reference_entity_code_example' # str | Code of the reference entity
code = 'code_example' # str | Code of the resource

try:
    # Update/create an attribute of a given reference entity
    api_instance.patch_reference_entity_attributes_code(body, reference_entity_code, code)
except ApiException as e:
    print("Exception when calling ReferenceEntityAttributeApi->patch_reference_entity_attributes_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttributesCodeBody1**](AttributesCodeBody1.md)|  | 
 **reference_entity_code** | **str**| Code of the reference entity | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

