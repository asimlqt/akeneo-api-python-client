# swagger_client.AttributeOptionApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_attributes_attribute_code_options**](AttributeOptionApi.md#get_attributes_attribute_code_options) | **GET** /api/rest/v1/attributes/{attribute_code}/options | Get list of attribute options
[**get_attributes_attribute_code_options_code**](AttributeOptionApi.md#get_attributes_attribute_code_options_code) | **GET** /api/rest/v1/attributes/{attribute_code}/options/{code} | Get an attribute option
[**patch_attributes_attribute_code_options**](AttributeOptionApi.md#patch_attributes_attribute_code_options) | **PATCH** /api/rest/v1/attributes/{attribute_code}/options | Update/create several attribute options
[**patch_attributes_attribute_code_options_code**](AttributeOptionApi.md#patch_attributes_attribute_code_options_code) | **PATCH** /api/rest/v1/attributes/{attribute_code}/options/{code} | Update/create an attribute option
[**post_attributes_attribute_code_options**](AttributeOptionApi.md#post_attributes_attribute_code_options) | **POST** /api/rest/v1/attributes/{attribute_code}/options | Create a new attribute option

# **get_attributes_attribute_code_options**
> AttributeOptions get_attributes_attribute_code_options(attribute_code, page=page, limit=limit, with_count=with_count)

Get list of attribute options

This endpoint allows you to get a list of attribute options. Attribute options are paginated and sorted by code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeOptionApi()
attribute_code = 'attribute_code_example' # str | Code of the attribute
page = 1 # int | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section (optional) (default to 1)
limit = 10 # int | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to 10)
with_count = false # bool | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way (optional) (default to false)

try:
    # Get list of attribute options
    api_response = api_instance.get_attributes_attribute_code_options(attribute_code, page=page, limit=limit, with_count=with_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeOptionApi->get_attributes_attribute_code_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_code** | **str**| Code of the attribute | 
 **page** | **int**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **int**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **with_count** | **bool**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**AttributeOptions**](AttributeOptions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _links, current_page, _embedded, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes_attribute_code_options_code**
> InlineResponse20010 get_attributes_attribute_code_options_code(attribute_code, code)

Get an attribute option

This endpoint allows you to get the information about a given attribute option.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeOptionApi()
attribute_code = 'attribute_code_example' # str | Code of the attribute
code = 'code_example' # str | Code of the resource

try:
    # Get an attribute option
    api_response = api_instance.get_attributes_attribute_code_options_code(attribute_code, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeOptionApi->get_attributes_attribute_code_options_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_code** | **str**| Code of the attribute | 
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_attributes_attribute_code_options**
> InlineResponse200 patch_attributes_attribute_code_options(attribute_code, body=body)

Update/create several attribute options

This endpoint allows you to update several attribute options at once.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeOptionApi()
attribute_code = 'attribute_code_example' # str | Code of the attribute
body = swagger_client.AttributeCodeOptionsBody1() # AttributeCodeOptionsBody1 |  (optional)

try:
    # Update/create several attribute options
    api_response = api_instance.patch_attributes_attribute_code_options(attribute_code, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeOptionApi->patch_attributes_attribute_code_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_code** | **str**| Code of the attribute | 
 **body** | [**AttributeCodeOptionsBody1**](AttributeCodeOptionsBody1.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_attributes_attribute_code_options_code**
> patch_attributes_attribute_code_options_code(body, attribute_code, code)

Update/create an attribute option

This endpoint allows you to update a given attribute option. Know more about <a href=\"/documentation/update.html#update-behavior\">Update behavior</a>. Note that if no attribute option exists for the given code, it creates it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeOptionApi()
body = swagger_client.OptionsCodeBody() # OptionsCodeBody | 
attribute_code = 'attribute_code_example' # str | Code of the attribute
code = 'code_example' # str | Code of the resource

try:
    # Update/create an attribute option
    api_instance.patch_attributes_attribute_code_options_code(body, attribute_code, code)
except ApiException as e:
    print("Exception when calling AttributeOptionApi->patch_attributes_attribute_code_options_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OptionsCodeBody**](OptionsCodeBody.md)|  | 
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

# **post_attributes_attribute_code_options**
> post_attributes_attribute_code_options(attribute_code, body=body)

Create a new attribute option

This endpoint allows you to create a new attribute option.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeOptionApi()
attribute_code = 'attribute_code_example' # str | Code of the attribute
body = swagger_client.AttributeCodeOptionsBody() # AttributeCodeOptionsBody |  (optional)

try:
    # Create a new attribute option
    api_instance.post_attributes_attribute_code_options(attribute_code, body=body)
except ApiException as e:
    print("Exception when calling AttributeOptionApi->post_attributes_attribute_code_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_code** | **str**| Code of the attribute | 
 **body** | [**AttributeCodeOptionsBody**](AttributeCodeOptionsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

