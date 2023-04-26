# swagger_client.ReferenceEntityAttributeOptionApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reference_entity_attributes_attribute_code_options**](ReferenceEntityAttributeOptionApi.md#get_reference_entity_attributes_attribute_code_options) | **GET** /api/rest/v1/reference-entities/{reference_entity_code}/attributes/{attribute_code}/options | Get a list of attribute options of a given attribute for a given reference entity
[**get_reference_entity_attributes_attribute_code_options_code**](ReferenceEntityAttributeOptionApi.md#get_reference_entity_attributes_attribute_code_options_code) | **GET** /api/rest/v1/reference-entities/{reference_entity_code}/attributes/{attribute_code}/options/{code} | Get an attribute option for a given attribute of a given reference entity
[**patch_reference_entity_attributes_attribute_code_options_code**](ReferenceEntityAttributeOptionApi.md#patch_reference_entity_attributes_attribute_code_options_code) | **PATCH** /api/rest/v1/reference-entities/{reference_entity_code}/attributes/{attribute_code}/options/{code} | Update/create a reference entity attribute option

# **get_reference_entity_attributes_attribute_code_options**
> list[InlineResponse20023] get_reference_entity_attributes_attribute_code_options(reference_entity_code, attribute_code)

Get a list of attribute options of a given attribute for a given reference entity

This endpoint allows you to get a list of attribute options for a given reference entity.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceEntityAttributeOptionApi()
reference_entity_code = 'reference_entity_code_example' # str | Code of the reference entity
attribute_code = 'attribute_code_example' # str | Code of the attribute

try:
    # Get a list of attribute options of a given attribute for a given reference entity
    api_response = api_instance.get_reference_entity_attributes_attribute_code_options(reference_entity_code, attribute_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceEntityAttributeOptionApi->get_reference_entity_attributes_attribute_code_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_entity_code** | **str**| Code of the reference entity | 
 **attribute_code** | **str**| Code of the attribute | 

### Return type

[**list[InlineResponse20023]**](InlineResponse20023.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_entity_attributes_attribute_code_options_code**
> InlineResponse20024 get_reference_entity_attributes_attribute_code_options_code(reference_entity_code, attribute_code, code)

Get an attribute option for a given attribute of a given reference entity

This endpoint allows you to get the information about a given attribute option.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceEntityAttributeOptionApi()
reference_entity_code = 'reference_entity_code_example' # str | Code of the reference entity
attribute_code = 'attribute_code_example' # str | Code of the attribute
code = 'code_example' # str | Code of the resource

try:
    # Get an attribute option for a given attribute of a given reference entity
    api_response = api_instance.get_reference_entity_attributes_attribute_code_options_code(reference_entity_code, attribute_code, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceEntityAttributeOptionApi->get_reference_entity_attributes_attribute_code_options_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_entity_code** | **str**| Code of the reference entity | 
 **attribute_code** | **str**| Code of the attribute | 
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_reference_entity_attributes_attribute_code_options_code**
> patch_reference_entity_attributes_attribute_code_options_code(body, reference_entity_code, attribute_code, code)

Update/create a reference entity attribute option

This endpoint allows you to update a given option for a given attribute and a given reference entity. Learn more about <a href=\"/documentation/update.html#patch-reference-entity-record-values\">Update behavior</a>. Note that if the option does not already exist for the given attribute of the given reference entity, it creates it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceEntityAttributeOptionApi()
body = swagger_client.OptionsCodeBody1() # OptionsCodeBody1 | 
reference_entity_code = 'reference_entity_code_example' # str | Code of the reference entity
attribute_code = 'attribute_code_example' # str | Code of the attribute
code = 'code_example' # str | Code of the resource

try:
    # Update/create a reference entity attribute option
    api_instance.patch_reference_entity_attributes_attribute_code_options_code(body, reference_entity_code, attribute_code, code)
except ApiException as e:
    print("Exception when calling ReferenceEntityAttributeOptionApi->patch_reference_entity_attributes_attribute_code_options_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OptionsCodeBody1**](OptionsCodeBody1.md)|  | 
 **reference_entity_code** | **str**| Code of the reference entity | 
 **attribute_code** | **str**| Code of the attribute | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

