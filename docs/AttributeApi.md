# swagger_client.AttributeApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_attributes**](AttributeApi.md#get_attributes) | **GET** /api/rest/v1/attributes | Get list of attributes
[**get_attributes_code**](AttributeApi.md#get_attributes_code) | **GET** /api/rest/v1/attributes/{code} | Get an attribute
[**patch_attributes**](AttributeApi.md#patch_attributes) | **PATCH** /api/rest/v1/attributes | Update/create several attributes
[**patch_attributes_code**](AttributeApi.md#patch_attributes_code) | **PATCH** /api/rest/v1/attributes/{code} | Update/create an attribute
[**post_attributes**](AttributeApi.md#post_attributes) | **POST** /api/rest/v1/attributes | Create a new attribute

# **get_attributes**
> Attributes get_attributes(authorization, search=search, page=page, limit=limit, with_count=with_count, with_table_select_options=with_table_select_options)

Get list of attributes

This endpoint allows you to get a list of attributes. Attributes are paginated and sorted by code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
search = 'search_example' # str | Filter attributes, for more details see the <a href=\"/documentation/filter.html#filter-attributes\">Filters</a> section. (optional)
page = 1 # int | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section (optional) (default to 1)
limit = 10 # int | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to 10)
with_count = false # bool | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way (optional) (default to false)
with_table_select_options = false # bool | Return the options of 'select' column types (of a table attribute) in the response. (Only available since the 7.0 version) (optional) (default to false)

try:
    # Get list of attributes
    api_response = api_instance.get_attributes(authorization, search=search, page=page, limit=limit, with_count=with_count, with_table_select_options=with_table_select_options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->get_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **search** | **str**| Filter attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-attributes\&quot;&gt;Filters&lt;/a&gt; section. | [optional] 
 **page** | **int**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **int**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **with_count** | **bool**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]
 **with_table_select_options** | **bool**| Return the options of &#x27;select&#x27; column types (of a table attribute) in the response. (Only available since the 7.0 version) | [optional] [default to false]

### Return type

[**Attributes**](Attributes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _links, current_page, _embedded, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes_code**
> InlineResponse2009 get_attributes_code(authorization, code, with_table_select_options=with_table_select_options)

Get an attribute

This endpoint allows you to get the information about a given attribute.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
code = 'code_example' # str | Code of the resource
with_table_select_options = false # bool | Return the options of 'select' column types (of a table attribute) in the response. (Only available since the 7.0 version) (optional) (default to false)

try:
    # Get an attribute
    api_response = api_instance.get_attributes_code(authorization, code, with_table_select_options=with_table_select_options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->get_attributes_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **code** | **str**| Code of the resource | 
 **with_table_select_options** | **bool**| Return the options of &#x27;select&#x27; column types (of a table attribute) in the response. (Only available since the 7.0 version) | [optional] [default to false]

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_attributes**
> InlineResponse200 patch_attributes(body=body)

Update/create several attributes

This endpoint allows you to update and/or create several attributes at once.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeApi()
body = swagger_client.V1AttributesBody1() # V1AttributesBody1 |  (optional)

try:
    # Update/create several attributes
    api_response = api_instance.patch_attributes(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->patch_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1AttributesBody1**](V1AttributesBody1.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_attributes_code**
> patch_attributes_code(body, code)

Update/create an attribute

This endpoint allows you to update a given attribute. Know more about <a href=\"/documentation/update.html#update-behavior\">Update behavior</a>. Note that if no attribute exists for the given code, it creates it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeApi()
body = swagger_client.AttributesCodeBody() # AttributesCodeBody | 
code = 'code_example' # str | Code of the resource

try:
    # Update/create an attribute
    api_instance.patch_attributes_code(body, code)
except ApiException as e:
    print("Exception when calling AttributeApi->patch_attributes_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttributesCodeBody**](AttributesCodeBody.md)|  | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_attributes**
> post_attributes(body=body)

Create a new attribute

This endpoint allows you to create a new attribute.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeApi()
body = swagger_client.V1AttributesBody() # V1AttributesBody |  (optional)

try:
    # Create a new attribute
    api_instance.post_attributes(body=body)
except ApiException as e:
    print("Exception when calling AttributeApi->post_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1AttributesBody**](V1AttributesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

